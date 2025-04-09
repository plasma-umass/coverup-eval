# file: lib/ansible/executor/interpreter_discovery.py:181-202
# asked: {"lines": [181, 183, 184, 185, 187, 189, 192, 194, 197, 202], "branches": [[184, 185], [184, 187], [194, 197], [194, 202]]}
# gained: {"lines": [181, 183, 184, 185, 187, 189, 192, 194, 197, 202], "branches": [[184, 185], [184, 187], [194, 197], [194, 202]]}

import pytest
from ansible.executor.interpreter_discovery import _version_fuzzy_match
from ansible.module_utils.compat.version import LooseVersion

def test_version_fuzzy_match_exact_match():
    version_map = {
        '1.0': 'python1.0',
        '2.0': 'python2.0',
        '3.0': 'python3.0'
    }
    assert _version_fuzzy_match('2.0', version_map) == 'python2.0'

def test_version_fuzzy_match_no_exact_match():
    version_map = {
        '1.0': 'python1.0',
        '2.0': 'python2.0',
        '3.0': 'python3.0'
    }
    assert _version_fuzzy_match('2.5', version_map) == 'python2.0'

def test_version_fuzzy_match_older_than_all():
    version_map = {
        '1.0': 'python1.0',
        '2.0': 'python2.0',
        '3.0': 'python3.0'
    }
    assert _version_fuzzy_match('0.5', version_map) == 'python1.0'

def test_version_fuzzy_match_newer_than_all():
    version_map = {
        '1.0': 'python1.0',
        '2.0': 'python2.0',
        '3.0': 'python3.0'
    }
    assert _version_fuzzy_match('4.0', version_map) == 'python3.0'

def test_version_fuzzy_match_no_versions():
    version_map = {}
    with pytest.raises(IndexError):
        _version_fuzzy_match('1.0', version_map)
