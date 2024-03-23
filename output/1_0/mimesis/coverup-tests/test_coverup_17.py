# file mimesis/providers/development.py:29-60
# lines [29, 40, 41, 43, 44, 45, 47, 48, 49, 50, 52, 54, 55, 56, 57, 58, 60]
# branches ['43->44', '43->52', '44->45', '44->47', '47->48', '47->49', '54->55', '54->60']

import pytest
from mimesis.providers.development import Development
from mimesis.random import Random


@pytest.fixture
def development_provider():
    return Development(Random())


def test_version_calver_edge_cases(development_provider, mocker):
    mocker.patch.object(development_provider.random, 'randints', return_value=(0, 0, 0))
    mocker.patch.object(development_provider.random, 'randint', return_value=2017)

    version = development_provider.version(calver=True)
    assert version.startswith("2017."), "Version should start with the year for calver"
    assert ".1.1" in version, "Minor and patch versions should be incremented if they are 0"

    version = development_provider.version(calver=False, pre_release=True)
    assert any(suffix in version for suffix in ('alpha', 'beta', 'rc')), "Pre-release version should contain a valid suffix"
    assert version.count('.') == 3, "Pre-release version should have two dots and one dash"

    mocker.stopall()
