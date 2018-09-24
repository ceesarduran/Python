print("***********************INICIO ****************************")
#Exercise 1:

#Create a Python script that has three variables: ip_addr1, ip_addr2, ip_addr3 (representing
#three corresponding IP addresses). Print these three variables to standard output using a single
#print statement."""


ip_addr1 = '10.10.255.1'
ip_addr2 = '172.16.255.1'
ip_addr3 = '192.168.255.1'

print('Primera direccion' , ip_addr1 )
print('Segunda direccion' , ip_addr2)
print('Tercera direccion' , ip_addr3)
print("TODAS: ", ip_addr1,ip_addr2,ip_addr3)
print("***********************Hasta Aqui ejercicio 1 ****************************")
#Excercise 2: 

#"""Prompt a user to enter in an IP address from standard input. Read the IP address in and break it
# up into its octets. Print out the octets in decimal, binary, and hex.
# Your program output should look like the following:
# $ python exercise2.py
# Please enter an IP address: 80.98.100.240
    # Octet1         Octet2         Octet3         Octet4
# ------------------------------------------------------------
      # 80             98             100            240
   # 0b1010000      0b1100010      0b1100100     0b11110000
     # 0x50           0x62           0x64           0xf0
# ------------------------------------------------------------
# Four columns, fifteen characters wide, a header column, data centered in the column.
# """

print ("Ingresa la dirección IP")
in_ip= input()
print ("IP address was" , in_ip)
inlist = list(in_ip)
octets = in_ip.split (".")
print (type (inlist))
print (inlist[2])
print ("octeto 1" , octets[0])
print ("octeto 2" , octets[1])
print ("octeto 3" , octets[2])
print ("octeto 4" , octets[3])
octets [2] = int(octets [2]) + 1
print ("nuevo" , octets[2])

print("***********************Hasta Aqui ejercicio 2 ****************************")
#Excercise 3: 
# """Create a show_version variable that contains the following
# show_version = "*0  	  CISCO881-SEC-K9       FTX0000038X    "
# Remove all leading and trailing whitespace from the string.
# Split the string and extract the model and serial_number from it.
# Check if 'Cisco' is contained in the model string (ignore capitalization).
# Check if '881' is in the model string.
# Print out both the serial number and the model.

show_version = "*0  	  CISCO881-SEC-K9       FTX0000038X    "
show_version45 = show_version.strip(' ')
print (show_version)
print (show_version45)
field = show_version.split()
no_importa= field[0]
Vendor = field[1]
Serial = field[2]

print ("primera {}" .format("no_importa"))
print ("segunda {}" .format("Vendor"))
print ("tercera {}" .format("Serial"))

vendor = 'cisco' in Vendor.lower()
print ("Verificamos si la palabra Cisco esta {}" .format(vendor))

modelo = '885' in Vendor
print ("Verificamos si el modelo es 885 {}" .format(modelo))

print("***********************Hasta Aqui ejercicio 3 ****************************")

#Excercise 4:
# You have the following three variables from the arp table of a router:
# mac1 = "Internet  10.220.88.29           94   5254.abbe.5b7b  ARPA   FastEthernet4"
# mac2 = "Internet  10.220.88.30            3   5254.ab71.e119  ARPA   FastEthernet4"
# mac3 = "Internet  10.220.88.32          231   5254.abc7.26aa  ARPA   FastEthernet4"
# Process these ARP entries and print out a table of "IP ADDR" to "MAC ADDRESS". The output
# should look like following:
             # IP ADDR          MAC ADDRESS
# -------------------- --------------------
        # 10.220.88.29       5254.abbe.5b7b
        # 10.220.88.30       5254.ab71.e119
        # 10.220.88.32       5254.abc7.26aa
# Two columns, 20 characters wide, data right aligned, a header column.


mac1 = "Internet  10.220.88.29           94   5254.abbe.5b7b  ARPA   FastEthernet4"
mac2 = "Internet  10.220.88.30            3   5254.ab71.e119  ARPA   FastEthernet4"
mac3 = "Internet  10.220.88.32          231   5254.abc7.26aa  ARPA   FastEthernet4"

print ("mac1" , mac1)
print ("mac2" , mac2)
print ("mac3" , mac3)

spl_mc1 = mac1.split()
spl_mc2 = mac2.split()
spl_mc3 = mac3.split()
print ("IP Address 1" , spl_mc1[1])
print ("Mac Address 1" , spl_mc1[3])
print ("IP Address 2" , spl_mc2[1])
print ("Mac Address 2" , spl_mc2[3])
print ("IP Address 3" , spl_mc3[1])
print ("Mac Address 3" , spl_mc3[3])


print()
print("{:>20} {:>20}".format("IP ADDR", "MAC ADDRESS"))
print("{:>20} {:>20}".format("-" * 20, "-" * 20))
print("{:>20} {:>20}".format(spl_mc1[1], spl_mc1[3]))
print("{:>20} {:>20}".format(spl_mc2[1], spl_mc2[3]))
print("{:>20} {:>20}".format(spl_mc3[1], spl_mc3[3]))
print()

print("***********************Hasta Aqui ejercicio 4 ****************************")
print("***********************Fin SEMANA 1 ****************************")