def is_valid_pin_codes(pin_codes):
    if not pin_codes:
        return False
    elif len(set(pin_codes)) != len(pin_codes):
        return False
    for pin in pin_codes:
        if not pin.isdigit() or len(pin) != 4:
            return False
    return True

pin_codes = ['1101', '9034', '0011']
valid = is_valid_pin_codes(pin_codes)
print(valid)