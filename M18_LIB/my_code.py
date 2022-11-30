
def testPalindrome(f):
    result = f("Sa i p Pua,?!kauPpias")
    
    if isinstance(result, bool):
        if result == True:
            return True
        else:
            return False
    else:
        return False
        


def ispal(s):
    s1 = s.strip()
    s2 = s1.replace(",","").replace(".","").replace("!","").replace("?","").replace(" ","")
    sana = s2.lower()
    reverse_sana = sana[::-1]
    
    if reverse_sana == sana:
        return True
    else:
        return False
     
if __name__=='__main__':
    rc=testPalindrome(ispal)
    print(ispal("Saippua, . kauppiaS"))
    print(rc)
