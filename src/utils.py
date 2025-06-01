import random
import string
import requests
import concurrent.futures
from typing import List, Dict, Optional
import time

def getUsername() -> str:
    allowed_chars = string.ascii_lowercase + string.digits + '_' + '.'
    
    while True:
        username = ''.join(random.choices(allowed_chars, k=3))
        if '..' not in username:
            return username

def check_proxy(proxy: str) -> Dict:
    proxies = {
        'http': f'http://{proxy}',
        'https': f'http://{proxy}'
    }
    
    try:
        start_time = time.time()
        r = requests.get(
            'https://discord.com',
            proxies=proxies,
            timeout=10
        )
        response_time = time.time() - start_time
        
        if r.status_code == 200:
            return {
                'proxy': proxy,
                'working': True,
                'response_time': response_time
            }
    except:
        pass
    
    return {
        'proxy': proxy,
        'working': False,
        'response_time': 0
    }

def load_proxies() -> List[str]:
    try:
        with open('proxies.txt', 'r') as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return []

def check_proxies() -> List[Dict]:
    proxies = load_proxies()
    if not proxies:
        return []
    
    working_proxies = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        results = list(executor.map(check_proxy, proxies))
        working_proxies = [r for r in results if r['working']]

    working_proxies.sort(key=lambda x: x['response_time'])
    return working_proxies

def check_token(token: str, proxy: Optional[Dict] = None) -> Dict:
    headers = {
        "Authorization": token.strip(),
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    proxies = None
    if proxy:
        proxies = {
            'http': f'http://{proxy["proxy"]}',
            'https': f'http://{proxy["proxy"]}'
        }

    try:
        r = requests.get(
            'https://discord.com/api/v9/users/@me',
            headers=headers,
            proxies=proxies,
            timeout=10
        )
        
        if r.status_code == 200:
            data = r.json()
            return {
                'valid': True,
                'username': data.get('username'),
                'discriminator': data.get('discriminator'),
                'email': data.get('email'),
                'phone': data.get('phone'),
                'mfa_enabled': data.get('mfa_enabled', False)
            }
    except:
        pass
    
    return {
        'valid': False,
        'username': None,
        'discriminator': None,
        'email': None,
        'phone': None,
        'mfa_enabled': False
    }

class TokenManager:
    def __init__(self):
        self.tokens: List[Dict] = []
        self.current_index = 0
        
    def load_tokens(self) -> List[Dict]:
        try:
            with open('tokens.txt', 'r') as f:
                return [{'token': line.strip(), 'used': False, 'locked': False} for line in f if line.strip()]
        except FileNotFoundError:
            return []
            
    def get_next_token(self, proxy: Optional[Dict] = None) -> Optional[str]:
        if not self.tokens:
            self.tokens = self.load_tokens()
            
        for _ in range(len(self.tokens)):
            token_data = self.tokens[self.current_index]
            
            if token_data['used'] or token_data['locked']:
                self.current_index = (self.current_index + 1) % len(self.tokens)
                continue
                
            token_info = check_token(token_data['token'], proxy)
            
            if token_info['valid']:
                return token_data['token']

            self.current_index = (self.current_index + 1) % len(self.tokens)
            
        return None
        
    def mark_token_captcha(self, token: str):
        for token_data in self.tokens:
            if token_data['token'] == token:
                token_data['used'] = True
                break
        
        self.current_index = (self.current_index + 1) % len(self.tokens)
        
    def mark_token_locked(self, token: str):
        for token_data in self.tokens:
            if token_data['token'] == token:
                token_data['locked'] = True
                break
        
        self.current_index = (self.current_index + 1) % len(self.tokens)

def isTaken(user: str, token: str, proxy: Optional[Dict] = None) -> int:
    api = "https://discord.com/api/v9/users/@me/relationships"
    headers = {
        "Authorization": token.strip(),
        "Content-Type": "application/json",
        "User-Agent": "idk bro",
    }
    jsonData = {
        'username': user,
        'discriminator': None
    }

    proxies = None
    if proxy:
        proxies = {
            'http': f'http://{proxy["proxy"]}',
            'https': f'http://{proxy["proxy"]}'
        }

    r = requests.post(api, json=jsonData, headers=headers, proxies=proxies, timeout=10)

    
    if "You need to verify your account in order to" in r.text: return "locked"
    if "captcha" in r.text: return "captcha"
    return r.status_code