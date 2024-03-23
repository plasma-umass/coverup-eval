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
def generic_provider_with_custom_attr():
    generic = Generic()
    generic._custom_attr = CustomDataProvider()
    yield generic
    del generic._custom_attr

def test_generic_dir(generic_provider_with_custom_attr):
    dir_list = generic_provider_with_custom_attr.__dir__()
    assert 'custom_attr' in dir_list
    assert 'custom_method' not in dir_list  # custom_method is not a direct attribute of Generic
