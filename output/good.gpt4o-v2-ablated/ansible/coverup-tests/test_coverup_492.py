# file: lib/ansible/modules/systemd.py:299-331
# asked: {"lines": [312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 326, 327, 328, 329, 330, 331], "branches": [[315, 316], [315, 331], [316, 317], [316, 326], [317, 315], [317, 318], [319, 320], [319, 323], [320, 321], [320, 323], [327, 315], [327, 328]]}
# gained: {"lines": [312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 326, 327, 328, 329, 330, 331], "branches": [[315, 316], [315, 331], [316, 317], [316, 326], [317, 318], [319, 320], [319, 323], [320, 321], [320, 323], [327, 315], [327, 328]]}

import pytest

def test_parse_systemctl_show_single_line():
    from ansible.modules.systemd import parse_systemctl_show

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
    from ansible.modules.systemd import parse_systemctl_show

    lines = [
        "ExecStart={",
        "/usr/bin/somecommand --option",
        "anotheroption",
        "}"
    ]
    expected = {
        "ExecStart": "{\n/usr/bin/somecommand --option\nanotheroption\n}"
    }
    result = parse_systemctl_show(lines)
    assert result == expected

def test_parse_systemctl_show_multiline_exec_single_line():
    from ansible.modules.systemd import parse_systemctl_show

    lines = [
        "ExecStart={/usr/bin/somecommand --option}"
    ]
    expected = {
        "ExecStart": "{/usr/bin/somecommand --option}"
    }
    result = parse_systemctl_show(lines)
    assert result == expected

def test_parse_systemctl_show_multiline_exec_incomplete():
    from ansible.modules.systemd import parse_systemctl_show

    lines = [
        "ExecStart={",
        "/usr/bin/somecommand --option"
    ]
    expected = {}
    result = parse_systemctl_show(lines)
    assert result == expected

def test_parse_systemctl_show_mixed():
    from ansible.modules.systemd import parse_systemctl_show

    lines = [
        "Description=Single line description",
        "ExecStart={",
        "/usr/bin/somecommand --option",
        "anotheroption",
        "}",
        "After=network.target"
    ]
    expected = {
        "Description": "Single line description",
        "ExecStart": "{\n/usr/bin/somecommand --option\nanotheroption\n}",
        "After": "network.target"
    }
    result = parse_systemctl_show(lines)
    assert result == expected
