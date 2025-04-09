# file lib/ansible/cli/arguments/option_helpers.py:50-78
# lines [50, 51, 54, 55, 56, 57, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 75, 76, 77, 78]
# branches ['56->57', '56->60', '60->61', '60->62']

import argparse
import pytest
from ansible.cli.arguments.option_helpers import PrependListAction

def test_prepend_list_action_nargs_zero():
    with pytest.raises(ValueError) as excinfo:
        PrependListAction(option_strings=['--test'], dest='test', nargs=0)
    assert 'nargs for append actions must be > 0' in str(excinfo.value)

def test_prepend_list_action_const_with_incorrect_nargs():
    with pytest.raises(ValueError) as excinfo:
        PrependListAction(option_strings=['--test'], dest='test', nargs=2, const='value')
    assert 'nargs must be %r to supply const' % argparse.OPTIONAL in str(excinfo.value)

def test_prepend_list_action_call(mocker):
    parser = mocker.MagicMock()
    namespace = argparse.Namespace()
    action = PrependListAction(option_strings=['--test'], dest='test', nargs='+')
    action(parser, namespace, ['value1', 'value2'], option_string='--test')
    assert getattr(namespace, 'test') == ['value1', 'value2']

    # Call the action again to ensure values are prepended
    action(parser, namespace, ['value3'], option_string='--test')
    assert getattr(namespace, 'test') == ['value3', 'value1', 'value2']
