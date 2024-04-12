# file mimesis/schema.py:47-111
# lines [47, 48, 73, 74, 76, 83, 85, 86, 88, 89, 90, 92, 93, 94, 96, 97, 99, 100, 101, 102, 104, 106, 107, 108, 109, 110, 111]
# branches ['73->74', '73->76', '85->86', '85->88', '89->exit', '89->90', '93->94', '93->106', '94->96', '94->104', '96->97', '96->99', '99->100', '99->106', '101->99', '101->102', '107->108', '107->109']

import pytest
from mimesis.schema import AbstractField, UndefinedField, UnacceptableField, UnsupportedField
from mimesis import Generic
from unittest.mock import Mock


class MockProvider:
    class Meta:
        name = 'mock_provider'

    @staticmethod
    def mock_method():
        return 'mock_value'


@pytest.fixture
def mock_generic(mocker):
    gen = mocker.Mock(spec=Generic)
    mocker.patch.object(gen, 'mock_provider', MockProvider(), create=True)
    mocker.patch.object(gen.mock_provider, 'Meta', MockProvider.Meta, create=True)
    mocker.patch.object(gen, 'choice', create=True)
    gen.choice.Meta.name = 'choice'
    return gen


def test_abstract_field_call_with_undefined_field():
    field = AbstractField()
    with pytest.raises(UndefinedField):
        field()


def test_abstract_field_call_with_unacceptable_field(mock_generic):
    field = AbstractField()
    field._gen = mock_generic
    field._table = {}
    with pytest.raises(UnacceptableField):
        field(name='mock_provider.mock_method.invalid')


def test_abstract_field_call_with_unsupported_field(mock_generic):
    field = AbstractField()
    field._gen = mock_generic
    field._table = {}
    with pytest.raises(UnsupportedField):
        field(name='nonexistent')


def test_abstract_field_call_with_valid_field_and_key_function(mock_generic):
    field = AbstractField()
    field._gen = mock_generic
    field._table = {}
    result = field(name='mock_provider.mock_method', key=lambda x: x.upper())
    assert result == 'MOCK_VALUE'


def test_abstract_field_call_with_valid_field_no_key_function(mock_generic):
    field = AbstractField()
    field._gen = mock_generic
    field._table = {}
    result = field(name='mock_provider.mock_method')
    assert result == 'mock_value'


def test_abstract_field_call_with_valid_nested_field(mock_generic):
    field = AbstractField()
    field._gen = mock_generic
    field._table = {}
    result = field(name='mock_provider.mock_method')
    assert result == 'mock_value'


def test_abstract_field_call_with_valid_nested_field_and_key_function(mock_generic):
    field = AbstractField()
    field._gen = mock_generic
    field._table = {}
    result = field(name='mock_provider.mock_method', key=lambda x: x.split())
    assert result == ['mock_value']
