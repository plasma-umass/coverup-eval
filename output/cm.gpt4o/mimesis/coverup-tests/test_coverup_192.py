# file mimesis/schema.py:47-111
# lines [88, 89, 90, 97]
# branches ['85->88', '89->exit', '89->90', '96->97']

import pytest
from mimesis.schema import AbstractField, UnsupportedField, UnacceptableField, UndefinedField

class MockProvider:
    class Meta:
        name = 'mock_provider'

    def mock_method(self):
        return 'mocked!'

class MockGenerator:
    choice = MockProvider()

    def __getattr__(self, item):
        if item == 'mock_provider':
            return MockProvider()
        raise AttributeError

@pytest.fixture
def abstract_field():
    af = AbstractField()
    af._gen = MockGenerator()
    af._table = {}
    return af

def test_tail_parser_unacceptable_field(abstract_field):
    with pytest.raises(UnacceptableField):
        abstract_field('mock_provider.mock_method.mock_tail')

def test_tail_parser_success(abstract_field):
    result = abstract_field('mock_provider.mock_method')
    assert result == 'mocked!'

def test_choice_meta_name(abstract_field):
    result = abstract_field('mock_provider.mock_method', key=lambda x: x.upper())
    assert result == 'MOCKED!'
    assert 'mock_provider.mock_method' in abstract_field._table

def test_undefined_field(abstract_field):
    with pytest.raises(UndefinedField):
        abstract_field()

def test_unsupported_field(abstract_field):
    with pytest.raises(UnsupportedField):
        abstract_field('non_existent_method')
