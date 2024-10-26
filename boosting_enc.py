import os
import time
import requests
import random
import asyncio
import aiohttp
import uuid
from concurrent.futures import ThreadPoolExecutor, as_completed

# Define colors for output
# Reset color
RESET = "\033[0m"

# Regular colors
BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
MAGENTA = "\033[36m"
WHITE = "\033[37m"

# Bright colors
BRIGHT_BLACK = "\033[90m"
BRIGHT_RED = "\033[91m"
BRIGHT_GREEN = "\033[92m"
BRIGHT_YELLOW = "\033[93m"
BRIGHT_BLUE = "\033[94m"
BRIGHT_MAGENTA = "\033[95m"
BRIGHT_MAGENTA = "\033[96m"
BRIGHT_WHITE = "\033[97m"

MAX_WORKERS = 20  # Adjusted to your request for a thread pool size of 30

# Function to clear the terminal
def clear_terminal():
    os.system('clear')

ah = "xyva-"
imt = "-M4786=="
ak = " yva-"
myid = uuid.uuid4().hex[:10].upper()

async def key():
    key1 = open('/data/data/com.termux/files/usr/bin/.exca.txt', 'r').read()
    clear_terminal()
    logo()
    async with aiohttp.ClientSession() as sess:
        async with sess.get('https://github.com/EzekielClervo/isaac/blob/fcc1b7a61333cddf99b6ce3eb5e03cdf6509f6ce/Approval.txt') as appro:
            r1 = await appro.text()
            if key1 in r1:
                os.system('clear')
                print("Your Key Is Approved")
                time.sleep(3)  # Delay to show approval message
                return True  # Indicate approval
            else:
                os.system("clear")
                print("\t \033[1;32m First Get Approval\033[1;37m ")
                time.sleep(5)
                os.system("clear")
                logo()
                print("")
                print(" YOU HAVE TO GET APPROVE FIRST BEFORE USING IT")
                print("")
                print(" Your Key is Not Approved ")
                print("")
                print(" Your Key : " + ak + ah + key1)
                print("")
                input(" Press Enter To Send Key")
                time.sleep(3.5)
                os.system('xdg-open https://www.messenger.com/t/100065316414713')
                return False  # Indicate no approval

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

def auto_unsubscribe(access_token, target_id):
    headers = {
        'Authorization': f'Bearer {access_token}',
        'User-Agent': W_ueragnt(),
        'Content-Type': 'application/json'
    }

    url = f'https://graph.facebook.com/v14.0/{target_id}/subscribers'  # Correct endpoint for subscribers

    try:
        response = requests.delete(url, headers=headers)

        if response.status_code == 200:
            print(f"{YELLOW} SUCCESSFULLY | TARGET ID: {target_id} using token.{WHITE}")
            return True  # Indicate success
        else:
            response_data = response.json()
            print(f"{RED} FAILED | TARGET ID: {target_id}{WHITE}")
            return False  # Indicate failure

    except Exception as e:
        print(f"{RED}( BOOST ) ERROR WHILE UNSUBSCRIBING | TARGET ID: {target_id}{WHITE}")
        return False  # Indicate failure

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def logo():
    print(f"{BRIGHT_RED}═════════════════════════════════")    
    print(f" _____             __            ")
    print(f"  / ___/__ ____ ___ / /____ ____   ")
    print(f" / /__/ _ `/ -_|_-</ __/ -_) __/   ")
    print(f" \___/\_,_/\__/___/\__/\__/_/      ")
    print(f"{BRIGHT_RED}OWNER : CAESTER")
    print(f"{BRIGHT_RED}TYPE : FACEBOOK TOOL")
    print(f"{BRIGHT_RED}═════════════════════════════════{WHITE}")

def overview():
    clear_terminal()
    logo()
    print(f"{YELLOW}Overview:")
    print(f"{BRIGHT_BLUE}TOTAL RPA ACCOUNTS: {count_lines('/sdcard/BOOSTINGTOOL/rpa.txt')}")
    print(f"{BRIGHT_BLUE}TOTAL FRA ACCOUNTS: {count_lines('/sdcard/BOOSTINGTOOL/fra.txt')}")
    print(f"{BRIGHT_BLUE}TOTAL RPA PAGES: {count_lines('sdcard/BOOSTINGTOOL/rpapage.txt')}")
    print(f"{BRIGHT_BLUE}TOTAL FRA PAGES: {count_lines('sdcard/BOOSTINGTOOL/frapage.txt')}")

