# test_tachycardia.py
import pytest


def test_is_tachycardic_normal():
    from tachycardia import is_tachycardic
    answer = is_tachycardic("tachycardic")
    expected = True
    assert answer == expected


def test_is_tachycardic_upper():
    from tachycardia import is_tachycardic
    answer = is_tachycardic("TACHYCARDIC")
    expected = True
    assert answer == expected


def test_is_tachycardic_mixed():
    from tachycardia import is_tachycardic
    answer = is_tachycardic("TAcHyCARDic")
    expected = True
    assert answer == expected


def test_is_tachycardic_punctuation():
    from tachycardia import is_tachycardic
    answer = is_tachycardic("TA.cHyCARDic?!.")
    expected = True
    assert answer == expected


def test_is_tachycardic_whitespace():
    from tachycardia import is_tachycardic
    answer = is_tachycardic(" TA.cHyCARDic?!. ")
    expected = True
    assert answer == expected


def test_is_tachycardic_not():
    from tachycardia import is_tachycardic
    answer = is_tachycardic(" cardic?!. ")
    expected = False
    assert answer == expected


@pytest.mark.parametrize("a, expected", [
    ("TAChyycardic", False),
    ("4", False),
    ("?!?!!!!!!!!!!tachycardic         ", True),
    (" tac?hycarDIC .", True),
])
def test_add_parametrize(a, expected):
    from tachycardia import is_tachycardic
    answer = is_tachycardic(a)
    assert answer == expected
