# file lib/ansible/plugins/action/copy.py:50-52
# lines [50, 52]
# branches []

import pytest
from ansible.plugins.action.copy import _create_remote_copy_args

def test_create_remote_copy_args():
    module_args = {
        'src': '/path/to/source',
        'dest': '/path/to/destination',
        'content': 'some content',
        'decrypt': True,
        'mode': '0644'
    }
    
    expected_result = {
        'src': '/path/to/source',
        'dest': '/path/to/destination',
        'mode': '0644'
    }
    
    result = _create_remote_copy_args(module_args)
    
    assert result == expected_result

@pytest.fixture(autouse=True)
def cleanup():
    # Cleanup code if necessary
    yield
    # Post-test cleanup code if necessary
