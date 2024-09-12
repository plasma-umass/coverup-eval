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

def test_singleton_thread_safety(monkeypatch):
    import threading

    def mock_rlock():
        return RLock()

    monkeypatch.setattr('ansible.utils.singleton.RLock', mock_rlock)

    def create_instance(value):
        return TestSingleton(value)

    thread1 = threading.Thread(target=create_instance, args=(1,))
    thread2 = threading.Thread(target=create_instance, args=(2,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    instance1 = TestSingleton(1)
    instance2 = TestSingleton(2)

    assert instance1 is instance2
    assert instance1.value == 1
    assert instance2.value == 1
