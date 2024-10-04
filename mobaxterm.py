import time
from pypresence import Presence  # Import the pypresence library
import psutil  # This library is used to check running processes

# Your Discord Application ID
APPLICATION_ID = 'discord_application_id'

# Create a presence object
rpc = Presence(APPLICATION_ID)
rpc.connect()  # Start the connection to Discord

# Get the current time
start_time = time.time()

# Function to check if MobaXterm is running
def is_mobaxterm_running():
    # Loop through running processes
    for process in psutil.process_iter(['pid', 'name']):
        if 'MobaXterm' in process.info['name']:
            return True
    return False

try:
    while True:
        if is_mobaxterm_running():
            # Update presence status when MobaXterm is running
            rpc.update(
                state="Using MobaXterm", 
                details="Probably either working for HPRC or playing around with Linux", 
                large_image="mobaxterm_icon",  # Image name from Discord Developer Portal
                large_text="MobaXterm Session",
                start=start_time  # This will start the timer from now
            )
        else:
            # Clear the presence if MobaXterm is not running
            rpc.clear()

        # Sleep for 15 seconds before checking again (Discord recommends a 15-second interval)
        time.sleep(15)

except Exception as e:
    print(f"An error occurred: {e}")
    rpc.clear()  # Clear the presence on exit
