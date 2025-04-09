# file thonny/jedi_utils.py:134-135
# lines [134, 135]
# branches []

import pytest
from unittest import mock

# Assuming the function _using_older_jedi is imported from thonny.jedi_utils
from thonny.jedi_utils import _using_older_jedi

def test_using_older_jedi():
    # Mocking the jedi module with different versions
    jedi_mock_1 = mock.Mock()
    jedi_mock_1.__version__ = "0.13.2"
    assert _using_older_jedi(jedi_mock_1) == True

    jedi_mock_2 = mock.Mock()
    jedi_mock_2.__version__ = "0.14.1"
    assert _using_older_jedi(jedi_mock_2) == True

    jedi_mock_3 = mock.Mock()
    jedi_mock_3.__version__ = "0.15.0"
    assert _using_older_jedi(jedi_mock_3) == True

    jedi_mock_4 = mock.Mock()
    jedi_mock_4.__version__ = "0.16.3"
    assert _using_older_jedi(jedi_mock_4) == True

    jedi_mock_5 = mock.Mock()
    jedi_mock_5.__version__ = "0.17.0"
    assert _using_older_jedi(jedi_mock_5) == True

    jedi_mock_6 = mock.Mock()
    jedi_mock_6.__version__ = "0.18.0"
    assert _using_older_jedi(jedi_mock_6) == False

    jedi_mock_7 = mock.Mock()
    jedi_mock_7.__version__ = "1.0.0"
    assert _using_older_jedi(jedi_mock_7) == False

    jedi_mock_8 = mock.Mock()
    jedi_mock_8.__version__ = "0.12.0"
    assert _using_older_jedi(jedi_mock_8) == False
