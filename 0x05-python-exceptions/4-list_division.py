#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):

    """
    INPUT: my_list_1, my_list_2, list_length
    OUTPUT: list = division of the 2 lists with
        length = Min(length of 1st list, len of 2nd list, list_length)
    """
    result = []
    try:
        for i in range(list_length):
            try:
                result.append(my_list_1[i] / my_list_2[i])
            except (TypeError, ValueError):
                print("wrong type")
                result.append(0)
                continue
            except ZeroDivisionError:
                print("division by 0")
                result.append(0)
                continue
    except IndexError:
        print("out of range")
        result.append(0)
    finally:
        return result
