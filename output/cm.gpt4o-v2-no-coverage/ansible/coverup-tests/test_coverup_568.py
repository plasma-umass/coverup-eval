# file: lib/ansible/module_utils/urls.py:1169-1183
# asked: {"lines": [1169, 1177, 1178, 1179, 1180, 1181, 1182, 1183], "branches": []}
# gained: {"lines": [1169, 1177, 1178, 1179, 1180, 1181, 1182, 1183], "branches": []}

import pytest
from ansible.module_utils.urls import rfc2822_date_string

def test_rfc2822_date_string_default_zone():
    timetuple = (2001, 11, 9, 1, 8, 47, 4, 313, 0)  # Corresponds to Fri, 09 Nov 2001 01:08:47
    expected = "Fri, 09 Nov 2001 01:08:47 -0000"
    result = rfc2822_date_string(timetuple)
    assert result == expected

def test_rfc2822_date_string_custom_zone():
    timetuple = (2001, 11, 9, 1, 8, 47, 4, 313, 0)  # Corresponds to Fri, 09 Nov 2001 01:08:47
    expected = "Fri, 09 Nov 2001 01:08:47 +0200"
    result = rfc2822_date_string(timetuple, "+0200")
    assert result == expected

def test_rfc2822_date_string_different_day():
    timetuple = (2023, 10, 4, 12, 0, 0, 2, 277, 0)  # Corresponds to Wed, 04 Oct 2023 12:00:00
    expected = "Wed, 04 Oct 2023 12:00:00 -0000"
    result = rfc2822_date_string(timetuple)
    assert result == expected

def test_rfc2822_date_string_different_month():
    timetuple = (2023, 1, 4, 12, 0, 0, 2, 4, 0)  # Corresponds to Wed, 04 Jan 2023 12:00:00
    expected = "Wed, 04 Jan 2023 12:00:00 -0000"
    result = rfc2822_date_string(timetuple)
    assert result == expected
