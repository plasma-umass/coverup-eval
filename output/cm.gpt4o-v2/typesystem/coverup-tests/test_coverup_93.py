# file: typesystem/json_schema.py:397-562
# asked: {"lines": [401, 402, 403, 404, 406, 407, 408, 410, 411, 412, 413, 414, 415, 417, 419, 420, 421, 422, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 439, 440, 441, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 458, 459, 460, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 476, 477, 478, 479, 481, 482, 484, 485, 487, 488, 489, 490, 491, 492, 493, 495, 496, 497, 498, 500, 501, 502, 504, 505, 507, 508, 509, 511, 512, 513, 514, 515, 516, 518, 519, 520, 522, 523, 524, 526, 527, 528, 530, 532, 533, 534, 536, 538, 539, 540, 542, 544, 545, 546, 547, 548, 549, 550, 552, 553, 554, 556, 557, 558, 560, 561, 562], "branches": [[401, 402], [401, 403], [403, 404], [403, 406], [410, 411], [410, 412], [412, 413], [412, 417], [414, 415], [414, 419], [419, 420], [419, 425], [425, 426], [425, 443], [428, 429], [428, 430], [430, 431], [430, 432], [432, 433], [432, 440], [433, 434], [433, 439], [440, 441], [440, 560], [443, 444], [443, 458], [447, 448], [447, 449], [449, 450], [449, 451], [451, 452], [451, 453], [453, 454], [453, 455], [455, 456], [455, 560], [458, 459], [458, 462], [462, 463], [462, 487], [465, 466], [465, 467], [467, 468], [467, 469], [469, 470], [469, 477], [470, 471], [470, 476], [477, 478], [477, 484], [478, 479], [478, 481], [484, 485], [484, 560], [487, 488], [487, 518], [490, 491], [490, 495], [495, 496], [495, 500], [500, 501], [500, 507], [501, 502], [501, 504], [507, 508], [507, 511], [511, 512], [511, 513], [513, 514], [513, 515], [515, 516], [515, 560], [518, 519], [518, 522], [522, 523], [522, 526], [526, 527], [526, 532], [532, 533], [532, 538], [538, 539], [538, 544], [544, 545], [544, 552], [546, 547], [546, 548], [548, 549], [548, 550], [552, 553], [552, 556], [556, 557], [556, 560], [560, 561], [560, 562]]}
# gained: {"lines": [401, 402, 403, 404, 406, 407, 408, 410, 411, 412, 413, 414, 415, 419, 420, 421, 422, 425, 426, 427, 428, 429, 430, 432, 440, 443, 444, 445, 446, 447, 449, 451, 453, 455, 458, 459, 460, 462, 463, 464, 465, 467, 469, 470, 476, 477, 478, 479, 484, 487, 488, 489, 490, 491, 492, 493, 495, 500, 501, 502, 507, 511, 513, 515, 518, 519, 520, 522, 523, 524, 526, 527, 528, 530, 532, 533, 534, 536, 538, 539, 540, 542, 544, 545, 546, 547, 548, 549, 550, 552, 553, 554, 556, 560, 561, 562], "branches": [[401, 402], [401, 403], [403, 404], [403, 406], [410, 411], [410, 412], [412, 413], [414, 415], [414, 419], [419, 420], [419, 425], [425, 426], [425, 443], [428, 429], [430, 432], [432, 440], [440, 560], [443, 444], [443, 458], [447, 449], [449, 451], [451, 453], [453, 455], [455, 560], [458, 459], [458, 462], [462, 463], [462, 487], [465, 467], [467, 469], [469, 470], [470, 476], [477, 478], [478, 479], [484, 560], [487, 488], [487, 518], [490, 491], [495, 500], [500, 501], [501, 502], [507, 511], [511, 513], [513, 515], [515, 560], [518, 519], [518, 522], [522, 523], [522, 526], [526, 527], [526, 532], [532, 533], [532, 538], [538, 539], [538, 544], [544, 545], [544, 552], [546, 547], [548, 549], [552, 553], [552, 556], [556, 560], [560, 561], [560, 562]]}

import pytest
from typesystem.json_schema import to_json_schema
from typesystem.fields import (
    Any, String, Integer, Float, Decimal, Boolean, Array, Object, Choice, Const, Union
)
from typesystem.schemas import Reference, SchemaDefinitions
from typesystem.composites import NeverMatch, OneOf, AllOf, IfThenElse, Not

def test_to_json_schema_any():
    field = Any()
    result = to_json_schema(field)
    assert result is True

def test_to_json_schema_never_match():
    field = NeverMatch()
    result = to_json_schema(field)
    assert result is False

def test_to_json_schema_string():
    field = String()
    result = to_json_schema(field)
    assert result["type"] == "string"

def test_to_json_schema_integer():
    field = Integer()
    result = to_json_schema(field)
    assert result["type"] == "integer"

def test_to_json_schema_float():
    field = Float()
    result = to_json_schema(field)
    assert result["type"] == "number"

def test_to_json_schema_decimal():
    field = Decimal()
    result = to_json_schema(field)
    assert result["type"] == "number"

def test_to_json_schema_boolean():
    field = Boolean()
    result = to_json_schema(field)
    assert result["type"] == "boolean"

def test_to_json_schema_array():
    field = Array(items=String())
    result = to_json_schema(field)
    assert result["type"] == "array"
    assert result["items"]["type"] == "string"

def test_to_json_schema_object():
    field = Object(properties={"name": String()})
    result = to_json_schema(field)
    assert result["type"] == "object"
    assert result["properties"]["name"]["type"] == "string"

def test_to_json_schema_choice():
    field = Choice(choices=[("A", "Option A"), ("B", "Option B")])
    result = to_json_schema(field)
    assert result["enum"] == ["A", "B"]

def test_to_json_schema_const():
    field = Const(const="fixed_value")
    result = to_json_schema(field)
    assert result["const"] == "fixed_value"

def test_to_json_schema_union():
    field = Union(any_of=[String(), Integer()])
    result = to_json_schema(field)
    assert result["anyOf"][0]["type"] == "string"
    assert result["anyOf"][1]["type"] == "integer"

def test_to_json_schema_one_of():
    field = OneOf(one_of=[String(), Integer()])
    result = to_json_schema(field)
    assert result["oneOf"][0]["type"] == "string"
    assert result["oneOf"][1]["type"] == "integer"

def test_to_json_schema_all_of():
    field = AllOf(all_of=[String(), Integer()])
    result = to_json_schema(field)
    assert result["allOf"][0]["type"] == "string"
    assert result["allOf"][1]["type"] == "integer"

def test_to_json_schema_if_then_else():
    field = IfThenElse(if_clause=String(), then_clause=Integer(), else_clause=Boolean())
    result = to_json_schema(field)
    assert result["if"]["type"] == "string"
    assert result["then"]["type"] == "integer"
    assert result["else"]["type"] == "boolean"

def test_to_json_schema_not():
    field = Not(negated=String())
    result = to_json_schema(field)
    assert result["not"]["type"] == "string"

def test_to_json_schema_reference():
    definitions = SchemaDefinitions({"SomeSchema": String()})
    field = Reference(to="SomeSchema", definitions=definitions)
    result = to_json_schema(field)
    assert "$ref" in result

def test_to_json_schema_schema_definitions():
    definitions = SchemaDefinitions({"SomeSchema": String()})
    result = to_json_schema(definitions)
    assert "SomeSchema" in result["definitions"]
