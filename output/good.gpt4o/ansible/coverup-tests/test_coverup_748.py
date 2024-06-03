# file lib/ansible/module_utils/facts/system/cmdline.py:26-29
# lines [26, 27, 28]
# branches []

import pytest
from ansible.module_utils.facts.system.cmdline import CmdLineFactCollector
from ansible.module_utils.facts.collector import BaseFactCollector

def test_cmdline_fact_collector_initialization():
    collector = CmdLineFactCollector()
    assert collector.name == 'cmdline'
    assert collector._fact_ids == set()
    assert isinstance(collector, BaseFactCollector)
