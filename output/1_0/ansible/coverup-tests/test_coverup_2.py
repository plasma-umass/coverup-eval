# file lib/ansible/plugins/doc_fragments/connection_pipelining.py:7-29
# lines [7, 10]
# branches []

import pytest
from ansible.plugins.doc_fragments.connection_pipelining import ModuleDocFragment

def test_module_doc_fragment(mocker):
    mocker.patch.dict('os.environ', {'ANSIBLE_PIPELINING': 'True'})
    doc_fragment = ModuleDocFragment()
    assert 'pipelining' in doc_fragment.DOCUMENTATION
    assert 'ANSIBLE_PIPELINING' in doc_fragment.DOCUMENTATION
    assert 'defaults' in doc_fragment.DOCUMENTATION
    assert 'pipelining' in doc_fragment.DOCUMENTATION
    assert 'boolean' in doc_fragment.DOCUMENTATION
    assert 'ansible_pipelining' in doc_fragment.DOCUMENTATION
