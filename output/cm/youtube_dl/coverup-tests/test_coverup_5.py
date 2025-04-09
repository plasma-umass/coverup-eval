# file youtube_dl/extractor/nrk.py:287-336
# lines [287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 305, 306, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 336]
# branches []

import pytest
from youtube_dl.extractor.nrk import NRKTVIE


@pytest.fixture
def nrktvie():
    return NRKTVIE()


def test_nrktvie_id_extraction(nrktvie):
    test_url = 'https://tv.nrk.no/program/MDDP12000117'
    expected_id = 'MDDP12000117'
    extracted_id = nrktvie._match_id(test_url)
    assert extracted_id == expected_id


def test_nrktvie_invalid_url(nrktvie):
    invalid_url = 'https://invalid.url/program/INVALID1234'
    with pytest.raises(AssertionError):
        nrktvie._match_id(invalid_url)
