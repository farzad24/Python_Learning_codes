import re
import socket

"""
mysocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysocket.connect (('tools.cisco.com', 443))
mysocket.send ("GET https://tools.cisco.com/security/center/ipshome.x\n")

while True:
    data = mysocket.recv(512)
    if (len(data) <1):
        break
    if re.search("var myData", data):
            #        result = re.findall(",\[\"([0-9]+/*[0-9]*\)]\",\"<a href=",line)
            result = re.findall("\[\"([0-9]+)/[0-9]+\",", data)
            print result
            break

    #print data


page = open("Cisco_ips_content_page.txt")



#["33459/0","<a
"""
"""
for lines in page:
    line = lines.rstrip()
    if re.search("var myData",line):
#        result = re.findall(",\[\"([0-9]+/*[0-9]*\)]\",\"<a href=",line)
        result = re.findall("\[\"([0-9]+)/[0-9]+\",",line)
        break

print result
"""

#page.close()
#mysocket.close()
