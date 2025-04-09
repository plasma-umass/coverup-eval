# file lib/ansible/utils/color.py:104-112
# lines [105, 106, 107, 108, 109, 111, 112]
# branches ['105->106', '105->112', '106->107', '106->108', '108->109', '108->111']

import pytest
from ansible.utils.color import hostcolor

@pytest.mark.parametrize("stats, expected_output, color", [
    ({"failures": 1, "unreachable": 0, "changed": 0}, u"%-37s" % "host", True),
    ({"failures": 0, "unreachable": 1, "changed": 0}, u"%-37s" % "host", True),
    ({"failures": 0, "unreachable": 0, "changed": 1}, u"%-37s" % "host", True),
    ({"failures": 0, "unreachable": 0, "changed": 0}, u"%-37s" % "host", True),
    ({"failures": 0, "unreachable": 0, "changed": 0}, u"%-26s" % "host", False),
])
def test_hostcolor(mocker, stats, expected_output, color):
    mocker.patch('ansible.utils.color.ANSIBLE_COLOR', True)
    mocker.patch('ansible.utils.color.stringc', return_value="host")
    mocker.patch('ansible.utils.color.C.COLOR_ERROR', "red")
    mocker.patch('ansible.utils.color.C.COLOR_CHANGED', "yellow")
    mocker.patch('ansible.utils.color.C.COLOR_OK', "green")

    result = hostcolor("host", stats, color)
    assert result == expected_output
