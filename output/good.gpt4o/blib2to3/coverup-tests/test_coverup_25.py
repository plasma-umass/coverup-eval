# file src/blib2to3/pgen2/tokenize.py:402-672
# lines [402, 403, 420, 421, 422, 423, 424, 428, 430, 431, 432, 433, 438, 439, 440, 441, 442, 443, 444, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 460, 461, 462, 463, 464, 465, 466, 467, 468, 470, 471, 472, 474, 475, 476, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 490, 491, 492, 493, 495, 496, 497, 499, 500, 501, 503, 504, 505, 506, 507, 508, 509, 510, 511, 513, 514, 516, 517, 518, 520, 521, 522, 523, 524, 526, 528, 529, 530, 531, 533, 535, 536, 537, 538, 541, 542, 543, 545, 546, 547, 548, 549, 550, 552, 553, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 584, 585, 586, 587, 588, 589, 590, 591, 593, 594, 595, 596, 597, 598, 600, 601, 602, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 618, 620, 621, 622, 623, 625, 626, 628, 629, 630, 632, 633, 634, 635, 636, 637, 639, 641, 642, 643, 645, 646, 648, 649, 650, 651, 652, 654, 655, 656, 657, 658, 659, 660, 661, 663, 664, 666, 667, 668, 670, 671, 672]
# branches ['438->439', '446->447', '446->478', '448->449', '448->450', '451->452', '451->462', '462->463', '462->474', '478->479', '478->541', '479->480', '479->481', '482->483', '482->492', '483->484', '483->485', '485->486', '485->487', '487->488', '487->490', '492->493', '492->495', '495->496', '495->499', '499->500', '499->503', '503->504', '503->516', '516->517', '516->520', '520->521', '520->535', '521->522', '521->526', '528->529', '528->533', '535->536', '535->545', '541->542', '541->543', '545->438', '545->546', '547->548', '547->663', '552->555', '552->556', '556->557', '556->567', '558->559', '558->560', '560->561', '560->562', '562->563', '562->565', '567->568', '567->573', '569->570', '569->572', '573->574', '573->588', '576->577', '576->584', '579->580', '579->582', '588->593', '588->608', '593->594', '593->604', '604->605', '604->607', '608->609', '608->646', '609->610', '609->620', '610->611', '610->620', '621->622', '621->625', '625->626', '625->641', '626->628', '626->641', '628->629', '628->632', '641->642', '641->645', '646->648', '646->654', '648->649', '648->651', '654->655', '654->656', '656->657', '656->658', '658->659', '658->661', '666->667', '666->670', '670->671', '670->672']

import pytest
from blib2to3.pgen2.tokenize import generate_tokens, TokenError, NAME, ASYNC, INDENT, DEDENT, NEWLINE, NL, COMMENT, STRING, NUMBER, OP, ENDMARKER
from blib2to3.pgen2.grammar import Grammar
from io import StringIO

def test_generate_tokens_multiline_string():
    def readline():
        lines = [
            '"""This is a\n',
            'multiline string"""\n',
        ]
        for line in lines:
            yield line
    readline = readline().__next__

    tokens = list(generate_tokens(readline))
    assert tokens[0][0] == STRING
    assert tokens[0][1] == '"""This is a\nmultiline string"""'
    assert tokens[-1][0] == ENDMARKER

def test_generate_tokens_unterminated_multiline_string():
    def readline():
        lines = [
            '"""This is a\n',
            'multiline string\n',
        ]
        for line in lines:
            yield line
    readline = readline().__next__

    with pytest.raises(TokenError, match="EOF in multi-line string"):
        list(generate_tokens(readline))

def test_generate_tokens_indentation_error():
    def readline():
        lines = [
            'def foo():\n',
            '    pass\n',
            '  pass\n',
        ]
        for line in lines:
            yield line
    readline = readline().__next__

    with pytest.raises(IndentationError, match="unindent does not match any outer indentation level"):
        list(generate_tokens(readline))

def test_generate_tokens_async_def():
    def readline():
        lines = [
            'async def foo():\n',
            '    pass\n',
        ]
        for line in lines:
            yield line
    readline = readline().__next__

    grammar = Grammar()
    grammar.async_keywords = True

    tokens = list(generate_tokens(readline, grammar))
    assert tokens[0][0] == ASYNC  # ASYNC
    assert tokens[1][0] == NAME  # NAME (def)
    assert tokens[-1][0] == ENDMARKER

def test_generate_tokens_continued_statement():
    def readline():
        lines = [
            'a = 1 + \\\n',
            '2\n',
        ]
        for line in lines:
            yield line
    readline = readline().__next__

    tokens = list(generate_tokens(readline))
    assert tokens[0][0] == NAME  # NAME (a)
    assert tokens[1][0] == OP  # OP (=)
    assert tokens[2][0] == NUMBER  # NUMBER (1)
    assert tokens[3][0] == OP  # OP (+)
    assert tokens[4][0] == NL  # NL (\\)
    assert tokens[5][0] == NUMBER  # NUMBER (2)
    assert tokens[-1][0] == ENDMARKER
