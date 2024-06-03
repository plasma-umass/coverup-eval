# file thefuck/shells/generic.py:38-40
# lines [38, 39, 40]
# branches []

import pytest
from thefuck.shells.generic import Generic

def test_app_alias():
    generic = Generic()
    alias_name = 'test_alias'
    expected_alias = """alias test_alias='eval "$(TF_ALIAS=test_alias PYTHONIOENCODING=utf-8 """ \
                     """thefuck "$(fc -ln -1)")"'"""
    result = generic.app_alias(alias_name)
    assert result == expected_alias

@pytest.fixture(autouse=True)
def cleanup(mocker):
    # This fixture will run before and after each test to ensure a clean state
    yield
    mocker.stopall()
