# file lib/ansible/cli/console.py:160-181
# lines [162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 180, 181]
# branches ['162->exit', '162->163', '163->exit', '163->164', '164->165', '164->166', '166->167', '166->168', '168->169', '168->170', '170->171', '170->172', '172->173', '172->174', '174->175', '174->180', '176->177', '176->178']

import os
import pytest
from ansible.cli.console import ConsoleCLI

@pytest.fixture
def console_cli(mocker):
    mocker.patch('ansible.cli.console.CLI')
    mocker.patch('cmd.Cmd')
    mocker.patch('ansible.cli.console.ConsoleCLI.parse', return_value=None)
    return ConsoleCLI(['console'])

@pytest.fixture
def fake_dir(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    (d / ".hidden").touch()
    (d / "__init__.py").touch()
    (d / "ignored.py").touch()
    (d / "_private.py").touch()
    (d / "valid_module.py").touch()
    (d / "valid.link").symlink_to("valid_module.py")
    return d

def test_find_modules_in_path(console_cli, fake_dir, mocker):
    mocker.patch('ansible.cli.console.C.REJECT_EXTS', ['.pyc', '.swp', '.pyo'])
    mocker.patch('ansible.cli.console.C.IGNORE_FILES', ['ignored.py'])

    modules = list(console_cli._find_modules_in_path(str(fake_dir)))

    assert '.hidden' not in modules
    assert '__init__' not in modules
    assert 'ignored' not in modules
    assert '_private' not in modules
    assert 'valid_module' in modules
    assert 'valid.link' not in modules
