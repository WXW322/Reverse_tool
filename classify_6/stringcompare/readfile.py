from scapy.all import *
from netzob.all import *
from classify import *
tftp=rdpcap("tftp.pcap")
start_str=[]
for t in tftp:
     ss=str(t)
     ss1=ss[32:]
     start_str.append(ss1)
print ("E ",len(start_str))
spart=classify(start_str)
spart.do_classify()
results=spart.link
file_object = open('thefile.txt', 'w+')
for r in results:
    for t in r:
      file_object.write(repr(t+1))
      file_object.write(' ')
      print t
    file_object.write('\r\n')
    file_object.write('\r\n')
    file_object.flush()
    print ""
    print ""
file_object.close()
