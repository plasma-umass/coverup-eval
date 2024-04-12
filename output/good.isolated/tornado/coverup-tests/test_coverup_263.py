# file tornado/options.py:187-208
# lines [204, 205, 206, 207]
# branches []

import pytest
from tornado.options import OptionParser, define, options

@pytest.fixture
def option_parser():
    parser = OptionParser()
    yield parser
    parser._options.clear()

def test_group_dict_with_group(option_parser):
    option_parser.define('option1', default='value1', group='group1')
    option_parser.define('option2', default='value2', group='group2')
    option_parser.define('option3', default='value3', group='group1')

    group_dict = option_parser.group_dict('group1')
    assert 'option1' in group_dict
    assert 'option3' in group_dict
    assert 'option2' not in group_dict
    assert group_dict['option1'] == 'value1'
    assert group_dict['option3'] == 'value3'

    # Cleanup after test
    option_parser._options.clear()

def test_group_dict_without_group(option_parser):
    option_parser.define('option1', default='value1')
    option_parser.define('option2', default='value2')

    group_dict = option_parser.group_dict(None)
    assert 'option1' in group_dict
    assert 'option2' in group_dict
    assert group_dict['option1'] == 'value1'
    assert group_dict['option2'] == 'value2'

    # Cleanup after test
    option_parser._options.clear()