def count_lines(file_path):
    try:
        with open(file_path) as f:
            return sum(1 for line in f)
    except FileNotFoundError:
        return 0

def auto_react(post_ids, token_file, limit):
    def react_to_post(token, post_id, reaction):
        url = f"https://graph.facebook.com/{post_id}/reactions"
        response = requests.post(url, params={'access_token': token, 'type': reaction})
        
        if response.status_code == 200:
            print(f"{YELLOW}SUCCESSFUL | POST ID: {post_id}{WHITE}")
            return True
        else:
            print(f"{RED}FAILED | POST ID: {post_id}{WHITE} - {response.json().get('error', {}).get('message', 'Unknown error')}")
            return False

    try:
        with open(token_file, 'r') as file:
            tokens = file.read().splitlines()

        print(f"{YELLOW}Choose a reaction:")
        print("1. Like")
        print("2. Love")
        print("3. Wow")
        print("4. Haha")
        print("5. Sad")
        print("6. Angry")
        print("7. Care")
        chosen_reaction = input("Enter reaction type (1-7): ")
        
        reactions = ['LIKE', 'LOVE', 'WOW', 'HAHA', 'SAD', 'ANGRY', 'CARE']
        
        if chosen_reaction.isdigit() and 1 <= int(chosen_reaction) <= len(reactions):
            reaction = reactions[int(chosen_reaction) - 1]
        else:
            print(f"{RED}INVALID REACTION TYPE.{WHITE}")
            return

        success_count = 0
        failure_count = 0
        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            futures = [
                executor.submit(react_to_post, token, post_id.strip(), reaction)
                for token in tokens[:limit]
                for post_id in post_ids
            ]
            
            for future in as_completed(futures):
                if future.result():
                    success_count += 1
                else:
                    failure_count += 1

        print(f"{BRIGHT_BLUE}═════════════════════════════════")    
        print(f"{BRIGHT_BLUE}| COMPLETED: {success_count}  |")
        print(f"{BRIGHT_BLUE}| FAILED: {failure_count}     |")
        print(f"{BRIGHT_BLUE}═════════════════════════════════")    

    except Exception as e:
        print(f"{RED}[ERROR] {str(e)}{WHITE}")

import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

def auto_comment(post_ids, token_file, limit):
    def comment_on_post(token, post_id, comment):
        url = f"https://graph.facebook.com/{post_id}/comments"
        response = requests.post(url, params={'access_token': token, 'message': comment})
        if response.status_code == 200:
            print(f"{YELLOW}SUCCESSFUL | POST ID: {post_id}{WHITE}")
            return True
        else:
            error_message = response.json().get('error', {}).get('message', 'Unknown error')
            print(f"{RED}FAILED | POST ID: {post_id} - {error_message}{WHITE}")
            return False

    try:
        with open(token_file, 'r') as file:
            tokens = file.read().splitlines()

        comments = input(f"{YELLOW}ENTER YOUR COMMENTS (separate by commas): ").split(',')
        target_count = int(input(f"{YELLOW}ENTER TARGET COMMENT COUNT PER POST: {WHITE}"))

        # Limit the number of tokens used
        tokens = tokens[:min(limit, len(tokens))]

        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            success_count = 0
            futures = []

            for post_id in post_ids:
                post_comment_count = 0
                while post_comment_count < target_count:
                    for token in tokens:
                        comment = comments[post_comment_count % len(comments)].strip()  # Cycle through comments
                        futures.append(executor.submit(comment_on_post, token, post_id, comment))
                        post_comment_count += 1
                        if post_comment_count >= target_count:
                            break  # Stop if target count is reached

            success_count = 0
            failure_count = 0
            for future in as_completed(futures):
                if future.result():
                    success_count += 1
                else:
                    failure_count += 1

            print(f"{BRIGHT_BLUE}═════════════════════════════════")    
            print(f"| COMPLETED: {success_count}  |")
            print(f"| FAILED: {failure_count}     |")
            print(f"{BRIGHT_BLUE}═════════════════════════════════")    

    except Exception as e:
        print(f"{BRIGHT_BLUE}[ERROR] {str(e)}{WHITE}")

