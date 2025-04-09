# file: lib/ansible/modules/expect.py:126-138
# asked: {"lines": [126, 127, 129, 130, 131, 132, 133, 135, 136, 138], "branches": []}
# gained: {"lines": [126, 127, 129, 130, 131, 132, 133, 135, 136, 138], "branches": []}

import pytest
from unittest.mock import Mock
from ansible.module_utils._text import to_bytes
from ansible.modules.expect import response_closure

def test_response_closure_with_responses():
    module = Mock()
    question = "What is your name?"
    responses = ["Alice", "Bob"]
    info = {'child_result_list': ["Alice", "Bob"]}

    wrapped = response_closure(module, question, responses)
    
    assert wrapped(info) == b'Alice\n'
    assert wrapped(info) == b'Bob\n'

def test_response_closure_no_remaining_responses():
    module = Mock()
    module.fail_json = Mock()
    question = "What is your name?"
    responses = ["Alice"]
    info = {'child_result_list': ["Alice"]}

    wrapped = response_closure(module, question, responses)
    
    assert wrapped(info) == b'Alice\n'
    wrapped(info)  # This should trigger StopIteration and call module.fail_json
    module.fail_json.assert_called_once_with(msg="No remaining responses for 'What is your name?', output was 'Alice'")

