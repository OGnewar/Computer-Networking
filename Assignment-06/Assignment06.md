## Tasks:
```
1. How many bytes is UDP header? What are the different fields. How are the field values set?
2. How many bytes is TCP header? What are the different fields. How are the field values set?
3. Verify in Wireshark.
```

# 1. How many bytes is UDP header? What are the different fields. How are the field values set?

The UDP (User Datagram Protocol) header is 8 bytes long.
The different UDP Header Fields with their brief explanation are as follows:

1. **Source Port (16 bits)**:

    It identifies the port number of the sending application. It can be set by the application to any valid port number.

2. **Destination Port (16 bits)**:

    It identifies the port number of the receiving application. This value is set based on the application or service that is being communicated with.

3. **Length (16 bits):**:

    It specifies the total length of the UDP header and data in bytes. The minimum value is 8 bytes, corresponding to the length of the UDP header with no data. The length is calculated as `8 + data length`.

4. **Checksum (16 bits)**:

    It is used for error-checking the header and data. This field is optional in IPv4 but mandatory in IPv6. If the checksum is not used, this field is set to zero. Otherwise, it's calculated using a pseudo-header (which includes parts of the IP header) and the UDP header and data.