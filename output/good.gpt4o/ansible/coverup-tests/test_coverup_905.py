# file lib/ansible/utils/collection_loader/_collection_finder.py:333-334
# lines [333, 334]
# branches []

import pytest
from unittest.mock import patch

# Assuming the class _AnsibleCollectionPkgLoaderBase is imported from the module
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionPkgLoaderBase

class MockAnsibleCollectionPkgLoaderBase(_AnsibleCollectionPkgLoaderBase):
    def __init__(self):
        pass

def test__validate_final():
    loader = MockAnsibleCollectionPkgLoaderBase()
    
    with patch.object(loader, '_validate_final', wraps=loader._validate_final) as mock_validate_final:
        result = loader._validate_final()
        mock_validate_final.assert_called_once()
        assert result is None
