with open("data03.csv") as f:
    l = []
    for i in f:
        l.append(i)
    print(l)
    heders = l[0][:-1].split("\t")
    print(heders)
    d = {}
    counter = 0
    for header in heders:
        d[header]= []
        for i in l[1:]:
            d[header].append(i[:-1].split("\t")[counter])
        counter += 1





    print(d)


    """
    """