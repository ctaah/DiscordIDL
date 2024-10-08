import os
import requests
from datetime import datetime, timezone
import colorama

# Replace with your APP token
TOKEN = '0000000000000000000000000000000000000000000000000000000000000'

def format_timestamp(timestamp):
    dt = datetime.fromtimestamp(timestamp, tz=timezone.utc)
    return dt.strftime("%d/%m/%Y %H:%M GMT+0")

def fetch_user_info(user_id):
    headers = {
        "Authorization": f"Bot {TOKEN}",
        "Content-Type": "application/json"
    }
    response = requests.get(f"https://discord.com/api/v10/users/{user_id}", headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

def display_user_info(user_data):
    user_name = user_data.get("username", "Unknown")
    discriminator = user_data.get("discriminator", "Unknown")
    user_id = user_data.get("id", "Unknown")
    created_at = ((int(user_id) >> 22) + 1420070400000) / 1000

    print(f"{colorama.Fore.YELLOW}--- User Information ---{colorama.Fore.RESET}")
    print(f"{colorama.Fore.YELLOW}Name: {colorama.Fore.WHITE}{user_name}#{discriminator}")
    print(f"{colorama.Fore.YELLOW}ID: {colorama.Fore.WHITE}{user_id}")
    print(f"{colorama.Fore.YELLOW}Created At: {colorama.Fore.WHITE}{format_timestamp(created_at)}")

    avatar_hash = user_data.get("avatar")
    banner_hash = user_data.get("banner")

    if avatar_hash:
        avatar_url = f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_hash}.png"
        print(f"{colorama.Fore.YELLOW}Avatar URL: {colorama.Fore.WHITE}{avatar_url}")
    else:
        print(f"{colorama.Fore.YELLOW}Avatar: {colorama.Fore.WHITE}No avatar")

    if banner_hash:
        banner_url = f"https://cdn.discordapp.com/banners/{user_id}/{banner_hash}.png"
        print(f"{colorama.Fore.YELLOW}Banner URL: {colorama.Fore.WHITE}{banner_url}")
    else:
        print(f"{colorama.Fore.YELLOW}Banner: {colorama.Fore.WHITE}No banner")

def initialize():
    while True:
        os.system('cls' if os.name == "nt" else "clear")
        print(f"{colorama.Fore.YELLOW}=== Discord User Info Fetcher ==={colorama.Fore.RESET}")

        user_id = input(f"{colorama.Fore.YELLOW}Enter the User ID >>> {colorama.Fore.WHITE}")

        if not user_id.isdigit():
            print(f"{colorama.Back.RED} {colorama.Fore.WHITE}[-] Invalid User ID!{colorama.Back.RESET}")
            input(f"{colorama.Fore.YELLOW}Press Enter to continue...{colorama.Fore.RESET}")
            continue

        user_data = fetch_user_info(user_id)

        if user_data:
            display_user_info(user_data)
            print(f"{colorama.Back.YELLOW} {colorama.Fore.WHITE}[+] User info fetched successfully!{colorama.Back.RESET}")
        else:
            print(f"{colorama.Back.RED} {colorama.Fore.WHITE}[-] User not found or an error occurred!{colorama.Back.RESET}")
        
        input(f"{colorama.Fore.YELLOW}Press Enter to continue...{colorama.Fore.RESET}")

if __name__ == '__main__':
    os.system('title Discord User Info Fetcher')
    colorama.init()
    initialize()
