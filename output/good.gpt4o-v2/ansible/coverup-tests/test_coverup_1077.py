# file: lib/ansible/modules/command.py:269-395
# asked: {"lines": [274, 275, 276, 277, 278, 279, 280, 281, 282, 284, 285, 286, 287, 289, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 304, 306, 307, 308, 310, 311, 312, 313, 315, 316, 317, 318, 320, 321, 323, 325, 326, 328, 329, 331, 333, 334, 336, 337, 338, 339, 340, 343, 344, 346, 349, 350, 351, 352, 354, 357, 358, 359, 360, 361, 363, 364, 367, 368, 369, 370, 371, 374, 375, 376, 378, 381, 383, 384, 385, 387, 388, 389, 391, 392, 393, 395], "branches": [[306, 307], [306, 310], [310, 311], [310, 315], [315, 316], [315, 320], [320, 321], [320, 323], [325, 326], [325, 328], [329, 331], [329, 333], [333, 334], [333, 343], [343, 344], [343, 346], [349, 350], [349, 357], [350, 351], [350, 357], [357, 358], [357, 363], [358, 359], [358, 363], [363, 364], [363, 367], [367, 368], [367, 374], [381, 383], [381, 387], [387, 388], [387, 391], [391, 392], [391, 395]]}
# gained: {"lines": [274, 275, 276, 277, 278, 279, 280, 281, 282, 284, 285, 286, 287, 289, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 304, 306, 310, 311, 312, 313, 315, 316, 317, 318, 320, 321, 323, 325, 326, 328, 329, 333, 334, 336, 337, 338, 339, 340, 343, 346, 349, 350, 351, 352, 354, 357, 358, 359, 360, 361, 363, 364, 367, 368, 369, 370, 371, 378, 381, 383, 384, 385, 387, 388, 389, 391, 395], "branches": [[306, 310], [310, 311], [310, 315], [315, 316], [315, 320], [320, 321], [325, 326], [329, 333], [333, 334], [333, 343], [343, 346], [349, 350], [349, 357], [350, 351], [357, 358], [357, 363], [358, 359], [363, 364], [363, 367], [367, 368], [381, 383], [387, 388], [391, 395]]}

import pytest
import datetime
import os
import glob
from unittest import mock
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils._text import to_text

def test_main_no_command_given(monkeypatch):
    from ansible.modules.command import main

    def mock_fail_json(*args, **kwargs):
        raise Exception(kwargs)

    def mock_params(self):
        self.params = {
            '_raw_params': '',
            'argv': None,
            '_uses_shell': False,
            'chdir': None,
            'executable': None,
            'creates': None,
            'removes': None,
            'warn': False,
            'stdin': None,
            'stdin_add_newline': True,
            'strip_empty_ends': True,
        }

    monkeypatch.setattr(AnsibleModule, "fail_json", mock_fail_json)
    monkeypatch.setattr(AnsibleModule, "_load_params", mock_params)
    monkeypatch.setattr(AnsibleModule, "exit_json", lambda *args, **kwargs: None)

    with pytest.raises(Exception) as excinfo:
        main()
    assert excinfo.value.args[0]['msg'] == "no command given"
    assert excinfo.value.args[0]['rc'] == 256

def test_main_both_args_and_argv_given(monkeypatch):
    from ansible.modules.command import main

    def mock_fail_json(*args, **kwargs):
        raise Exception(kwargs)

    def mock_params(self):
        self.params = {
            '_raw_params': 'echo test',
            'argv': ['echo', 'test'],
            '_uses_shell': False,
            'chdir': None,
            'executable': None,
            'creates': None,
            'removes': None,
            'warn': False,
            'stdin': None,
            'stdin_add_newline': True,
            'strip_empty_ends': True,
        }

    monkeypatch.setattr(AnsibleModule, "fail_json", mock_fail_json)
    monkeypatch.setattr(AnsibleModule, "_load_params", mock_params)
    monkeypatch.setattr(AnsibleModule, "exit_json", lambda *args, **kwargs: None)

    with pytest.raises(Exception) as excinfo:
        main()
    assert excinfo.value.args[0]['msg'] == "only command or argv can be given, not both"
    assert excinfo.value.args[0]['rc'] == 256

