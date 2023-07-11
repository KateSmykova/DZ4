abs_path = r'C:\User\Desktop\Python\dz_5.txt'


def split_path(abs_path: str) -> tuple():
    list_abs_path = abs_path.split('\\')
    list_last_elem = list_abs_path[-1].split('.')
    path = '\\'.join(list_abs_path[0:-1])
    name = list_last_elem[0]
    expansion = list_last_elem[1]
    return path, name, expansion


if __name__ == '__main__':
    print(split_path(abs_path))