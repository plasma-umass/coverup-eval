# file: lib/ansible/playbook/base.py:871-876
# asked: {"lines": [871, 873, 874, 876], "branches": [[873, 874], [873, 876]]}
# gained: {"lines": [871, 873, 874, 876], "branches": [[873, 874], [873, 876]]}

import pytest
from unittest.mock import MagicMock

from ansible.playbook.base import Base

class TestBase:

    def test_get_dep_chain_with_parent(self):
        parent_mock = MagicMock()
        parent_mock.get_dep_chain.return_value = 'parent_chain'
        
        base_instance = Base()
        base_instance._parent = parent_mock
        
        result = base_instance.get_dep_chain()
        
        assert result == 'parent_chain'
        parent_mock.get_dep_chain.assert_called_once()

    def test_get_dep_chain_without_parent(self):
        base_instance = Base()
        base_instance._parent = None
        
        result = base_instance.get_dep_chain()
        
        assert result is None
