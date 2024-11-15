import pickle

d = {"a":100}

with open("data.pickle","wb") as f:
    pickle.dump(d,f)

with open("data.pickle", "rb") as f:
    d2 = pickle.load(f)

    # Note:
    # we can save obj by pickle but we can not by json.