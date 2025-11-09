if __name__ == '__main__':
    li = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        li.append([name,score])                     #create the 2d list
        
    sec = list(sorted(set(i[1] for i in li)))[1]    # get the second largest score from it
    
    # getting the second largest names
    li2=[]
    for i in li:
        if i[1] == sec:
            li2.append(i[0])
    
    l = sorted(li2) 
    #output 
    for o in l:print(o)

s = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

sec_low = list(sorted(list(set(i[1] for i in s))))[1]

li = []
for i in s:
    if i[1] == sec_low:
        li.append(i[0])
l = sorted(li)
print(l)