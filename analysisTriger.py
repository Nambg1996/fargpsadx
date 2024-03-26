import requests
import time

url = "http://192.168.161.126/08.%20NAM_TEST/fargpsadx/server/pageSecond/analysisOperatingTimeEveryday.php"

# Data to be sent in the POST request
data = {'data': ''}  # Assuming 'data' is the key you are using in your PHP script

def triggerAnalysisPerDay(url, data):
    """
    Triggers the analysis per day by sending a POST request to the specified URL.

    Parameters:
    - url (str): The URL to send the POST request to.
    - data (dict): The data payload for the request.

    Returns:
    None
    """
    try:
        response = requests.post(url, data=data)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            print("Page triggered successfully.")
        else:
            print(f"Failed to trigger the page. Status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        print("Failed to connect to the server. Will retry later.")

def scheduleTrigger(url, data, interval_minutes=10):
    """
    Schedules the triggerAnalysisPerDay function to run every specified interval.

    Parameters:
    - url (str): The URL to send the POST request to.
    - data (dict): The data payload for the request.
    - interval_minutes (int): The interval in minutes between each execution.

    Returns:
    None
    """

    while True:
        try:
            triggerAnalysisPerDay(url, data)
        except Exception as e:
            print(f"An error occurred during execution: {e}")
        time.sleep(interval_minutes * 60)  # Convert minutes to seconds

scheduleTrigger(url, data)
