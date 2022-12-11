
from random import randint


def ordenate_list(num_list: list) -> list:
    new_list = sorted(num_list)
    return new_list


def add_one(num_list: list) -> list:
    new_list = ordenate_list(num_list)

    sample_rate = new_list[1] - new_list[0]
    new_list.append(new_list[-1] + sample_rate)

    return new_list

def remove_one(num_list: list) -> list:
    new_list = ordenate_list(num_list)

    new_list.pop()

    return new_list


if __name__ == '__main__':
    my_list = [randint(1,10) for i in range(randint(2,10))]

    print("My List Original: {}".format(my_list))

    my_list_one = add_one(my_list)

    print("My List Addedv  : {}".format(my_list_one))
