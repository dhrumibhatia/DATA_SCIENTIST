def split_and_join(line):
    # write your code here
    result = '-'.join(line.split())
    return result

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

# another solution
def fun2(st):
    result = st.replace(' ', '-')
    return result

def fun3(st):
    sp = st.split(" ")
    jo = '-'.join(sp)
    res = jo
    return res
