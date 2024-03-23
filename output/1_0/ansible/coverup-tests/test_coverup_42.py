# file lib/ansible/plugins/doc_fragments/template_common.py:10-59
# lines [10, 13]
# branches []

import pytest

# Assuming the ModuleDocFragment class is in a file named template_common.py
from ansible.plugins.doc_fragments.template_common import ModuleDocFragment

def test_module_doc_fragment():
    # Access the DOCUMENTATION attribute to ensure it is parsed/executed
    doc_fragment_content = ModuleDocFragment.DOCUMENTATION

    # Assertions to verify the content of the documentation
    assert 'description' in doc_fragment_content
    assert 'options' in doc_fragment_content
    assert 'src' in doc_fragment_content
    assert 'dest' in doc_fragment_content
    assert 'newline_sequence' in doc_fragment_content
    assert 'block_start_string' in doc_fragment_content
    assert 'block_end_string' in doc_fragment_content

    # Verify specific options and their defaults
    # The newline character needs to be escaped properly in the assertion
    assert "default: '\\n'" in doc_fragment_content
    assert "default: '{%'" in doc_fragment_content
    assert "default: '%}'" in doc_fragment_content

    # Verify version_added strings
    assert "version_added: '2.4'" in doc_fragment_content

    # Verify template variables
    assert 'ansible_managed' in doc_fragment_content
    assert 'template_host' in doc_fragment_content
    assert 'template_uid' in doc_fragment_content
    assert 'template_path' in doc_fragment_content
    assert 'template_fullpath' in doc_fragment_content
    assert 'template_destpath' in doc_fragment_content
    assert 'template_run_date' in doc_fragment_content

    # No cleanup is necessary as we are not modifying any state
