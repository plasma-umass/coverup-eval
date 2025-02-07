# file: lib/ansible/modules/expect.py:126-138
# asked: {"lines": [126, 127, 129, 130, 131, 132, 133, 135, 136, 138], "branches": []}
# gained: {"lines": [126, 127, 129, 130, 131, 132, 133, 135, 136, 138], "branches": []}

import pytest
from ansible.module_utils._text import to_bytes
from ansible.modules.expect import response_closure

class MockModule:
    def fail_json(self, **kwargs):
        raise Exception(kwargs['msg'])

def test_response_closure():
    module = MockModule()
    question = "What is your name?"
    responses = ["Alice", "Bob"]

    wrapped = response_closure(module, question, responses)

    # Test normal response
    info = {'child_result_list': ['']}
    assert wrapped(info) == b'Alice\n'
    assert wrapped(info) == b'Bob\n'

    # Test StopIteration and fail_json
    with pytest.raises(Exception) as excinfo:
        wrapped(info)
    assert str(excinfo.value) == "No remaining responses for 'What is your name?', output was ''"