def auto_react_to_comments(post_ids, token_file, limit, reaction_type):
    def react_to_comment(token, comment_id):
        url = f"https://graph.facebook.com/{comment_id}/reactions"
        payload = {
            'access_token': token,
            'type': reaction_type  # The type of reaction, e.g., 'LIKE', 'LOVE', etc.
        }
        response = requests.post(url, params=payload)
        if response.status_code == 200:
            print(f"{YELLOW}SUCCESSFUL | COMMENT ID: {comment_id}{WHITE}")
            return True
        else:
            print(f"{RED}FAILED | COMMENT ID: {comment_id}{WHITE}")
            return False

    try:
        with open(token_file, 'r') as file:
            tokens = file.read().splitlines()

        # Here you should collect comments from each post_id
        comments_to_react_to = []
        for post_id in post_ids:
            # Fetch comments for the post
            comments_url = f"https://graph.facebook.com/{post_id}/comments"
            for token in tokens:
                response = requests.get(comments_url, params={'access_token': token})
                if response.status_code == 200:
                    comments_data = response.json().get('data', [])
                    comments_to_react_to.extend(comment['id'] for comment in comments_data)

        # Limit the number of tokens to use
        tokens_to_use = tokens[:limit] if limit < len(tokens) else tokens

        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            futures = []
            for token in tokens_to_use:
                for comment_id in comments_to_react_to:
                    futures.append(executor.submit(react_to_comment, token, comment_id))

            success_count = 0
            failure_count = 0
            
            # Collect results from futures
            for future in as_completed(futures):
                if future.result():
                    success_count += 1
                else:
                    failure_count += 1

            print(f"{BRIGHT_BLUE}═════════════════════════════════")    
            print(f"| COMPLETED: {success_count}  |")
            print(f"| FAILED: {failure_count}     |")
            print(f"{BRIGHT_BLUE}═════════════════════════════════")    

    except Exception as e:
        print(f"{BRIGHT_BLUE}[ERROR] {str(e)}{WHITE}")
def auto_follow(user_ids, token_file, limit):
    def follow_user(token, user_id):
        url = f"https://graph.facebook.com/v19.0/{user_id}/subscribers"
        response = requests.post(url, headers={'Authorization': f'Bearer {token}'})
        if response.status_code == 200:
            print(f"{YELLOW}SUCCESSFUL FOLLOW | USER ID: {user_id}{WHITE}")
            return True
        else:
            print(f"{RED}FAILED TO FOLLOW | USER ID: {user_id}{WHITE}")
            return False

    try:
        with open(token_file, 'r') as file:
            tokens = file.read().splitlines()

        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            futures = []
            for token in tokens[:limit]:
                for user_id in user_ids:
                    futures.append(executor.submit(follow_user, token, user_id.strip()))  # Strip whitespace from user IDs

            success_count = 0
            failure_count = 0
            for future in as_completed(futures):
                if future.result():
                    success_count += 1
                else:
                    failure_count += 1

            print(f"{BRIGHT_BLUE}═════════════════════════════════")    
            print(f"{BRIGHT_BLUE}| COMPLETED: {success_count}  |")
            print(f"{BRIGHT_BLUE}| FAILED: {failure_count}     |")
            print(f"{BRIGHT_BLUE}═════════════════════════════════")    

    except Exception as e:
        print(f"{BRIGHT_BLUE}[ERROR] {str(e)}{WHITE}")

