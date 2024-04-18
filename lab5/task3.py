def lazy_file_read():
    f = open("C:\\users\\user\\Desktop\\lab_5.txt", "r")
    for line in f:
        yield line
    f.close()


def line_filter(filter, num):
    for _ in range(num):
        line = next(file_reader)
        line.


file_reader = lazy_file_read()

for _ in range(10):
    print(next(file_reader))
