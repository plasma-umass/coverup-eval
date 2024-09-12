# file: lib/ansible/module_utils/urls.py:1169-1183
# asked: {"lines": [1169, 1177, 1178, 1179, 1180, 1181, 1182, 1183], "branches": []}
# gained: {"lines": [1169, 1177, 1178, 1179, 1180, 1181, 1182, 1183], "branches": []}

import pytest
from ansible.module_utils.urls import rfc2822_date_string

def test_rfc2822_date_string():
    timetuple = (2001, 11, 9, 1, 8, 47, 4, 313, 0)  # Corresponds to Fri, 09 Nov 2001 01:08:47
    expected = "Fri, 09 Nov 2001 01:08:47 -0000"
    assert rfc2822_date_string(timetuple) == expected

    timetuple = (2023, 10, 5, 14, 30, 0, 3, 278, 0)  # Corresponds to Thu, 05 Oct 2023 14:30:00
    expected = "Thu, 05 Oct 2023 14:30:00 +0200"
    assert rfc2822_date_string(timetuple, "+0200") == expected

    timetuple = (1999, 1, 1, 0, 0, 0, 4, 0, 0)  # Corresponds to Fri, 01 Jan 1999 00:00:00
    expected = "Fri, 01 Jan 1999 00:00:00 +0530"
    assert rfc2822_date_string(timetuple, "+0530") == expected
