import os
import requests
import random
import string
from concurrent.futures import ThreadPoolExecutor
import sys

# Color codes for aesthetics
RESET = '\033[0m'
LIGHT_GREEN = '\033[92m'
LIGHT_RED = '\033[91m'
LIGHT_YELLOW = '\033[93m'
LIGHT_CYAN = '\033[96m'
BOLD = '\033[1m'

# Ensure necessary directories and files exist
def ensure_directories():
    paths = [
        '/sdcard/BOOSTINGTOOL',
        '/sdcard/BOOSTINGTOOL/fra.txt',
        '/sdcard/BOOSTINGTOOL/rpa.txt',
        '/sdcard/BOOSTINGTOOL/frapage.txt',
        '/sdcard/BOOSTINGTOOL/rpapage.txt'
    ]
    for path in paths:
        if os.path.isdir(path):
            continue  # It's a directory
        elif os.path.isfile(path):
            continue  # The file already exists
        elif path.endswith(".txt"):
            with open(path, 'a'):  # Create file
                pass
        else:
            os.makedirs(path)  # Create directory

# Function to clear the terminal
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Display logo
def display_logo():
    logo = f"""
{BOLD}{LIGHT_GREEN}
██████╗  █████╗ ██╗   ██╗██╗     ██╗███╗   ██╗ ██████╗ 
██╔══██╗██╔══██╗██║   ██║██║     ██║████╗  ██║██╔════╝ 
██████╔╝███████║██║   ██║██║     ██║██╔██╗ ██║██║  ███╗
██╔═══╝ ██╔══██║██║   ██║██║     ██║██║╚██╗██║██║   ██║
██║       ██║  ██║╚██████╔╝███████╗██║ ╚████║╚██████╔╝
╚═╝       ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝  ╚═════╝ 
{RESET}
{LIGHT_CYAN}WELCOME TO THE TOKEN EXTRACTOR{RESET}
"""
    print(logo)

# Generate a random user agent string
def W_ueragnt():
    chrome_version = random.randint(80, 99)
    webkit_version = random.randint(500, 599)
    safari_version = random.randint(400, 499)
    windows_version = random.randint(8, 10)
    is_win64 = random.choice([True, False])
    
    if is_win64:
        user_agent = f'Mozilla/5.0 (Windows NT {windows_version}; Win64; x64) AppleWebKit/{webkit_version}.0 (KHTML, like Gecko) Chrome/{chrome_version}.0.0.0 Safari/{safari_version}.0'
    else:
        user_agent = f'Mozilla/5.0 (Windows NT {windows_version}; WOW64) AppleWebKit/{webkit_version}.0 (KHTML, like Gecko) Chrome/{chrome_version}.0.0.0 Safari/{safari_version}.0'
    return user_agent

# Generate random values for fbav, fbbv, fbrv, adid
def generate_random_values():
    fbav = f'{random.randint(111, 999)}.0.0.{random.randint(11, 99)}.{random.randint(111, 999)}'
    fbbv = str(random.randint(111111111, 999999999))
    fbrv = '0'
    random_seed = random.Random()
    adid = ''.join(random_seed.choices(string.hexdigits, k=16))
    return fbav, fbbv, fbrv, adid

