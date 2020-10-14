def filter_string(string):
    s = ''
    for i in string:
        if '0' <= i <= '9':
            s += i
    return int(s)
print(filter_string('a1s2d3'))