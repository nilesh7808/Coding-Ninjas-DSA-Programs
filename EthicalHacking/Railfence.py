plainText = " Hello "
plainText = plainText.upper()
plainText = plainText.replace(" ","")
ct = " "
for i in range(0,len(plainText),2):
    ct = ct + plainText[i]
for i in range(1,len(plainText)-1,2):
    ct = ct + plainText[i]
print(ct)