# Tobby Lie
# CSCI 4742
# Lab1
# Last modified: 9/10/19 @ 6:35PM

import ipaddress

def parseIP(cidrNotation):
    '''Parse IP given cidr notation as input'''
    # split up given cidr address (cidrNotation) we split it up
    # by the '/' at the very end before the right most number
    # for example 192.168.100.0/18 we split it up wehre the '/' appears
    addressSplit = cidrNotation.split('/')
    # the ip address is what is to the left of the '/'
    # for the above example ip is 192.168.100.0
    ip = addressSplit[0]
    # cidrSubnet now holds the value to the left of '/'
    # which in the example above is 18
    # this number specifies that 18 bits are the network
    # part of the address leaving the 32-18=14 bits for specific
    # host addresses
    cidrSubnet = addressSplit[1]

    # split up the ip by getting each of
    # the 4 numbers split up by '.'
    ipSplit = ip.split('.')
    return ipSplit, cidrSubnet


def convertCidrToDec(cidrSubnet):
    '''returns netmask given a cidr subnet'''
    # initiallize netmask to empty string
    netmask = ""
    # to construct netmask, 1's are added to the left most of the address
    # these are bits and the number of bits is equal to the value of cidrSubnet
    for x in range(0, int(cidrSubnet)):
        netmask += str(1)
    # to further construct the netmask, 0's are added to the right of the 1's
    # from above, the number of 0's is equal to the value of 32-cidrSubnet
    # 32 because there are a total of 32 bits and the cidrSubnet represents
    # the size of the network ID
    for x in range(0, 32 - int(cidrSubnet)):
        netmask += str(0)
    # netmask 1-4 are representative of the 4 values between the
    # 3 decimal points
    netmask1 = netmask2 = netmask3 = netmask4 = ""
    # for the first 8 bits in the first fourth of the address add
    # the values of netmask at given x
    for x in range(0, 8):
        netmask1 += str(netmask[x])
    # for the second 8 bits in the second fourth of the address add
    # the values of netmask at given x
    for x in range(8, 16):
        netmask2 += str(netmask[x])
    # for the third 8 bits in the third fourth of the address add
    # the values of netmask at given x
    for x in range(16, 24):
        netmask3 += str(netmask[x])
    # for the fourth 8 bits in the last fourth of the address add
    # the values of netmask at given x
    for x in range(24, 32):
        netmask4 += str(netmask[x])

    # convert each netmask 1-4 from binary bits to
    # decimal format and then
    # convert each one into a string to return
    netmask1 = str(int(netmask1, base=2))
    netmask2 = str(int(netmask2, base=2))
    netmask3 = str(int(netmask3, base=2))
    netmask4 = str(int(netmask4, base=2))

    # return as a tuple containing netmask 1-4
    return netmask1, netmask2, netmask3, netmask4

def printIPsInSubnet(ip, netmask):
    '''Used to print all addresses in host IDs for third and fourth octets depending on subnet length'''
    # if 3rd octet in net mask is less than 255
    # we subtract it from 255
    if int(netmask[2]) < 255:
        # count3 is the available number of addresses
        # based on the value of netmask[2]
        count3 = 255 - int(netmask[2])
        # for all values from 0 to count3 populate addresses from 1-255
        # populate all host IDs
        for loop3 in range(0, count3):
            for loop4 in range(1, 256):
                # had to add in str(int(ip[x])+loop(x+1) into code to make it consistent with module used
                print("{}.{}.{}.{}".format(ip[0], ip[1], str(int(ip[2])+loop3), str(int(ip[3])+loop4)))
    # else if 4th octet in net mask is less than 255
    # subtract it from 255    elif int(netmask[3]) < 255:
    elif int(netmask[3]) < 255:
        # count4 is the available number of addresses
        # based on the value of netmask[3]
        count4 = 255 - int(netmask[3])
        # for all values from 0 to count 4 populate addresses from 1-255
        for loop4 in range(1, count4):
            # had to add in str(int(ip[x])+loop(x+1) into code to make it consistent with module used
            print("{}.{}.{}.{}".format(ip[0], ip[1], ip[2], str(int(ip[3])+loop4)))

