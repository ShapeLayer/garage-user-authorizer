from os import chdir
from subprocess import run

def install():
    path_offset = ''
    if __name__ == '__main__':
        path_offset = '../'

    print('[Gua] Install Python dependencies...')
    run(['pip', 'install', '-r' f'{path_offset}requirements.txt'])
    run(['pip', 'install', '--upgrade', 'pip'])
    print('[Gua] Install Node.js dependencies...')
    chdir(f'{path_offset}gua/views/front')
    run(['npm', 'install'])
    print('[Gua] All dependencies installed successfully.')

if __name__ == '__main__':
    install()
