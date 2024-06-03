# file apimd/parser.py:494-511
# lines [497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 511]
# branches ['498->exit', '498->499', '499->500', '499->506', '500->501', '500->505', '502->503', '502->505', '506->507', '506->508', '508->509', '508->511']

import pytest
from unittest.mock import Mock
from dataclasses import dataclass
from typing import Optional, Sequence, Iterator
from apimd.parser import Parser

@dataclass
class Arg:
    arg: str
    annotation: Optional[str] = None

@pytest.fixture
def parser():
    return Parser()

def test_func_ann(parser, mocker):
    root = "root"
    resolve_mock = mocker.patch.object(parser, 'resolve', side_effect=lambda root, ann, self_ty="": f"resolved_{ann}_{self_ty}")

    # Test case to cover lines 497-511
    args = [
        Arg(arg="self", annotation="self_annotation"),
        Arg(arg="*", annotation=None),
        Arg(arg="arg1", annotation="arg1_annotation"),
        Arg(arg="arg2", annotation=None)
    ]
    
    result = list(parser.func_ann(root, args, has_self=True, cls_method=True))
    
    assert result == [
        'type[Self]',  # Line 505
        '',            # Line 507
        'resolved_arg1_annotation_resolved_self_annotation_',  # Line 509
        'Any'          # Line 511
    ]
    
    resolve_mock.assert_any_call(root, "self_annotation")
    resolve_mock.assert_any_call(root, "arg1_annotation", "resolved_self_annotation_")

    # Clean up
    mocker.stopall()
