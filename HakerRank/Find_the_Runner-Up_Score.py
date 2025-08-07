if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    a = list(arr)
    a.sort()
    m= max(a)
    print([i for i in a if i != m][-1])
