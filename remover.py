import os
import sys
import uuid
import base64
import random
import requests
import httpx
from os import system as sm
from sys import platform as pf
from time import sleep as sp
from urllib.parse import urlparse, parse_qs
from rich import print as rp
from rich.panel import Panel as pan

# Color Definitions
R = "[bold red]"
G = "[bold green]"
Y = "[bold yellow]"
B = "[bold blue]"
M = "[bold magenta]"
C = "[bold cyan]"
W = "[bold white]"

TOKEN_FILE = os.path.join(os.getcwd(), "accesstoken.txt")

def randc():
    return random.choice([R, G, Y, B, M, C])

def logo():
    rp(pan(f"""{randc()}
  ______________________________
 /  _____/\\_   _____/\\__    ___/
/   \\  ___ |    __)_   |    |   
\\    \\_\\  \\|        \\  |    |   
 \\______  /_______  /  |____|   
        \\/        \\/""", 
    title=f"{Y}FACEBOOK AUTOMATION SUITE", 
    subtitle=f"{R}DEVELOPED BY GABO",
    border_style="bold purple"))

def clear():
    sm('cls' if pf in ['win32', 'win64'] else 'clear')
    logo()

########################################################################
# Updated Token Getter Function with Correct Header for "User-Agent"
def get_fb_token(email, password):
    # Predefined access token for device-based login
    base_access_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
    
    data = {
        'adid': str(uuid.uuid4()),
        'format': 'json',
        'device_id': str(uuid.uuid4()),
        'credentials_type': 'device_based_login_password',
        'email': email,
        'password': password,
        'access_token': base_access_token,
        'generate_session_cookies': '1',
        'method': 'auth.login'
    }
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    
    try:
        response = httpx.post("https://b-graph.facebook.com/auth/login", headers=headers, data=data, timeout=30)
        if response.status_code == 200:
            result = response.json()
            if 'access_token' in result:
                return result['access_token']
            elif 'error' in result:
                rp(f"{R}Error: {result['error']['message']}")
        else:
            rp(f"{R}Failed: HTTP code {response.status_code}")
    except Exception as e:
        rp(f"{R}Connection Error: {str(e)}")
    
    return None

########################################################################
# Other Automation Functions

def extract_comment_id_from_url(url):
    """Extracts the comment ID from a Facebook comment URL"""
    try:
        parsed_url = urlparse(url)
        query_params = parse_qs(parsed_url.query)
        encoded_comment_id = query_params.get('comment_id', [None])[0]

        if not encoded_comment_id:
            raise ValueError("No comment_id found in the URL.")

        decoded_str = base64.b64decode(encoded_comment_id).decode('utf-8')
        return decoded_str.split("_")[-1]

    except Exception as e:
        rp(f"{R}Error extracting comment ID: {str(e)}")
        return None

def convert_post_link(url):
    """Converts a Facebook post URL to the proper ID format"""
    try:
        parsed_url = urlparse(url)
        path_parts = parsed_url.path.split('/')

        if 'posts' in path_parts:
            index = path_parts.index('posts')
            return f"{path_parts[index-1]}_{path_parts[index+1]}"
        elif 'story.php' in parsed_url.path:
            story_id = parse_qs(parsed_url.query).get('story_fbid', [None])[0]
            return f"{path_parts[1]}_{story_id}"
        return parsed_url.path.split('/')[-1]

    except Exception as e:
        rp(f"{R}Error converting post URL: {str(e)}")
        return None

def react_to_comment(access_token, comment_id, reaction_type="LIKE"):
    """Sends reaction to a Facebook comment"""
    try:
        url = f"https://graph.facebook.com/v19.0/{comment_id}/reactions"
        params = {
            "type": reaction_type,
            "access_token": access_token
        }
        response = requests.post(url, params=params)
        return response.json()
    except Exception as e:
        rp(f"{R}Error reacting to comment: {str(e)}")
        return None

def post_comment(access_token, post_id, message):
    """Posts a comment on a Facebook post"""
    try:
        url = f"https://graph.facebook.com/v19.0/{post_id}/comments"
        params = {
            "message": message,
            "access_token": access_token
        }
        response = requests.post(url, params=params)
        return response.json()
    except Exception as e:
        rp(f"{R}Error posting comment: {str(e)}")
        return None

def follow_user(access_token, user_id):
    """Subscribes to a Facebook user's updates"""
    try:
        url = f"https://graph.facebook.com/v19.0/{user_id}/subscribers"
        params = {
            "access_token": access_token
        }
        response = requests.post(url, params=params)
        return response.json()
    except Exception as e:
        rp(f"{R}Error subscribing to user: {str(e)}")
        return None

