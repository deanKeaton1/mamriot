"""
xor data - this script get a 'frequent value' and 'xor_with_value'
The script takes the 'xor_with_value' and performs XOR operation with the data that appeared in the
frequency value position - according to the value 'frequent value'
"""


def xor_data(frequent_value, xor_with_value):
    frequent = frequent_value

    """original file"""
    file_name = "C:\\tmp\\pic.jpg"

    """new file"""
    new_file_name = "C:\\tmp\\new_pic.jpg"

    with open(file_name, "rb") as f:
        with open(new_file_name, 'wb') as new_file:
            byte = f.read(1)
            while byte:
                # Get the current position in the file
                seek_position = f.tell()
                # Check if the current position is fit to the frequency.
                if seek_position % frequent == 0:
                    # XOR action can be performed on int type
                    int_value__from_byte = int.from_bytes(byte, 'big')
                    # preform XOR action
                    output_xored_value = int_value__from_byte ^ xor_with_value
                    print('seek_position: ', seek_position)
                    print('org value:', byte)
                    print('int from byte', int_value__from_byte)
                    print('xored value: ', output_xored_value)
                    new_file.write(int.to_bytes(output_xored_value, 1, 'big'))

                else:
                    new_file.write(byte)
                # Read the next byte
                byte = f.read(1)
    new_file.close()


if __name__ == '__main__':
    xor_data(frequent_value=3, xor_with_value=11)
