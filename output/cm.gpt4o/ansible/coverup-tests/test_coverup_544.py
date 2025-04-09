# file lib/ansible/module_utils/urls.py:658-670
# lines [658, 659, 662, 663, 664, 666, 670]
# branches []

import pytest
from ansible.module_utils.urls import ParseResultDottedDict

def test_parse_result_dotted_dict():
    # Create an instance of ParseResultDottedDict with some test data
    data = {
        'scheme': 'http',
        'netloc': 'example.com',
        'path': '/index.html',
        'params': '',
        'query': 'a=1&b=2',
        'fragment': 'section1'
    }
    parse_result = ParseResultDottedDict(data)

    # Verify that the dictionary is correctly initialized
    assert parse_result['scheme'] == 'http'
    assert parse_result['netloc'] == 'example.com'
    assert parse_result['path'] == '/index.html'
    assert parse_result['params'] == ''
    assert parse_result['query'] == 'a=1&b=2'
    assert parse_result['fragment'] == 'section1'

    # Verify that the as_list method returns the correct list
    expected_list = ['http', 'example.com', '/index.html', '', 'a=1&b=2', 'section1']
    assert parse_result.as_list() == expected_list

    # Verify that the __dict__ attribute is correctly set
    assert parse_result.__dict__ == parse_result

    # Clean up (not strictly necessary in this case, but good practice)
    del parse_result

@pytest.fixture(autouse=True)
def cleanup():
    yield
    # Perform any necessary cleanup here
