from os.path import abspath, join, dirname


PROJECT_ROOT_PATH = abspath(join(dirname(abspath(__file__)), '../douglasmiranda/'))


def relative_to_project_path(dirname):
    return join(PROJECT_ROOT_PATH, dirname)
