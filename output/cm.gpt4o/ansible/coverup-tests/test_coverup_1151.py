# file lib/ansible/modules/expect.py:126-138
# lines [126, 127, 129, 130, 131, 132, 133, 135, 136, 138]
# branches []

import pytest
from ansible.module_utils.basic import AnsibleModule
from ansible.modules.expect import response_closure

def test_response_closure_exhausted_responses(mocker):
    # Mocking AnsibleModule
    module = mocker.Mock(spec=AnsibleModule)
    module.fail_json = mocker.Mock()

    # Define question and responses
    question = "What is your name?"
    responses = ["Alice", "Bob"]

    # Create the response closure
    wrapped = response_closure(module, question, responses)

    # Simulate the info dictionary
    info = {'child_result_list': ['Alice', 'Bob']}

    # Call wrapped to exhaust responses
    assert wrapped(info) == b'Alice\n'
    assert wrapped(info) == b'Bob\n'

    # Now the responses are exhausted, this should trigger fail_json
    wrapped(info)

    # Verify that fail_json was called with the expected message
    module.fail_json.assert_called_once_with(
        msg="No remaining responses for 'What is your name?', output was 'Bob'"
    )
