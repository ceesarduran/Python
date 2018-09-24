print("***********************INICIO ****************************")

#Exercise 1:
# ""Open the "show_version.txt" file for reading. Use the .read() method to read in the entire file
# contents to a variable. Print out the file contents to the screen. Also print out the type of the
# variable (you should have a string at this point).
# Close the file.
# Open the file a second time using a Python context manager (with statement). Read in the file
# contents using the .readlines() method. Print out the file contents to the screen. Also print out
# the type of the variable (you should have a list at this point).
# ""

file = open('show_version.txt')
fileRead = file.read()
print (fileRead)
print (type(fileRead))
file.close()

file = open('show_version.txt')
fileREAD = file.readlines()
print (fileREAD)
print (type(fileREAD))
#print("***********************Hasta Aqui ejercicio 1 ****************************")


#Excercise 2: 
# """Create a list of five IP addresses.
# Use the .append() method to add an IP address onto the end of the list. Use the .extend()
# method to add two more IP addresses to the end of the list.
# Use list concatenation to add two more IP addresses to the end of the list.
# Print out the entire list of ip addresses. Print out the first IP address in the list. Print out
# the last IP address in the list.
# Using the .pop() method to remove the first IP address in the list and the last IP address in
# the list.
# Update the new first IP address in the list to be '2.2.2.2'. Print out the new first IP address
# in the list.
# """
print("***********************Ejercicio 2 ****************************")
listex2 = ['10.10.10.10','10.20.20.20','10.30.30.30','10.40.40.40','10.50.50.50']
print (listex2)
listex2.append('10.60.60.60')
print (listex2)
listex2.extend(['10.70.70.70' , '10.80.80.80'])
print (listex2)
listex2 = listex2 + ['10.90.90.90' , '10.100.100.100']
print (listex2)
listex = listex2.pop(0)
print (listex2)
listex2[0] = '10.0.0.0'
print (listex2)
fl= open("SalidaEjercicio2.txt" , 'w')
fl.write (str(listex2))
fl.write('\n')
fl.write ("Aqui termina Ejercicio 2")
fl.close

#print("***********************Hasta Aqui ejercicio 1 ****************************")



print("***********************Ejercicio 3 ****************************")


#Excercise 3:

# """Read in the "show_arp.txt" file using the readlines() method. Use a list slice to
# remove the header line.
# Use pretty print to print out the resulting list to the screen, syntax is:
# ----
# from pprint import pprint
# pprint(some_var)
# ----
# Use the list .sort() method to sort the list based on IP addresses.
# Create a new list slice that is only the first three ARP entries.
# Use the .join() method to join these first three arp entries back together as a single string
# using the newline character ('\n') as the separator.
# Write this string containing the three ARP entries out to a file named "arp_entries.txt".
# """
from pprint import *
with open ("show_arp.txt") as farp:
	show_arp = farp.readlines()
pprint(show_arp)
show_arp = show_arp[1:]
pprint(show_arp)

show_arp.sort()

myentries = show_arp[:3]
myentries = '\n'.join(myentries)
pprint(myentries)

with open ("arp_new.txt", "wt") as farp2:
	farp2.write(myentries)

print("***********************Ejercicio 4 ****************************")

	
#Excercise 4:	
# """Read in the "show_ip_int_brief.txt" file into your program using the
# .readlines() method.
# Obtain the list entry associated with the FastEthernet4 interface. You can
# just hard-code the index at this point since we haven't covered for-loops
# or regular expressions:
# Use the string .split() method to obtain both the IP address and the
# corresponding interface associated with the IP.
# Create a two element tuple from the result (intf_name, ip_address).
# Print that tuple to the screen.
# Use pycodestyle on this script. Get the warnings/errors to zero. You might need
# to 'pip install pycodestyle' on your computer (should be able to type this from
# the shell prompt). Alternatively, you can type:
# 'python -m pip install pycodestyle'
  
with open ("show_ip_int_brief.txt") as fileip:
	ipbrief = fileip.readlines()

pprint (ipbrief)  

print ("que es" , ipbrief[5])
print ("que es" , ipbrief[0])  

ipbrief4 = ipbrief[5].strip()
print(ipbrief4)
ipbrief = ipbrief4.split()
dato1= ipbrief[0]
dato2= ipbrief[1]
dato3= ipbrief[2]

my_result  = (dato1, dato2, dato3)
print (my_result)

if dato3 == 'YES':
	print (dato1, dato2)

print("***********************Ejercicio 5 ****************************")

	
#Excercise 4:
# """Read the 'show_ip_bgp_summ.txt' file into your program. From this BGP output obtain the
# first and last lines of the output.
# From the first line use the string .split() method to obtain the local AS number.
# From the last line use the string .split() method to obtain the BGP peer IP address.
# Print both local AS number and the BGP peer IP address to the screen.	

with open ("show_ip_bgp_summ.txt") as fbgp:
	filebgp = fbgp.read()
print("Leida", filebgp)
filebgpsumm= filebgp.splitlines()
print ("Separada de linea", filebgpsumm)
firstline= filebgpsumm [0]
print ("primera linea", firstline)
lastline = filebgpsumm[-1]
print ("ultima linea" , lastline)

ASnumber = firstline.split()[-1]
print ("numero AS" , ASnumber)
BGP_peer = lastline.split()[0]
print ("BGP Peer" , BGP_peer)
print (" AS y BGP", ASnumber, BGP_peer)
hola= str([ASnumber , BGP_peer])
with open ("AS_BGP.txt", "w") as fasbgp:
	fasbgp.write(hola)