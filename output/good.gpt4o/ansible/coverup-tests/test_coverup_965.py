# file lib/ansible/module_utils/facts/packages.py:14-16
# lines [14, 16]
# branches []

import pytest
from unittest.mock import patch

# Assuming get_all_subclasses and PkgMgr, CLIMgr, LibMgr are defined in the module
from ansible.module_utils.facts.packages import get_all_pkg_managers

class PkgMgr:
    pass

class CLIMgr(PkgMgr):
    pass

class LibMgr(PkgMgr):
    pass

class Yum(PkgMgr):
    pass

class Apt(PkgMgr):
    pass

def get_all_subclasses(cls):
    return cls.__subclasses__()

def test_get_all_pkg_managers(mocker):
    mocker.patch('ansible.module_utils.facts.packages.get_all_subclasses', side_effect=get_all_subclasses)
    mocker.patch('ansible.module_utils.facts.packages.PkgMgr', PkgMgr)
    mocker.patch('ansible.module_utils.facts.packages.CLIMgr', CLIMgr)
    mocker.patch('ansible.module_utils.facts.packages.LibMgr', LibMgr)
    
    result = get_all_pkg_managers()
    assert 'yum' in result
    assert 'apt' in result
    assert 'climgr' not in result
    assert 'libmgr' not in result
    assert result['yum'] == Yum
    assert result['apt'] == Apt
