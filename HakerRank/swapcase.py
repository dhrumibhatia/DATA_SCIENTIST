def swap_case(s):
    res = ''
    for i in s:
        if i == i.lower():
            res+=i.upper()
        elif i == i.upper():
            res+=i.lower()
    return res

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)