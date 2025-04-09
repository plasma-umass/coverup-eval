# file lib/ansible/playbook/task_include.py:90-102
# lines [91, 93, 94, 96, 97, 98, 100, 102]
# branches ['94->96', '94->102', '96->94', '96->97', '97->98', '97->100']

import pytest
from ansible.errors import AnsibleParserError
from ansible.playbook.task_include import TaskInclude
from ansible.utils.sentinel import Sentinel

# Mocking the necessary Ansible constants and classes
class MockConstants:
    _ACTION_ALL_INCLUDE_ROLE_TASKS = ['include_role', 'include_tasks']
    INVALID_TASK_ATTRIBUTE_FAILED = True

@pytest.fixture
def task_include():
    return TaskInclude()

def test_preprocess_data_with_invalid_attribute_and_failure_enabled(mocker, task_include):
    # Set up the constants and the data structure (ds)
    constants_mock = mocker.patch('ansible.playbook.task_include.C', new=MockConstants)
    ds = {'action': 'include_tasks', 'name': 'test', 'invalid_attr': 'value', 'another_invalid': Sentinel}

    # Expecting an AnsibleParserError to be raised due to invalid attributes
    with pytest.raises(AnsibleParserError) as excinfo:
        task_include.preprocess_data(ds)
    assert "'invalid_attr' is not a valid attribute for a TaskInclude" in str(excinfo.value)

    # Ensure that the 'another_invalid' attribute with Sentinel value is ignored and does not raise an error
    ds = {'action': 'include_tasks', 'name': 'test', 'another_invalid': Sentinel}
    try:
        task_include.preprocess_data(ds)
    except AnsibleParserError:
        pytest.fail("AnsibleParserError raised unexpectedly!")

def test_preprocess_data_with_invalid_attribute_and_failure_disabled(mocker, task_include):
    # Set up the constants and the data structure (ds)
    constants_mock = mocker.patch('ansible.playbook.task_include.C', new=MockConstants)
    constants_mock.INVALID_TASK_ATTRIBUTE_FAILED = False
    ds = {'action': 'include_tasks', 'name': 'test', 'invalid_attr': 'value'}

    # Mock the display.warning to check if it's called with the expected message
    mock_warning = mocker.patch('ansible.playbook.task_include.display.warning')

    # Process the data structure
    result_ds = task_include.preprocess_data(ds)

    # Check that the warning was displayed for the invalid attribute
    mock_warning.assert_called_once_with("Ignoring invalid attribute: invalid_attr")

    # Check that the invalid attribute is still in the result_ds since it's just a warning
    assert 'invalid_attr' in result_ds
