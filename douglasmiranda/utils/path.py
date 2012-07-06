from os.path import abspath, join, dirname


PROJECT_ROOT_PATH = abspath(join(dirname(abspath(__file__)), 'douglasmiranda'))


def abspath(dirname):
    return join(PROJECT_ROOT_PATH, dirname)
