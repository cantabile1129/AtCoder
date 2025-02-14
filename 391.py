D = [["E", "W"], ["N", "S"], ["NE", "SW"], ["NW", "SE"]]
C = input()
for i in range(4):
    if (C == D[i][0]):
        print(D[i][1])
    elif (C == D[i][1]):
        print(D[i][0])
        
