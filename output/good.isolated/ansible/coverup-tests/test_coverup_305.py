# file lib/ansible/utils/_junit_xml.py:67-83
# lines [67, 68, 69, 70, 71, 72, 73, 74, 76, 77, 78, 79, 80, 82]
# branches []

import decimal
import pytest
from ansible.utils._junit_xml import TestCase, TestError, TestFailure

def test_testcase_full_coverage(tmp_path, mocker):
    # Setup
    test_case_name = "test_case"
    assertions = 1
    classname = "TestClass"
    status = "passed"
    time = decimal.Decimal("0.123")
    errors = [TestError(message="error1", output="error_output1")]
    failures = [TestFailure(message="failure1", output="failure_output1")]
    skipped = "skipped_reason"
    system_out = "system_out_log"
    system_err = "system_err_log"
    is_disabled = True

    # Create a TestCase instance with all fields populated
    test_case = TestCase(
        name=test_case_name,
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

    # Assertions to ensure all fields are correctly set
    assert test_case.name == test_case_name
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

    # No cleanup required as no external resources are being modified
