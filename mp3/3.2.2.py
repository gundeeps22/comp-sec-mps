#!/usr/bin/python2.7
import dpkt
import sys
import socket

def main():
    if(len(sys.argv) < 2):
        print "error: need argument"
        sys.exit(1)
    
    # read in pcap file
    f = open(sys.argv[1])
    pcap = dpkt.pcap.Reader(f)

    # SYN & SYN+ACK mappings {IP address : count}
    syn_count = {}
    synack_count = {}
    
    # iterate thru each packet
    for ts, buf in pcap: # ts=timestamp; buf=packet data
        try: # parse & decode a raw buffer into python objects
            eth = dpkt.ethernet.Ethernet(buf)
        except dpkt.UnpackError or AttributeError:
            continue # skip malformed packets
        
        # if the packet is an IP packet
        if eth.type == dpkt.ethernet.ETH_TYPE_IP:
            ip = eth.data
            # if the packet is a TCP packet
            if ip.p == dpkt.ip.IP_PROTO_TCP:
                tcp = ip.data
                # convert ip addr into its standard dotted-quad string representation
                ip_src = socket.inet_ntoa(ip.src)
                ip_dst = socket.inet_ntoa(ip.dst)
                # if SYN flag is 1 (but ACK flag is 0)
                if ((tcp.flags & dpkt.tcp.TH_SYN != 0) and (tcp.flags & dpkt.tcp.TH_ACK == 0)):
                    if ip_src not in syn_count:
                        syn_count[ip_src] = 0
                    syn_count[ip_src] += 1
                # if SYN+ACK flag is 1
                if ((tcp.flags & dpkt.tcp.TH_SYN != 0) and (tcp.flags & dpkt.tcp.TH_ACK != 0)):
                    if ip_dst not in synack_count:
                        synack_count[ip_dst] = 0
                    synack_count[ip_dst] += 1

    for ip_addr in syn_count:
        # if there are no SYN+ACK packets for the corresponding SYN packets
        if ip_addr not in synack_count:
            synack_count[ip_addr] = 0
        # if there are SYN packets sent more than 3 times the corresponding SYN+ACK packets
        if syn_count[ip_addr] > synack_count[ip_addr] * 3:
            print ip_addr

if __name__ == '__main__':
    main()
