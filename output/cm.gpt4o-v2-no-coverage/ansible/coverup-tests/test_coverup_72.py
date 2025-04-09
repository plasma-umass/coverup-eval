# file: lib/ansible/modules/systemd.py:299-331
# asked: {"lines": [299, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 326, 327, 328, 329, 330, 331], "branches": [[315, 316], [315, 331], [316, 317], [316, 326], [317, 315], [317, 318], [319, 320], [319, 323], [320, 321], [320, 323], [327, 315], [327, 328]]}
# gained: {"lines": [299, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 326, 327, 328, 329, 330, 331], "branches": [[315, 316], [315, 331], [316, 317], [316, 326], [317, 318], [319, 320], [319, 323], [320, 321], [327, 315], [327, 328]]}

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
        "arg1",
        "arg2",
        "}"
    ]
    expected = {
        "ExecStart": "{\n/usr/bin/example\narg1\narg2\n}"
    }
    result = parse_systemctl_show(lines)
    assert result == expected

def test_parse_systemctl_show_multiline_non_exec():
    lines = [
        "Description={This is a single line with braces}",
        "After=network.target"
    ]
    expected = {
        "Description": "{This is a single line with braces}",
        "After": "network.target"
    }
    result = parse_systemctl_show(lines)
    assert result == expected

def test_parse_systemctl_show_multiline_exec_incomplete():
    lines = [
        "ExecStart={",
        "/usr/bin/example",
        "arg1",
        "arg2"
    ]
    expected = {}
    result = parse_systemctl_show(lines)
    assert result == expected

def test_parse_systemctl_show_empty():
    lines = []
    expected = {}
    result = parse_systemctl_show(lines)
    assert result == expected
