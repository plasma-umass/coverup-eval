# file lib/ansible/plugins/doc_fragments/return_common.py:9-42
# lines [9, 11]
# branches []

import pytest

# Assuming the ModuleDocFragment class is in a file named return_common.py
from ansible.plugins.doc_fragments.return_common import ModuleDocFragment

def test_module_doc_fragment():
    # Instantiate the ModuleDocFragment to ensure its RETURN attribute is accessed
    doc_fragment = ModuleDocFragment()
    assert isinstance(doc_fragment.RETURN, str)
    # Check if the RETURN attribute contains expected keys
    assert 'changed' in doc_fragment.RETURN
    assert 'failed' in doc_fragment.RETURN
    assert 'msg' in doc_fragment.RETURN
    assert 'skipped' in doc_fragment.RETURN
    assert 'results' in doc_fragment.RETURN
    assert 'exception' in doc_fragment.RETURN
