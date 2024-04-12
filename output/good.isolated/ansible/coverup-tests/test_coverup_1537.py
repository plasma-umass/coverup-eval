# file lib/ansible/plugins/action/include_vars.py:218-247
# lines [226, 227, 228, 229, 230, 231, 233, 234, 236, 237, 238, 239, 240, 241, 242, 244, 245, 247]
# branches ['229->230', '229->233', '238->239', '238->240', '240->241', '240->244']

import pytest
from ansible.plugins.action.include_vars import ActionModule
from ansible.parsing.dataloader import DataLoader
from ansible.utils.unsafe_proxy import AnsibleUnsafeText

@pytest.fixture
def action_module(mocker):
    action_module = ActionModule(None, None, None, None, None, None)
    action_module._loader = DataLoader()
    action_module.valid_extensions = ['.yml', '.yaml', '.json']
    action_module.included_files = []
    return action_module

def test_load_files_with_invalid_extension(action_module, mocker, tmp_path):
    invalid_file = tmp_path / "test.invalid"
    invalid_file.write_text(u"invalid content")
    mocker.patch.object(action_module, '_is_valid_file_ext', return_value=False)
    failed, err_msg, results = action_module._load_files(str(invalid_file), validate_extensions=True)
    assert failed
    assert "does not have a valid extension" in err_msg
    assert results == {}

def test_load_files_with_non_dict_content(action_module, mocker, tmp_path):
    non_dict_file = tmp_path / "test.json"
    non_dict_file.write_text(u'"string content"')
    mocker.patch.object(action_module, '_is_valid_file_ext', return_value=True)
    mocker.patch.object(action_module._loader, '_get_file_contents', return_value=(b'"string content"', True))
    mocker.patch.object(action_module._loader, 'load', return_value=AnsibleUnsafeText("string content"))
    failed, err_msg, results = action_module._load_files(str(non_dict_file))
    assert failed
    assert "must be stored as a dictionary/hash" in err_msg
    assert results == {}

def test_load_files_with_valid_dict_content(action_module, mocker, tmp_path):
    valid_dict_file = tmp_path / "test.json"
    valid_dict_file.write_text(u'{"key": "value"}')
    mocker.patch.object(action_module, '_is_valid_file_ext', return_value=True)
    mocker.patch.object(action_module._loader, '_get_file_contents', return_value=(b'{"key": "value"}', True))
    mocker.patch.object(action_module._loader, 'load', return_value={"key": "value"})
    failed, err_msg, results = action_module._load_files(str(valid_dict_file))
    assert not failed
    assert err_msg == ""
    assert results == {"key": "value"}
    assert str(valid_dict_file) in action_module.included_files
