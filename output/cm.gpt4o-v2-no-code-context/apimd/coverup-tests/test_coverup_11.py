# file: apimd/loader.py:30-33
# asked: {"lines": [30, 32, 33], "branches": []}
# gained: {"lines": [30, 32, 33], "branches": []}

import pytest
import os

from apimd.loader import _write

def test_write_creates_file(monkeypatch, tmp_path):
    test_path = tmp_path / "test_file.txt"
    test_doc = "This is a test document."

    _write(str(test_path), test_doc)

    assert test_path.exists()
    with open(test_path, 'r', encoding='utf-8') as f:
        content = f.read()
    assert content == test_doc

def test_write_overwrites_file(monkeypatch, tmp_path):
    test_path = tmp_path / "test_file.txt"
    initial_doc = "Initial content."
    new_doc = "New content."

    with open(test_path, 'w', encoding='utf-8') as f:
        f.write(initial_doc)

    _write(str(test_path), new_doc)

    with open(test_path, 'r', encoding='utf-8') as f:
        content = f.read()
    assert content == new_doc
