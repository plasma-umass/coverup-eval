# file: string_utils/validation.py:393-415
# asked: {"lines": [393, 407, 408, 411, 412, 413, 415], "branches": [[407, 408], [407, 411], [411, 412], [411, 415], [412, 411], [412, 413]]}
# gained: {"lines": [393, 407, 408, 411, 412, 413, 415], "branches": [[407, 408], [407, 411], [411, 412], [411, 415], [412, 411], [412, 413]]}

import pytest
from string_utils.validation import is_ip_v4
from string_utils._regex import SHALLOW_IP_V4_RE
from string_utils.validation import is_full_string

def test_is_ip_v4_valid_ip(monkeypatch):
    monkeypatch.setattr('string_utils.validation.is_full_string', lambda x: True)
    monkeypatch.setattr('string_utils._regex.SHALLOW_IP_V4_RE', SHALLOW_IP_V4_RE)
    assert is_ip_v4('255.200.100.75') == True

def test_is_ip_v4_invalid_ip_non_string(monkeypatch):
    monkeypatch.setattr('string_utils.validation.is_full_string', lambda x: False)
    assert is_ip_v4(12345) == False

def test_is_ip_v4_invalid_ip_format(monkeypatch):
    monkeypatch.setattr('string_utils.validation.is_full_string', lambda x: True)
    monkeypatch.setattr('string_utils._regex.SHALLOW_IP_V4_RE', SHALLOW_IP_V4_RE)
    assert is_ip_v4('nope') == False

def test_is_ip_v4_invalid_ip_out_of_range(monkeypatch):
    monkeypatch.setattr('string_utils.validation.is_full_string', lambda x: True)
    monkeypatch.setattr('string_utils._regex.SHALLOW_IP_V4_RE', SHALLOW_IP_V4_RE)
    assert is_ip_v4('255.200.100.999') == False

def test_is_ip_v4_empty_string(monkeypatch):
    monkeypatch.setattr('string_utils.validation.is_full_string', lambda x: False)
    assert is_ip_v4('') == False
