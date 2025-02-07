# file: lib/ansible/executor/playbook_executor.py:78-273
# asked: {"lines": [78, 84, 85, 86, 87, 89, 90, 91, 93, 96, 97, 98, 99, 101, 103, 105, 106, 107, 109, 111, 114, 115, 116, 119, 120, 122, 123, 124, 126, 127, 128, 130, 133, 136, 137, 138, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 153, 154, 155, 156, 157, 159, 162, 163, 164, 166, 167, 169, 171, 174, 176, 177, 179, 181, 182, 183, 184, 185, 187, 189, 190, 191, 192, 193, 194, 197, 198, 199, 205, 206, 208, 209, 210, 214, 215, 218, 220, 221, 223, 225, 226, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 240, 242, 243, 244, 245, 247, 250, 251, 253, 254, 257, 258, 259, 260, 262, 263, 264, 266, 267, 268, 270, 273], "branches": [[93, 96], [93, 253], [97, 98], [97, 101], [105, 106], [105, 109], [114, 115], [114, 119], [126, 127], [126, 225], [127, 128], [127, 130], [141, 142], [141, 162], [142, 143], [142, 162], [153, 142], [153, 154], [154, 155], [154, 159], [166, 167], [166, 169], [169, 171], [169, 174], [182, 183], [182, 185], [185, 187], [185, 220], [197, 198], [197, 205], [208, 209], [208, 214], [220, 221], [220, 223], [225, 226], [225, 229], [229, 230], [229, 250], [230, 231], [230, 247], [234, 235], [234, 247], [235, 236], [235, 237], [237, 238], [237, 240], [244, 245], [244, 247], [250, 93], [250, 251], [253, 254], [253, 257], [257, 258], [257, 259], [259, 260], [259, 262], [262, 263], [262, 266], [266, 267], [266, 273]]}
# gained: {"lines": [78, 84, 85, 86, 87, 89, 90, 91, 93, 96, 97, 101, 103, 105, 109, 111, 114, 119, 120, 122, 123, 124, 126, 127, 130, 133, 136, 137, 138, 141, 162, 163, 164, 166, 169, 174, 176, 177, 179, 181, 182, 183, 184, 185, 220, 223, 225, 229, 230, 247, 250, 253, 257, 258, 259, 260, 262, 266, 273], "branches": [[93, 96], [93, 253], [97, 101], [105, 109], [114, 119], [126, 127], [126, 225], [127, 130], [141, 162], [166, 169], [169, 174], [182, 183], [185, 220], [220, 223], [225, 229], [229, 230], [230, 247], [250, 93], [253, 257], [257, 258], [259, 260], [262, 266], [266, 273]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.executor.playbook_executor import PlaybookExecutor
from ansible.playbook.play import Play
from ansible.playbook import Playbook
from ansible.template import Templar
from ansible import context

@pytest.fixture
def playbook_executor():
    playbooks = ['test_playbook.yml']
    inventory = MagicMock()
    variable_manager = MagicMock()
    loader = MagicMock()
    passwords = MagicMock()
    executor = PlaybookExecutor(playbooks, inventory, variable_manager, loader, passwords)
    executor._tqm = MagicMock()
    executor._tqm._failed_hosts = {}
    executor._tqm._unreachable_hosts = {}
    executor._unreachable_hosts = set()
    return executor

def test_run_playbook_executor(playbook_executor, monkeypatch):
    # Mocking necessary functions and methods
    monkeypatch.setattr('ansible.plugins.loader.connection_loader.all', lambda class_only: [])
    monkeypatch.setattr('ansible.plugins.loader.shell_loader.all', lambda class_only: [])
    monkeypatch.setattr('ansible.plugins.loader.become_loader.all', lambda class_only: [])
    monkeypatch.setattr('ansible.utils.collection_loader._collection_finder._get_collection_playbook_path', lambda x: None)
    monkeypatch.setattr('ansible.utils.collection_loader._collection_finder._get_collection_name_from_path', lambda x: None)
    monkeypatch.setattr('ansible.playbook.Playbook.load', lambda x, variable_manager, loader: MagicMock(get_plays=lambda: [MagicMock(_included_path=None, vars_prompt=[])], _basedir='/tmp'))
    monkeypatch.setattr('ansible.template.Templar.template', lambda self, x: x)
    monkeypatch.setattr('ansible.module_utils.parsing.convert_bool.boolean', lambda x: x)
    monkeypatch.setattr('ansible.executor.task_queue_manager.TaskQueueManager.run', lambda self, play: 0)
    monkeypatch.setattr('ansible.executor.task_queue_manager.TaskQueueManager.send_callback', lambda self, event, *args: None)
    monkeypatch.setattr('ansible.executor.task_queue_manager.TaskQueueManager.load_callbacks', lambda self: None)
    monkeypatch.setattr('ansible.executor.task_queue_manager.TaskQueueManager.cleanup', lambda self: None)
    monkeypatch.setattr('ansible.utils.display.Display.display', lambda self, msg: None)
    monkeypatch.setattr('ansible.utils.display.Display.warning', lambda self, msg: None)
    monkeypatch.setattr('ansible.utils.display.Display.error', lambda self, msg: None)
    monkeypatch.setattr('ansible.utils.display.Display.vv', lambda self, msg: None)
    monkeypatch.setattr('ansible.utils.display.Display.do_var_prompt', lambda self, *args: 'mocked_value')
    monkeypatch.setattr('os.path.dirname', lambda x: '/tmp')
    monkeypatch.setattr('os.path.abspath', lambda x: x)
    monkeypatch.setattr('os.path.splitext', lambda x: ('/tmp/test_playbook', '.yml'))
    monkeypatch.setattr('os.path.join', lambda *args: '/tmp/test_playbook.retry')
    monkeypatch.setattr('os.path.realpath', lambda x: x)
    monkeypatch.setattr('os.path.basename', lambda x: 'test_playbook.yml')
    monkeypatch.setattr('os.path.exists', lambda x: True)
    monkeypatch.setattr('os.remove', lambda x: None)

    context.CLIARGS = {'syntax': False, 'start_at_task': None}

    result = playbook_executor.run()

    assert result == 0
    playbook_executor._tqm.cleanup.assert_called_once()
    playbook_executor._loader.cleanup_all_tmp_files.assert_called_once()
