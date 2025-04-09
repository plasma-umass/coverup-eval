# file lib/ansible/modules/iptables.py:541-550
# lines [541, 542, 543, 544, 546, 547, 548, 550]
# branches ['542->543', '542->546', '543->exit', '543->544', '546->exit', '546->547', '547->548', '547->550']

import pytest
from unittest import mock

# Assuming the function append_param is part of a class or module, we need to import it.
# For this example, let's assume it's part of a module named `iptables_module`.

def test_append_param(mocker):
    from ansible.modules.iptables import append_param

    # Test case 1: param is a list
    rule = []
    param = ['item1', 'item2']
    flag = '--flag'
    is_list = True
    append_param(rule, param, flag, is_list)
    assert rule == ['--flag', 'item1', '--flag', 'item2']

    # Test case 2: param is not None and starts with '!'
    rule = []
    param = '!value'
    flag = '--flag'
    is_list = False
    append_param(rule, param, flag, is_list)
    assert rule == ['!', '--flag', 'value']

    # Test case 3: param is not None and does not start with '!'
    rule = []
    param = 'value'
    flag = '--flag'
    is_list = False
    append_param(rule, param, flag, is_list)
    assert rule == ['--flag', 'value']

    # Test case 4: param is None
    rule = []
    param = None
    flag = '--flag'
    is_list = False
    append_param(rule, param, flag, is_list)
    assert rule == []

    # Clean up if necessary (not needed in this case as no external state is modified)
