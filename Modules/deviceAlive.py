#Matches input hostname to ip address of endpoint. CSV file in "filePointer" is required to have column 1 the device names and column 2 corresponding ip's


import subprocess, csv, os, time, socket

filePointer = "../Resources/All_VC_Systems.csv" #CHANGE TO YOUR FILE NAME
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Creates a TCP/IP socket
script_dir = os.path.dirname(__file__) #Script Directory
endpointListFile = os.path.join(script_dir, filePointer)
csv_file = csv.reader(open(endpointListFile, "rb"), delimiter = ',')
prompt = "> "
hostname = raw_input("What endpoint would you like to check?\n" + prompt)
print "---------------------------------"


#opening reader for CSV file
def ipLookUp(csv_file, hostname):
    for row in csv_file:
        if hostname == row [0]:
            host_ip = row [1]
    return host_ip

tpd_ip = ipLookUp(csv_file, hostname)
try:
    result = subprocess.check_output(["ping", "-c", "1", "-n", "-W", "2", tpd_ip], stderr=subprocess.STDOUT,universal_newlines=True)
    print "Device is up\n"
except subprocess.CalledProcessError:
    print "Device not reachable\n"
