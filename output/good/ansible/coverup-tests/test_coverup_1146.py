# file lib/ansible/parsing/splitter.py:155-286
# lines [207, 208, 214, 215, 233, 234, 236, 237, 238, 239, 240, 241, 242, 244, 245, 252, 253, 258, 259, 264, 265, 276, 284]
# branches ['206->207', '213->214', '232->233', '235->236', '236->237', '236->238', '238->239', '238->244', '240->241', '240->242', '251->252', '257->258', '263->264', '269->202', '275->276', '283->284']

import pytest
from ansible.errors import AnsibleParserError
from ansible.parsing.splitter import split_args

def test_split_args_coverage():
    # Test for lines 207-208
    assert split_args('a=1  b=2') == ['a=1 ', 'b=2']
    
    # Test for lines 214-215
    assert split_args('a=1 \\ b=2') == ['a=1', 'b=2']
    
    # Test for lines 233-234
    assert split_args('a="1 2" b=3') == ['a="1 2"', 'b=3']
    
    # Test for lines 236-245
    assert split_args('a="1 2" b=3 c="{{ d }} e"') == ['a="1 2"', 'b=3', 'c="{{ d }} e"']
    assert split_args('a="1 2" b=3 c="{{ d }}\ne"') == ['a="1 2"', 'b=3', 'c="{{ d }}\ne"']
    
    # Test for lines 252-253
    assert split_args('a={{ b }} c') == ['a={{ b }}', 'c']
    
    # Test for lines 258-259
    assert split_args('a={% b %} c') == ['a={% b %}', 'c']
    
    # Test for lines 264-265
    assert split_args('a={# b #} c') == ['a={# b #}', 'c']
    
    # Test for line 276
    assert split_args('a=1\nb=2') == ['a=1\n', 'b=2']
    
    # Test for line 284
    with pytest.raises(AnsibleParserError):
        split_args('a="1 2 b=3')
    
    # Test for branch 269->202
    assert split_args('a=1 b=2 c=3') == ['a=1', 'b=2', 'c=3']
