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
git clone https://github.com/cointhedev/token-checker.git
cd token-checker
```

### Method 2: Manual Download
1. Click the green "Code" button on this repository
2. Select "Download ZIP"
3. Extract the ZIP file to your desired location

### Next Steps
1. Make sure you have Python 3.8 or higher installed
   - Download from: https://www.python.org/downloads/
   - During installation, make sure to check "Add Python to PATH"

2. Create `tokens.txt` with your Discord tokens (one per line):
```
token1
token2
token3
```

3. (Optional) Create `proxies.txt` with your proxies (one per line):
```
ip:port
username:password@ip:port
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