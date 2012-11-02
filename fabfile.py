# -*- coding: utf-8 -*-
import os
import sys
import time
import xmlrpclib
from fabric.api import cd, env, roles, run, local
from fabric.contrib.files import exists
from fabric.contrib.files import upload_template


env.root = os.path.dirname(os.path.abspath(__file__))
env.repo = 'git@bitbucket.org:douglasmiranda/douglasmiranda.com.git'
env.project = 'douglasmiranda_app'
env.project_root = '/home/douglas777/webapps/%(project)s' % env
env.app_root = os.path.join(env.project_root, 'project')
env.virtualenv_dir = '/home/douglas777/.virtualenvs/douglasmiranda'
env.user = 'douglas777'
env.roledefs = {
    'server': ['douglas777.webfactional.com'],
}


@roles('server')
def install_app():
    def write_output(output):
        f = file('output_app_installed.txt', 'w')
        f.write(output)
        f.close()

    output = _webfaction_create_app()
    run('git clone %(repo)s %(project_root)s' % env)

    _install_pip()
    _install_virtualenv()
    _create_virtualenv()
    write_output(output)
    print 'check the output in output_app_installed.txt'


def _webfaction_create_app():
    """
        cria uma app "custom app with port" usando a API da webfaction
    """
    password = raw_input('Senha para ("%(user)s"):' % env)
    server = xmlrpclib.ServerProxy('https://api.webfaction.com/')
    session_id, account = server.login(env.user, password)

    try:
        response = server.create_app(session_id, env.project, 'custom_app_with_port', False, '')
        print "App on webfaction created: %s" % response
        return response

    except xmlrpclib.Fault:
        print "Não foi possível criar a app %s, talvez o nome dessa app já esteja em uso." % env.project
        sys.exit(1)


@roles('server')
def _install_pip():
    run("easy_install-2.7 pip")


@roles('server')
def _install_virtualenv():
    run("pip install virtualenv")


@roles('server')
def _create_virtualenv():
    run("virtualenv --no-site-packages --python=python2.7 %(virtualenv_dir)s" % env)


@roles('server')
def update_app():
    with cd(env.project_root):
        run("git pull origin master")


def update_repo():
    local("git push origin master")


@roles('server')
def pip_install():
    run("%(virtualenv_dir)s/bin/pip install -r %(project_root)s/requirements.txt" % env)


@roles('server')
def collect_static_files():
    with cd(env.project_root):
        run("%(virtualenv_dir)s/bin/python manage.py collectstatic -v 0 --noinput  --settings=douglasmiranda.settings.prod" % env)


@roles('server')
def start_migration():
    with cd(env.project_root):
        run("%(virtualenv_dir)s/bin/python manage.py db-migrate" % env)


@roles('server')
def start_gunicorn():
    with cd(env.project_root):
        run('./start_gunicorn.py')


@roles('server')
def stop_gunicorn():
    with cd(env.project_root):
        if exists('gunicorn.pid'):
            run('kill `cat gunicorn.pid`')


@roles('server')
def restart_gunicorn():
    stop_gunicorn()
    time.sleep(10)
    start_gunicorn()


@roles('server')
def create_user():
    with cd(env.project_root):
        run("%(virtualenv_dir)s/bin/python manage.py createsuperuser --settings=douglasmiranda.settings.prod" % env)


@roles('server')
def syncdb():
    with cd(env.project_root):
        run("%(virtualenv_dir)s/bin/python manage.py syncdb --settings=douglasmiranda.settings.prod --noinput" % env)


@roles('server')
def upload_django_settings():
    upload_template('douglasmiranda/settings/prod.py', '%(project_root)s/douglasmiranda/settings/' % env)


@roles('server')
def upload_gunicorn_settings():
    upload_template('start_gunicorn.sh', '%(project_root)s' % env)
    upload_template('etc/gunicorn.prod.conf', '%(project_root)s/etc/' % env)


@roles('server')
def deploy():
    update_repo()
    update_app()
    pip_install()
    collect_static_files()
    restart_gunicorn()
