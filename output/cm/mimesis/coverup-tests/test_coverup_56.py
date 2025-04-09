# file mimesis/providers/person.py:43-46
# lines [43, 44, 46]
# branches []

import pytest
from mimesis.providers.person import Person

def test_person_meta_name():
    person_provider = Person()
    assert person_provider.Meta.name == 'person'
