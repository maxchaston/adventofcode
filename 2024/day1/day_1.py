# Part 1
f = open("input.txt", "r")
l1 = []
l2 = []
distances = []
for p in f.readlines():
    x = p.strip().split(" ")
    l1.append(int(x[0]))
    l2.append(int(x[-1]))
l1.sort()
l2.sort()

for i in range(len(l1)):
    distances.append(abs(l1[i]-l2[i]))
print(sum(distances))

# Part 2
similarity = []
for i in l1:
    similarity.append(i * l2.count(i))
print(sum(similarity))
