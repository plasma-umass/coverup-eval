# file: lib/ansible/modules/systemd.py:299-331
# asked: {"lines": [299, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 326, 327, 328, 329, 330, 331], "branches": [[315, 316], [315, 331], [316, 317], [316, 326], [317, 315], [317, 318], [319, 320], [319, 323], [320, 321], [320, 323], [327, 315], [327, 328]]}
# gained: {"lines": [299, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 326, 327, 328, 329, 330, 331], "branches": [[315, 316], [315, 331], [316, 317], [316, 326], [317, 315], [317, 318], [319, 320], [319, 323], [320, 321], [320, 323], [327, 315], [327, 328]]}

import pytest
from ansible.modules.systemd import parse_systemctl_show

def test_parse_systemctl_show_single_line():
    lines = [
        "Description=Single line description",
        "ExecStart={/bin/echo Hello World}",
    ]
    expected = {
        "Description": "Single line description",
        "ExecStart": "{/bin/echo Hello World}",
    }
    result = parse_systemctl_show(lines)
    assert result == expected

def test_parse_systemctl_show_multi_line():
    lines = [
        "Description=Single line description",
        "ExecStart={/bin/echo Hello",
        "World}",
    ]
    expected = {
        "Description": "Single line description",
        "ExecStart": "{/bin/echo Hello\nWorld}",
    }
    result = parse_systemctl_show(lines)
    assert result == expected

def test_parse_systemctl_show_exec_without_closing_brace():
    lines = [
        "Description=Single line description",
        "ExecStart={/bin/echo Hello",
        "World",
        "}",
    ]
    expected = {
        "Description": "Single line description",
        "ExecStart": "{/bin/echo Hello\nWorld\n}",
    }
    result = parse_systemctl_show(lines)
    assert result == expected

def test_parse_systemctl_show_no_equals():
    lines = [
        "Description Single line description",
        "ExecStart={/bin/echo Hello World}",
    ]
    expected = {
        "ExecStart": "{/bin/echo Hello World}",
    }
    result = parse_systemctl_show(lines)
    assert result == expected
