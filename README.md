# MobaXterm as Discord Activity

This project allows you to display custom Discord Activity information when using **MobaXterm**, a popular terminal software. It integrates with the Discord Rich Presence API to show details like the current session type (e.g., SSH/Telnet) and the time spent in the session. The presence can be customized to include images and descriptions that update dynamically as you use MobaXterm.

## Features

- **Rich Presence Integration**: Display real-time session information such as "Using MobaXterm."
- **Customizable Display**: Add images, detailed descriptions, and even track the time you've spent in a session.
- **Works with Virtual Environments**: Leverages Python and `pypresence` to interact with Discord’s API.

## Requirements

- **Python 3.6+**
- **Discord desktop client** (must be running)
- **MobaXterm** installed and in use

### Python Packages

Install the following Python packages within a virtual environment:

- `pypresence`
- `psutil`

To install these dependencies, use the following command:

```bash
pip install pypresence psutil
```

## Installation and Setup

### ⚠️ Warning: WSL Won't Work

This script won't work in **WSL** because Discord Rich Presence requires the Discord client to be running on the same platform as the script. ```pypresence``` is not able to detect Discord from WSL environment. This is because WSL is a separate environment from Windows, and pypresence attempts to find Discord via inter-process communication (IPC), which cannot cross from WSL to Windows.

Please follow the steps below to run the script in a **Windows environment**.

If you're using PowerShell, you'll need to bypass the execution policy to activate the virtual environment:

1. Open **Windows PowerShell** as an Administrator.
2. Run the following command to temporarily bypass the execution policy:

   ```bash
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
    ```

Then, follow the step below to run the script.

### 1. Clone the Repository

First, clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/mobaxterm_discord_extension.git
cd mobaxterm_discord_extension
```

### 2. Create and Activate a Virtual Environment

Windows: Open Command Prompt and run

```bash
python -m venv mobaxterm_pypresence
mobaxterm_pypresence\Scripts\activate.bat
```

### 3. Install Required Dependencies

Once the virtual environment is activated, install the necessary Python packages:

```bash
pip install pypresence psutil
```

### 4. Configure Discord Rich Presence

Go to the Discord Developer Portal and create a new application.
Navigate to Rich Presence > Art Assets and upload any images you'd like to use.
Copy the Application ID of the application.

### 5. Update the Python Script

Edit mobaxterm.py and replace 'your_application_id' with your actual **Application ID** from the Discord Developer Portal:

```bash
APPLICATION_ID = 'your_application_id'
```

You can also customize the details and large image for the presence:

```bash
rpc.update(
    state="Probably either working for HPRC or playing around with Linux",
    details="Using MobaXterm",
    large_image="mobaxterm_icon",  # The asset name you uploaded
    large_text="MobaXterm Session",
    start=time.time() 
)
```

### 6. Run the Script

Make sure Discord is running on your machine, then run the script:

```bash
python mobaxterm.py
```
