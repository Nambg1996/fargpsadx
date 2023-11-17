import socket

def get_local_ip_address():
    try:
        # Use a dummy socket to get the local IP address
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 0))  # Connect to a known external server
        local_ip_address = s.getsockname()[0]
        s.close()
        return local_ip_address
    except Exception as e:
        print(f"Error getting local IP address: {e}")
        return None

# Get the local IP address
ip_address = get_local_ip_address()

# Check if the IP address is obtained successfully
if ip_address:
    datasensor = {"ax": 500.244, "ay": -9.766, "az": 957.275, "asum": 1080.1457586441747, "lat": "0.000000", "lon": "0.000000"}

    # Add the IP address to the datasensor dictionary
    datasensor=json.loads(datasensor)
    datasensor["ip_address"] = ip_address

    # Now datasensor includes the correct IP address
    print(datasensor)
else:
    print("Failed to obtain the local IP address.")
