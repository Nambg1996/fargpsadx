import subprocess


def is_wifi_available():
    try:
        response = subprocess.run(['ping', '-c', '1', 'www.google.com'], capture_output=True, text=True)
        return response.returncode == 0
    except subprocess.CalledProcessError:
        return False
    
def connect_to_wifi():
    ssid = "TYK_Network"  # Replace with your actual Wi-Fi SSID
    password = "x4RTA6Xn"  # Replace with your actual Wi-Fi password
    cmd = f"sudo nmcli dev wifi connect '{ssid}' password '{password}'"
    subprocess.run(cmd, shell=True)

    print("Wi-Fi connection established")
    
    
    
