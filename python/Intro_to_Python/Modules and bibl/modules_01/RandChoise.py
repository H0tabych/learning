import random


def rand_elem_list(orig_list=None):
    if orig_list is None:
        return None
    return random.choice(orig_list)


if __name__ == '__main__':
    print(rand_elem_list())
