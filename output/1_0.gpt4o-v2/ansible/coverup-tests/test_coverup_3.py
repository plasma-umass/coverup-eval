# file: lib/ansible/plugins/doc_fragments/return_common.py:9-42
# asked: {"lines": [9, 11], "branches": []}
# gained: {"lines": [9, 11], "branches": []}

import pytest
from ansible.plugins.doc_fragments.return_common import ModuleDocFragment

def test_module_doc_fragment_return():
    # Ensure the RETURN attribute is a string and contains expected documentation keys
    assert isinstance(ModuleDocFragment.RETURN, str)
    assert "changed:" in ModuleDocFragment.RETURN
    assert "failed:" in ModuleDocFragment.RETURN
    assert "msg:" in ModuleDocFragment.RETURN
    assert "skipped:" in ModuleDocFragment.RETURN
    assert "results:" in ModuleDocFragment.RETURN
    assert "exception:" in ModuleDocFragment.RETURN
