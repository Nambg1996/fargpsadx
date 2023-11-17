import time
import subprocess
import networks  # Assuming networks is a module you've defined

script_name = "pushToremoteDatabase.py"
time.sleep(15)

while True:
    if networks.is_wifi_available():
        print("wifi is ok")
        time.sleep(5)
    else:
        print("Wi-Fi connection lost. Terminating {}...".format(script_name))
        try:
            
            subprocess.run(["pkill", "-f", script_name])
        except Exception as e:
            print(f"Error terminating process: {e}")

        print("Restarting {} in 5 seconds...".format(script_name))
        time.sleep(8)

        # Start the script again
        try:
            subprocess.Popen(["python3", script_name])  # Adjust the command as needed
            print("restart ok")
        except Exception as e:
            print(f"Error starting process: {e}")


