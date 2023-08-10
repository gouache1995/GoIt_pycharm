def format_string(string, length):
    if len(string) < length:
        ryad = (length - len(string)) // 2
        return (' '*ryad + string)
    else:
        return string

format_string(string = 'abaa', length = 15)