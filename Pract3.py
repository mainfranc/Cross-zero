# 1

def file_create(f_name, f_text):
    f = open(f_name, "w")
    f.write(f_text)
    f.close()

    f = open(f_name, "rb")
    for line_ in f:
        print(line_)
    f.close()


file_create('test.txt', 'какой-то текст' + '/n' + 'rgrgrgr')
