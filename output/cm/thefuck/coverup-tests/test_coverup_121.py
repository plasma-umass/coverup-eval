# file thefuck/logs.py:137-141
# lines [138, 139, 140, 141]
# branches []

import pytest
from thefuck.logs import version
from unittest.mock import patch

def test_version_output(capsys):
    with patch('sys.stderr') as mock_stderr:
        version('1.0', '3.8', 'Bash')
        mock_stderr.write.assert_called_once_with(
            u'The Fuck 1.0 using Python 3.8 and Bash\n'
        )
