#0. What happens when...
This question is a classic and still widely used interview question for many types of software engineering position. It is used to assess a candidate’s general knowledge of how the web stack works on top of the internet. One important guideline to begin answering this question is that you should ask your interviewer whether they would like you to focus in on one specific area of the workflow. For a front-end position they may want you to talk at length about how the DOM is rendering. For an SRE position they may want you to go into the load balancing mechanism.

This question is a good test of whether you understand DNS. Many software engineering candidates struggle with this concept, so if you do well on this question, you are already way ahead of the curve. If you take this project seriously and write an excellent article, it may be something that will grab the attention of future employers.

Write a blog post explaining what happens when you type https://www.google.com in your browser and press Enter.

Requirements, your post must cover:

- DNS request
- TCP/IP
- Firewall
- HTTPS/SSL
- Load-balancer
- Web server
- Application server
- Database

1. DNS Request:
   Your browser sends a DNS (Domain Name System) request to a DNS resolver to translate the human-readable domain name "www.google.com" into an IP address.
   The DNS resolver queries the authoritative DNS server for the domain "google.com" to obtain the corresponding IP address.
   Once the IP address is obtained, it is returned to the browser, allowing it to establish a connection with the server hosting Google's website.

2. TCP/IP:
   After obtaining the IP address, your browser initiates a TCP (Transmission Control Protocol) connection with the web server hosting Google's website.
   TCP ensures reliable, ordered, and error-checked delivery of data packets over the internet.
   A three-way handshake is performed between the client (your browser) and the server to establish the connection.

3. Firewall:
   Firewalls may exist at various points in the network infrastructure, including on your local machine, your network router, and the server's network.
   Firewalls monitor and control incoming and outgoing network traffic based on predefined security rules.
   They ensure that only authorized traffic is allowed to pass through, protecting against unauthorized access and malicious activities.

4. HTTPS/SSL:
   HTTPS (Hypertext Transfer Protocol Secure) encrypts the data transmitted between your browser and the web server using SSL (Secure Sockets Layer) or its successor, TLS (Transport Layer Security).
   When establishing the connection, your browser and the server negotiate a secure communication channel using SSL/TLS encryption.
   This encryption protects the confidentiality and integrity of the data exchanged, preventing eavesdropping and tampering by malicious actors.

5. Load Balancer:
   Google likely employs load balancers to distribute incoming web traffic across multiple servers to ensure scalability, reliability, and availability.
   Load balancers monitor the health and performance of servers and route traffic to the most suitable server based on factors such as server load, response time, and geographic proximity of the client.

6. Web Server:
   Once the TCP connection is established and the HTTPS handshake is completed, your browser sends an HTTP request to the web server hosting Google's website.
   The web server (e.g., Google's servers running Apache, Nginx, or another web server software) receives the request, processes it, and generates an HTTP response containing the requested web page content.

7. Application Server:
   Google's web servers may interact with application servers to process dynamic content or execute application logic.
   Application servers handle tasks such as user authentication, database queries, and business logic execution, generating dynamic web pages tailored to the user's request.

8. Database:
   If the requested web page requires data from a database (e.g., search results, user information), the application server queries the database server to retrieve the relevant data.
   The database server processes the SQL queries and returns the requested data to the application server, which incorporates it into the web page content.

