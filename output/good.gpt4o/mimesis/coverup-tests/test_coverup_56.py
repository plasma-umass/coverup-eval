# file mimesis/providers/generic.py:86-104
# lines [86, 94, 95, 97, 98, 99, 100, 101, 103, 104]
# branches ['97->98', '97->104', '98->97', '98->99', '99->100', '99->103']

import pytest
from mimesis.providers.generic import Generic
from mimesis.providers.base import BaseDataProvider

@pytest.fixture
def generic_provider():
    return Generic()

def test_generic_dir(generic_provider):
    # Adding attributes to the generic_provider instance
    generic_provider._test_attr = 'test_value'
    generic_provider.test_attr2 = 'test_value2'
    
    # Expected attributes should exclude those in BaseDataProvider and process the ones in Generic
    expected_attributes = ['test_attr', 'test_attr2']
    
    # Get the attributes from the __dir__ method
    attributes = generic_provider.__dir__()
    
    # Assertions to verify the correct attributes are returned
    for attr in expected_attributes:
        assert attr in attributes

    # Clean up by removing the added attributes
    del generic_provider._test_attr
    del generic_provider.test_attr2
