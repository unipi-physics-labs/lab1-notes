import struct

file_path = 'data/byte.dat'

with open(file_path, encoding='windows-1252') as input_file:
    print(input_file.read())

with open(file_path, 'rb') as input_file:
    data = input_file.read()
    print(struct.unpack('B', data)[0])
    print(struct.unpack('b', data)[0])
