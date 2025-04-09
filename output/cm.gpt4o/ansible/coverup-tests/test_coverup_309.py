# file lib/ansible/utils/_junit_xml.py:67-83
# lines [67, 68, 69, 70, 71, 72, 73, 74, 76, 77, 78, 79, 80, 82]
# branches []

import pytest
import decimal
from ansible.utils._junit_xml import TestCase, TestError, TestFailure

def test_testcase_initialization():
    # Test initialization with all fields
    name = "test_case_1"
    assertions = 5
    classname = "TestClass"
    status = "passed"
    time = decimal.Decimal("1.23")
    errors = [TestError(message="error1", type="type1")]
    failures = [TestFailure(message="failure1", type="type1")]
    skipped = "skipped_reason"
    system_out = "system output"
    system_err = "system error"
    is_disabled = True

    test_case = TestCase(
        name=name,
        assertions=assertions,
        classname=classname,
        status=status,
        time=time,
        errors=errors,
        failures=failures,
        skipped=skipped,
        system_out=system_out,
        system_err=system_err,
        is_disabled=is_disabled
    )

    assert test_case.name == name
    assert test_case.assertions == assertions
    assert test_case.classname == classname
    assert test_case.status == status
    assert test_case.time == time
    assert test_case.errors == errors
    assert test_case.failures == failures
    assert test_case.skipped == skipped
    assert test_case.system_out == system_out
    assert test_case.system_err == system_err
    assert test_case.is_disabled == is_disabled

def test_testcase_default_initialization():
    # Test initialization with default values
    name = "test_case_2"
    test_case = TestCase(name=name)

    assert test_case.name == name
    assert test_case.assertions is None
    assert test_case.classname is None
    assert test_case.status is None
    assert test_case.time is None
    assert test_case.errors == []
    assert test_case.failures == []
    assert test_case.skipped is None
    assert test_case.system_out is None
    assert test_case.system_err is None
    assert test_case.is_disabled is False
