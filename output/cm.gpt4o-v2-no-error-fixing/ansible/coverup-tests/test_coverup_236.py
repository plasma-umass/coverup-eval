# file: lib/ansible/constants.py:48-60
# asked: {"lines": [48, 49, 50, 51, 52, 54, 55, 56, 58, 59, 60], "branches": []}
# gained: {"lines": [48, 49, 50, 51, 52, 54, 55, 56, 58, 59, 60], "branches": []}

import pytest
from ansible.module_utils.common.collections import Sequence
from ansible.constants import _DeprecatedSequenceConstant, _deprecated

class TestDeprecatedSequenceConstant:
    
    def test_len(self, mocker):
        value = [1, 2, 3]
        msg = "This is deprecated"
        version = "2.0"
        
        mock_deprecated = mocker.patch('ansible.constants._deprecated')
        
        seq = _DeprecatedSequenceConstant(value, msg, version)
        
        assert len(seq) == 3
        mock_deprecated.assert_called_once_with(msg, version)
    
    def test_getitem(self, mocker):
        value = [1, 2, 3]
        msg = "This is deprecated"
        version = "2.0"
        
        mock_deprecated = mocker.patch('ansible.constants._deprecated')
        
        seq = _DeprecatedSequenceConstant(value, msg, version)
        
        assert seq[1] == 2
        mock_deprecated.assert_called_once_with(msg, version)
