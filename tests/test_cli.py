import os
import subprocess

here = os.path.abspath(os.path.dirname(__file__))


def test_cli_runner():
    esmcol_file = os.path.join(here, 'test_data/good_collection.json')
    cmd = ['esmcol-validator', esmcol_file, '--timer', '--verbose', '--log-level', 'DEBUG']
    p = subprocess.Popen(cmd, stdin=subprocess.DEVNULL, stderr=subprocess.DEVNULL,)

    p.communicate()
    assert p.returncode == 0


def test_empty_input():
    p = subprocess.Popen(['esmcol-validator'], stdin=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    p.communicate()
    assert p.returncode != 0
