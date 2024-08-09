## Tasks:
    1. What is Computer Network? Write its uses.
    2. What are different layers of OSI Model. Write their uses.
    3. Differentiate between OSI Model and TCP/IP Model.
    4. Simulate in packet tracer a ping request from one network to a different network.
  
## 1. What is Computer Network? Write its uses.

A computer network is a collection of interconnected computing devices (such as computers, servers, routers, and switches) that communicate with each other to share resources, data, and information. These devices are linked by various communication protocols over wired or wireless media.

Its uses are explained below:

1. **Business Application**:
   
    - Resource Sharing: sharing of hardware (printer, scanner, fax), software and data across network irrespective of geographical location, reducing costs and increasing productivity.
   
    - High Reliability: high accessibility and availability of data since there are multiple copies in multiple devices across the network.
   
    - Saving Money: little to no cost for sharing resources, no need to use mainframe computer, can use cheap desktop computer.
   
    - Scalability: easy to add and integrate new devices into the network for higher computational power.

2. **Home Application**:

    - E-commerce: paying bills, transfer cash, online shopping
      
    - Access to Information: access to information anywhere at all times via the internet at home
      
    - Communication: communicate via text, voice, video calls, etc.
      
    - Entertainment: multiplayer games, videos, movies, music, social media, etc.
      
    - Online Education: online classrooms, notebooks, youtube, websites, etc.
      
3. **Mobile Application**:
   
    - Same features as home application but with mobile computers like cell phones, laptops, notebook computers and tablets.
    - High portability and efficiency.
 
## 2. What are different layers of OSI Model. Write their uses.

The OSI (Open Systems Interconnection) model is a conceptual framework used to understand and standardize the functions of a telecommunication or computing system without regard to its underlying internal structure and technology. It divides the process of communication into seven distinct layers.

The seven layers along with their brief introduction and uses are as follows:

1. **Physical Layer**:

    The Physical Layer is the lowest layer of the OSI model, responsible for the transmission of raw data bits over a physical medium, such as cables or wireless signals. It defines the hardware elements involved, including cables, switches, and the electrical signals used. This layer ensures that when one device sends a bit, it is correctly received by another device.
2. **Datalink Layer**:

    The Data Link Layer is responsible for establishing a reliable link between two directly connected nodes, providing error detection and correction, as well as frame synchronization. It is divided into two sublayers: MAC (Media Access Control) and LLC (Logical Link Control). The MAC sublayer controls how devices on the same network segment access the physical medium, while LLC manages communication between devices and ensures error-free transmission.
3. **Network Layer**:

    The Network Layer is responsible for determining the best path for data to travel from the source to the destination across multiple networks (routing). It handles logical addressing (such as IP addresses) and manages traffic problems like packet switching, congestion control, and packet forwarding. This layer ensures that data reaches its correct destination.
4. **Transport Layer**:

    The Transport Layer ensures reliable data transfer between devices, providing services such as flow control, error correction, and data segmentation. It manages end-to-end communication, ensuring that data is delivered error-free, in sequence, and without losses or duplicates. Protocols like TCP (Transmission Control Protocol) and UDP (User Datagram Protocol) operate at this layer.
5. **Session Layer**:

    The Session Layer is responsible for establishing, managing, and terminating connections (sessions) between applications. It manages sessions in a way that they are synchronized and organized, even in cases of prolonged data transfer. This layer ensures that connections between different applications are maintained and properly coordinated.
6. **Presentation Layer**:

    The Presentation Layer translates data between the application layer and the network, ensuring that data sent by the application layer of one system can be read by the application layer of another. It handles data encryption, compression, and formatting, ensuring data is in a usable format. This layer is responsible for data representation, making sure that the data is readable regardless of system differences.
7. **Application Layer**:

    The Application Layer is the topmost layer, providing network services directly to end-users and applications. It handles high-level protocols, including HTTP, FTP, SMTP, and DNS, allowing applications to interact with the network. This layer serves as the interface between the user and the network, enabling activities like web browsing, email, and file transfers.

## 3. Differentiate between OSI Model and TCP/IP Model.

| OSI Model | TCP/IP Model |
| ------------- | ------------- |
| 1. It is seven-layered reference model. | 1. It is four-layered model. |
| 2. Internetworking is not supported.  | 2. TCP/IP supports internetworking.  |
| 3. It clearly distinguishes between services, interfaces and protocols.  | 3. It fails to distinguish between services, interfaces and protocols.  |
| 4. Network layer provides both connection-oriented and connectionless services.  | 4. Internet layer provides connectionless services.  |
| 5. Transport layer provides only connection-oriented services.  | 5. Transport layer provides both connection-oriented and connectionless services.  |
| 6. Protocols are better hidden and can be replaced easily.  | 6. Protocols are not hidden and cannot be replaced easily.  |
