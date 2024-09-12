# file: tornado/queues.py:336-346
# asked: {"lines": [339, 341, 343, 345], "branches": [[338, 339], [340, 341], [342, 343], [344, 345]]}
# gained: {"lines": [339, 341, 343, 345], "branches": [[338, 339], [340, 341], [342, 343], [344, 345]]}

import pytest
from tornado.queues import Queue

@pytest.fixture
def queue():
    return Queue(maxsize=10)

def test_format_empty_queue(queue):
    assert queue._format() == "maxsize=10"

def test_format_with_queue(queue, monkeypatch):
    monkeypatch.setattr(queue, "_queue", [1, 2, 3])
    assert queue._format() == "maxsize=10 queue=[1, 2, 3]"

def test_format_with_getters(queue, monkeypatch):
    monkeypatch.setattr(queue, "_getters", [1, 2])
    assert queue._format() == "maxsize=10 getters[2]"

def test_format_with_putters(queue, monkeypatch):
    monkeypatch.setattr(queue, "_putters", [1, 2, 3])
    assert queue._format() == "maxsize=10 putters[3]"

def test_format_with_unfinished_tasks(queue, monkeypatch):
    monkeypatch.setattr(queue, "_unfinished_tasks", 5)
    assert queue._format() == "maxsize=10 tasks=5"

def test_format_full(queue, monkeypatch):
    monkeypatch.setattr(queue, "_queue", [1, 2, 3])
    monkeypatch.setattr(queue, "_getters", [1, 2])
    monkeypatch.setattr(queue, "_putters", [1, 2, 3])
    monkeypatch.setattr(queue, "_unfinished_tasks", 5)
    assert queue._format() == "maxsize=10 queue=[1, 2, 3] getters[2] putters[3] tasks=5"
