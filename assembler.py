def convertBinToHex(bin):
    hex =" "
    if bin == "0000":
        hex = "0"
    elif bin == "0001":
        hex = "1"
    elif bin == "0010":
        hex = "2"
    elif bin == "0011":
        hex = "3"
    elif bin == "0100":
        hex = "4"
    elif bin == "0101":
        hex = "5"
    elif bin == "0110":
        hex = "6"
    elif bin == "0111":
        hex = "7"
    elif bin == "1000":
        hex = "8"
    elif bin == "1001":
        hex = "9"
    elif bin == "1010":
        hex = "A"
    elif bin == "1011":
        hex = "B"
    elif bin == "1100":
        hex = "C"
    elif bin == "1101":
        hex = "D"
    elif bin == "1110":
        hex = "E"
    elif bin == "1111":
        hex = "F"
    return hex

# AND   r3    r4     r5
# 0001  0011  0100   0101
# 1     3      4      5
# 1345

def checkInstruction(inst):
    convertInstruction = " "
    if inst == "add":
        convertInstruction = "0000"
    elif  inst == "nand":
        convertInstruction = "0000"
    elif  inst == "nor":
        convertInstruction = "0000"
    elif  inst == "slt":
        convertInstruction = "0000"
    elif  inst == "subi":
        convertInstruction = "0001"
    elif inst == "ori":
        convertInstruction = "0010"
    elif inst == "beq":
        convertInstruction = "0011"
    elif inst == "lw":
        convertInstruction = "0100"
    elif inst == "sw":
        convertInstruction = "0101"
    elif inst == "j":
        convertInstruction = "1000"
    else:
        convertInstruction = "Invalid instrcutions"
    return convertInstruction


def checkRegister(reg):
    
    convertReg = ""
    if  reg == "r0": 
        convertReg ="0000" 
    elif reg == "r1":
        convertReg ="0001"
    elif reg == "r2":
        convertReg ="0010"
    elif reg == "r3":
        convertReg ="0011"
    elif reg == "r4":
        convertReg ="0100"
    elif reg == "r5":
        convertReg ="0101"
    elif reg == "r6":
        convertReg ="0110"
    elif reg == "r7":
        convertReg ="0111"
    elif reg == "r8":
        convertReg ="1000"
    elif reg == "r9":
        convertReg ="1001"
    elif reg == "r10":
        convertReg ="1010"
    elif reg == "r11":
        convertReg ="1011"
    elif reg == "r12":
        convertReg ="1100"
    elif reg == "r13":
        convertReg ="1101"
    elif reg == "r14":
        convertReg ="1110"
    elif reg == "r15":
        convertReg ="1111"
    else:
        convertReg =="Invalid Register"
        
    return convertReg

def binaryToHex(binary):
    # Make sure the binary string length is a multiple of 4
    while len(binary) % 4 != 0:
        binary = '0' + binary
    
    hex_result = ""
    for i in range(0, len(binary), 4):
        hex_digit = convertBinToHex(binary[i:i+4])
        hex_result += hex_digit
    
    return hex_result.strip()

def decimalToBinary(num):

    if(num<0):
        num =  16 + num

    ext = ""
    result = ""
    
    while(num>0):
        if num % 2 == 0:
            result = "0" + result
        else:
            result = "1" + result
        #result = (num%2 == 0 ? "0" : "1") + result
        num = num//2

    for i in range(6 - len(result)):
        ext = "0" + ext

    result = ext + result


    return result

#a[1,6,7,8]
#for(i=0, i<4, i++ )
#    {
#        a[i];
#    }

#a = ['apple', 'ball', 'cat', 'dog']
#for i in a:
#    i

readf = open("inputs","r")
writef = open("outputs","w")
writef.write("v2.0 raw\n")

# A quick brown fox jumped over a lazy dog

#print(f.readline())
for i in readf:
    splitted = i.split()
#the assembly is written like op rd rs rt func
#desired outcome should be op rs rt rd func
    
    if(splitted[0] == "add"):
        conv_inst = checkInstruction(splitted[0])
        conv_rd = checkRegister(splitted[1])
        conv_rs = checkRegister(splitted[2])
        conv_rt = checkRegister(splitted[3])

        binary = conv_inst + conv_rs + conv_rt + conv_rd + "00"
        #print(out)
        #writef.write(out+"\n")
        
        hex_output = binaryToHex(binary)
        print(f"Binary: {binary}, Hex: {hex_output}")
        writef.write(hex_output+"\n")

    elif(splitted[0] == "nand"):
        conv_inst = convertBinToHex(checkInstruction(splitted[0]))
        conv_rd = checkRegister(splitted[1])
        conv_rs = checkRegister(splitted[2])
        conv_rt = checkRegister(splitted[3])

        binary = conv_inst + conv_rs + conv_rt + conv_rd + "01"
        hex_output = binaryToHex(binary)
        print(f"Binary: {binary}, Hex: {hex_output}")
        writef.write(hex_output+"\n")

    elif(splitted[0] == "nor"):
        conv_inst = checkInstruction(splitted[0])
        conv_rd = checkRegister(splitted[1])
        conv_rs = checkRegister(splitted[2])
        conv_rt = checkRegister(splitted[3])

        binary = conv_inst + conv_rs + conv_rt + conv_rd + "10"
        hex_output = binaryToHex(binary)
        print(f"Binary: {binary}, Hex: {hex_output}")
        writef.write(hex_output+"\n")

    elif(splitted[0] == "slt"):
        conv_inst = checkInstruction(splitted[0])
        conv_rd = checkRegister(splitted[1])
        conv_rs = checkRegister(splitted[2])
        conv_rt = checkRegister(splitted[3])

        binary = conv_inst + conv_rs + conv_rt + conv_rd + "11"
        hex_output = binaryToHex(binary)
        print(f"Binary: {binary}, Hex: {hex_output}")
        writef.write(hex_output+"\n")

    elif(splitted[0] == "lw" or splitted[0] == "sw" or splitted[0] == "beq" or splitted[0] == "subi" or splitted[0] == "ori"):
        conv_inst = checkInstruction(splitted[0])
        conv_rs = checkRegister(splitted[1])
        conv_rt = checkRegister(splitted[2])
        conv_im = decimalToBinary(int(splitted[3])) #decimal converted to 6bits

        binary = conv_inst + conv_rs + conv_rt + conv_im  #rt will behave as rd when regdst is 1
        hex_output = binaryToHex(binary)
        print(f"Binary: {binary}, Hex: {hex_output}")
        writef.write(hex_output+"\n") 
     
    elif(splitted[0] == "j"):
        conv_inst = convertBinToHex(checkInstruction(splitted[0]))
        #conv_target = convertBinToHex(decimalToBinary(int(splitted[1])))
        hexval = hex(int(splitted[1]))
        exF2 = hexval[2:]
        ext = ""
        for i in range(4 - len(exF2)):
            ext = "0" + ext

        conv_target = ext + exF2
        conv_target = conv_target[-4:]  # Ensure it's no longer than 4 hex digits

        out = conv_inst + conv_target
        print(out)
        writef.write(out+"\n") 


    
