# file lib/ansible/modules/replace.py:192-210
# lines [203]
# branches ['202->203']

import os
import pytest
import tempfile
from ansible.modules.replace import write_changes

def test_write_changes_without_percent_s_in_validate(mocker):
    module_mock = mocker.MagicMock()
    module_mock.params = {
        'validate': '/usr/bin/validate_script',
        'unsafe_writes': False
    }
    module_mock.tmpdir = tempfile.gettempdir()
    module_mock.fail_json.side_effect = Exception('validate must contain %s')

    contents = b"Sample contents"
    path = os.path.join(tempfile.gettempdir(), "testfile")

    with pytest.raises(Exception) as excinfo:
        write_changes(module_mock, contents, path)
    assert "validate must contain %s" in str(excinfo.value)

    # Cleanup
    if os.path.exists(path):
        os.remove(path)
