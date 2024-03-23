# file lib/ansible/plugins/doc_fragments/constructed.py:9-58
# lines [9, 11]
# branches []

import pytest

# Assuming the ModuleDocFragment class is in a file named constructed.py
from ansible.plugins.doc_fragments.constructed import ModuleDocFragment

def test_module_doc_fragment():
    # Instantiate the ModuleDocFragment to access the DOCUMENTATION attribute
    doc_fragment = ModuleDocFragment()
    documentation = doc_fragment.DOCUMENTATION

    # Assert that the DOCUMENTATION attribute is a non-empty string
    assert isinstance(documentation, str)
    assert len(documentation) > 0

    # Parse the DOCUMENTATION string as YAML to access the structure
    import yaml
    doc_data = yaml.safe_load(documentation)

    # Assert that the expected keys are in the documentation
    assert 'options' in doc_data
    options = doc_data['options']
    assert 'strict' in options
    assert 'compose' in options
    assert 'groups' in options
    assert 'keyed_groups' in options

    # Assert the defaults and types for 'strict', 'compose', and 'groups'
    assert options['strict']['default'] == False  # Corrected from 'no' to False
    assert options['strict']['type'] == 'bool'
    assert options['compose']['default'] == {}
    assert options['compose']['type'] == 'dict'
    assert options['groups']['default'] == {}
    assert options['groups']['type'] == 'dict'

    # Assert the defaults and structure for 'keyed_groups'
    assert options['keyed_groups']['default'] == []
    assert options['keyed_groups']['type'] == 'list'
    assert options['keyed_groups']['elements'] == 'dict'
    assert 'suboptions' in options['keyed_groups']
    suboptions = options['keyed_groups']['suboptions']
    assert 'parent_group' in suboptions
    assert 'prefix' in suboptions
    assert 'separator' in suboptions
    assert 'key' in suboptions
    assert 'default_value' in suboptions
    assert 'trailing_separator' in suboptions

    # Assert the defaults for suboptions where applicable
    assert suboptions['prefix']['default'] == ''
    assert suboptions['separator']['default'] == "_"
    assert 'default' not in suboptions['key']  # key does not have a default

    # Assert the version_added for 'default_value'
    assert suboptions['default_value']['version_added'] == '2.12'

    # Assert the mutual exclusivity in the documentation
    default_value_description = " ".join(suboptions['default_value']['description'])
    assert 'mutually exclusive with C(trailing_separator)' in default_value_description
    trailing_separator_description = " ".join(suboptions['trailing_separator']['description'])
    assert 'mutually exclusive with C(default_value)' in trailing_separator_description
