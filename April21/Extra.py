l = [10,20,10,20,40,50]

dup_01 = []
[dup_01.append(x) for x in l if x not in dup_01]
print(f"{dup_01}")