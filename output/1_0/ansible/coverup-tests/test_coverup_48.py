# file lib/ansible/plugins/doc_fragments/inventory_cache.py:9-58
# lines [9, 12]
# branches []

import pytest

# Assuming the ModuleDocFragment class is in a file named inventory_cache.py
from ansible.plugins.doc_fragments.inventory_cache import ModuleDocFragment

def test_module_doc_fragment():
    # Access the DOCUMENTATION attribute to trigger the code execution
    documentation = ModuleDocFragment.DOCUMENTATION

    # Assertions to verify the postconditions
    assert 'cache' in documentation
    assert 'cache_plugin' in documentation
    assert 'cache_timeout' in documentation
    assert 'cache_connection' in documentation

    # Verify that the environment variables are being read correctly
    assert 'ANSIBLE_INVENTORY_CACHE' in documentation
    assert 'ANSIBLE_CACHE_PLUGIN' in documentation
    assert 'ANSIBLE_INVENTORY_CACHE_PLUGIN' in documentation
    assert 'ANSIBLE_CACHE_PLUGIN_TIMEOUT' in documentation
    assert 'ANSIBLE_INVENTORY_CACHE_TIMEOUT' in documentation
    assert 'ANSIBLE_CACHE_PLUGIN_CONNECTION' in documentation
    assert 'ANSIBLE_INVENTORY_CACHE_CONNECTION' in documentation

    # Verify that the ini configuration is being read correctly
    assert 'section: inventory' in documentation
    assert 'key: cache' in documentation
    assert 'section: defaults' in documentation
    assert 'key: fact_caching' in documentation
    assert 'key: cache_plugin' in documentation
    assert 'key: cache_timeout' in documentation
