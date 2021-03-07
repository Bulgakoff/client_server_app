from utest_pj.new1 import  f_obj, s_calc, s_side, s_circle, s_full


def test_f_obj():
    assert f_obj(0) == 200


def test_f_obj2():
    assert f_obj(200) == 400


def test_s_calc():
    assert s_calc(50, 30) == (25120.0,9420.0)


def test_s_side():
    assert s_side(5, 6) == 188.4


def test_s_circle():
    assert s_circle(5) == 78.5


def test_s_full():
    assert s_full(5, 6) == 345.4
