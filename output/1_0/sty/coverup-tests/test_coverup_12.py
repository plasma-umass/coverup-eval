# file sty/register.py:78-121
# lines [78, 79, 81, 83, 84, 85, 87, 88, 92, 93, 94, 95, 96, 97, 98, 99, 101, 104, 105, 106, 107, 108, 109, 110, 111, 114, 115, 116, 117, 118, 119, 120, 121]
# branches []

import pytest
from sty import BgRegister, Sgr, EightbitBg, Style, renderfunc

def test_bg_register_init(mocker):
    # Mock the render functions to avoid side effects
    mocker.patch('sty.renderfunc.sgr')
    mocker.patch('sty.renderfunc.eightbit_bg')
    mocker.patch('sty.renderfunc.rgb_bg')

    # Instantiate BgRegister to cover the __init__ method
    bg_register = BgRegister()

    # Assertions to verify the postconditions
    assert isinstance(bg_register.black, Style)
    assert isinstance(bg_register.red, Style)
    assert isinstance(bg_register.green, Style)
    assert isinstance(bg_register.yellow, Style)
    assert isinstance(bg_register.blue, Style)
    assert isinstance(bg_register.magenta, Style)
    assert isinstance(bg_register.cyan, Style)
    assert isinstance(bg_register.li_grey, Style)
    assert isinstance(bg_register.rs, Style)
    assert isinstance(bg_register.da_grey, Style)
    assert isinstance(bg_register.li_red, Style)
    assert isinstance(bg_register.li_green, Style)
    assert isinstance(bg_register.li_yellow, Style)
    assert isinstance(bg_register.li_blue, Style)
    assert isinstance(bg_register.li_magenta, Style)
    assert isinstance(bg_register.li_cyan, Style)
    assert isinstance(bg_register.white, Style)
    assert isinstance(bg_register.da_black, Style)
    assert isinstance(bg_register.da_red, Style)
    assert isinstance(bg_register.da_green, Style)
    assert isinstance(bg_register.da_yellow, Style)
    assert isinstance(bg_register.da_blue, Style)
    assert isinstance(bg_register.da_magenta, Style)
    assert isinstance(bg_register.da_cyan, Style)
    assert isinstance(bg_register.grey, Style)

    # Verify that the correct render functions are set
    assert bg_register.renderfuncs[Sgr] == renderfunc.sgr
    assert bg_register.renderfuncs[EightbitBg] == renderfunc.eightbit_bg

    # Verify that the correct calls are set
    assert bg_register.eightbit_call == renderfunc.eightbit_bg
    assert bg_register.rgb_call == renderfunc.rgb_bg
