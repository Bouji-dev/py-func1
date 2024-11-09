def my_generator():
    x = 1
    print("first time :")
    yield x

    x += 1
    print("second time :")
    yield x

    x *= 10
    print("third time :")
    yield x