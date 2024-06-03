# file lib/ansible/plugins/filter/mathstuff.py:179-186
# lines [179, 181, 182, 183, 184, 185, 186]
# branches []

import pytest
from ansible.plugins.filter.mathstuff import human_readable
from ansible.errors import AnsibleFilterTypeError, AnsibleFilterError

def test_human_readable_type_error(mocker):
    mocker.patch('ansible.plugins.filter.mathstuff.formatters.bytes_to_human', side_effect=TypeError("bad input"))
    with pytest.raises(AnsibleFilterTypeError) as excinfo:
        human_readable("invalid_size")
    assert "human_readable() failed on bad input" in str(excinfo.value)

def test_human_readable_general_exception(mocker):
    mocker.patch('ansible.plugins.filter.mathstuff.formatters.bytes_to_human', side_effect=Exception("general error"))
    with pytest.raises(AnsibleFilterError) as excinfo:
        human_readable("another_invalid_size")
    assert "human_readable() can't interpret following string" in str(excinfo.value)
