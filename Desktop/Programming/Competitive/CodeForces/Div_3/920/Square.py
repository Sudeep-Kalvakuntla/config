i = int(input())
coords = []

for j in range(0 , i):
    for k in range(0 , 4):
        s = input().split()
        coords.append([int(s[0]) , int(s[-1])])

    if coords[0][0] == coords[1][0]:
        l = coords[0][1] - coords[1][1]
    if coords[0][0] == coords[2][0]:
        l = coords[0][1] - coords[2][1]
    if coords[0][0] == coords[3][0]:
        l = coords[0][1] - coords[3][1]

    if coords[1][0] == coords[2][0]:
        l = coords[1][1] - coords[2][1]
    if coords[1][0] == coords[3][0]:
        l = coords[1][1] - coords[2][1]

    if coords[2][0] == coords[3][0]:
        l = coords[2][1] - coords[3][1]

    print(l**2)
