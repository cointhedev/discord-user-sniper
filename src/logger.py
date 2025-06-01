from colorama import init, Fore, Style
import time

init()

def info(text: str, delay: float = 0) -> None:
    print(f"{Fore.GREEN}[*] {text}{Style.RESET_ALL}")
    if delay > 0:
        time.sleep(delay)

def warn(text: str, delay: float = 0) -> None:
    print(f"{Fore.YELLOW}[!] {text}{Style.RESET_ALL}")
    if delay > 0:
        time.sleep(delay)

def error(text: str, delay: float = 0) -> None:
    print(f"{Fore.RED}[!] {text}{Style.RESET_ALL}")
    if delay > 0:
        time.sleep(delay)

def success(text: str, delay: float = 0) -> None:
    print(f"{Fore.GREEN}[+] {text}{Style.RESET_ALL}")
    if delay > 0:
        time.sleep(delay)

def highlight(text: str, color: str = "cyan") -> str:
    color_map = {
        "cyan": Fore.CYAN,
        "yellow": Fore.YELLOW,
        "green": Fore.GREEN,
        "red": Fore.RED,
        "blue": Fore.BLUE,
        "magenta": Fore.MAGENTA
    }
    return f"{color_map.get(color.lower(), Fore.CYAN)}{text}{Style.RESET_ALL}"

def print_header(title: str) -> None:
    width = 60
    print(f"\n{Fore.CYAN}{Style.BRIGHT}╔{'═' * (width-2)}╗")
    print(f"║{Fore.YELLOW}  {title.center(width-6)}{Fore.CYAN}  ║")
    print(f"╚{'═' * (width-2)}╝{Style.RESET_ALL}\n")

def print_separator(char: str = "=", length: int = 60) -> None:
    print(f"\n{char * length}\n") 