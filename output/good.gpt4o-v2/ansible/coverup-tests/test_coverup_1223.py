# file: lib/ansible/cli/doc.py:55-60
# asked: {"lines": [56, 57, 58, 59, 60], "branches": []}
# gained: {"lines": [56, 57, 58, 59, 60], "branches": []}

import pytest
from unittest.mock import patch, Mock
from ansible.errors import AnsibleError
from ansible.module_utils._text import to_native
from ansible.module_utils.common.json import AnsibleJSONEncoder
import json
import traceback

# Assuming jdump is imported from ansible.cli.doc
from ansible.cli.doc import jdump

def test_jdump_success(monkeypatch):
    mock_display = Mock()
    monkeypatch.setattr('ansible.cli.doc.display.display', mock_display)
    
    test_data = {"key": "value"}
    jdump(test_data)
    
    mock_display.assert_called_once_with(json.dumps(test_data, cls=AnsibleJSONEncoder, sort_keys=True, indent=4))

def test_jdump_type_error(monkeypatch):
    mock_display_vvv = Mock()
    monkeypatch.setattr('ansible.cli.doc.display.vvv', mock_display_vvv)
    
    invalid_data = set([1, 2, 3])  # sets are not JSON serializable
    
    with pytest.raises(AnsibleError) as excinfo:
        jdump(invalid_data)
    
    mock_display_vvv.assert_called_once()
    assert 'We could not convert all the documentation into JSON as there was a conversion issue' in str(excinfo.value)
