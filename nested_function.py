def outer_func():
    def inner_func():
        print("hi nested")
    inner_func()

outer_func()