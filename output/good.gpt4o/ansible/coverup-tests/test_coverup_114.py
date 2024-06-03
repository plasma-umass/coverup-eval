# file lib/ansible/cli/arguments/option_helpers.py:50-78
# lines [50, 51, 54, 55, 56, 57, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 75, 76, 77, 78]
# branches ['56->57', '56->60', '60->61', '60->62']

import argparse
import copy
import pytest
from ansible.cli.arguments.option_helpers import PrependListAction

def ensure_value(namespace, name, default):
    if not hasattr(namespace, name):
        setattr(namespace, name, default)
    return getattr(namespace, name)

def test_prepend_list_action_nargs_zero():
    with pytest.raises(ValueError, match=r"nargs for append actions must be > 0; if arg strings are not supplying the value to append, the append const action may be more appropriate"):
        PrependListAction(option_strings=['--test'], dest='test', nargs=0)

def test_prepend_list_action_const_nargs_not_optional():
    with pytest.raises(ValueError, match=r"nargs must be '\?' to supply const"):
        PrependListAction(option_strings=['--test'], dest='test', nargs='+', const='const')

def test_prepend_list_action_call(mocker):
    parser = argparse.ArgumentParser()
    mock_namespace = mocker.Mock()
    action = PrependListAction(option_strings=['--test'], dest='test', nargs='+')
    
    # Mock ensure_value to return a list
    mocker.patch('ansible.cli.arguments.option_helpers.ensure_value', return_value=['existing'])
    
    action(parser, mock_namespace, ['new_value'])
    
    # Ensure the values are prepended
    assert mock_namespace.test == ['new_value', 'existing']

@pytest.fixture(autouse=True)
def cleanup():
    yield
    # Cleanup code if necessary

