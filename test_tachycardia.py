# test_tachycardia.py


def test_is_tachycardic_normal():
    from tachycardia import is_tachycardic
    answer = is_tachycardic("tachycardic")
    expected = True
    assert answer == expected
