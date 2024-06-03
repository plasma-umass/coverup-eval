# file lib/ansible/modules/iptables.py:566-568
# lines [566, 567, 568]
# branches ['567->exit', '567->568']

import pytest
from unittest.mock import patch

# Assuming the append_csv function is part of a class or module, we need to import it correctly.
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

# Clean up is not necessary in this case as the function does not modify any external state.
