import socket
import sqlite3
from dnslib import DNSRecord, DNSHeader, RR, QTYPE, A
import logging

# Configure logging
logging.basicConfig(
    filename="dns_server.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def handle_dns_request(data):
    try:
        # Parse the DNS query
        query = DNSRecord.parse(data)
        qname = str(query.q.qname)[:-1]  # Remove trailing dot

        # Create a DNS reply
        reply = query.reply()
        if is_blocked(qname):
            logging.info(f"Blocked: {qname}")
            reply.add_answer(RR(qname, QTYPE.A, rdata=A(BLOCKED_IP)))
        else:
            logging.info(f"Forwarded: {qname}")
            # Forward the query to an external DNS server
            forwarder = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            forwarder.sendto(data, ("8.8.8.8", 53))
            response_data, _ = forwarder.recvfrom(512)
            forwarder.close()
            return response_data

        return reply.pack()
    except Exception as e:
        logging.error(f"Error handling request: {e}")
        return None
    
# Define the IP address for the "blocked" page
BLOCKED_IP = "127.0.0.1"

# Function to check if a domain is blocked
def is_blocked(domain):
    conn = sqlite3.connect("blocklist.db")
    cursor = conn.cursor()
    cursor.execute("SELECT 1 FROM blocklist WHERE domain = ?", (domain,))
    result = cursor.fetchone()
    conn.close()
    return result is not None

# Function to handle DNS requests
def handle_dns_request(data):
    try:
        # Parse the DNS query
        query = DNSRecord.parse(data)
        qname = str(query.q.qname)[:-1]  # Remove trailing dot

        # Create a DNS reply
        reply = query.reply()
        if is_blocked(qname):
            print(f"Blocked: {qname}")
            reply.add_answer(RR(qname, QTYPE.A, rdata=A(BLOCKED_IP)))
        else:
            print(f"Forwarding: {qname}")
            # Forward the query to an external DNS server
            forwarder = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            forwarder.sendto(data, ("8.8.8.8", 53))
            response_data, _ = forwarder.recvfrom(512)
            forwarder.close()
            return response_data

        return reply.pack()
    except Exception as e:
        print(f"Error handling request: {e}")
        return None

# Start the DNS server
def start_dns_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(("0.0.0.0", 53))  # Bind to port 53 (DNS port)
    print("DNS server is running...")

    while True:
        try:
            data, addr = server_socket.recvfrom(512)
            response = handle_dns_request(data)
            if response:
                server_socket.sendto(response, addr)
        except KeyboardInterrupt:
            print("\nShutting down DNS server...")
            break
        except Exception as e:
            print(f"Error: {e}")

    server_socket.close()

if __name__ == "__main__":
    start_dns_server()
