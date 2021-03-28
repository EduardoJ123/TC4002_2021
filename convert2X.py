import unittest
import pycodestyle


def decTohex(dec):
    hexa = ''
    if(dec == 10):
        hexa = 'A'
    elif(dec == 11):
        hexa = 'B'
    elif(dec == 12):
        hexa = 'C'
    elif(dec == 13):
        hexa = 'D'
    elif(dec == 14):
        hexa = 'E'
    elif(dec == 15):
        hexa = 'F'
    return hexa


def convert2X():
    binary_num = ''
    hex_num = ''
    error_flag = 0
    try:
        input_num = int(input("Introduce a decimal number: "))
    except:
        print("Introduced value not a number")
        error_flag = 1
        return 1

    if(not error_flag):
        if(input_num == 0):
            binary_num = 0
            hex_num = 0
        elif(input_num == 1):
            binary_num = 1
            hex_num = 1
        else:
            binary_copy = input_num
            while True:
                binary_num = str(int(binary_copy) % 2) + binary_num
                binary_copy = int(binary_copy) / 2
                if(binary_copy == 0):
                    break
            while True:
                hex_copy = int(input_num) % 16
                if(hex_copy > 9):
                    hex_copy = decTohex(hex_copy)
                hex_num = str(hex_copy) + hex_num
                input_num = int(input_num) / 16
                if(input_num == 0):
                    break
        print("Binary number: ", binary_num)
        print("Hex number: ", hex_num)
    return 0


class convert2XTest(unittest.TestCase):
    def test_negative_float(self):
        self.assertAlmostEqual(convert2X(), 1)

    def test_functional(self):
        self.assertAlmostEqual(convert2X(), 0)

    def test_functional_high_value(self):
        self.assertAlmostEqual(convert2X(), 0)

    def test_functional_zero(self):
        self.assertAlmostEqual(convert2X(), 0)

    def test_functional_one(self):
        self.assertAlmostEqual(convert2X(), 0)

    def test_functional_F(self):
        self.assertAlmostEqual(convert2X(), 0)


if __name__ == '__main__':
    unittest.main()
