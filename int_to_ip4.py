Complete the function that takes an unsigned 32 bit number and returns a string representation of its IPv4 address.


def int32_to_ip(int32):
    if int32 == [] or int32 == "" or int32 == '' or int32 == 0:
        return '0.0.0.0'
    else:
        conv = ""
        wholeN = []
        newN = 0
        n = []
        counter = 0
        while int32 >= 1: # divide 2 untij int 32 is 0 and modulo
            counter += 1
            newN = int32%2
            if newN == 0:
                n.insert(0, 0)
            else: n.insert(0, 1)
            if counter == 8 or counter == 16 or counter == 24 or counter == 32: # put data into table 2d
                wholeN.append(n)
                n = []
            int32 = int32//2
        print(counter)
        if counter < 32: # if number in system of 2 are less than 32
                for i in range(counter+1, 33):
                    n.insert(0, 0)
                    counter +=1
                    if counter == 8 or counter == 16 or counter == 24 or counter == 32:
                        wholeN.append(n)
                        n = []
    
        wholeN=wholeN[::-1]
    
        print (wholeN)
        licz = 0
        strLicz = ""
    
        for i in wholeN:
            licz = 0
            c=8
            for j in i:
                c -= 1
                if j == 1:
                    licz = licz + pow(2, c)
    
            strLicz = strLicz + str(licz) + "."
    
        return (strLicz[:-1])
