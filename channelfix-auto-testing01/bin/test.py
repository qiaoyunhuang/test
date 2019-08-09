import subprocess
import sys
from multiprocessing import Process

import settings


def complete_shell(filename):
    return 'python {}/{}.py'.format(settings.BIN_PATH, filename)


def auto_test_shell(command):
    subprocess.run(
        command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)


def run_shell(command=None):
    _args = ['app', 'web'] if command is None else [command]
    _shell = [complete_shell(item) for item in _args]
    processes = [
        Process(
            target=auto_test_shell, args=(command, )
        ) for command in _shell
    ]
    for arg, process in zip(_args, processes):
        sys.stdout.write('process start: auto test {}\n'.format(arg))
        process.start()
    for process in processes:
        process.join()


argv = sys.argv
if len(argv) == 1:
    run_shell()
elif len(argv) == 2:
    if argv[1] == 'app' or argv[1] == 'web':
        run_shell(argv[1])
    else:
        sys.stderr.write('not understand {}'.format(argv[0]))
else:
    sys.stderr.write('the shell you input is not understand')