def unfollow_user(access_token, user_id):
    """Unsubscribes from a Facebook user's updates"""
    try:
        url = f"https://graph.facebook.com/v19.0/{user_id}/subscribers"
        params = {
            "access_token": access_token
        }
        response = requests.delete(url, params=params)
        return response.json()
    except Exception as e:
        rp(f"{R}Error unsubscribing from user: {str(e)}")
        return None

def extract_user_id_from_url(url):
    """Extracts the user ID from a Facebook profile URL"""
    try:
        parsed_url = urlparse(url)
        query_params = parse_qs(parsed_url.query)
        user_id = query_params.get('id', [None])[0]

        if not user_id:
            raise ValueError("No user ID found in the URL.")

        return user_id

    except Exception as e:
        rp(f"{R}Error extracting user ID: {str(e)}")
        return None

def share_post(access_token, post_id):
    """Shares a Facebook post using the /me/feed endpoint."""
    try:
        url = f"https://graph.facebook.com/v19.0/me/feed"
        params = {
            "link": f"https://www.facebook.com/{post_id}",
            "access_token": access_token
        }
        response = requests.post(url, params=params)
        if response.status_code != 200:
            rp(f"{R}Failed to share post: {response.json()}")
        return response.json()
    except Exception as e:
        rp(f"{R}Error sharing post: {str(e)}")
        return None

########################################################################
# User Interface Functions

def main_menu():
    clear()
    rp(pan(f"""{Y}[1]{G} Token Getter (Email & Password)
{Y}[2]{G} Auto Post Reaction
{Y}[3]{G} Auto Comment Reaction
{Y}[4]{G} Auto Post Comment
{Y}[5]{G} Auto Follow User
{Y}[6]{G} Auto Unfollow User
{Y}[7]{G} Auto Share Post
{Y}[8]{R} Exit""", 
    border_style="bold purple"))
    return input(f"{C}Choose option: {Y}")

def read_access_token():
    # Now uses the TOKEN_FILE in the current directory
    try:
        with open(TOKEN_FILE, 'r') as f:
            return f.read().strip()
    except Exception as e:
        rp(f"{R}Error reading access token: {str(e)}")
        return None

def save_access_token(token):
    try:
        with open(TOKEN_FILE, 'w') as f:
            f.write(token)
    except Exception as e:
        rp(f"{R}Error saving access token: {str(e)}")

def token_getter_flow():
    clear()
    email = input(f"{C}Enter Facebook Email/ID: {Y}")
    password = input(f"{C}Enter Password: {Y}")
    token = get_fb_token(email, password)
    clear()
    if token:
        # Save the token to file so other flows can access it
        save_access_token(token)
        rp(pan(f"{G}Token obtained successfully!", border_style="bold green"))
        rp(f"{C}{token}")
    else:
        rp(pan(f"{R}Failed to obtain token!", border_style="bold red"))
    input(f"{C}\nPress Enter to return to main menu...")

def auto_post_reaction_flow():
    clear()
    token = read_access_token()
    if not token:
        rp(f"{R}No access token found. Please obtain one first (Option 1).")
        input(f"{C}Press Enter to return to main menu...")
        return

    post_link = input(f"{C}Enter post URL: {Y}")
    reaction_type = input(f"{C}Reaction type (LIKE/LOVE/HAHA/WOW/SAD/ANGRY): {Y}").upper()
    count = int(input(f"{C}How many times do you want to react? {Y}"))

    post_id = convert_post_link(post_link)
    if not post_id:
        rp(f"{R}Invalid post URL!")
        input(f"{C}Press Enter to return to main menu...")
        return

    for _ in range(count):
        try:
            url = f"https://graph.facebook.com/v19.0/{post_id}/reactions"
            params = {
                "type": reaction_type,
                "access_token": token
            }
            response = requests.post(url, params=params)
            if response.status_code == 200:
                rp(f"{G}Successfully reacted to post!")
            else:
                error = response.json().get('error', {}).get('message', 'Unknown error')
                rp(f"{R}Failed: {error}")
            sp(1)
        except Exception as e:
            rp(f"{R}Error: {str(e)}")
    
    input(f"{C}Press Enter to continue...")

