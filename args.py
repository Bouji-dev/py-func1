def average(*args):
    for i in args:
        if not isinstance(i,(int,float)):
            raise "Type Error"
    return sum(args)/len(args)


