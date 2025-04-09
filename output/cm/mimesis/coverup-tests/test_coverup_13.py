# file mimesis/providers/generic.py:86-104
# lines [86, 94, 95, 97, 98, 99, 100, 101, 103, 104]
# branches ['97->98', '97->104', '98->97', '98->99', '99->100', '99->103']

import pytest
from mimesis.providers.generic import Generic
from mimesis.providers.base import BaseDataProvider

class CustomDataProvider(BaseDataProvider):
    def custom_method(self):
        pass

@pytest.fixture
def generic_provider_with_custom_method():
    generic = Generic()
    generic._custom_method = CustomDataProvider().custom_method
    return generic

def test_generic_dir_includes_custom_method(generic_provider_with_custom_method):
    dir_list = generic_provider_with_custom_method.__dir__()
    assert 'custom_method' in dir_list
    assert '_custom_method' not in dir_list