def auto_comment_reaction_flow():
    clear()
    token = read_access_token()
    if not token:
        rp(f"{R}No access token found. Please obtain one first (Option 1).")
        input(f"{C}Press Enter to return to main menu...")
        return

    comment_link = input(f"{C}Enter comment URL: {Y}")
    reaction_type = input(f"{C}Reaction type (LIKE/LOVE/HAHA/WOW/SAD/ANGRY): {Y}").upper()
    count = int(input(f"{C}How many times do you want to react? {Y}"))

    comment_id = extract_comment_id_from_url(comment_link)
    if not comment_id:
        rp(f"{R}Invalid comment URL!")
        input(f"{C}Press Enter to return to main menu...")
        return

    for _ in range(count):
        result = react_to_comment(token, comment_id, reaction_type)
        if result and 'success' in result:
            rp(f"{G}Successfully reacted to comment!")
        else:
            rp(f"{R}Failed to react to comment!")
        sp(1)

    input(f"{C}Press Enter to continue...")

def auto_post_comment_flow():
    clear()
    token = read_access_token()
    if not token:
        rp(f"{R}No access token found. Please obtain one first (Option 1).")
        input(f"{C}Press Enter to return to main menu...")
        return

    post_link = input(f"{C}Enter post URL: {Y}")
    message = input(f"{C}Enter comment message: {Y}")
    count = int(input(f"{C}How many times do you want to post this comment? {Y}"))

    post_id = convert_post_link(post_link)
    if not post_id:
        rp(f"{R}Invalid post URL!")
        input(f"{C}Press Enter to return to main menu...")
        return

    for _ in range(count):
        result = post_comment(token, post_id, message)
        if result and 'id' in result:
            rp(f"{G}Successfully posted comment!")
        else:
            rp(f"{R}Failed to post comment!")
        sp(1)

    input(f"{C}Press Enter to continue...")

def auto_follow_user_flow():
    clear()
    token = read_access_token()
    if not token:
        rp(f"{R}No access token found. Please obtain one first (Option 1).")
        input(f"{C}Press Enter to return to main menu...")
        return

    profile_url = input(f"{C}Enter profile URL: {Y}")
    user_id = extract_user_id_from_url(profile_url)
    if not user_id:
        rp(f"{R}Invalid profile URL!")
        input(f"{C}Press Enter to return to main menu...")
        return

    count = int(input(f"{C}How many times do you want to subscribe to this user? {Y}"))

    for _ in range(count):
        result = follow_user(token, user_id)
        if result and 'success' in result:
            rp(f"{G}Successfully subscribed to user!")
        else:
            rp(f"{R}Failed to subscribe to user!")
        sp(1)

    input(f"{C}Press Enter to continue...")

def auto_unfollow_user_flow():
    clear()
    token = read_access_token()
    if not token:
        rp(f"{R}No access token found. Please obtain one first (Option 1).")
        input(f"{C}Press Enter to return to main menu...")
        return

    profile_url = input(f"{C}Enter profile URL: {Y}")
    user_id = extract_user_id_from_url(profile_url)
    if not user_id:
        rp(f"{R}Invalid profile URL!")
        input(f"{C}Press Enter to return to main menu...")
        return

    count = int(input(f"{C}How many times do you want to unsubscribe from this user? {Y}"))

    for _ in range(count):
        result = unfollow_user(token, user_id)
        if result and 'success' in result:
            rp(f"{G}Successfully unsubscribed from user!")
        else:
            rp(f"{R}Failed to unsubscribe from user!")
        sp(1)

    input(f"{C}Press Enter to continue...")

def auto_share_post_flow():
    clear()
    token = read_access_token()
    if not token:
        rp(f"{R}No access token found. Please obtain one first (Option 1).")
        input(f"{C}Press Enter to return to main menu...")
        return

    post_link = input(f"{C}Enter post URL: {Y}")
    count = int(input(f"{C}How many times do you want to share this post? {Y}"))

    post_id = convert_post_link(post_link)
    if not post_id:
        rp(f"{R}Invalid post URL!")
        input(f"{C}Press Enter to return to main menu...")
        return

    for _ in range(count):
        result = share_post(token, post_id)
        if result and 'id' in result:
            rp(f"{G}Successfully shared post!")
        else:
            rp(f"{R}Failed to share post!")
        sp(1)

    input(f"{C}Press Enter to continue...")

########################################################################
# Main Loop

if __name__ == "__main__":
    while True:
        option = main_menu()
        if option == '1':
            token_getter_flow()
        elif option == '2':
            auto_post_reaction_flow()
        elif option == '3':
            auto_comment_reaction_flow()
        elif option == '4':
            auto_post_comment_flow()
        elif option == '5':
            auto_follow_user_flow()
        elif option == '6':
            auto_unfollow_user_flow()
        elif option == '7':
            auto_share_post_flow()
        elif option == '8':
            rp(f"{G}Exiting the program. Goodbye!")
            break
        else:
            rp(f"{R}Invalid option! Please try again.")
