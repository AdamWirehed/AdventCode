# Intcode program from "Advent of Code: Day 2 and Day 5"


def opcode(act, ix, arglist):

    im = [0, 0]  # Since we have position mode by default

    if act > 9:
        opc = int(str(act)[-2:])  # Gets the Opcode
        k = 0
        for nr in reversed(str(act)[0:-2]):       # Gets the immediate mode
            im[k] = int(nr)
            k += 1
    else:
        opc = act
    # Getting the values depending on the instruction
    if (opc == 3) or (opc == 4):
        i1 = arglist[ix + 1]
    else:
        # Choosing the right values depending on the immediate mode
        if int(im[0]) == 0:
            v1 = arglist[arglist[ix + 1]]
        else:
            v1 = arglist[ix + 1]

        if int(im[1]) == 0:
            v2 = arglist[arglist[ix + 2]]
        else:
            v2 = arglist[ix + 2]

        i3 = arglist[ix + 3]

    # The different operations
    def first():
        arglist[i3] = v1 + v2
        k = 4
        return k

    def second():
        arglist[i3] = v1 * v2
        k = 4
        return k

    def third():
        iv = int(input("Enter value : "))
        arglist[i1] = iv
        k = 2
        return k

    def fourth():
        if im[0] == 0:
            print(testList[i1])     # Since "third" writes to the index i1
        else:                       # I did the if-statement for immediate mode here instead
            print(i1)
        k = 2
        return k

    def fith():
        if v1 != 0:
            k = v2 - ix   # Since we add "k" (jump) to the pointer
        else:
            k = 3                       # Three digits in instruction, (operation, param1, param 2)
        return k

    def sixth():
        if v1 == 0:
            k = v2 - ix  # Since we add "k" (jump) to the pointer
        else:
            k = 3
        return k

    def seventh():
        if v1 < v2:
            testList[i3] = 1
        else:
            testList[i3] = 0
        k = 4
        return k

    def eigth():
        if v1 == v2:
            testList[i3] = 1
        else:
            testList[i3] = 0
        k = 4
        return k

    def default():
        print("Unvalid opcode")
        k = 0
        return k

    dictmap = {
        1: first,
        2: second,
        3: third,
        4: fourth,
        5: fith,
        6: sixth,
        7: seventh,
        8: eigth,
    }

    lenjump = dictmap.get(opc, default)()
    return lenjump


# ------------------- main function ------------------------

# Change input list here #
testList = [3,225,1,225,6,6,1100,1,238,225,104,0,1102,46,47,225,2,122,130,224,101,-1998,224,224,4,224,1002,223,8,223,1001,224,6,224,1,224,223,223,1102,61,51,225,102,32,92,224,101,-800,224,224,4,224,1002,223,8,223,1001,224,1,224,1,223,224,223,1101,61,64,225,1001,118,25,224,101,-106,224,224,4,224,1002,223,8,223,101,1,224,224,1,224,223,223,1102,33,25,225,1102,73,67,224,101,-4891,224,224,4,224,1002,223,8,223,1001,224,4,224,1,224,223,223,1101,14,81,225,1102,17,74,225,1102,52,67,225,1101,94,27,225,101,71,39,224,101,-132,224,224,4,224,1002,223,8,223,101,5,224,224,1,224,223,223,1002,14,38,224,101,-1786,224,224,4,224,102,8,223,223,1001,224,2,224,1,223,224,223,1,65,126,224,1001,224,-128,224,4,224,1002,223,8,223,101,6,224,224,1,224,223,223,1101,81,40,224,1001,224,-121,224,4,224,102,8,223,223,101,4,224,224,1,223,224,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,1008,677,226,224,1002,223,2,223,1005,224,329,1001,223,1,223,107,677,677,224,102,2,223,223,1005,224,344,101,1,223,223,1107,677,677,224,102,2,223,223,1005,224,359,1001,223,1,223,1108,226,226,224,1002,223,2,223,1006,224,374,101,1,223,223,107,226,226,224,1002,223,2,223,1005,224,389,1001,223,1,223,108,226,226,224,1002,223,2,223,1005,224,404,1001,223,1,223,1008,677,677,224,1002,223,2,223,1006,224,419,1001,223,1,223,1107,677,226,224,102,2,223,223,1005,224,434,1001,223,1,223,108,226,677,224,102,2,223,223,1006,224,449,1001,223,1,223,8,677,226,224,102,2,223,223,1006,224,464,1001,223,1,223,1007,677,226,224,1002,223,2,223,1006,224,479,1001,223,1,223,1007,677,677,224,1002,223,2,223,1005,224,494,1001,223,1,223,1107,226,677,224,1002,223,2,223,1006,224,509,101,1,223,223,1108,226,677,224,102,2,223,223,1005,224,524,1001,223,1,223,7,226,226,224,102,2,223,223,1005,224,539,1001,223,1,223,8,677,677,224,1002,223,2,223,1005,224,554,101,1,223,223,107,677,226,224,102,2,223,223,1006,224,569,1001,223,1,223,7,226,677,224,1002,223,2,223,1005,224,584,1001,223,1,223,1008,226,226,224,1002,223,2,223,1006,224,599,101,1,223,223,1108,677,226,224,102,2,223,223,1006,224,614,101,1,223,223,7,677,226,224,102,2,223,223,1005,224,629,1001,223,1,223,8,226,677,224,1002,223,2,223,1006,224,644,101,1,223,223,1007,226,226,224,102,2,223,223,1005,224,659,101,1,223,223,108,677,677,224,1002,223,2,223,1006,224,674,1001,223,1,223,4,223,99,226]

# Index counter
i = 0

while i < len(testList):
    inst = testList[i]

    if inst == 99:
        break
    jump = opcode(inst, i, testList)
    i += jump

