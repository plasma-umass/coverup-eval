# file: sty/primitive.py:78-91
# asked: {"lines": [78, 80, 82, 83, 85, 86, 88, 91], "branches": [[80, 82], [80, 91], [82, 83], [82, 85]]}
# gained: {"lines": [78, 80, 82, 83, 85, 86, 88, 91], "branches": [[80, 82], [80, 91], [82, 83], [82, 85]]}

import pytest
from sty.primitive import Register, Style
from sty.rendertype import RenderType, RgbFg, Sgr

@pytest.fixture
def register():
    return Register()

def test_setattr_with_style(register, mocker):
    mocker.patch.object(register, 'is_muted', False)
    mocker.patch.object(register, 'renderfuncs', {RgbFg: lambda r, g, b: f'\x1b[38;2;{r};{g};{b}m', Sgr: lambda x: f'\x1b[{x}m'})
    
    style = Style(RgbFg(1, 5, 10), Sgr(1))
    register.__setattr__('orange', style)
    
    assert isinstance(register.orange, Style)
    assert str(register.orange) == '\x1b[38;2;1;5;10m\x1b[1m'
    assert all(isinstance(rule, type(expected_rule)) and rule.args == expected_rule.args for rule, expected_rule in zip(register.orange.rules, (RgbFg(1, 5, 10), Sgr(1))))

def test_setattr_with_style_muted(register, mocker):
    mocker.patch.object(register, 'is_muted', True)
    
    style = Style(RgbFg(1, 5, 10), Sgr(1))
    register.__setattr__('orange', style)
    
    assert isinstance(register.orange, Style)
    assert str(register.orange) == ''
    assert all(isinstance(rule, type(expected_rule)) and rule.args == expected_rule.args for rule, expected_rule in zip(register.orange.rules, (RgbFg(1, 5, 10), Sgr(1))))

def test_setattr_with_non_style(register):
    register.__setattr__('non_style', 'some_value')
    
    assert register.non_style == 'some_value'
