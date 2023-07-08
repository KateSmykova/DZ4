def hash_dicts(**kwargs):
    data = dict()
    for i, item in kwargs.items():
        if isinstance(item, (list, dict, set, bytearray)):
            item = str(item)
        data[item] = i
    return data


if __name__ == '__main__':
    print(hash_dicts(first="one", second=2, third=3, fourth="four", fifth=[2, 3]))