# file: lib/ansible/module_utils/facts/system/python.py:33-60
# asked: {"lines": [38, 39, 40, 41, 42, 43, 44, 45, 47, 48, 49, 52, 53, 54, 55, 56, 57, 58, 60], "branches": []}
# gained: {"lines": [38, 39, 40, 41, 42, 43, 44, 45, 47, 48, 49, 52, 53, 54, 55, 56, 57, 58, 60], "branches": []}

import pytest
import sys
from ansible.module_utils.facts.system.python import PythonFactCollector

def test_python_fact_collector(monkeypatch):
    collector = PythonFactCollector()

    # Mock sys attributes
    monkeypatch.setattr(sys, 'version_info', (3, 9, 1, 'final', 0))
    monkeypatch.setattr(sys, 'executable', '/usr/bin/python3')
    monkeypatch.setattr(sys, 'implementation', type('impl', (object,), {'name': 'cpython'}))

    # Mock HAS_SSLCONTEXT
    monkeypatch.setattr('ansible.module_utils.facts.system.python.HAS_SSLCONTEXT', True)

    # Mock sys.subversion only if it exists
    if hasattr(sys, 'subversion'):
        monkeypatch.setattr(sys, 'subversion', ('CPython', '', ''))

    facts = collector.collect()

    assert facts['python']['version'] == {
        'major': 3,
        'minor': 9,
        'micro': 1,
        'releaselevel': 'final',
        'serial': 0
    }
    assert facts['python']['version_info'] == [3, 9, 1, 'final', 0]
    assert facts['python']['executable'] == '/usr/bin/python3'
    assert facts['python']['has_sslcontext'] == True
    if hasattr(sys, 'subversion'):
        assert facts['python']['type'] == 'CPython'
    else:
        assert facts['python']['type'] == 'cpython'

def test_python_fact_collector_no_subversion(monkeypatch):
    collector = PythonFactCollector()

    # Mock sys attributes
    monkeypatch.setattr(sys, 'version_info', (3, 9, 1, 'final', 0))
    monkeypatch.setattr(sys, 'executable', '/usr/bin/python3')
    monkeypatch.delattr(sys, 'subversion', raising=False)
    monkeypatch.setattr(sys, 'implementation', type('impl', (object,), {'name': 'cpython'}))

    # Mock HAS_SSLCONTEXT
    monkeypatch.setattr('ansible.module_utils.facts.system.python.HAS_SSLCONTEXT', True)

    facts = collector.collect()

    assert facts['python']['version'] == {
        'major': 3,
        'minor': 9,
        'micro': 1,
        'releaselevel': 'final',
        'serial': 0
    }
    assert facts['python']['version_info'] == [3, 9, 1, 'final', 0]
    assert facts['python']['executable'] == '/usr/bin/python3'
    assert facts['python']['has_sslcontext'] == True
    assert facts['python']['type'] == 'cpython'

def test_python_fact_collector_no_implementation(monkeypatch):
    collector = PythonFactCollector()

    # Mock sys attributes
    monkeypatch.setattr(sys, 'version_info', (3, 9, 1, 'final', 0))
    monkeypatch.setattr(sys, 'executable', '/usr/bin/python3')
    monkeypatch.delattr(sys, 'subversion', raising=False)
    monkeypatch.delattr(sys, 'implementation', raising=False)

    # Mock HAS_SSLCONTEXT
    monkeypatch.setattr('ansible.module_utils.facts.system.python.HAS_SSLCONTEXT', True)

    facts = collector.collect()

    assert facts['python']['version'] == {
        'major': 3,
        'minor': 9,
        'micro': 1,
        'releaselevel': 'final',
        'serial': 0
    }
    assert facts['python']['version_info'] == [3, 9, 1, 'final', 0]
    assert facts['python']['executable'] == '/usr/bin/python3'
    assert facts['python']['has_sslcontext'] == True
    assert facts['python']['type'] == None
