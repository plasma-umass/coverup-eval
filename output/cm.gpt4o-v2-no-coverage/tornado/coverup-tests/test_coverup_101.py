# file: tornado/options.py:187-208
# asked: {"lines": [187, 204, 205, 206, 207], "branches": []}
# gained: {"lines": [187, 204, 205, 206, 207], "branches": []}

import pytest
from tornado.options import OptionParser

@pytest.fixture
def option_parser():
    parser = OptionParser()
    yield parser
    # Clean up if necessary

def test_group_dict_with_group(option_parser):
    option_parser.define('template_path', group='application', default='/templates')
    option_parser.define('static_path', group='application', default='/static')
    result = option_parser.group_dict('application')
    assert result == {'template_path': '/templates', 'static_path': '/static'}

def test_group_dict_without_group(option_parser):
    option_parser.define('template_path', default='/templates')
    option_parser.define('static_path', default='/static')
    result = option_parser.group_dict('')
    assert 'template_path' in result
    assert 'static_path' in result

def test_group_dict_with_nonexistent_group(option_parser):
    option_parser.define('template_path', group='application', default='/templates')
    result = option_parser.group_dict('nonexistent')
    assert result == {}
