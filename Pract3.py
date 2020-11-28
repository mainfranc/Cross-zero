import json


# files

def file_create(f_name):
    with open(f_name, "w") as f:
        f.write(input())


    with open(f_name, "rb") as f:
        for line_ in f:
            print(line_)


#file_create('test.txt')


# JSON
def look_at_json(in_struct):
    val = json.dumps(in_struct)
    print(val)
    with open('test.txt', "w") as f:
        f.write(val)


comp_struct = {i: [str(k) for k in range(5)] for i in range(7)}
look_at_json(comp_struct)


# Pickling
def pickling(in_struct):
    p_struct = pickle.dumps(in_struct)
    print(p_struct)
    with open('test.txt', "wb") as f:
        f.write(p_struct)
        print(f)

    return tuple(pickle.loads(p_struct))

print(pickling(comp_struct))


# OS
def load_enviromental():
    e_dict = os.environ
    if not e_dict.get('PY_DEBUG', False):
        for i in e_dict:
            print(i, e_dict[i])


load_enviromental()
