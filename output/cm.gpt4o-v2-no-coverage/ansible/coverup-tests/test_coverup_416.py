# file: lib/ansible/modules/pip.py:610-621
# asked: {"lines": [610, 611, 612, 613, 614, 615, 617, 618, 619, 620], "branches": [[611, 612], [611, 613]]}
# gained: {"lines": [610, 611, 612, 613, 614, 615, 617, 618, 619, 620], "branches": [[611, 612], [611, 613]]}

import pytest
from unittest.mock import Mock, patch
from ansible.module_utils.compat.version import LooseVersion
from ansible.modules.pip import Package

@pytest.fixture
def package():
    pkg = Package("example")
    pkg._plain_package = True
    pkg._requirement = Mock()
    return pkg

def test_is_satisfied_by_with_specifier(package):
    package._requirement.specifier.contains.return_value = True
    assert package.is_satisfied_by("1.0.0")
    package._requirement.specifier.contains.assert_called_once_with("1.0.0", prereleases=True)

def test_is_satisfied_by_without_specifier(package):
    package._requirement.specifier.contains.side_effect = AttributeError
    package._requirement.specs = [('==', '1.0.0')]
    with patch('ansible.modules.pip.op_dict', {'==': lambda x, y: x == y}):
        assert package.is_satisfied_by("1.0.0")
        assert package.is_satisfied_by("1.0.0") == True

def test_is_satisfied_by_plain_package_false(package):
    package._plain_package = False
    assert not package.is_satisfied_by("1.0.0")
