import getpass
import sys
import telnetlib

user = input("Enter your telnet username: ")  
password = getpass.getpass()

for n in range (132,134):
    print('Telnet to host'+ str(n))
    HOST = "192.168.232." + str(n)
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password:")
        tn.write(password.encode('ascii') + b"\n")

        tn.write(b"enable\n")
        tn.write(b"cisco\n")
        tn.write(b"conf t\n")
    
        for v in range(2,4):
            tn.write(b"vlan " + str(v).encode('ascii') + b"\n")
            tn.write(b"name VLAN " + str(v).encode('ascii') + b"\n" )

        tn.write(b"end\n")
        tn.write(b"exit\n")

        print(tn.read_all().decode('ascii'))
