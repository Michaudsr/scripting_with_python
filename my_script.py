
# open a file
steven_file = open('steven.txt', 'a')

numbers = [1,2,3]
for i in range(len(numbers)):
    num = numbers[i]
    steven_file.write("{}\n".format(num))

# write to the file
# steven_file.write('\nHello\n')
steven_file.close()

# read a file
# print(steven_file.read())

# If file is not found, one will be created for you
adam_file = open('adam.txt', 'w')
adam_file.write('Adam')
adam_file.close()


new_file = open('new_file.txt')
file_items = new_file.readline()\

for i in range(len(file_items)):
    each_item = file_items[i]
    print('Before: {}'.format(each_item))
    print(each_item[0:-1])
    file_items[i] = each_item[0:-1]
    print(file_items)

print(file_items)

new_file.close()