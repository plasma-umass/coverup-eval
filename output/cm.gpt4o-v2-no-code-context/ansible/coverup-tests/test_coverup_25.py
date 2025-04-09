# file: lib/ansible/plugins/callback/junit.py:205-249
# asked: {"lines": [205, 208, 209, 211, 212, 214, 216, 217, 219, 220, 222, 223, 224, 225, 227, 228, 230, 232, 233, 234, 235, 236, 237, 238, 239, 241, 242, 243, 244, 246, 247, 249], "branches": [[211, 212], [211, 214], [216, 217], [216, 219], [219, 220], [219, 222], [227, 228], [227, 230], [232, 233], [232, 242], [233, 234], [233, 237], [237, 238], [237, 241], [242, 243], [242, 249], [243, 244], [243, 246]]}
# gained: {"lines": [205, 208, 209, 211, 214, 216, 219, 220, 222, 223, 224, 225, 227, 228, 230, 232, 233, 234, 235, 236, 237, 238, 239, 241, 242, 243, 244, 246, 247, 249], "branches": [[211, 214], [216, 219], [219, 220], [219, 222], [227, 228], [227, 230], [232, 233], [232, 242], [233, 234], [233, 237], [237, 238], [237, 241], [242, 243], [243, 244], [243, 246]]}

import pytest
from unittest.mock import Mock, patch
from ansible.plugins.callback.junit import CallbackModule
from junit_xml import TestCase, TestSuite

@pytest.fixture
def callback_module():
    return CallbackModule()

@pytest.fixture
def task_data():
    mock_task_data = Mock()
    mock_task_data.play = "play"
    mock_task_data.name = "name"
    mock_task_data.path = "/path/to/task.yml"
    mock_task_data.start = 0
    return mock_task_data

@pytest.fixture
def host_data():
    mock_host_data = Mock()
    mock_host_data.name = "host"
    mock_host_data.finish = 10
    mock_host_data.result = Mock()
    return mock_host_data

def test_build_test_case_included(callback_module, task_data, host_data):
    host_data.status = 'included'
    host_data.result = "result"
    
    test_case = callback_module._build_test_case(task_data, host_data)
    
    assert test_case.name == "[host] play: name"
    assert test_case.classname == "/path/to/task.yml"
    assert test_case.time == 10
    assert test_case.system_out == "result"

def test_build_test_case_ok(callback_module, task_data, host_data):
    host_data.status = 'ok'
    host_data.result._result = {'rc': 0}
    
    with patch.object(callback_module, '_dump_results', return_value="dumped results"):
        with patch.object(callback_module, '_cleanse_string', return_value="cleansed results"):
            test_case = callback_module._build_test_case(task_data, host_data)
    
    assert test_case.name == "[host] play: name"
    assert test_case.classname == "/path/to/task.yml"
    assert test_case.time == 10
    assert test_case.system_out == "cleansed results"

def test_build_test_case_failed_with_exception(callback_module, task_data, host_data):
    host_data.status = 'failed'
    host_data.result._result = {'exception': 'Exception: error\nTraceback'}
    
    with patch.object(callback_module, '_dump_results', return_value="dumped results"):
        with patch.object(callback_module, '_cleanse_string', return_value="cleansed results"):
            test_case = callback_module._build_test_case(task_data, host_data)
    
    assert test_case.errors[0].message == "Traceback"
    assert test_case.errors[0].output == "Exception: error\nTraceback"

def test_build_test_case_failed_with_msg(callback_module, task_data, host_data):
    host_data.status = 'failed'
    host_data.result._result = {'msg': 'failure message'}
    
    with patch.object(callback_module, '_dump_results', return_value="dumped results"):
        with patch.object(callback_module, '_cleanse_string', return_value="cleansed results"):
            test_case = callback_module._build_test_case(task_data, host_data)
    
    assert test_case.failures[0].message == "failure message"
    assert test_case.failures[0].output == "cleansed results"

def test_build_test_case_failed_with_rc(callback_module, task_data, host_data):
    host_data.status = 'failed'
    host_data.result._result = {}
    
    with patch.object(callback_module, '_dump_results', return_value="dumped results"):
        with patch.object(callback_module, '_cleanse_string', return_value="cleansed results"):
            test_case = callback_module._build_test_case(task_data, host_data)
    
    assert test_case.failures[0].message == "rc=0"
    assert test_case.failures[0].output == "cleansed results"

def test_build_test_case_skipped_with_reason(callback_module, task_data, host_data):
    host_data.status = 'skipped'
    host_data.result._result = {'skip_reason': 'reason'}
    
    test_case = callback_module._build_test_case(task_data, host_data)
    
    assert test_case.skipped == "reason"

def test_build_test_case_skipped_without_reason(callback_module, task_data, host_data):
    host_data.status = 'skipped'
    host_data.result._result = {}
    
    test_case = callback_module._build_test_case(task_data, host_data)
    
    assert test_case.skipped == "skipped"
