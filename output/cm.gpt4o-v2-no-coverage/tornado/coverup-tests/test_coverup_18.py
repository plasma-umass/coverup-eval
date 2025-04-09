# file: tornado/queues.py:336-346
# asked: {"lines": [336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346], "branches": [[338, 339], [338, 340], [340, 341], [340, 342], [342, 343], [342, 344], [344, 345], [344, 346]]}
# gained: {"lines": [336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346], "branches": [[338, 339], [338, 340], [340, 341], [340, 342], [342, 343], [342, 344], [344, 345], [344, 346]]}

import pytest
from tornado.queues import Queue

@pytest.fixture
def queue():
    return Queue(maxsize=10)

def test_format_empty_queue(queue):
    expected = "maxsize=10"
    assert queue._format() == expected

def test_format_with_queue(queue, monkeypatch):
    monkeypatch.setattr(queue, "_queue", [1, 2, 3])
    expected = "maxsize=10 queue=[1, 2, 3]"
    assert queue._format() == expected

def test_format_with_getters(queue, monkeypatch):
    monkeypatch.setattr(queue, "_getters", [1, 2])
    expected = "maxsize=10 getters[2]"
    assert queue._format() == expected

def test_format_with_putters(queue, monkeypatch):
    monkeypatch.setattr(queue, "_putters", [1])
    expected = "maxsize=10 putters[1]"
    assert queue._format() == expected

def test_format_with_unfinished_tasks(queue, monkeypatch):
    monkeypatch.setattr(queue, "_unfinished_tasks", 5)
    expected = "maxsize=10 tasks=5"
    assert queue._format() == expected

def test_format_combined(queue, monkeypatch):
    monkeypatch.setattr(queue, "_queue", [1, 2, 3])
    monkeypatch.setattr(queue, "_getters", [1, 2])
    monkeypatch.setattr(queue, "_putters", [1])
    monkeypatch.setattr(queue, "_unfinished_tasks", 5)
    expected = "maxsize=10 queue=[1, 2, 3] getters[2] putters[1] tasks=5"
    assert queue._format() == expected
