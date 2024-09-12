# file: lib/ansible/plugins/callback/junit.py:205-249
# asked: {"lines": [205, 208, 209, 211, 212, 214, 216, 217, 219, 220, 222, 223, 224, 225, 227, 228, 230, 232, 233, 234, 235, 236, 237, 238, 239, 241, 242, 243, 244, 246, 247, 249], "branches": [[211, 212], [211, 214], [216, 217], [216, 219], [219, 220], [219, 222], [227, 228], [227, 230], [232, 233], [232, 242], [233, 234], [233, 237], [237, 238], [237, 241], [242, 243], [242, 249], [243, 244], [243, 246]]}
# gained: {"lines": [205, 208, 209, 211, 214, 216, 219, 220, 222, 223, 224, 225, 227, 228, 230, 232, 233, 234, 235, 236, 237, 238, 239, 241, 242, 243, 244, 246, 247, 249], "branches": [[211, 214], [216, 219], [219, 220], [219, 222], [227, 228], [227, 230], [232, 233], [232, 242], [233, 234], [233, 237], [237, 238], [237, 241], [242, 243], [243, 244], [243, 246]]}

import pytest
from unittest.mock import Mock, patch
from ansible.plugins.callback.junit import CallbackModule
from ansible.utils._junit_xml import TestCase, TestError, TestFailure

@pytest.fixture
def task_data():
    mock = Mock()
    mock.play = "test_play"
    mock.name = "test_task"
    mock.path = "/path/to/task"
    mock.start = 1.0
    return mock

@pytest.fixture
def host_data():
    mock = Mock()
    mock.name = "test_host"
    mock.finish = 2.0
    mock.status = "ok"
    mock.result = Mock()
    mock.result._result = {"rc": 0, "msg": "All good"}
    return mock

@pytest.fixture
def callback_module():
    module = CallbackModule()
    module._task_relative_path = None
    module._task_class = 'false'
    module._dump_results = Mock(return_value="dumped results")
    module._cleanse_string = Mock(return_value="cleansed results")
    return module

def test_build_test_case_ok(callback_module, task_data, host_data):
    host_data.status = 'ok'
    test_case = callback_module._build_test_case(task_data, host_data)
    assert isinstance(test_case, TestCase)
    assert test_case.name == '[test_host] test_play: test_task'
    assert test_case.classname == '/path/to/task'
    assert test_case.time == 1.0
    assert test_case.system_out == 'cleansed results'

def test_build_test_case_failed_with_exception(callback_module, task_data, host_data):
    host_data.status = 'failed'
    host_data.result._result = {'exception': 'Traceback (most recent call last):\nException: error message'}
    test_case = callback_module._build_test_case(task_data, host_data)
    assert isinstance(test_case, TestCase)
    assert len(test_case.errors) == 1
    assert test_case.errors[0].message == 'Exception: error message'
    assert test_case.errors[0].output == 'Traceback (most recent call last):\nException: error message'

def test_build_test_case_failed_with_msg(callback_module, task_data, host_data):
    host_data.status = 'failed'
    host_data.result._result = {'msg': 'failure message'}
    test_case = callback_module._build_test_case(task_data, host_data)
    assert isinstance(test_case, TestCase)
    assert len(test_case.failures) == 1
    assert test_case.failures[0].message == 'failure message'
    assert test_case.failures[0].output == 'cleansed results'

def test_build_test_case_failed_with_rc(callback_module, task_data, host_data):
    host_data.status = 'failed'
    host_data.result._result = {}
    test_case = callback_module._build_test_case(task_data, host_data)
    assert isinstance(test_case, TestCase)
    assert len(test_case.failures) == 1
    assert test_case.failures[0].message == 'rc=0'
    assert test_case.failures[0].output == 'cleansed results'

def test_build_test_case_skipped_with_reason(callback_module, task_data, host_data):
    host_data.status = 'skipped'
    host_data.result._result = {'skip_reason': 'not applicable'}
    test_case = callback_module._build_test_case(task_data, host_data)
    assert isinstance(test_case, TestCase)
    assert test_case.skipped == 'not applicable'

def test_build_test_case_skipped_without_reason(callback_module, task_data, host_data):
    host_data.status = 'skipped'
    host_data.result._result = {}
    test_case = callback_module._build_test_case(task_data, host_data)
    assert isinstance(test_case, TestCase)
    assert test_case.skipped == 'skipped'

def test_build_test_case_included(callback_module, task_data, host_data):
    host_data.status = 'included'
    test_case = callback_module._build_test_case(task_data, host_data)
    assert isinstance(test_case, TestCase)
    assert test_case.system_out == str(host_data.result)
