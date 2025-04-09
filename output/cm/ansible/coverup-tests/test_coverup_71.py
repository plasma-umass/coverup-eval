# file lib/ansible/modules/systemd.py:299-331
# lines [299, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 326, 327, 328, 329, 330, 331]
# branches ['315->316', '315->331', '316->317', '316->326', '317->315', '317->318', '319->320', '319->323', '320->321', '320->323', '327->315', '327->328']

import pytest

@pytest.fixture
def systemctl_show_output():
    # Fixture to simulate systemctl show output
    return [
        "ExecStart={/usr/bin/mydaemon",
        "arg1",
        "arg2}",
        "Description=A single line description starting with { but not ending with }",
        "ExecReload={/usr/bin/mydaemon-reload",
        "reload-arg}",
        "NormalKey=Value"
    ]

def test_parse_systemctl_show(systemctl_show_output, mocker):
    from ansible.modules.systemd import parse_systemctl_show

    parsed = parse_systemctl_show(systemctl_show_output)

    # Assertions to verify postconditions
    assert parsed.get('ExecStart') == "{/usr/bin/mydaemon\narg1\narg2}"
    assert parsed.get('Description') == "A single line description starting with { but not ending with }"
    assert parsed.get('ExecReload') == "{/usr/bin/mydaemon-reload\nreload-arg}"
    assert parsed.get('NormalKey') == "Value"
    assert 'arg1' not in parsed
    assert 'arg2}' not in parsed
    assert 'reload-arg}' not in parsed

    # No cleanup is necessary as the test does not modify any external state
