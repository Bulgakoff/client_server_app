def ext_func(var_1):
    def int_func(var_2):
        return var_1 + var_2

    return int_func


f_obj = ext_func(200)  # f_obj - функция
print(f_obj(300))


def s_side(r_val, h_val):
    return 2 * 3.14 * r_val * h_val


def s_circle(r_val):
    return 3.14 * r_val ** 2


def s_full(r_val, h_val):
    return s_side(r_val, h_val) + 2 * s_circle(r_val)


def s_calc(r_val, h_val):
    # площадь боковой поверхности цилиндра:
    s_side(r_val, h_val)
    # площадь одного основания цилиндра:
    s_circle(r_val)
    # полная площадь цилиндра:
    return s_full(r_val, h_val), s_side(r_val, h_val)


qwe, asd = s_calc(56, 6)
print(f"Площадь боковой пов-ти - {round(qwe)}; Полная площадь - {round(asd)}")
