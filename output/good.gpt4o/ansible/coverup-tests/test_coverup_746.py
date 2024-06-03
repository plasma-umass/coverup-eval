# file lib/ansible/module_utils/facts/virtual/sunos.py:137-139
# lines [137, 138, 139]
# branches []

import pytest
from ansible.module_utils.facts.virtual.sunos import SunOSVirtualCollector, SunOSVirtual
from unittest.mock import patch

def test_sunos_virtual_collector():
    with patch('ansible.module_utils.facts.virtual.sunos.VirtualCollector.__init__', return_value=None) as mock_init:
        collector = SunOSVirtualCollector()
        assert collector._fact_class == SunOSVirtual
        assert collector._platform == 'SunOS'
        mock_init.assert_called_once()
