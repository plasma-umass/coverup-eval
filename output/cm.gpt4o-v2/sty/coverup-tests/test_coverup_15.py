# file: sty/primitive.py:78-91
# asked: {"lines": [83], "branches": [[82, 83]]}
# gained: {"lines": [83], "branches": [[82, 83]]}

import pytest
from sty.primitive import Register, Style

@pytest.fixture
def register():
    return Register()

def test_setattr_with_muted_style(register, mocker):
    # Mock the is_muted attribute to return True
    mocker.patch.object(register, 'is_muted', True)
    
    # Create a Style object
    style = Style('rule1', 'rule2')
    
    # Set the attribute
    register.test_attr = style
    
    # Verify that the attribute was set correctly
    assert isinstance(register.test_attr, Style)
    assert register.test_attr.rules == ('rule1', 'rule2')
    assert str(register.test_attr) == ''

def test_setattr_with_non_muted_style(register, mocker):
    # Mock the is_muted attribute to return False
    mocker.patch.object(register, 'is_muted', False)
    
    # Mock the _render_rules function
    mock_render_rules = mocker.patch('sty.primitive._render_rules', return_value=('rendered_value', ['rule1', 'rule2']))
    
    # Create a Style object
    style = Style('rule1', 'rule2')
    
    # Set the attribute
    register.test_attr = style
    
    # Verify that the _render_rules function was called correctly
    mock_render_rules.assert_called_once_with(register.renderfuncs, style.rules)
    
    # Verify that the attribute was set correctly
    assert isinstance(register.test_attr, Style)
    assert register.test_attr.rules == ('rule1', 'rule2')
    assert str(register.test_attr) == 'rendered_value'

def test_setattr_with_non_style(register):
    # Set a non-Style attribute
    register.test_attr = 'non_style_value'
    
    # Verify that the attribute was set correctly
    assert register.test_attr == 'non_style_value'
