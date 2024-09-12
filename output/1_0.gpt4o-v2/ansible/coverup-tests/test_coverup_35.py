# file: lib/ansible/playbook/handler.py:27-59
# asked: {"lines": [27, 29, 31, 32, 34, 36, 38, 40, 42, 43, 44, 45, 47, 48, 49, 50, 51, 53, 54, 56, 57, 58, 59], "branches": [[48, 49], [48, 51]]}
# gained: {"lines": [27, 29, 31, 32, 34, 36, 38, 40, 42, 43, 44, 45, 47, 48, 49, 50, 51, 53, 54, 56, 57, 58, 59], "branches": [[48, 49], [48, 51]]}

import pytest
from ansible.playbook.handler import Handler
from ansible.playbook.attribute import FieldAttribute
from ansible.playbook.task import Task

@pytest.fixture
def handler():
    return Handler()

def test_handler_init(handler):
    assert handler.notified_hosts == []
    assert handler.cached_name is False

def test_handler_repr(handler, mocker):
    mocker.patch.object(handler, 'get_name', return_value='test_handler')
    assert repr(handler) == "HANDLER: test_handler"

def test_handler_load(mocker):
    data = {}
    mocker.patch('ansible.playbook.handler.Handler.load_data', return_value='loaded_data')
    handler = Handler.load(data)
    assert handler == 'loaded_data'

def test_handler_notify_host(handler):
    host = 'localhost'
    assert handler.notify_host(host) is True
    assert handler.notified_hosts == [host]
    assert handler.notify_host(host) is False

def test_handler_is_host_notified(handler):
    host = 'localhost'
    handler.notified_hosts.append(host)
    assert handler.is_host_notified(host) is True
    assert handler.is_host_notified('other_host') is False

def test_handler_serialize(handler, mocker):
    mocker.patch('ansible.playbook.task.Task.serialize', return_value={})
    result = handler.serialize()
    assert result['is_handler'] is True
