# file: lib/ansible/module_utils/facts/virtual/freebsd.py:77-79
# asked: {"lines": [77, 78, 79], "branches": []}
# gained: {"lines": [77, 78, 79], "branches": []}

import pytest
from ansible.module_utils.facts.virtual.freebsd import FreeBSDVirtualCollector, FreeBSDVirtual

def test_FreeBSDVirtualCollector_class_attributes():
    assert FreeBSDVirtualCollector._fact_class == FreeBSDVirtual
    assert FreeBSDVirtualCollector._platform == 'FreeBSD'