def validateInput(cidrNotation, input_cidr):
    '''Used to validate user input to verify that cidrNotation is in correct format'''
    # try-except block 1
    try:
        # if either the '.' or the '/' in cidrNotation is the first character
        # in the address then raise an exception
        if cidrNotation.index(".") < 0 or cidrNotation.index("/") < 0:
            return False
    except ValueError:
        return False
    # it must have 3 dots, with 4 numbers in between, followed by a /, followed by a number
    addressSplit = cidrNotation.split('/')
    ip = addressSplit[0]
    cidrSubnet = addressSplit[1]
    ipSplit = ip.split('.')
    # try-except block 2
    try:
        # are there 3 dots?
        if cidrNotation.count(".") != 3:
            return False
    except ValueError:
        return False
    # try-except block 3
    try:
        # are there 4 numbers in between the dots?
        if len(ipSplit) != 4:
            return False
    except ValueError:
        return False
    # first number - left most (significant one) can not be 0, but the rest can be 0
    # try-except block 4
    try:
        if int(ipSplit[0]) < 1 or int(ipSplit[0]) > 255:
            return False
    except ValueError:
        return False
    # numbers 2-4 can be zero but cannot be greater than 255
    # try-except block 5
    try:
        # loop through all ip's starting at ip 2
        # in ipSplit and make sure
        # each value is between 0 and 255
        for ip in ipSplit[1:]:
            if int(ip) < 0 or int(ip) > 255:
                return False
    except ValueError:
        return False
    # the subnet size must be less than 32
    # and also greater than 0
    # try-except block 6
    try:
        if int(cidrSubnet) < 0 or int(cidrSubnet) > 32:
            return False
    except ValueError:
        return False
    # try-except block 7
    # this block is very important
    # without it we would get host bits set error
    try:
        if cidrNotation != input_cidr:
            return False
    except ValueError:
        return False

    return True

def main():
    # welcome prompt
    print("Tobby Lie, CIDR Notation")
    # input cidrNotation
    cidrNotation = input("Enter your network in CIDR: ")
    # input validation
    # if incorrect input just exit program
    # parseString contains (['first number', 'secondn number', 'third number', 'fourth number'], 'subnet')
    parseString = parseIP(cidrNotation)
    #  ip is now set to ['first number', 'secondn number', 'third number', 'fourth number']
    ip = parseString[0]
    # cidrSubnet is not set to 'subnet' from above
    cidrSubnet = parseString[1]
    ############################################################################################
    # this section is necessary to prevent "host bits set" error
    # when given cidrNotation with a subnet length, there must be zero bits
    # to the right of the kth bit, k being the subnet length
    # there must be 32-k zero bits for the host addresses
    # if this is not correct, it is invalid input as there would already be
    # a bit in the place where there must be host IDs

    netmask_2 = ""
    # get bitmask for cidrSubnet
    for x in range(0, int(cidrSubnet)):
        netmask_2 += str(1)
    for x in range(0, 32 - int(cidrSubnet)):
        netmask_2 += str(0)

    # get binary representation of ip octets and create long string of bits
    ip_temp = ""
    for octet in ip:
        temp_val = int(octet)
        temp_val = bin(temp_val)[2:].zfill(8)
        temp_val = str(temp_val)
        ip_temp += temp_val
    ip_temp = str(ip_temp)

    # preserve bits that are masked with 1 and then
    # fill zeros everywhere else to the right of this
    newCidrBit = ""
    for indx, bit in enumerate(netmask_2):
        if bit == '1':
            newCidrBit += ip_temp[indx]
        elif bit == '0':
            newCidrBit += '0'

    # new variable to hold correct value given the subnet length
    # will be used against actual input to make sure it is input correctly
    # and there is enough space for host IDs
    input_CidrBit = ""

    # create first_octet of just bits
    first_octet = ""
    for bit in newCidrBit[:8]:
        first_octet += bit

    # create second_octet of just bits
    second_octet = ""
    for bit in newCidrBit[8:16]:
        second_octet += bit

    # create third octet of just bits
    third_octet = ""
    for bit in newCidrBit[16:24]:
        third_octet += bit

    # create fourth octet of just bits
    fourth_octet = ""
    for bit in newCidrBit[24:32]:
        fourth_octet += bit

    # construct address from bits converted to decimal
    input_CidrBit += str(int(first_octet, base=2))
    input_CidrBit += "."
    input_CidrBit += str(int(second_octet, base=2))
    input_CidrBit += "."
    input_CidrBit += str(int(third_octet, base=2))
    input_CidrBit += "."
    input_CidrBit += str(int(fourth_octet, base=2))
    input_CidrBit += "/"
    input_CidrBit += cidrSubnet
    ############################################################################################

    # validate input before using it for any functions
    # if input invalid, gracefully exit program
    if not validateInput(cidrNotation, input_CidrBit):
        # incorrect input message
        print("wrong input: input is not in CIDR format")
        return

    # prompt that you are using functions made from scratch
    print("Using my own functions")
    # print the entire IP and the subnet specifying the network ID size
    print("IP:{}.{}.{}.{}\tCIDR:{}".format(ip[0], ip[1], ip[2], ip[3], cidrSubnet))

    # get netmask by converting cidrSubnet into binary bitmask and then converting to decimal
    netmask = convertCidrToDec(cidrSubnet)

    # print subnet and all IPs in subnet
    print("subnet: {}.{}.{}.{}".format(netmask[0], netmask[1], netmask[2], netmask[3]))
    print("IPs in Subnet:")
    printIPsInSubnet(ip, netmask)

    # using the ipaddress module of Python
    print("Using import ipaddress:")
    # get network based on cidrNotation
    network = ipaddress.ip_network(cidrNotation)
    # print out the IP and subnet
    print("IP:{}".format(network, cidrSubnet))
    print("subnet:{}".format(network.netmask))
    print("IPs in Subnet")
    # print all hosts based off of network
    for host in network.hosts():
        print(host)

if __name__ == "__main__": main()
