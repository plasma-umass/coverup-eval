# file: sty/primitive.py:132-140
# asked: {"lines": [132, 139, 140], "branches": []}
# gained: {"lines": [132, 139, 140], "branches": []}

import pytest
from unittest.mock import Mock, patch
from sty.primitive import Register, RenderType

@pytest.fixture
def register():
    return Register()

def test_set_rgb_call(register):
    mock_render_type = Mock(spec=RenderType)
    mock_func = Mock()
    
    with patch.object(register, 'renderfuncs', {mock_render_type: mock_func}):
        register.set_rgb_call(mock_render_type)
        assert register.rgb_call == mock_func
