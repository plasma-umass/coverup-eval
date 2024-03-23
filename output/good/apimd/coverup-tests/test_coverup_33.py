# file apimd/parser.py:451-492
# lines [454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 472, 473, 474, 475, 476, 477, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492]
# branches ['455->456', '455->457', '460->461', '460->488', '461->462', '461->467', '463->464', '463->465', '465->460', '465->466', '467->472', '467->480', '473->474', '473->475', '475->460', '475->476', '476->477', '476->479', '480->460', '480->481', '481->460', '481->482', '482->483', '482->484', '486->481', '486->487', '488->489', '488->490', '490->exit', '490->491']

import pytest
from apimd.parser import Parser
from ast import AnnAssign, Assign, Delete, Name, Constant, walk
from dataclasses import dataclass

@dataclass
class MockExpr:
    id: str

def test_class_api_coverage(mocker):
    parser = Parser()
    parser.doc = {}
    parser.resolve = mocker.MagicMock(side_effect=lambda root, d: f"resolved_{d.id}")

    root = "root"
    name = "MyClass"
    bases = [MockExpr(id="base1"), MockExpr(id="base2")]
    body = [
        AnnAssign(target=Name(id="public_attr"), annotation=MockExpr(id="int"), simple=1),
        Assign(targets=[Name(id="enum_attr")], value=Constant(value=1), type_comment=None),
        Assign(targets=[Name(id="private_attr")], value=Constant(value=1), type_comment="str"),
        Delete(targets=[Name(id="public_attr")]),
    ]

    def is_public_family(attr):
        return not attr.startswith("_")

    mocker.patch('apimd.parser.is_public_family', side_effect=is_public_family)

    # Initialize the doc for the class name
    parser.doc[name] = ""

    parser.class_api(root, name, bases, body)

    parser.resolve.assert_any_call(root, bases[0])
    parser.resolve.assert_any_call(root, bases[1])
    parser.resolve.assert_any_call(root, body[0].annotation)

    assert "resolved_base1" in parser.doc[name]
    assert "resolved_base2" in parser.doc[name]
    assert "enum_attr" in parser.doc[name]
    assert "resolved_int" in parser.doc[name] or "str" in parser.doc[name]
