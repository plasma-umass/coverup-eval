# file: lib/ansible/modules/iptables.py:566-568
# asked: {"lines": [567, 568], "branches": [[567, 0], [567, 568]]}
# gained: {"lines": [567, 568], "branches": [[567, 0], [567, 568]]}

import pytest
from unittest.mock import patch

# Assuming the append_csv function is part of a class or module, we need to import it.
# For this example, let's assume it's a standalone function in a module named iptables.

from ansible.modules.iptables import append_csv

def test_append_csv_with_param():
    rule = []
    param = ['value1', 'value2']
    flag = '--flag'
    
    append_csv(rule, param, flag)
    
    assert rule == ['--flag', 'value1,value2']

def test_append_csv_without_param():
    rule = []
    param = None
    flag = '--flag'
    
    append_csv(rule, param, flag)
    
    assert rule == []

# Clean up after tests if necessary
@pytest.fixture(autouse=True)
def cleanup():
    yield
    # Perform any necessary cleanup here
