# file: lib/ansible/modules/systemd.py:299-331
# asked: {"lines": [], "branches": [[317, 315], [320, 323]]}
# gained: {"lines": [], "branches": [[320, 323]]}

import pytest

from ansible.modules.systemd import parse_systemctl_show

def test_parse_systemctl_show_single_line():
    lines = [
        "Description=Single line description",
        "After=network.target"
    ]
    expected = {
        "Description": "Single line description",
        "After": "network.target"
    }
    result = parse_systemctl_show(lines)
    assert result == expected

def test_parse_systemctl_show_multiline_exec():
    lines = [
        "ExecStart={",
        "/usr/bin/example",
        "another line",
        "}"
    ]
    expected = {
        "ExecStart": "{\n/usr/bin/example\nanother line\n}"
    }
    result = parse_systemctl_show(lines)
    assert result == expected

def test_parse_systemctl_show_multiline_exec_single_line():
    lines = [
        "ExecStart={single line}"
    ]
    expected = {
        "ExecStart": "{single line}"
    }
    result = parse_systemctl_show(lines)
    assert result == expected

def test_parse_systemctl_show_multiline_exec_incomplete():
    lines = [
        "ExecStart={",
        "/usr/bin/example"
    ]
    expected = {}
    result = parse_systemctl_show(lines)
    assert result == expected

def test_parse_systemctl_show_mixed():
    lines = [
        "Description=Single line description",
        "ExecStart={",
        "/usr/bin/example",
        "another line",
        "}",
        "After=network.target"
    ]
    expected = {
        "Description": "Single line description",
        "ExecStart": "{\n/usr/bin/example\nanother line\n}",
        "After": "network.target"
    }
    result = parse_systemctl_show(lines)
    assert result == expected
