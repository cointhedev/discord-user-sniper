import os
import sys
from src.logger import *
from src.utils import getUsername, isTaken, check_proxies, check_token, TokenManager

os.system('cls' if os.name == 'nt' else 'clear')

print_header("Discord Username Sniper")
info("This tool will help you find a 3 character username on Discord!", 0.5)
warn("Make sure tokens.txt is configured correctly!", 0.5)
warn("Educational purposes only, btw. I'm not responsible for any misuse.", 0.5)
info(f"Made by {highlight('@coin.dev')}")
print_separator()

info("Checking proxies... (proxies.txt)")
working_proxies = check_proxies()
if working_proxies:
    success(f"Found {len(working_proxies)} working proxies!")
else:
    warn("No working proxies found. Running without proxies.")

token_manager = TokenManager()
current_token = token_manager.get_next_token(working_proxies[0] if working_proxies else None)

if not current_token:
    error("No valid tokens found in tokens.txt!")
    sys.exit()

token_info = check_token(current_token, working_proxies[0] if working_proxies else None)
success(f"Token loaded successfully!")
info(f"Logged in as: {highlight(token_info['username'])}#{token_info['discriminator']}")
if token_info['mfa_enabled']:
    warn("2FA is enabled on this account")

found = False
user = ""
proxy_index = 0

while not found:
    user = getUsername()
    
    current_proxy = None
    if working_proxies:
        current_proxy = working_proxies[proxy_index]
        proxy_index = (proxy_index + 1) % len(working_proxies)
    
    taken = isTaken(user, current_token, current_proxy)
    if taken == 200 or taken == 201: found = True
    if found: break
    if taken == "captcha" or taken == "locked":
        if taken == "captcha": 
            warn("Captcha detected! Rotating token and proxy...")
            token_manager.mark_token_captcha(current_token)
        if taken == "locked": 
            warn("Account locked! Rotating token and proxy...")
            token_manager.mark_token_locked(current_token)
            
        current_token = token_manager.get_next_token(current_proxy)
        if not current_token:
            error("No more valid tokens available! All tokens have been rate limited or locked.")
            sys.exit(1)
        token_info = check_token(current_token, current_proxy)
        info(f"Switched to: {highlight(token_info['username'])}#{token_info['discriminator']}")
        continue
    info(f"Username {user} is taken!")

if found: success(f"Username {user} isn't taken!!!!!!!!!!!!!!")