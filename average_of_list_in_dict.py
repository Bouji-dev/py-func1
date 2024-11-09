

def my_func () -> dict:

    user_dict = {}
    finall_dict = {}
    dict_length = int(input("Enter dict length : "))
    list_length = int(input("Enter list length : "))
    key_list = []
    value_list = []
    average_list = []
    sum_value = 0
    average_value = 0

    for i in range(dict_length):

        value = []
        key = input("Enter key :")
        for j in range (list_length):

            print ( "Enter element ", j, "for value : ")
            value.append(int(input()))

        user_dict.update({key:value})
        key_list = list(user_dict.keys())
        value_list = list(user_dict.values())

    for i in range(dict_length):
        for j in range(list_length):

            sum_value = sum_value + value_list[i][j]
            average_value = int(sum_value/list_length)

        average_list.append(average_value)
        finall_dict.update({key_list[i] + "_average": average_list[i]})

        sum_value = 0
        average_value = 0

    print(finall_dict)
    return finall_dict



my_func()





