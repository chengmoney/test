def triangles(n):
    L = [1]
    S = []
    for _ in range(n):
        yield L
        L = [1] + S + [1]
        S = []
        for i in range(len(L)-1):
            S.append(L[i] + L[i+1])


for i in triangles(4):
    print(i)








