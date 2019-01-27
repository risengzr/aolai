from base.read_yaml import read_data


def read_yaml_file():
    li = []
    data = read_data("login.yaml")
    for i in data.keys():
        a = []
        for j in data.get(i).values():
            a.append(j)
        b = tuple(a)
        li.append(b)
    print(li)

read_yaml_file()