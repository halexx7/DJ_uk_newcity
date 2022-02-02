def check_value_len(_min, _max, value):
    _value = str(value)
    if len(_value) < _min:
        raise ValueError(f"minimum number of characters {_min}")
    elif len(_value) > _max:
        raise ValueError(f"maximum number of characters {_max}")
    else:
        return True


def check_value_is_alpha(value):
    checked_str = str(value).replace("-", "")
    if checked_str.isalpha():
        return True
    else:
        raise ValueError('special characters are not allowed except for "-"')


def check_value_is_digit(value):
    if value.isdigit():
        return True
    else:
        raise ValueError("the value must be numeric")
