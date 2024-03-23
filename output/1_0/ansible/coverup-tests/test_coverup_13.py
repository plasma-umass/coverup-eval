# file lib/ansible/plugins/doc_fragments/validate.py:9-21
# lines [9, 11]
# branches []

import pytest

# Assuming the ModuleDocFragment class is in a file named validate.py
from ansible.plugins.doc_fragments.validate import ModuleDocFragment

def test_module_doc_fragment_documentation():
    # Instantiate the ModuleDocFragment to access the DOCUMENTATION attribute
    doc_fragment = ModuleDocFragment()
    
    # Check if the DOCUMENTATION attribute contains the expected string
    assert 'The validation command to run before copying the updated file into the final destination.' in doc_fragment.DOCUMENTATION
    assert '%s' in doc_fragment.DOCUMENTATION
    assert 'https://docs.ansible.com/ansible/devel/reference_appendices/faq.html' in doc_fragment.DOCUMENTATION
