# file: lib/ansible/plugins/filter/urls.py:26-27
# asked: {"lines": [26, 27], "branches": []}
# gained: {"lines": [26, 27], "branches": []}

import pytest
from ansible.plugins.filter.urls import do_urldecode
from ansible.module_utils.six import PY3

@pytest.mark.parametrize("input_string, expected_output", [
    ("hello%20world", "hello world"),
    ("a%2Bb%3Dc", "a+b=c"),
    ("", ""),
])
def test_do_urldecode(input_string, expected_output):
    assert do_urldecode(input_string) == expected_output

def test_do_urldecode_py2(mocker):
    if PY3:
        pytest.skip("This test is for Python 2 only")
    
    mocker.patch('ansible.plugins.filter.urls.PY3', False)
    mocker.patch('ansible.plugins.filter.urls.to_bytes', side_effect=lambda x: x.encode('utf-8'))
    mocker.patch('ansible.plugins.filter.urls.to_text', side_effect=lambda x: x.decode('utf-8'))
    
    input_string = "hello%20world"
    expected_output = "hello world"
    assert do_urldecode(input_string) == expected_output
