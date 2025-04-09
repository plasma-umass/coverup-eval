# file: tornado/options.py:718-723
# asked: {"lines": [718, 723], "branches": []}
# gained: {"lines": [718, 723], "branches": []}

import pytest
from io import StringIO
from tornado.options import print_help, OptionParser

@pytest.fixture
def mock_option_parser(monkeypatch):
    mock_parser = OptionParser()
    monkeypatch.setattr('tornado.options.options', mock_parser)
    return mock_parser

def test_print_help_default_stderr(mock_option_parser, capsys):
    print_help()
    captured = capsys.readouterr()
    assert 'Usage:' in captured.err
    assert 'Options:' in captured.err

def test_print_help_custom_file(mock_option_parser):
    output = StringIO()
    print_help(output)
    contents = output.getvalue()
    assert 'Usage:' in contents
    assert 'Options:' in contents
