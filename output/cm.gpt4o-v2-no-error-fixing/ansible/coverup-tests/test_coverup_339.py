# file: lib/ansible/module_utils/urls.py:1169-1183
# asked: {"lines": [1169, 1177, 1178, 1179, 1180, 1181, 1182, 1183], "branches": []}
# gained: {"lines": [1169, 1177, 1178, 1179, 1180, 1181, 1182, 1183], "branches": []}

import pytest
from ansible.module_utils.urls import rfc2822_date_string

def test_rfc2822_date_string():
    timetuple = (2001, 11, 9, 1, 8, 47, 4, 313, 0)  # Corresponds to Fri, 09 Nov 2001 01:08:47
    expected_result = "Fri, 09 Nov 2001 01:08:47 -0000"
    assert rfc2822_date_string(timetuple) == expected_result

    timetuple = (2023, 10, 5, 14, 30, 0, 3, 278, 0)  # Corresponds to Thu, 05 Oct 2023 14:30:00
    expected_result = "Thu, 05 Oct 2023 14:30:00 +0200"
    assert rfc2822_date_string(timetuple, "+0200") == expected_result

    timetuple = (1999, 12, 31, 23, 59, 59, 4, 365, 0)  # Corresponds to Fri, 31 Dec 1999 23:59:59
    expected_result = "Fri, 31 Dec 1999 23:59:59 +0530"
    assert rfc2822_date_string(timetuple, "+0530") == expected_result
