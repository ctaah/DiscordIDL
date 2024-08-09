import os
import time
import requests
import colorama
from datetime import datetime, timezone

# bot token
TOKEN = ''

def format_timestamp(timestamp):
    """Convert the Discord timestamp to a readable format."""
    dt = datetime.fromtimestamp(timestamp, tz=timezone.utc)
    return dt.strftime("%d/%m/%Y %H:%M GMT+0")

def fetch_user_info(user_id):
    """Fetch user information from Discord API using bot token."""
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
    """Display user information."""
    user_name = user_data.get("username", "Unknown")
    discriminator = user_data.get("discriminator", "Unknown")
    user_id = user_data.get("id", "Unknown")
    avatar_hash = user_data.get("avatar", None)
    banner_hash = user_data.get("banner", None)
    accent_color = user_data.get("accent_color", None)
    created_at = ((int(user_id) >> 22) + 1420070400000) / 1000

    print(f"{colorama.Fore.MAGENTA}--- User Information ---{colorama.Fore.RESET}")
    print(f"{colorama.Fore.MAGENTA}Name: {colorama.Fore.WHITE}{user_name}#{discriminator}")
    print(f"{colorama.Fore.MAGENTA}ID: {colorama.Fore.WHITE}{user_id}")
    print(f"{colorama.Fore.MAGENTA}Created At: {colorama.Fore.WHITE}{format_timestamp(created_at)}")

    if accent_color:
        print(f"{colorama.Fore.MAGENTA}Profile Color: {colorama.Fore.WHITE}#{accent_color:06X}")
    else:
        print(f"{colorama.Fore.MAGENTA}Profile Color: {colorama.Fore.WHITE}None")

    if avatar_hash:
        avatar_url = f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_hash}.png"
        print(f"{colorama.Fore.MAGENTA}Avatar URL: {colorama.Fore.WHITE}{avatar_url}")
    else:
        print(f"{colorama.Fore.MAGENTA}Avatar: {colorama.Fore.WHITE}No avatar")

    if banner_hash:
        banner_url = f"https://cdn.discordapp.com/banners/{user_id}/{banner_hash}.png"
        print(f"{colorama.Fore.MAGENTA}Banner URL: {colorama.Fore.WHITE}{banner_url}")
    else:
        print(f"{colorama.Fore.MAGENTA}Banner: {colorama.Fore.WHITE}No banner")

def initialize():
    """Initialize the script."""
    while True:
        os.system('cls' if os.name == "nt" else "clear")
        print(rf"""{colorama.Fore.MAGENTA}
                   __           __                      __         
                  /\ \__       /\ \                    /\ \        
      ___   __  __\ \ ,_\    __\ \ \___     ___     ___\ \ \/'\    
     /'___\/\ \/\ \\ \ \/  /'__\ \  _ \  / __\  / __\ \ , <    
    /\ \__/\ \ \_\ \\ \ \_/\  __/\ \ \ \ \/\ \L\ \/\ \L\ \ \ \\\  
    \ \____\\ \____/ \ \__\ \____\\ \_\ \_\ \____/\ \____/\ \_\ \_\
     \/____/ \/___/   \/__/\/____/ \/_/\/_/\/___/  \/___/  \/_/\/_/
                                                          with <3
         """)
        
        user_id = input(f"{colorama.Fore.MAGENTA}Enter the User ID > {colorama.Fore.WHITE}")

        if not user_id.isdigit():
            print(f"{colorama.Back.RED} {colorama.Fore.WHITE}[-] Invalid User ID!{colorama.Back.RESET}")
            input(f"{colorama.Fore.MAGENTA}Press Enter to continue...{colorama.Fore.RESET}")
            continue

        user_data = fetch_user_info(user_id)

        if user_data:
            display_user_info(user_data)
            print(f"{colorama.Back.MAGENTA} {colorama.Fore.WHITE}[+] User info fetched successfully!{colorama.Back.RESET}")
        else:
            print(f"{colorama.Back.RED} {colorama.Fore.WHITE}[-] User not found or an error occurred!{colorama.Back.RESET}")
        
        input(f"{colorama.Fore.MAGENTA}Press Enter to continue...{colorama.Fore.RESET}")

if __name__ == '__main__':
    os.system('title cutehook on top LOL')
    os.system('cls' if os.name == "nt" else "clear")
    colorama.init()
    initialize()
