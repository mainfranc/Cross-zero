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


