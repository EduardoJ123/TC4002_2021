def decTohex(dec):
    hexa = ''
    if(dec == 10): hexa      = 'A'
    elif(dec == 11): hexa    = 'B'
    elif(dec == 12): hexa    = 'C'
    elif(dec == 13): hexa    = 'D'
    elif(dec == 14): hexa    = 'E'
    elif(dec == 15): hexa    = 'F'
    return hexa

binary_num = ''
hex_num = ''
error_flag = 0
try: input_num = int(input("Introduce a decimal number: "))
except: 
    print("Introduced value not a number")
    error_flag = 1
    
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
            if(binary_copy == 0): break
        while True:
            hex_copy = int(input_num) % 16
            if(hex_copy > 9): hex_copy = decTohex(hex_copy)
            hex_num = str(hex_copy) + hex_num
            #hex_num = str(decTohex(int(input_num) % 16)) + hex_num
            input_num = int(input_num) / 16
            if(input_num == 0): break
    print("Binary number: ", binary_num)
    print("Hex number: ", hex_num)