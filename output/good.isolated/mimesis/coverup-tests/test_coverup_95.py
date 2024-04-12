# file mimesis/builtins/ru.py:37-48
# lines [37, 46, 47, 48]
# branches []

import pytest
from mimesis.enums import Gender
from mimesis.builtins.ru import RussiaSpecProvider

def test_russia_spec_provider_patronymic():
    provider = RussiaSpecProvider()

    # Test for male gender
    male_patronymic = provider.patronymic(gender=Gender.MALE)
    assert any(male_patronymic.endswith(suffix) for suffix in ['евич', 'ович']), "Should return a male patronymic"

    # Test for female gender
    female_patronymic = provider.patronymic(gender=Gender.FEMALE)
    assert any(female_patronymic.endswith(suffix) for suffix in ['евна', 'овна']), "Should return a female patronymic"

    # Test for default (random) gender
    default_patronymic = provider.patronymic()
    assert any(default_patronymic.endswith(suffix) for suffix in ['евич', 'ович', 'евна', 'овна']), "Should return a patronymic for any gender"
