# file thefuck/exceptions.py:5-6
# lines [5, 6]
# branches []

import pytest
from thefuck.exceptions import NoRuleMatched

def test_no_rule_matched_exception():
    with pytest.raises(NoRuleMatched) as exc_info:
        raise NoRuleMatched("No rule matched for this command")

    assert str(exc_info.value) == "No rule matched for this command"
