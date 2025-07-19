file_path = 'data/iotest.txt'

with open(file_path) as input_file:
    for ch in input_file.read():
        print(ch, ord(ch), bin(ord(ch)))
