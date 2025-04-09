# file lib/ansible/module_utils/facts/system/python.py:33-60
# lines [38, 39, 40, 41, 42, 43, 44, 45, 47, 48, 49, 52, 53, 54, 55, 56, 57, 58, 60]
# branches []

import sys
import pytest
from ansible.module_utils.facts.system.python import PythonFactCollector

def test_python_fact_collector(mocker):
    mocker.patch.object(sys, 'version_info', [3, 8, 6, 'final', 0])
    mocker.patch.object(sys, 'executable', '/usr/bin/python3')
    mocker.patch.object(sys, 'subversion', ['CPython'], create=True)
    mocker.patch('ansible.module_utils.facts.system.python.HAS_SSLCONTEXT', True)

    collector = PythonFactCollector()
    facts = collector.collect()

    assert facts['python']['version']['major'] == 3
    assert facts['python']['version']['minor'] == 8
    assert facts['python']['version']['micro'] == 6
    assert facts['python']['version']['releaselevel'] == 'final'
    assert facts['python']['version']['serial'] == 0
    assert facts['python']['version_info'] == [3, 8, 6, 'final', 0]
    assert facts['python']['executable'] == '/usr/bin/python3'
    assert facts['python']['has_sslcontext'] is True
    assert facts['python']['type'] == 'CPython'
