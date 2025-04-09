# file pypara/dcc.py:338-346
# lines [346]
# branches []

import pytest
from pypara.dcc import DCCRegistryMachinery

@pytest.fixture
def dcc_registry_machinery():
    return DCCRegistryMachinery()

def test_find_with_stripped_uppercased_name(dcc_registry_machinery, mocker):
    # Mock the _find_strict method to control its behavior
    mocker.patch.object(dcc_registry_machinery, '_find_strict', side_effect=lambda x: "Found" if x == "TEST" else None)

    # Test with a name that requires stripping and uppercasing
    result = dcc_registry_machinery.find(" test ")

    # Verify that the result is as expected and that the line is covered
    assert result == "Found"
    dcc_registry_machinery._find_strict.assert_has_calls([mocker.call(" test "), mocker.call("TEST")])
