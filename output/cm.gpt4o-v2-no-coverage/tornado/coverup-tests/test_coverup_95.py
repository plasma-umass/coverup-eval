# file: tornado/options.py:466-468
# asked: {"lines": [466, 467, 468], "branches": [[467, 0], [467, 468]]}
# gained: {"lines": [466, 467, 468], "branches": [[467, 0], [467, 468]]}

import pytest
from tornado.options import OptionParser

def test_run_parse_callbacks(monkeypatch):
    parser = OptionParser()
    callback_executed = []

    def mock_callback():
        callback_executed.append(True)

    parser.add_parse_callback(mock_callback)
    parser.run_parse_callbacks()

    assert callback_executed == [True]

    # Clean up
    parser._parse_callbacks.clear()
