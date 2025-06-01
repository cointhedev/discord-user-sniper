# Discord Username Sniper

A tool to find available 3-character usernames on Discord.

## Features

- Checks for available 3-character usernames
- Supports multiple tokens with automatic rotation
- Proxy support with automatic rotation
- Handles rate limits and captchas
- Colored console output

## Setup

### Method 1: Clone Repository
1. Make sure you have Git installed
   - Download from: https://git-scm.com/downloads
2. Open terminal/command prompt and run:
```bash
git clone https://github.com/cointhedev/discord-user-sniper.git
cd discord-user-sniper
```

### Method 2: Manual Download
1. Click the green "Code" button on this repository
2. Select "Download ZIP"
3. Extract the ZIP file to your desired location

### Next Steps
1. Make sure you have Python 3.8 or higher installed
   - Download from: https://www.python.org/downloads/
   - During installation, make sure to check "Add Python to PATH"

2. Edit `tokens.txt` with your Discord tokens (one per line):
```
token1
token2
token3
```

3. (Optional) Edit `proxies.txt` with your proxies (one per line):
```
ip:port
username:password@ip:port
```

## Customization

### Changing Username Length
By default, the tool searches for 3-character usernames. To change this:

1. Open `src/utils.py`
2. Find the `getUsername()` function
3. Change `k=3` to your desired length (e.g., `k=4` for 4 characters)
4. Save the file and run the script

Example:
```python
def getUsername() -> str:
    allowed_chars = string.ascii_lowercase + string.digits + '_' + '.'
    
    while True:
        username = ''.join(random.choices(allowed_chars, k=4))  # Changed from k=3 to k=4
        if '..' not in username:
            return username
```

## Usage

### Windows Users
Simply double-click `start.bat` to run the script. The batch file will:
- Check if Python is installed
- Install required packages
- Run the script

### Manual Run
If you prefer to run manually or are on a different OS:

1. Install requirements:
```bash
pip install -r requirements.txt
```

2. Run the script:
```bash
python main.py
```

## Educational Purposes Only

This tool is for educational purposes only. Use responsibly and at your own risk.

## Author

Made by @coin.dev 