def choose_token_file():
    clear_terminal()
    print(f"{BRIGHT_BLUE}Choose a token file to use:{WHITE}")
    print(f"{BRIGHT_BLUE}═════════════════════════════════")    
    print(f"{BRIGHT_BLUE}1. /sdcard/BOOSTINGTOOL/RPA.TXT")
    print(f"{BRIGHT_BLUE}═════════════════════════════════")    
    print(f"{BRIGHT_BLUE}2. /sdcard/BOOSTINGTOOL/FRA.TXT")
    print(f"{BRIGHT_BLUE}═════════════════════════════════")    
    print(f"{BRIGHT_BLUE}3. /sdcard/BOOSTINGTOOL/RPAPAGE.TXT")
    print(f"{BRIGHT_BLUE}═════════════════════════════════")    
    print(f"{BRIGHT_BLUE}4. /sdcard/BOOSTINGTOOL/FRAPAGE.TXT")

    choice = input("Choose an option (1-4): ")
    token_files = {
        '1': '/sdcard/BOOSTINGTOOL/rpa.txt',
        '2': '/sdcard/BOOSTINGTOOL/fra.txt',
        '3': '/sdcard/BOOSTINGTOOL/rpapage.txt',
        '4': '/sdcard/BOOSTINGTOOL/frapage.txt'
    }

    return token_files.get(choice, None)

def main_menu():
    while True:
        clear_terminal()
        overview()
        print(f"{YELLOW}MAIN MENU{WHITE}")
        print(f"{BRIGHT_BLUE}1. AUTO FOLLOW")
        print(f"{BRIGHT_BLUE}2. AUTO REACT")
        print(f"{BRIGHT_BLUE}3. AUTO COMMENT")
        print(f"{BRIGHT_BLUE}4. AUTO COMMENT REACT")
        print(f"{BRIGHT_BLUE}5. AUTO UNSUBSCRIBE")  # New option for auto-unsubscribe
        print(f"{BRIGHT_BLUE}0. Exit")

        choice = input("CHOOSE AN OPTION: ")
        
        if choice == '0':
            print(f"{BRIGHT_BLUE}EXITING...{WHITE}")
            break

        token_file = choose_token_file()
        if not token_file:
            print(f"{BRIGHT_BLUE}INVALID SELECTION, RETURNING TO MAIN MENU...{WHITE}")
            continue

        if choice == '1':
            user_ids = input("Enter user IDs (comma-separated): ").split(',')
            limit = int(input("Enter limit for following: "))
            auto_follow(user_ids, token_file, limit)
        elif choice == '2':
            post_ids = input("ENTER POST IDS (comma-separated): ").split(',')
            limit = int(input("ENTER LIMIT FOR REACTIONS: "))
            auto_react(post_ids, token_file, limit)
        elif choice == '3':
            post_ids = input("ENTER POST IDS (comma-separated): ").split(',')
            limit = int(input("ENTER LIMIT FOR COMMENTS: "))
            auto_comment(post_ids, token_file, limit)
        elif choice == '4':
            post_ids = input("ENTER POST IDS (comma-separated): ").split(',')
            limit = int(input("ENTER LIMIT FOR COMMENT REACTIONS: "))
            auto_comment_react(post_ids, token_file, limit)
        elif choice == '5':
            target_ids = input("ENTER PAGE IDS TO UNSUBSCRIBE (comma-separated): ").split(',')
            limit = int(input("ENTER LIMIT FOR UNSUBSCRIBING: "))
            
            with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
                futures = []
                for token in open(token_file).read().splitlines()[:limit]:
                    for target_id in target_ids:
                        futures.append(executor.submit(auto_unsubscribe, token.strip(), target_id.strip()))

                success_count = 0
                failure_count = 0
                for future in as_completed(futures):
                    if future.result():
                        success_count += 1
                    else:
                        failure_count += 1

                print(f"{BRIGHT_BLUE}═════════════════════════════════")    
                print(f"{BRIGHT_BLUE}| COMPLETED: {success_count}  |")
                print(f"{BRIGHT_BLUE}| FAILED: {failure_count}     |")
                print(f"{BRIGHT_BLUE}═════════════════════════════════")    

        else:
            print(f"{RED}INVALID OPTION! PLEASE TRY AGAIN.{WHITE}")

        # Prompt user if they want to go back to the main menu
        go_back = input(f"{YELLOW}Do you want to return to the main menu? (y/n): ").strip().lower()
        if go_back != 'y':
            print(f"{GREEN}EXITING...{WHITE}")
            break
            

async def main():
    clear_terminal()
    logo()
    is_approved = await key()
    if is_approved:
        clear_terminal()
        logo()
        await main_menu()
    else:
        print("Approval required to access commands.")
        await asyncio.sleep(0.5)

if __name__ == "__main__":
    asyncio.run(main())
