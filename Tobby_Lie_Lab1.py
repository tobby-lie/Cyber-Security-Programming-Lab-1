# Tobby Lie
# CSCI 4742
# Lab1

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
    '''returns netmask given an cidr subnet'''
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
    # if 3rd octet in net mask is less than 255
    # we subtract it from 255
    if int(netmask[2]) < 255:
        # count3 is the available number of addresses
        # based on the value of netmask[2]
        count3 = 255 - int(netmask[2]
        # for all values from 0 to count3 populate addresses from 1-255
        for loop3 in range(0, count3):
            for loop4 in range(1, 256):
                print("{}.{}.{}.{}".format(ip[0], ip[1], loop3, loop4))
    # else if 4th octet in net mask is less than 255
    # subtract it from 255
    elif int(netmask[3]) < 255:
        # count4 is the available number of addresses
        # based on the value of netmask[3]
        count4 = 255 - int(netmask[3])
        # for all values from 0 to count 4 populate addresses from 1-255
        for loop4 in range(1, count4):
            print("{}.{}.{}.{}".format(ip[0], ip[1], ip[2], loop4))

def validateInput(cidrNotation):
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
    try:
        # are there 3 dots?
        if cidrNotation.count(".") != 3:
            return False
    except ValueError:
        return False
    print(cidrSubnet)
    try:
        # are there 4 numbers in between the dots?
        if len(ipSplit) != 4:
            return False
    except ValueError:
        return False
    # first number - left most (significant one) can not be 0, but the rest can be 0
    try:
        if int(ipSplit[0]) < 1 or int(ipSplit[0]) > 255:
            return False
    except ValueError:
        return False
    # numbers 2-4 can be zero but cannot be greater than 255
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
    try:
        if int(cidrSubnet) < 0 or int(cidrSubnet) > 32:
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
    if not validateInput(cidrNotation):
        # incorrect input message
        print("wrong input: input is not in CIDR format")
        #exit(1)
        return

    # parseString contains (['first number', 'secondn number', 'third number', 'fourth number'], 'subnet')
    parseString = parseIP(cidrNotation)
    #  ip is now set to ['first number', 'secondn number', 'third number', 'fourth number']
    ip = parseString[0]
    # cidrSubnet is not set to 'subnet' from above
    cidrSubnet = parseString[1]
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

    '''# need to split up again
    addressSplit = cidrNotation.split('/')
    ip = addressSplit[0]
    cidrSubnet = addressSplit[1]
    ipSplit = ip.split('.')
    ipSplit = [int(i) for i in ipSplit]
    if int(cidrSubnet) >= 1 and int(cidrSubnet) <= 8:
        indx = 1
        for octet in ipSplit[1:]:
            ipSplit[indx] = 0
            indx += 1
    elif int(cidrSubnet) >= 9 and int(cidrSubnet) <= 16:
        indx = 2
        for octet in ipSplit[2:]:
            ipSplit[indx] = 0
            indx += 1
    elif int(cidrSubnet) >= 17 and int(cidrSubnet) <= 31:
        indx = 3
        for octet in ipSplit[3:]:
            ipSplit[indx] = 0
            indx += 1

    ipSplit = [str(i) for i in ipSplit]
    cidrNotation = ""

    cidrNotation = ""
    for indx,ip  in enumerate(netmask):
        cidrNotation += ip
        if indx < 3:
            cidrNotation += "."
        else:
            cidrNotation +="/"
    cidrNotation += cidrSubnet
    #print(netmask)
    print(cidrNotation)
    '''

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
