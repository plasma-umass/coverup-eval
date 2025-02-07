# file: tornado/options.py:187-208
# asked: {"lines": [204, 205, 206, 207], "branches": []}
# gained: {"lines": [204, 205, 206, 207], "branches": []}

import pytest
from tornado.options import OptionParser

@pytest.fixture
def option_parser():
    parser = OptionParser()
    # Remove the 'help' option to avoid interference in tests
    del parser._options['help']
    return parser

def test_group_dict_with_group(option_parser):
    option_parser.define('template_path', group='application', default='/templates')
    option_parser.define('static_path', group='application', default='/static')
    result = option_parser.group_dict('application')
    assert result == {'template_path': '/templates', 'static_path': '/static'}

def test_group_dict_without_group(option_parser):
    option_parser.define('debug', default=True)
    option_parser.define('logging', default='info')
    result = option_parser.group_dict('')
    assert result == {'debug': True, 'logging': 'info'}
