# file lib/ansible/executor/interpreter_discovery.py:181-202
# lines [183, 184, 185, 187, 189, 192, 194, 197, 202]
# branches ['184->185', '184->187', '194->197', '194->202']

import pytest
from unittest.mock import patch
from ansible.executor.interpreter_discovery import _version_fuzzy_match
from distutils.version import LooseVersion
import bisect

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
