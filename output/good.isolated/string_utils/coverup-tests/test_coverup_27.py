# file string_utils/validation.py:204-244
# lines [204, 220, 221, 223, 225, 228, 229, 232, 233, 234, 236, 238, 240, 242, 244]
# branches ['220->221', '220->223', '228->229', '228->232', '233->234', '233->236', '240->242', '240->244']

import re
import pytest
from string_utils.validation import is_email

@pytest.fixture
def mock_email_re(mocker):
    pattern_mock = mocker.MagicMock(spec=re.Pattern)
    match_mock = mocker.MagicMock(return_value=True)
    pattern_mock.match = match_mock
    mocker.patch('string_utils.validation.EMAIL_RE', new=pattern_mock)
    return match_mock

def test_is_email_with_escaped_at_sign(mock_email_re):
    assert is_email('valid\\@email.com') == True
    mock_email_re.assert_called_once()
