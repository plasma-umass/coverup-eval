# file lib/ansible/modules/expect.py:126-138
# lines [126, 127, 129, 130, 131, 132, 133, 135, 136, 138]
# branches []

import pytest
from ansible.module_utils.basic import AnsibleModule
from ansible.modules.expect import response_closure

def test_response_closure_with_no_remaining_responses(mocker):
    # Mock the AnsibleModule to avoid side effects
    mock_module = mocker.MagicMock(spec=AnsibleModule)
    mock_module.fail_json.side_effect = Exception("No remaining responses")

    # Define a question and responses
    question = "What is your name?"
    responses = ["Arthur", "King of the Britons"]

    # Create the closure with the mock module, question, and responses
    closure = response_closure(mock_module, question, responses)

    # Simulate the responses being used
    info = {'child_result_list': ['Arthur\n', 'King of the Britons\n']}
    assert closure(info) == b'Arthur\n'
    assert closure(info) == b'King of the Britons\n'

    # Now there should be no remaining responses, so it should raise an exception
    with pytest.raises(Exception) as exc_info:
        closure(info)
    assert str(exc_info.value) == "No remaining responses"

    # Verify that the mock module's fail_json method was called with the correct message
    mock_module.fail_json.assert_called_once_with(
        msg="No remaining responses for 'What is your name?', output was 'King of the Britons\n'"
    )
