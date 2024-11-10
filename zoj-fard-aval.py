from avalfunc import adad_aval

def zoj_fard_aval(l:list)-> dict:
    
    if not isinstance(l,list):
        raise TypeError("l should be a list")

    result = {"zoj":[],"fard":[],"aval":[]}

    for i in l:
        if i%2==0:
            result["zoj"].append(i)
        else:
            result["fard"].append(i)
        
        if adad_aval(i):
            result["aval"].append(i)

    return result



print(zoj_fard_aval([2,1,5,6,77,34,23,11,9]))