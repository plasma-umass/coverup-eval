# file mimesis/builtins/ru.py:37-48
# lines [37, 46, 47, 48]
# branches []

import pytest
from mimesis.builtins.ru import RussiaSpecProvider
from mimesis.enums import Gender

@pytest.fixture
def russia_spec_provider():
    return RussiaSpecProvider()

def test_patronymic_male(russia_spec_provider):
    patronymic = russia_spec_provider.patronymic(Gender.MALE)
    assert patronymic in russia_spec_provider._data['patronymic']['male']

def test_patronymic_female(russia_spec_provider):
    patronymic = russia_spec_provider.patronymic(Gender.FEMALE)
    assert patronymic in russia_spec_provider._data['patronymic']['female']

def test_patronymic_none(russia_spec_provider):
    patronymic = russia_spec_provider.patronymic()
    assert patronymic in russia_spec_provider._data['patronymic']['male'] + russia_spec_provider._data['patronymic']['female']
