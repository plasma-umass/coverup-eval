# file mimesis/providers/person.py:171-221
# lines [171, 191, 192, 193, 195, 198, 199, 201, 202, 204, 205, 206, 208, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 221]
# branches ['198->199', '198->201', '201->202', '201->204', '204->205', '204->208', '211->212', '211->221', '212->213', '212->214', '214->215', '214->216', '216->217', '216->218', '218->211', '218->219']

import pytest
from mimesis.providers.person import Person
from mimesis.exceptions import NonEnumerableError
from unittest.mock import Mock

def test_username_with_unsupported_template(mocker):
    person = Person()
    mocker.patch.object(person.random, 'choice', side_effect=person.random.choice)
    mocker.patch.object(person.random, 'randint', side_effect=person.random.randint)

    with pytest.raises(ValueError):
        person.username(template="unsupported_template")

    assert person.random.choice.call_count == 0
    assert person.random.randint.call_count == 0
