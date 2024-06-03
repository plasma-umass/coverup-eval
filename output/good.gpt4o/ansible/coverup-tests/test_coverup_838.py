# file lib/ansible/plugins/filter/core.py:569-571
# lines [569, 570]
# branches []

import pytest
from ansible.plugins.filter.core import FilterModule

def test_filter_module_initialization():
    # Test the initialization of the FilterModule class
    filter_module = FilterModule()
    assert isinstance(filter_module, FilterModule)
