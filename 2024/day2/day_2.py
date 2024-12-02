# Part 1
f = open("input.txt", "r")
count = 0

def validline(l, asc):
    for i in range(1, len(l)):
        if asc:
            if (l[i-1] > l[i]) or (l[i] - l[i-1] > 3 or l[i] - l[i-1] < 1):
                return False
        if not asc:
            if (l[i-1] < l[i]) or (l[i-1] - l[i] > 3 or l[i-1] - l[i] < 1):
                return False
    return True

for line in f.readlines():
    la = line.strip().split(" ")
    la = list(map(int, la))
    asc = False
    if la[0] < la[1]:
        asc = True
    if validline(la, asc):
        count+=1
        
print(count)

'''
Pretty basic solution, seems the obvious way to do it.
'''


# Part 2

count=0
f.seek(0)
for line in f.readlines():
    la = line.strip().split(" ")
    la = list(map(int, la))
    asc = False
    if la[0] < la[1]:
        asc = True
    if validline(la, asc):
        count+=1
    else:
        for i in range(len(la)):
            lb = la[:]
            lb.pop(i)
            asc = False
            if lb[0] < lb[1]:
                asc = True
            if validline(lb, asc):
                count+=1
                break
            

print(count)

'''
Was trying to think of a clever way of only testing suspected error indexes.
Couldn't think of a neat solution to apply to the later indexes that would also easily transfer to the first ones.
That'd probably be the way to go about it for much longer lines, as you could make a good guess as to where the error was.
As it stands now, it tests them all until a solution is found or it runs out.
'''
