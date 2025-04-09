# file lib/ansible/modules/pip.py:583-602
# lines [589, 590, 591, 596, 597, 601, 602]
# branches ['588->589', '595->596']

import pytest
from ansible.modules.pip import Package
from pkg_resources import Requirement

@pytest.fixture
def cleanup_package():
    # Setup fixture if needed
    yield
    # Cleanup code if needed

def test_package_init_version_digit(mocker, cleanup_package):
    mocker.patch('pkg_resources.Requirement.parse', return_value=mocker.Mock(project_name='mypackage'))
    package = Package('mypackage', '1.0.0')
    assert package.package_name == 'mypackage'
    assert package._plain_package == True

def test_package_init_version_non_digit(mocker, cleanup_package):
    mocker.patch('pkg_resources.Requirement.parse', return_value=mocker.Mock(project_name='mypackage'))
    package = Package('mypackage', '>=1.0.0')
    assert package.package_name == 'mypackage'
    assert package._plain_package == True

def test_package_init_distribute_setuptools(mocker, cleanup_package):
    mocker.patch('pkg_resources.Requirement.parse', return_value=mocker.Mock(project_name='distribute'))
    package = Package('setuptools', '1.0.0')
    assert package.package_name == 'setuptools'
    assert package._plain_package == True

def test_package_init_value_error(mocker, cleanup_package):
    mocker.patch('pkg_resources.Requirement.parse', side_effect=ValueError)
    package = Package('mypackage', 'invalid_version')
    assert package.package_name == 'mypackage'
    assert package._plain_package == False
