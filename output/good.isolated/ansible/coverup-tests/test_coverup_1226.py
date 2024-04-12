# file lib/ansible/modules/iptables.py:541-550
# lines [542, 543, 544, 546, 547, 548, 550]
# branches ['542->543', '542->546', '543->exit', '543->544', '546->exit', '546->547', '547->548', '547->550']

import pytest

# Assuming the actual iptables module is imported as iptables_module
# Replace 'iptables_module' with the actual module name if different
from ansible.modules.iptables import append_param

@pytest.fixture
def cleanup_rules():
    # Assuming there's a cleanup function in the iptables module, mock it
    # Replace 'cleanup_function' with the actual cleanup function name if different
    # If there's no cleanup function, this fixture can be omitted
    yield
    # Here you would call the cleanup function if it exists

def test_append_param_with_list(cleanup_rules):
    rule = []
    param = ['value1', '!value2']
    flag = '--test-flag'
    is_list = True

    append_param(rule, param, flag, is_list)

    assert rule == ['--test-flag', 'value1', '!', '--test-flag', 'value2']

def test_append_param_with_negation(cleanup_rules):
    rule = []
    param = '!value'
    flag = '--test-flag'
    is_list = False

    append_param(rule, param, flag, is_list)

    assert rule == ['!', '--test-flag', 'value']

def test_append_param_without_negation(cleanup_rules):
    rule = []
    param = 'value'
    flag = '--test-flag'
    is_list = False

    append_param(rule, param, flag, is_list)

    assert rule == ['--test-flag', 'value']
