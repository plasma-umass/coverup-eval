# file lib/ansible/plugins/shell/powershell.py:120-133
# lines [123, 124, 125, 126, 128, 132, 133]
# branches ['123->124', '123->125']

import pytest
from ansible.plugins.shell.powershell import ShellModule

@pytest.fixture
def powershell_shell(mocker):
    mocker.patch.object(ShellModule, '_encode_script')
    mocker.patch.object(ShellModule, '_escape')
    mocker.patch.object(ShellModule, '_unquote')
    mocker.patch.object(ShellModule, 'get_option', return_value='C:\\Windows\\Temp')
    shell_module = ShellModule()
    shell_module._encode_script.side_effect = lambda script: script
    shell_module._escape.side_effect = lambda x: x
    shell_module._unquote.side_effect = lambda x: x
    return shell_module

def test_mkdtemp_without_basefile(powershell_shell):
    # Test mkdtemp without providing a basefile
    temp_dir_name = "ansible_temp"
    powershell_shell.__class__._generate_temp_dir_name = lambda: temp_dir_name
    result = powershell_shell.mkdtemp()
    expected_script = '''
$tmp_path = [System.Environment]::ExpandEnvironmentVariables('C:\\Windows\\Temp')
$tmp = New-Item -Type Directory -Path $tmp_path -Name 'ansible_temp'
Write-Output -InputObject $tmp.FullName
'''.strip()
    # Normalize the script by removing extra indentation
    result = "\n".join(line.strip() for line in result.splitlines())
    assert result == expected_script
    assert powershell_shell._encode_script.called
    assert powershell_shell._escape.called
    assert powershell_shell._unquote.called

def test_mkdtemp_with_basefile_and_tmpdir(powershell_shell):
    # Test mkdtemp with providing a basefile and tmpdir
    basefile = "custom_base"
    tmpdir = "D:\\Custom\\Temp"
    result = powershell_shell.mkdtemp(basefile=basefile, tmpdir=tmpdir)
    expected_script = '''
$tmp_path = [System.Environment]::ExpandEnvironmentVariables('D:\\Custom\\Temp')
$tmp = New-Item -Type Directory -Path $tmp_path -Name 'custom_base'
Write-Output -InputObject $tmp.FullName
'''.strip()
    # Normalize the script by removing extra indentation
    result = "\n".join(line.strip() for line in result.splitlines())
    assert result == expected_script
    assert powershell_shell._encode_script.called
    assert powershell_shell._escape.called
    assert powershell_shell._unquote.called
