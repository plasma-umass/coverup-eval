# file mimesis/schema.py:47-111
# lines [73, 74, 76, 83, 85, 86, 88, 89, 90, 92, 93, 94, 96, 97, 99, 100, 101, 102, 104, 106, 107, 108, 109, 110, 111]
# branches ['73->74', '73->76', '85->86', '85->88', '89->exit', '89->90', '93->94', '93->106', '94->96', '94->104', '96->97', '96->99', '99->100', '99->106', '101->99', '101->102', '107->108', '107->109']

import pytest
from mimesis.schema import AbstractField, UndefinedField, UnacceptableField, UnsupportedField
from unittest.mock import Mock

class TestAbstractField:
    @pytest.fixture
    def abstract_field(self):
        af = AbstractField()
        af._table = {}
        af._gen = Mock()
        af._gen.choice.Meta.name = 'choice'
        af._gen.choice = Mock()
        return af

    def test_call_with_none_name(self, abstract_field):
        with pytest.raises(UndefinedField):
            abstract_field()

    def test_call_with_unacceptable_field(self, abstract_field):
        with pytest.raises(UnacceptableField):
            abstract_field('provider.method.submethod')

    def test_call_with_unsupported_field(self, abstract_field):
        with pytest.raises(UnsupportedField):
            abstract_field('unsupported_field')

    def test_call_with_valid_field(self, abstract_field):
        mock_method = Mock(return_value='result')
        abstract_field._gen.provider = Mock()
        setattr(abstract_field._gen.provider, 'method', mock_method)
        abstract_field._table['provider.method'] = mock_method

        result = abstract_field('provider.method')
        assert result == 'result'
        mock_method.assert_called_once()

    def test_call_with_key_function(self, abstract_field):
        mock_method = Mock(return_value='result')
        abstract_field._gen.provider = Mock()
        setattr(abstract_field._gen.provider, 'method', mock_method)
        abstract_field._table['provider.method'] = mock_method

        key_function = Mock(return_value='keyed_result')
        result = abstract_field('provider.method', key=key_function)
        assert result == 'keyed_result'
        mock_method.assert_called_once()
        key_function.assert_called_once_with('result')

    def test_call_with_choice_meta_name(self, abstract_field):
        mock_choice = Mock(return_value='choice_result')
        abstract_field._gen.choice = mock_choice
        abstract_field._table['choice'] = mock_choice

        result = abstract_field('choice')
        assert result == 'choice_result'
        mock_choice.assert_called_once()

    def test_call_with_new_provider_method(self, abstract_field):
        mock_method = Mock(return_value='new_result')
        new_provider = Mock()
        setattr(new_provider, 'new_method', mock_method)
        setattr(abstract_field._gen, 'new_provider', new_provider)

        result = abstract_field('new_method')
        assert result == 'new_result'
        mock_method.assert_called_once()
