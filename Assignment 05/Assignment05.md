## Tasks:
```
1. Use Wireshark to demonstrate different packets involved in getting IP address from a DHCP server.
2. In the preferred language of your choice, write a web application that allows you to upload a file of minimum 10 MB size. Capture the upload in Wireshark. In your Wireshark capture, follow the TCP stream to inspect connection initiation, file transfer and connection termination.
3. Filter a Wireshark capture on IPV6 and explain why its field has the value it does?
```

## 1. Use Wireshark to demonstrate different packets involved in getting IP address from a DHCP server.

1. Start capturing packets with Wireshark.
2. Open the command prompt and release the IP Address with the command:
    ```
    ipconfig /release
    ```
3. Request a new IP Address with the command:
    ```
    ipconfig /renew
    ```
4. Now stop capturing packets in Wireshark.
5. Filter out the DHCP packets.

<img src="01.pcapng">