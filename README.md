# TCP Lab Securing Client-Server Application with TLS
### Step 1: Setting up the virtual environment
**1. Create the first VM (Server):**

First download an OS image, for example: [Ubuntu 26.04.1 LTS](https://ubuntu.com/download/server#manual-install-tab)
We will use the same OS for both client and server VMs to ensure having the same environment and full tool compatibility (same python, OpenSSL, wireshark...).  
On VMware Workstation, create a new VM and follow the instructions to install the OS  
Once installed, type the following command the see your IP address (look for interface ens33 and note the inet IP address.  
```bash
ip a
```
**2. Install the required tools:**  
- Python3
- OpenSSL: Open-source library that implements Secure Sockets Layer (SSL) and Transport Layer Security (TLS) protocols and cryptography library
- Tshark: command line version of Wireshark since we're running headless VMs
```bash
sudo apt update
```
```bash
sudo apt install python3 python3-pip openssl libssl-dev
```
```bash
sudo apt install tshark
```
**3. Clone the previous VM to create a second one (Client):**

Before cloning the VM, it must be powered off. Use the command
```bash
sudo shutdown now
```
Then use the menu to clone the VM  
<img width="415" height="357" alt="image" src="https://github.com/user-attachments/assets/f99692cc-0dcc-4d74-ada6-edfff939d7ce" />  
Ensure to choose the "Create a full clone" option  
<img width="331" height="272" alt="image" src="https://github.com/user-attachments/assets/8cdcede8-4883-4326-b254-3d495f055689" />  
  
Power one the newly created Client VM and check its IP Address, you'll notice that **the two IPs are different**!  

**4. Set up the communication between the two VMs**  
Change the network connection from NAT to Host-only for **both VMS**:  
- To create a private network that connects the two VMS and your host machine, but it's isolated from the external internet
- This ensure that any communication stays contained in your virtual environment
- When you use Wireshark, it won't be flooded with random internet traffic
- Ensure complete isolation and security

  <img width="571" height="496" alt="image" src="https://github.com/user-attachments/assets/eca94181-804d-463a-835d-7c5f1e84283e" />

Run a `ping <server IP>` to test the connection between the two hosts

### Step 2: Set up a self-signed certificate

Using the server VM, create a directory for certifications
```bash
mkdir tls-lab-certs
cd tls-lab-certs
```
Then use OpenSSL library to generate the server's private kay.**This private key will be used during the TLS handshake to authenticate the server**.  
We'll use an rsa-2028 encryption algorithm
```bash
openssl genrsa -out server.key 2048
```
Now, instead of sending a Certificate Signing Request (CSR) to a CA server, we self-sign the certificate directly:
```bash
openssl req -new -x509 -days 365 -key server.key -out server.crt
```
<img width="184" height="20" alt="image" src="https://github.com/user-attachments/assets/caf6d2a6-37b5-4617-89a7-39f5bab72cc0" />  

`server.crt` is the public certificate which contains the server's public key and identity information. During the TLS handshake, the server will send it to the client so it knows it's talking with the right machine.





