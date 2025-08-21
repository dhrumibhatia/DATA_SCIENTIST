def count_substring(string, sub_string):
    l = len(sub_string)
    sl = len(string)
    c = 0
    if l==sl and sub_string in string:
        return 1
    
    for i in range(l,sl,l):
        print(i,string[i],string[i-l:i])
    #     if string[i-l:i] == sub_string:
    #         c+=1
    # return c
print(count_substring("ABCDCDC", "CDC"))    