plainText = " Hello "
plainText = plainText.upper()
plainText = plainText.replace(" ","")
pt = [ ]
cip = [ ]
ct = " "
for i in range(0,len(plainText)-1):
    for j in range(0,len(plainText)-1):
        pt[i][j] = input()

    ct = ct + plainText[i]
