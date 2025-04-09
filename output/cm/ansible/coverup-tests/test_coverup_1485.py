# file lib/ansible/module_utils/yumdnf.py:178-180
# lines [180]
# branches []

import pytest
from ansible.module_utils.yumdnf import YumDnf
from unittest.mock import MagicMock

# Test function to cover the abstract method
def test_yumdnf_abstract_run_method(mocker):
    mocker.patch.multiple(YumDnf, __abstractmethods__=set())
    yumdnf_instance = YumDnf(MagicMock())
    with pytest.raises(NotImplementedError):
        yumdnf_instance.run()
