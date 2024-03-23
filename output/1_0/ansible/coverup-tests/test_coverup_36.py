# file lib/ansible/module_utils/facts/namespace.py:44-51
# lines [44, 45, 46, 47, 49, 50, 51]
# branches []

import pytest
from ansible.module_utils.facts.namespace import PrefixFactNamespace

# Test function for PrefixFactNamespace
def test_prefix_fact_namespace_transform():
    # Create an instance of PrefixFactNamespace with a specific prefix
    prefix_namespace = PrefixFactNamespace(namespace_name='test', prefix='prefix_')

    # Test the transform method with a name
    transformed_name = prefix_namespace.transform('TestName')

    # Assert that the transformed name is as expected
    assert transformed_name == 'prefix_TestName'

    # Test the transform method with a name and no prefix
    no_prefix_namespace = PrefixFactNamespace(namespace_name='test', prefix='')
    transformed_name_no_prefix = no_prefix_namespace.transform('TestName')

    # Assert that the transformed name is as expected when no prefix is provided
    assert transformed_name_no_prefix == 'TestName'
