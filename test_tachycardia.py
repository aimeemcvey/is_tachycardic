# test_tachycardia.py


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
