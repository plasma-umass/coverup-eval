# file lib/ansible/modules/apt_repository.py:366-369
# lines [367, 368, 369]
# branches ['367->368', '367->369']

import pytest
from ansible.modules.apt_repository import SourcesList

@pytest.fixture
def sources_list(mocker):
    mock_module = mocker.Mock()
    mock_apt_pkg = mocker.patch('ansible.modules.apt_repository.apt_pkg', autospec=True)
    mock_apt_pkg.config.find_file.return_value = '/dev/null'
    return SourcesList(mock_module)

def test_choice_new_is_none(sources_list):
    old_value = "old_value"
    new_value = None
    result = sources_list._choice(new_value, old_value)
    assert result == old_value, "Expected old value to be returned when new value is None"

def test_choice_new_is_not_none(sources_list):
    old_value = "old_value"
    new_value = "new_value"
    result = sources_list._choice(new_value, old_value)
    assert result == new_value, "Expected new value to be returned when new value is not None"
