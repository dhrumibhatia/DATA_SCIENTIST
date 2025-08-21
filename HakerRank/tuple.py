if __name__ == '__main__':
    n = int(input())                     # read number of elements
    integer_list = map(int, input().split())  # read integers
    t = tuple(integer_list)              # convert list to tuple
    print(hash(t))                       # print hash value
