# file: sty/primitive.py:78-91
# asked: {"lines": [83], "branches": [[82, 83]]}
# gained: {"lines": [83], "branches": [[82, 83]]}

import pytest
from sty.primitive import Register, Style

class MockStyle(Style):
    def __new__(cls, *rules, value=''):
        return super().__new__(cls, *rules, value=value)

@pytest.fixture
def register():
    class TestRegister(Register):
        is_muted = False
        renderfuncs = []

    return TestRegister()

def test_setattr_with_muted_style(register, mocker):
    mocker.patch.object(register, 'is_muted', True)
    style = MockStyle('rule1', 'rule2')
    register.__setattr__('test_attr', style)
    assert isinstance(register.test_attr, Style)
    assert register.test_attr.rules == ('rule1', 'rule2')
    assert register.test_attr == ''

def test_setattr_with_non_muted_style(register, mocker):
    def mock_render_rules(renderfuncs, rules):
        return 'rendered_value', rules

    mocker.patch.object(register, 'is_muted', False)
    mocker.patch('sty.primitive._render_rules', side_effect=mock_render_rules)
    style = MockStyle('rule1', 'rule2')
    register.__setattr__('test_attr', style)
    assert isinstance(register.test_attr, Style)
    assert register.test_attr.rules == ('rule1', 'rule2')
    assert register.test_attr == 'rendered_value'

def test_setattr_with_non_style(register):
    register.__setattr__('test_attr', 'non_style_value')
    assert register.test_attr == 'non_style_value'