def test_main_change_directory_failure(monkeypatch):
    from ansible.modules.command import main

    def mock_fail_json(*args, **kwargs):
        raise Exception(kwargs)

    def mock_params(self):
        self.params = {
            '_raw_params': 'echo test',
            'argv': None,
            '_uses_shell': False,
            'chdir': '/nonexistent',
            'executable': None,
            'creates': None,
            'removes': None,
            'warn': False,
            'stdin': None,
            'stdin_add_newline': True,
            'strip_empty_ends': True,
        }

    monkeypatch.setattr(AnsibleModule, "fail_json", mock_fail_json)
    monkeypatch.setattr(AnsibleModule, "_load_params", mock_params)
    monkeypatch.setattr(AnsibleModule, "exit_json", lambda *args, **kwargs: None)
    monkeypatch.setattr(os, "chdir", mock.Mock(side_effect=OSError("Unable to change directory")))

    with pytest.raises(Exception) as excinfo:
        main()
    assert excinfo.value.args[0]['msg'] == "Unable to change directory before execution: Unable to change directory"

def test_main_creates_file_exists(monkeypatch):
    from ansible.modules.command import main

    def mock_exit_json(*args, **kwargs):
        raise Exception(kwargs)

    def mock_params(self):
        self.params = {
            '_raw_params': 'echo test',
            'argv': None,
            '_uses_shell': False,
            'chdir': None,
            'executable': None,
            'creates': '/tmp/testfile',
            'removes': None,
            'warn': False,
            'stdin': None,
            'stdin_add_newline': True,
            'strip_empty_ends': True,
        }

    monkeypatch.setattr(AnsibleModule, "exit_json", mock_exit_json)
    monkeypatch.setattr(AnsibleModule, "_load_params", mock_params)
    monkeypatch.setattr(glob, "glob", lambda path: [path])

    with pytest.raises(Exception) as excinfo:
        main()
    assert excinfo.value.args[0]['msg'] == "Did not run command since '/tmp/testfile' exists"
    assert excinfo.value.args[0]['rc'] == 0

def test_main_removes_file_not_exists(monkeypatch):
    from ansible.modules.command import main

    def mock_exit_json(*args, **kwargs):
        raise Exception(kwargs)

    def mock_params(self):
        self.params = {
            '_raw_params': 'echo test',
            'argv': None,
            '_uses_shell': False,
            'chdir': None,
            'executable': None,
            'creates': None,
            'removes': '/tmp/testfile',
            'warn': False,
            'stdin': None,
            'stdin_add_newline': True,
            'strip_empty_ends': True,
        }

    monkeypatch.setattr(AnsibleModule, "exit_json", mock_exit_json)
    monkeypatch.setattr(AnsibleModule, "_load_params", mock_params)
    monkeypatch.setattr(glob, "glob", lambda path: [])

    with pytest.raises(Exception) as excinfo:
        main()
    assert excinfo.value.args[0]['msg'] == "Did not run command since '/tmp/testfile' does not exist"
    assert excinfo.value.args[0]['rc'] == 0

def test_main_command_execution(monkeypatch):
    from ansible.modules.command import main

    def mock_exit_json(*args, **kwargs):
        raise Exception(kwargs)

    def mock_params(self):
        self.params = {
            '_raw_params': 'echo test',
            'argv': None,
            '_uses_shell': False,
            'chdir': None,
            'executable': None,
            'creates': None,
            'removes': None,
            'warn': False,
            'stdin': None,
            'stdin_add_newline': True,
            'strip_empty_ends': True,
        }

    def mock_run_command(self, args, **kwargs):
        return 0, "test output", ""

    monkeypatch.setattr(AnsibleModule, "exit_json", mock_exit_json)
    monkeypatch.setattr(AnsibleModule, "_load_params", mock_params)
    monkeypatch.setattr(AnsibleModule, "run_command", mock_run_command)

    with pytest.raises(Exception) as excinfo:
        main()
    assert excinfo.value.args[0]['stdout'] == "test output"
    assert excinfo.value.args[0]['rc'] == 0
    assert excinfo.value.args[0]['changed'] is True
