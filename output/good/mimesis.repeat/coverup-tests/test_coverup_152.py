# file mimesis/providers/structure.py:19-21
# lines [19, 20]
# branches []

import pytest
from mimesis.providers.structure import Structure

@pytest.fixture
def structure_provider():
    return Structure()

def test_structure_provider_methods(structure_provider):
    # Get all public methods of Structure class
    methods = [func for func in dir(structure_provider) if callable(getattr(structure_provider, func)) and not func.startswith("_")]

    # Call each method and assert it returns a value (not None)
    for method_name in methods:
        method = getattr(structure_provider, method_name)
        # Some methods like 'reseed' might intentionally return None, so we skip the assertion for them
        if method_name == 'reseed':
            method()  # Call the method to ensure it is covered
        else:
            result = method()
            assert result is not None, f"Method {method_name} returned None"
