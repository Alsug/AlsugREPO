def estDans(L,e):
    for i in range(len(L)):
        if L[i]==e:
            return True
    return False

def myst(L1,L2):
    t1=len(L1)
    t2=len(L2)
    if t1<t2:
        return False
    for elt in L2:
        if estDans(L1, elt):
            continue
        else:
            return False

    return True

print(myst([12,45,16,28,4,28,7],[4,11,7]))