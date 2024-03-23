# file mimesis/schema.py:47-111
# lines [97]
# branches ['89->exit', '96->97']

import pytest
from mimesis.schema import AbstractField, UndefinedField, UnacceptableField, UnsupportedField
from mimesis import Generic
from unittest.mock import Mock, patch

def test_abstract_field_call_with_undefined_field():
    field = AbstractField()
    field._gen = Generic()
    field._table = {}

    with pytest.raises(UndefinedField):
        field()

def test_abstract_field_call_with_unacceptable_field():
    field = AbstractField()
    field._gen = Generic()
    field._table = {}

    with pytest.raises(UnacceptableField):
        field(name='choice.Meta.name')

def test_abstract_field_call_with_unsupported_field():
    field = AbstractField()
    field._gen = Generic()
    field._table = {}

    with pytest.raises(UnsupportedField):
        field(name='nonexistent')

def test_abstract_field_call_with_choice_meta_name():
    field = AbstractField()
    field._gen = Generic()
    field._table = {}

    # Mock the choice.Meta.name to match the condition
    with patch('mimesis.schema.Generic') as mock_generic:
        mock_choice = Mock()
        mock_choice.Meta.name = 'choice'
        mock_generic.return_value = Mock(choice=mock_choice)
        field._gen = mock_generic.return_value

        field(name='choice')
        assert field._table['choice'] == field._gen.choice

# Include this test to improve coverage for branch 89->exit
def test_abstract_field_call_with_tail_parser():
    field = AbstractField()
    field._gen = Generic()
    field._table = {}

    # Mock the Generic object to have a provider with a method
    mock_provider = Mock()
    mock_method = Mock(return_value='mocked_value')
    setattr(mock_provider, 'mock_method', mock_method)
    setattr(field._gen, 'mock_provider', mock_provider)

    result = field(name='mock_provider.mock_method')
    assert result == 'mocked_value'
