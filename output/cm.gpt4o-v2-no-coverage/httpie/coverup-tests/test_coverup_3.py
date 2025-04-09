# file: httpie/utils.py:124-136
# asked: {"lines": [124, 131, 132, 133, 134, 135, 136], "branches": [[131, 0], [131, 132], [132, 133], [132, 134], [135, 131], [135, 136]]}
# gained: {"lines": [124, 131, 132, 133, 134, 135, 136], "branches": [[131, 0], [131, 132], [132, 133], [132, 134], [135, 131], [135, 136]]}

import pytest
from datetime import datetime, timedelta

def test_max_age_to_expires():
    from httpie.utils import _max_age_to_expires

    now = datetime.now().timestamp()

    # Test case 1: Cookie with 'expires' already set
    cookies = [{'expires': now + 1000}]
    _max_age_to_expires(cookies, now)
    assert cookies[0]['expires'] == now + 1000

    # Test case 2: Cookie with 'max-age' set to a valid digit
    cookies = [{'max-age': '1000'}]
    _max_age_to_expires(cookies, now)
    assert cookies[0]['expires'] == now + 1000

    # Test case 3: Cookie with 'max-age' set to a non-digit
    cookies = [{'max-age': 'abc'}]
    _max_age_to_expires(cookies, now)
    assert 'expires' not in cookies[0]

    # Test case 4: Cookie with no 'max-age' and no 'expires'
    cookies = [{}]
    _max_age_to_expires(cookies, now)
    assert 'expires' not in cookies[0]

    # Test case 5: Multiple cookies with mixed attributes
    cookies = [
        {'expires': now + 1000},
        {'max-age': '1000'},
        {'max-age': 'abc'},
        {}
    ]
    _max_age_to_expires(cookies, now)
    assert cookies[0]['expires'] == now + 1000
    assert cookies[1]['expires'] == now + 1000
    assert 'expires' not in cookies[2]
    assert 'expires' not in cookies[3]
