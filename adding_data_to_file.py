
"""
This scripts gets 'adding data' parameter and add its value to the end of file.

"""


def add_data(adding_data):
    file_name = "C:\\tmp\\pic.jpg"
    file = open(file_name, 'ab')
    new_byte = [adding_data]
    byte_array = bytearray(new_byte)
    file.write(byte_array)
    file.close()


def main():
    add_data(adding_data=127)


if __name__ == '__main__':
    main()



