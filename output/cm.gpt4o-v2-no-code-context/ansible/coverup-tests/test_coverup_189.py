# file: lib/ansible/utils/singleton.py:11-29
# asked: {"lines": [11, 12, 16, 17, 18, 19, 21, 22, 23, 25, 26, 27, 29], "branches": [[22, 23], [22, 25], [26, 27], [26, 29]]}
# gained: {"lines": [11, 12, 16, 17, 18, 19, 21, 22, 23, 25, 26, 27, 29], "branches": [[22, 23], [22, 25], [26, 27]]}

import pytest
from threading import RLock

# Assuming the Singleton class is defined in ansible/utils/singleton.py
from ansible.utils.singleton import Singleton

class TestSingleton(metaclass=Singleton):
    def __init__(self, value):
        self.value = value

def test_singleton_instance_creation():
    instance1 = TestSingleton(1)
    instance2 = TestSingleton(2)
    
    assert instance1 is instance2
    assert instance1.value == 1
    assert instance2.value == 1

def test_singleton_thread_safety(mocker):
    # Mock RLock to ensure thread safety is tested
    mock_rlock = mocker.patch('ansible.utils.singleton.RLock', return_value=RLock())

    instance1 = TestSingleton(1)
    instance2 = TestSingleton(2)
    
    assert instance1 is instance2
    assert instance1.value == 1
    assert instance2.value == 1

@pytest.fixture(autouse=True)
def cleanup_singleton():
    # Cleanup Singleton instance to avoid state pollution
    yield
    TestSingleton._Singleton__instance = None
