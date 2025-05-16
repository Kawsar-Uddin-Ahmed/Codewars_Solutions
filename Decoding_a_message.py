def decode(message):
    a = []
    for i in message:
        if (i.islower()):
            c = chr(219 - ord(i))
            a.append(c)
        elif(i.isupper()):
            d = chr(155 - ord(i))
            a.append(d)
        else:
            a.append(i)
    y = ''.join(a)
    return y
a = decode("qzezxirkg rh z srts ovevo wbmznrx fmgbkvw zmw rmgvikivgvw kiltiznnrmt ozmtfztv rg szh yvvm hgzmwziwravw rm gsv vxnzxirkg ozmtfztv hkvxrurxzgrlm zolmthrwv sgno zmw xhh rg rh lmv lu gsv gsivv vhhvmgrzo gvxsmloltrvh lu dliow drwv dvy xlmgvmg kilwfxgrlm gsv nzqlirgb lu dvyhrgvh vnkolb rg zmw rg rh hfkkligvw yb zoo nlwvim dvy yildhvih drgslfg koftrmh")
print(a)