file_object = open('test.txt', 'r')

for lines in file_object:
    each_line = lines.split('.')
    try:
        print(each_line[0])
    except:
        print("Specified index is invalid")
