# file lib/ansible/module_utils/urls.py:1187-1228
# lines [1187, 1188, 1189, 1190, 1209, 1210, 1211, 1212, 1213, 1214, 1215, 1216, 1217, 1218, 1219, 1220, 1221, 1222, 1223, 1224, 1225, 1226, 1228]
# branches ['1210->1211', '1210->1212', '1225->1226', '1225->1228']

import pytest
from ansible.module_utils.urls import Request
from http.cookiejar import CookieJar

def test_request_init_with_non_dict_headers():
    with pytest.raises(ValueError) as excinfo:
        Request(headers="not-a-dict")
    assert "headers must be a dict" in str(excinfo.value)

def test_request_init_with_cookiejar():
    cj = CookieJar()
    r = Request(cookies=cj)
    assert r.cookies is cj

def test_request_init_without_cookiejar():
    r = Request(cookies=None)
    assert isinstance(r.cookies, CookieJar)
