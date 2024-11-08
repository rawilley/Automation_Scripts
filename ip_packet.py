from scapy.all import *

L2 = Ether(src="00:50:56:BC:D0:01",dst="00:00:00:00:00:00")
L3 = IP(src="1.1.1.1",dst="127.0.0.1")
L4 = TCP(sport=5678, dport=23)
data = "Robert Willey"

send = sendp(L2/L3/ICMP(),count=25)

L2.show()
L3.show()
L4.show()