# Main function to get the token
def auto_token_getter(uid, password):
    fbav, fbbv, fbrv, adid = generate_random_values()
    
    headers = {
        'user-agent': W_ueragnt(),
        'viewport-width': '847',
        'x-asbd-id': '129477',
        'x-fb-friendly-name': 'GroupCometJoinForumMutation',
        'x-fb-lsd': 'wGh6ACr3OJ2v2rPBdXy-1o',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    data = {
        'uid': uid,
        'password': password,
        'locale': 'en_SV',
        'client_country_code': 'SV',
        'fb_api_req_friendly_name': 'authenticate',
        'api_key': '882a8490361da98702bf97a021ddc14d',
        'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
        'fbav': fbav,
        'fbbv': fbbv,
        'fbrv': fbrv,
        'adid': adid
    }

    url = 'https://graph.facebook.com/auth/login'

    try:
        # Make the POST request
        response = requests.post(url, headers=headers, data=data)
        response_data = response.json()

        # Check for success and retrieve the token
        if response.ok and 'access_token' in response_data:
            print(f"{LIGHT_GREEN}(BOOST) SUCCESS EXTRACT - {uid}{RESET}")
            return response_data['access_token'], True
        else:
            print(f"{LIGHT_RED}(BOOST) FAILED EXTRACT - {uid}{RESET}")
            return None, False

    except requests.exceptions.RequestException as e:
        print(f"{LIGHT_RED}Request failed: {str(e)}{RESET}")
        return None, False

# Read credentials from the user-defined file path
def read_credentials(credentials_path):
    try:
        with open(credentials_path, 'r') as file:
            credentials = []
            for line in file:
                if '|' in line:
                    uid, password = line.strip().split('|', 1)
                    credentials.append((uid.strip(), password.strip()))
            return credentials
    except FileNotFoundError:
        print(f"{LIGHT_RED}Credential file not found. Please check the path and try again.{RESET}")
        return []

# Save extracted tokens to the selected path
def save_tokens(tokens, choice):
    save_paths = [
        '/sdcard/BOOSTINGTOOL/fra.txt',
        '/sdcard/BOOSTINGTOOL/rpa.txt',
        '/sdcard/BOOSTINGTOOL/frapage.txt',
        '/sdcard/BOOSTINGTOOL/rpapage.txt'
    ]
    
    if choice in range(1, 5):
        save_path = save_paths[choice - 1]
        with open(save_path, 'a') as f:
            for token in tokens:
                f.write(token + '\n')
        print(f"{LIGHT_GREEN}Tokens saved to {save_path}{RESET}")
    else:
        print(f"{LIGHT_RED}Invalid choice. Tokens not saved.{RESET}")

# Function to ask user if they want to return to the menu or exit
def return_to_menu():
    while True:
        choice = input(f"\n{LIGHT_YELLOW}Do you want to go back to the main menu? (yes/no): {RESET}").lower()
        if choice == 'yes':
            clear_terminal()
            main_menu()
            break
        elif choice == 'no':
            print(f"{LIGHT_CYAN}Exiting...{RESET}")
            break
        else:
            print(f"{LIGHT_RED}Invalid input. Please type 'yes' or 'no'.{RESET}")

# Check if the credentials path exists
def check_credentials_path(credentials_path):
    return os.path.exists(credentials_path)

# Main menu function
def main_menu():
    display_logo()
    print(f"{LIGHT_CYAN}1. Extract tokens from credentials file{RESET}")
    print(f"{LIGHT_CYAN}2. Exit{RESET}")

    choice = input(f"{LIGHT_YELLOW}Enter your choice (1 or 2): {RESET}")

    if choice == '1':
        clear_terminal()
        extract_tokens_process()
    elif choice == '2':
        print(f"{LIGHT_CYAN}Exiting...{RESET}")
    else:
        print(f"{LIGHT_RED}Invalid input. Please choose 1 or 2.{RESET}")
        return_to_menu()

# Process to extract tokens
def extract_tokens_process():
    # Prompt for the credentials file path
    credentials_path = input(f"{LIGHT_YELLOW}Enter the path to the credentials file (format: uid|PASSWORD): {RESET}")

    if not check_credentials_path(credentials_path):
        print(f"{LIGHT_RED}Credentials path does not exist. Please check the path.{RESET}")
        return

    clear_terminal()
    credentials = read_credentials(credentials_path)

    total_extracted = 0
    failed_total = 0
    success_total = 0
    tokens = []

    # Use ThreadPoolExecutor for faster processing
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(auto_token_getter, uid, password): (uid, password) for uid, password in credentials}

        for future in futures:
            token, success = future.result()
            if success:
                tokens.append(token)
                total_extracted += 1
                success_total += 1
            else:
                failed_total += 1

    print(f"\n{LIGHT_GREEN}TOTAL EXTRACTED: {total_extracted}{RESET}")
    print(f"{LIGHT_RED}FAILED TOTAL: {failed_total}{RESET}")
    print(f"{LIGHT_GREEN}SUCCESS TOTAL: {success_total}{RESET}")

    if tokens:
        print(f"\n{LIGHT_YELLOW}Choose where to save the tokens:{RESET}")
        print(f"{LIGHT_CYAN}1. FRA Accounts{RESET}")
        print(f"{LIGHT_CYAN}2. RPA Accounts{RESET}")
        print(f"{LIGHT_CYAN}3. FRA Pages{RESET}")
        print(f"{LIGHT_CYAN}4. RPA Pages{RESET}")

        save_choice = int(input(f"{LIGHT_YELLOW}Enter your choice (1-4): {RESET}"))
        save_tokens(tokens, save_choice)

    return_to_menu()

# Entry point of the script
if __name__ == "__main__":
    ensure_directories()
    clear_terminal()
    main_menu()
