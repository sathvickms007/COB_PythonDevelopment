import re

def ipv4_format(ipadd):

    #ipv4 is a 32 bit address represented by 4 octets seperated by dots
    match = re.match(r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$', ipadd)

    if match:
        octets = [int(match.group(i)) for i in range(1, 5)]
        for oct in octets:
            if oct < 0 or oct > 255:
                return False
        return True
    else:
        return False

ipadd = input("Enter an IPv4 address: ")

if ipv4_format(ipadd):
    print(f"{ipadd} is a valid IPv4 address.")
else:
    print(f"{ipadd} is not a valid IPv4 address.")
