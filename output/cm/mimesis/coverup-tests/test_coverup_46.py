# file mimesis/providers/generic.py:37-64
# lines [37, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64]
# branches []

import pytest
from mimesis.providers.generic import Generic
from mimesis.providers import Person, Address, Datetime, Business, Text, Food, Science
from mimesis.providers import Transport, Code, UnitSystem, File, Numbers, Development
from mimesis.providers import Hardware, Clothing, Internet, Path, Payment, Cryptographic, Structure, Choice

@pytest.fixture
def generic_provider():
    return Generic()

def test_generic_initialization(generic_provider):
    assert issubclass(generic_provider._person, Person)
    assert issubclass(generic_provider._address, Address)
    assert issubclass(generic_provider._datetime, Datetime)
    assert issubclass(generic_provider._business, Business)
    assert issubclass(generic_provider._text, Text)
    assert issubclass(generic_provider._food, Food)
    assert issubclass(generic_provider._science, Science)
    assert isinstance(generic_provider.transport, Transport)
    assert isinstance(generic_provider.code, Code)
    assert isinstance(generic_provider.unit_system, UnitSystem)
    assert isinstance(generic_provider.file, File)
    assert isinstance(generic_provider.numbers, Numbers)
    assert isinstance(generic_provider.development, Development)
    assert isinstance(generic_provider.hardware, Hardware)
    assert isinstance(generic_provider.clothing, Clothing)
    assert isinstance(generic_provider.internet, Internet)
    assert isinstance(generic_provider.path, Path)
    assert isinstance(generic_provider.payment, Payment)
    assert isinstance(generic_provider.cryptographic, Cryptographic)
    assert isinstance(generic_provider.structure, Structure)
    assert isinstance(generic_provider.choice, Choice)
