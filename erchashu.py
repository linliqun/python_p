num=int(input())
tree={'0':[1,0]}
for i in range(num-1):
    parent,children=input().split()
    if parent in tree and tree[parent][1]<2:
        tree[children]=[tree[parent][0]+1,0]
        tree[parent][1]+=1
depth=[x[0] for x in tree.values()]
print(max(depth)) 