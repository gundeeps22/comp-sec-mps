# comp-sec-mps

This is a personal guide to working machine problems in **CS461: Computer Security I** and a portfolio for me to keep track of what I have learned in the class. It is not intended to just give out my code to future students; in fact, many of the answers are going to be *different* due to hashing for each student. Other students, however, can refer to this guide for help whenever they are stuck on a problem or in need of a place to get started with, but please do not take advantage of this guide to get work done.

## Getting Started

First and foremost, **working environment** must be set up. The course website provides an Ubuntu image called *cs461.ova* which you can use to import to [Oracle's VM VirtualBox](https://www.virtualbox.org/). You will mostly be working on this virtual machine for this class, although I think you *could* work from your local machine and commit to svn where grading is actually done. If you're unfamiliar with svn (Subversion), please acquaint yourself with it, although all you need to know is checking out and committing.

So for your general working environment, you need to:
1. Download an Ubuntu image from the course website.
2. Install [VirtualBox](https://www.virtualbox.org/wiki/Downloads).
3. Import Virtual Appliance with the VM image.
4. *svn checkout* the selected mp folder from the class's svn shared repository.
5. Install any necessary libraries or packages along the way.
6. *svn commit* whenever you're done with a problem.

## MP1: Cryptography

### Checkpoint 1

#### 1.1.1.2 Converting Hexadecimal to Binary and Decimal

To convert from [hex to dec](http://www.binaryhexconverter.com/hex-to-decimal-converter), multiply each digit by base 16 raised to digit location and add it all up.

e.g. 7DE = (7 * 16<sup>2</sup>) + (13 * 16<sup>1</sup>) + (14 * 16<sup>0</sup>) = 2014

To convert from [hex to bin](http://www.binaryhexconverter.com/hex-to-binary-converter), change each digit to binary and append them all.

e.g. 7 = 0111, D = 1101, E = 1110; 7DE = 0111 1101 1110

#### 1.1.2.1 Substitution Cipher

The ciphertext is as shown:

	UVKG IXWVIAFPW QIFGTPXIG TB KVI KXIX XGCVRUFGSXA RZ JTPLXPCFTPG SXUA FP CSFG JFCZ FP 1929  1949

The key to decode it is 

	VRJAXBWSFEDUNPTQOIGCMLKHZY

which means V is A, R is B, J is C, and so on in alphabetical order.

You are to write a **python script** that takes *the ciphertext file*, *the key file*, and *the output file* as three arguments from the command line and successfully write the decoded plaintext to the output file.

There are many ways to approach this problem, but I used Python dictionary to help me map.

#### 1.1.2.2 Decrypting AES

#### 1.1.2.3 Breaking a Weak AES Key

#### 1.1.2.4 Decrypting a Ciphertext with RSA

#### 1.1.3.1 Avalanche Effect

#### 1.1.3.2 Weak Hashing Algorithm

### Checkpoint 2

#### 1.2.1.2 Conduct a Length Extension Attack

#### 1.2.2.2 MD5 Hash Collision Attack

#### 1.2.3 Exploiting a Padding Oracle

#### 1.2.4 Mining Your Ps and Qs

#### 1.2.5 Creating Colliding Certificates

## MP2: Application Security

## MP3: Network Security

Objectives for this MP:
* Examining a network trace from a sample network.
* Cracking password for a WiFi network protected with WEP.
* Analyzing network traffic.
* Obtaining a victim's credentials.

### Checkpoint 1

#### Getting Started

For MP3, **do not use VM**. Install [Wireshark](https://www.wireshark.org/download.html) on your local machine, as VM may have restrictions sniffing a wireless network. TAs recommended 32-bit Wireshark since 64-bit had some problems in the past, but 64-bit being the only option for Mac, I had no problem doing the MP with 64-bit. Wireshark is all you need to complete Checkpoint 1, and really, the platform should not matter (even Windows should work) since all you are doing is analyzing pre-captured files. *I used Wireshark v2.4.2, but things may vary depending on future patches.*

#### 3.1.1 Exploring Network Traces

You are given a pcap file (3.1.1.pcap) which you are supposed to examine. Open the capture file with Wireshark.

**3.1.1.1**: To identify all the hosts on the local network, first find all IP addresses in the cap file by going to *Statistics > IPv4 Statistics > All Addresses*. These are all the hosts, but some are not in the local network. For example, 8.8.4.4, if you figured out already, is Google's DNS and therefore an external network. 10.0.2.2 is also not. Basically, IP addresses in the range of 10.1.236.* are all local. Then find their corresponding MAC addresses, which you can find easily by looking at their packets.

**3.1.1.2**: To find TCP conversations, go to *Statistics > Conversations*, and on the TCP tab, you'll see the total number of unique TCP conversations in the cap file. 

**3.1.1.3**: The easiest way of finding the IP address of the gateway (or the router) is knowing that it usually ends in 1. If there is no IP address that ends in 1, look at how packets are sent to an external network (e.g. 8.8.4.4). In order to send packets to Google, it must pass through a router, which means the destination MAC address of that packet is the MAC address of the router. Then identify an IP address that has the same MAC address.

**3.1.1.4**: FTP stands for File Transfer Protocol, so for this problem, you should expect to retrieve some file. If you have looked at the cap file enough, you should realize that there are two main FTP conversations, one active and one passive. Now which one is active, and which one is passive? The difference is well explained [here](https://stackoverflow.com/questions/1699145/what-is-the-difference-between-active-and-passive-ftp), but basically,
* **Active**:
	* Client Port X -> Server Port 21 in the command channel
	* Server Port 20 -> Client Port Y in the data channel
* **Passive**:
	* Client Port X -> Server Port 21 in the command channel
	* Client Port Y -> Server Port Z in the data channel

So if you have realized already, the conversation that has port 20 is active, and the other one will most likely use a random port. After you distinguished it, find a packet called *FTP-DATA*. Right-click, then *Follow > TCP Stream*. There you will find a secret message of the file. You can save the file or just copy the message into the answer file.

**3.1.1.5**: To identify a port scanner, just find an IP address that plays with ports a lot. It may use ICMP protocol and often have "Destination unreachable (Port unreachable)" as packet info.

#### 3.1.2 HTTPS Traffic

**3.1.2.1**: To find the year the traffic was captured, go to *any packet* and under the frame layer, you will see the arrival time.

**3.1.2.2**: There are many ways to find a hostname of the server. One way is to go to *any HTTP GET request packet*, and under the HTTP layer, you will see the Fully Qualified Domain Name.

**3.1.2.3**: To find a list of supported cipher suites, go to *any Client Hello packet*, and under the SSL layer, you will see many cipher suites that the client supports. To copy all the cipher suites, right-click the packet, mark it, and go to *File > Export Packet Dissections > As Plain Text*. Then select *Marked Packets Only* for packet range and *All Expanded* for packet format.

**3.1.2.4**: To find which cipher suite the server chose, go to *any Server Hello packet*, and under the SSL layer, you will see one cipher suite.

**3.1.2.5**: Notice that a client *searched* on the *website*. This should give us enough hints that we should look for HTTP packets. Go to *File > Export Objects > HTTP...* There you will find a list of HTTP objects in the cap file. Look for *search.php* and the value should be the name of a person they entered in the search box.

**3.1.2.6**: Same as 3.1.2.5. Go to *File > Export Objects > HTTP...* and find a *send.php* packet. Save it and the body of the message should be everything after *body=* and before the ampersand (&).

**3.1.2.7**: This is the same packet as 3.1.2.6. Go to the packet, right-click it, and *Follow > TCP Stream*. You will see "Cookie: " but a lot of them in the stream. Scroll down until you locate the correct packet (simply left-click the portion of the stream to see which packet you're looking at) and find the appropriate cookie. *If you don't follow TCP stream but only look at the packet, you will only find a truncated cookie.*

### Checkpoint 2

#### Setup

Before starting Checkpoint 2, it is very important that you set up your environment correctly.
* **For Windows/Non-Mac Users**, I recommend you use Kali Linux Live booted from a USB drive (preferably 8GB or higher). Windows has a lot of restrictions when observing wireless activities, and since Kali Linux comes with many pre-installed packages (e.g. aircrack-ng suites and nmap), it is very convenient for this MP. To be honest, I had a hard time booting Kali Linux on my Mac as well as many other students, so if you have a Mac, I *highly recommend* you use built-in features in Mac. But here are the general steps you would need to take to set up Kali Linux:
  1. Download Kali Linux Light 32 bit [here](https://www.kali.org/downloads/).
  2. Create a Kali Live Bootable USB drive. [[Instructions](https://docs.kali.org/downloading/kali-linux-live-usb-install)]
  3. Add *persistence* to your drive. (This allows data and configuration to be *saved* after reboot.) [[Instructions](https://docs.kali.org/downloading/kali-linux-live-usb-persistence)]
  4. Boot from your USB drive, then choose "Live USB Persistence" from the menu.
  5. Install Wireshark:
    ```
    apt-get update
    apt-get install wireshark
    ```
* **For Mac (OS X) Users**, use built-in features. I am using macOS Sierra version 10.12.6, and some things may vary. Refer [here](https://guide.macports.org/#installing) for more info on different versions. For Mac OS X 10.9 or later:
  1. Install [XCode](https://itunes.apple.com/us/app/xcode/id497799835).
  2. Install **XCode Command Line Tools** by opening a terminal and run:
  ```
  xcode-select --install
  ```
  3. Install [MacPorts](https://guide.macports.org/#installing.macports).
  4. Install **aircrack-ng** using MacPorts:
  ```
  sudo port install aircrack-ng
  ```
  5. Enter the following symlink to use a built-in utility called **airport**:
  ```
  sudo ln -s /System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport /usr/local/bin/airport
  ```
  6. Install [nmap](https://nmap.org/download.html#macosx).
  7. Install **dpkt**:
  ```
  pip install dpkt
  ```
*I will be using Mac OS X (v10.12.6) for this guide, so refer to different resources if you're using a different OS.*

#### 3.2.1.1 WEP Cracking

The very first thing you need to do in Checkpoint 2 is to crack a Wifi network that TAs set up and find out the WiFi password (WEP key). Though it may sound hard, WEP is one of the huge failures in security and can be easily cracked by aircrack-ng. Assuming everything is correctly set up, first figure out which channel to sniff by running:
```
sudo airport -s
```
which will list all the wireless networks around you. In it, you will find something like this:
```
        SSID BSSID             RSSI CHANNEL HT CC SECURITY (auth/unicast/group)
cs461mp3fa17 60:38:e0:11:9b:b2 -30  1       Y  -- WEP
```
If not, the router is not up and running, and you might need to consult to the TA in charge. But if you are able to identify a WEP network like above, sniff the selected channel (in this case, 1):
```
sudo airport en0 sniff [CHANNEL]
```
If you are getting a help message after running the above command, it might be because the OS X version is different. Go to Network Utility on your Mac to check which ethernet port is for WiFi. (The other case is usually *en1*.) After running the sniff command, you will start to capture 802.11 packets. If so, open another terminal and find the capture file which is located in /tmp/airportSniff*.cap. After locating the capture file, run:
```
aircrack-ng -1 -a 1 -b [TARGET_MAC_ADDRESS] [CAP_FILE]
```
where TARGET_MAC_ADDRESS is BSSID found earlier (in this case, 60:38:e0:11:9b:b2) and CAP_FILE is the name of the capture file you found in /tmp. Executing aircrack-ng might give you:
```
                                 Aircrack-ng 1.2 rc4


                 [00:00:01] Tested 131137 keys (got 9619 IVs)

   KB    depth   byte(vote)
    0   16/ 17   BC(12032) 9A(12032) BF(12032) D5(12032) FB(12032) 
    1    7/  9   06(13824) 35(13312) 61(13312) 0E(13056) B8(12800) 
    2   10/ 12   E2(12288) 48(12288) 3D(12032) 86(12032) 63(12032) 
    3   29/  3   D2(11776) 1E(11520) F1(11520) 1C(11520) DF(11520) 
    4   23/  4   0E(11776) 56(11520) 4B(11520) E8(11520) 9B(11520) 

   Attack failed. Possible reasons:

     * Out of luck: you must capture more IVs. Usually, 104-bit WEP
       can be cracked with about 80 000 IVs, sometimes more.

     * Try to raise the fudge factor (-f).
```
This means you have not collected enough IVs to crack WEP, and you need to wait a bit more until you have sufficient IVs. Generally, you need around 20,000 IVs, which takes around 10-20 minutes, but it really depends on luck. It should not take more than an hour however. Successful cracking will show:
```
                                                     Aircrack-ng 1.2 rc4


                                     [00:00:03] Tested 1872 keys (got 18506 IVs)

   KB    depth   byte(vote)
    0    0/  1   79(28160) DA(25088) 84(24576) 4A(24320) 82(23808) 67(23552) A8(23552) 0E(23296) F6(23296) 
    1    1/  3   B7(26880) 55(25856) AB(24832) 0E(24576) 35(24576) 84(24064) 49(23808) 25(23552) 78(23552) 
    2    2/  5   65(23552) 95(23296) 3B(23296) CD(23296) 1F(23296) 9E(23040) 7D(23040) FE(23040) BC(22784) 
    3    5/ 14   BB(23808) 3C(23296) 2C(23296) 6F(23040) E0(23040) 86(22784) 92(22784) D0(22784) B5(22784) 
    4    0/ 10   E6(25600) 88(25344) 20(25344) 4A(25088) 44(24832) 1C(24832) FA(24576) 13(23808) E0(23552) 

                         KEY FOUND! [ 79:B7:9D:BB:E6 ] 
	Decrypted correctly: 100%
```
Now enter the key (without colons) to connect to the network and you're in!

#### 3.2.1.2/3 Client/Server IP Address

After you cracked the WiFi password, you should now observe what is going on in the network. To do that, you must be in **monitor mode**. Go to *Capture > Options...* and check monitor mode. But when you start capturing traffic, you will only see 802.11 packets but almost no TCP packets. This is because you have not told Wireshark to decrypt 802.11 packets. To decrypt them, simply go to *Preferences... > Protocols > IEEE 802.11 > Decryption Keys > Edit...* and enter in your WEP key (with colons) you have found in 3.2.1.1. When you start capturing traffic again and filter by TCP, you will see two IP addresses talking back and forth **consistently with pattern**. One is client and the other is server. However, you may have more than one client set up and may need to find different repetitive conversations. If you do not see any conversations, either the clients or the server is down, or possibly both. Make sure you turn on name resolution by going to *View > Name Resolution > Resolve Network Addresses* so that you see the names of the server and the client(s). If you see a name of a person, that's most likely other student in the network, but he or she will be most likely talking to the server.

#### 3.2.1.4 Services

To find the services provided by the server, you should use **nmap**. First, connect to the network and on a terminal, run:
```
nmap [SERVER_IP_ADDRESS]
```
This will start port scanning and list the names of services the server is providing.
```
PORT    STATE SERVICE
21/tcp  open  ftp
22/tcp  open  ssh
443/tcp open  https
```
*I never got HTTP using nmap, but HTTP seemed to be one of the answers as well.*

#### 3.2.1.5 Server's Secret

You are asked to find a server's secret file using the services from 3.2.1.4. In the previous problem, you may have found there was a protocol that deals with file transfer. Yes, FTP (File Transfer Protocol). To *use* FTP, run on a terminal while connected to the network:
```
ftp [SERVER_IP_ADDRESS]
```
The above command will connect you to a FTP server, but you have to login. Enter the name of the server (in my case it was "anonymous") and leave the password blank. After a successful login, list the directory:
```
ftp> ls
229 Entering Extended Passive Mode (|||14239|)
150 Here comes the directory listing.
drwx-wx-wx    3 501      20            102 Oct 05 03:15 Drop Box
-rw-r--r--    1 501      20         139872 Oct 24 21:03 proj3.pdf
-rw-r--r--    1 0        0            1513 Oct 26 19:44 server.crt
-rw-r--r--    1 0        0            1675 Oct 26 19:44 server.key
226 Directory send OK.
```
and you will see the server's secret file (RSA private key)! Set your download directory (Desktop may be convenient):
```
ftp> lcd ~/Desktop
Local directory now: /Users/mincloud/Desktop
```
and finally get the file!
```
ftp> get server.key
local: server.key remote: server.key
229 Entering Extended Passive Mode (|||34155|)
150 Opening BINARY mode data connection for server.key (1675 bytes).
100% |************************************************************|  1675      981.83 KiB/s    00:00 ETA
226 Transfer complete.
1675 bytes received in 00:00 (464.69 KiB/s)
```

#### 3.2.1.6 Client's Credentials

After getting the RSA private key from 3.2.1.5, open Wireshark and go to *Preferences... > Protocols > SSL > RSA Keys List > Edit...* Enter the server's IP address, port 443, http protocol, and the location of your key file. Then start capturing traffic in monitor mode again, you will start to see HTTP packets that have been decrypted from TLS. Go to a HTTP packet with *HEAD /secret/index.html HTTP/1.1* and under the HTTP layer > Authorization, you will see the client's credentials.

#### 3.2.1.7 Client's Secret Message

You might have noticed there was a URL link to https://[SERVER_IP_ADDRESS]/secret/index.html when getting the client's credentials. Click the link and enter the client's username and password. The client's credentials expire in an hour, so make sure you are using the one you just collected. After a successful login, it will show a secret message!

#### 3.2.1.8 Jail Time

According to [18 USC § 2511](https://www.law.cornell.edu/uscode/text/18/2511), you can spend up to **5 years** in jail for
intercepting traffic on an encrypted WiFi network without permission.

#### 3.2.2 Anomaly Detection

You are to create a Python program that analyzes a given pcap file and accomplishes anomaly detection. In this exercise, you will only deal with a SYN scan and print out IP addresses that send more than 3 times as many SYN packets as the number of SYN+ACK packets they receive. This rule applies even if the number of packets is very small. The following cases are all considered attacks:
```
SYN=4 ACK+SYN=1
SYN=4 ACK+SYN=0
SYN=1 ACK+SYN=0
```
In addition, the program MUST:
* take only one argument.
* print each IP address only once.
* silently ignore malformed packets or those that are not using Ethernet, IP, and TCP.

## MP4: Web Security
