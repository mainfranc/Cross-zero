# files

def file_create(f_name):
    with open(f_name, "w") as f:
        f.write(input())


    with open(f_name, "rb") as f:
        for line_ in f:
            print(line_)


file_create('test.txt')

