# file mimesis/providers/person.py:243-275
# lines [255, 256, 259, 260, 262, 264, 265, 267, 268, 270, 272, 273, 274]
# branches ['255->256', '255->259', '259->260', '259->262', '264->265', '264->267', '267->268', '267->270']

import pytest
from mimesis.providers import Person
from mimesis.data import EMAIL_DOMAINS

def test_email_with_unique_and_seed(mocker):
    person = Person(seed=1234)
    with pytest.raises(ValueError, match='You cannot use «unique» parameter with a seeded provider'):
        person.email(unique=True)

def test_email_with_custom_domains():
    person = Person()
    custom_domains = ['example.com', 'test.org']
    email = person.email(domains=custom_domains)
    assert any(email.endswith(f'@{domain}') for domain in custom_domains)

def test_email_with_default_domains(mocker):
    person = Person()
    mocker.patch('mimesis.providers.person.EMAIL_DOMAINS', ['default.com'])
    email = person.email()
    assert email.endswith('@default.com')

def test_email_with_unique():
    person = Person()
    email = person.email(unique=True)
    assert '@' in email
    assert len(email.split('@')[0]) > 0

def test_email_without_unique():
    person = Person()
    email = person.email(unique=False)
    assert '@' in email
    assert len(email.split('@')[0]) > 0
