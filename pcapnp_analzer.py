from scapy.all import *

# open the PCAPNG file
pcap = rdpcap("example.pcapng")

# loop through each packet in the file
for packet in pcap:
  # print out the packet's source and destination IP addresses
  print("Source IP: " + packet[IP].src)
  print("Destination IP: " + packet[IP].dst)

  # check if the packet contains TCP data
  if TCP in packet:
    # print out the packet's source and destination TCP ports
    print("Source Port: " + str(packet[TCP].sport))
    print("Destination Port: " + str(packet[TCP].dport))

  # check if the packet contains DNS data
  if DNS in packet:
    # print out the packet's DNS queries
    for query in packet[DNS].qd:
      print("DNS Query: " + str(query.qname))

  # print a separator between packets
  print("-------------------")
