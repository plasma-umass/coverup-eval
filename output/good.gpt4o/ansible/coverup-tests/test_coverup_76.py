# file lib/ansible/modules/systemd.py:299-331
# lines [299, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 326, 327, 328, 329, 330, 331]
# branches ['315->316', '315->331', '316->317', '316->326', '317->315', '317->318', '319->320', '319->323', '320->321', '320->323', '327->315', '327->328']

import pytest
from unittest import mock

def test_parse_systemctl_show():
    from ansible.modules.systemd import parse_systemctl_show

    # Test case 1: Single-line key-value pairs
    lines = [
        "Description=Single line description",
        "After=network.target"
    ]
    expected = {
        "Description": "Single line description",
        "After": "network.target"
    }
    assert parse_systemctl_show(lines) == expected

    # Test case 2: Multi-line value for ExecStart
    lines = [
        "ExecStart={",
        "/usr/bin/somecommand --option",
        "anotheroption",
        "}"
    ]
    expected = {
        "ExecStart": "{\n/usr/bin/somecommand --option\nanotheroption\n}"
    }
    assert parse_systemctl_show(lines) == expected

    # Test case 3: Single-line value starting with {
    lines = [
        "Description={Single line description}"
    ]
    expected = {
        "Description": "{Single line description}"
    }
    assert parse_systemctl_show(lines) == expected

    # Test case 4: Mixed single-line and multi-line values
    lines = [
        "Description=Service with multi-line exec",
        "ExecStart={",
        "/usr/bin/somecommand --option",
        "anotheroption",
        "}",
        "After=network.target"
    ]
    expected = {
        "Description": "Service with multi-line exec",
        "ExecStart": "{\n/usr/bin/somecommand --option\nanotheroption\n}",
        "After": "network.target"
    }
    assert parse_systemctl_show(lines) == expected

    # Test case 5: Multi-line value for non-Exec key (should not be treated as multi-line)
    lines = [
        "Description={",
        "This should not be multi-line",
        "}"
    ]
    expected = {
        "Description": "{"
    }
    assert parse_systemctl_show(lines) == expected

    # Test case 6: Empty input
    lines = []
    expected = {}
    assert parse_systemctl_show(lines) == expected
