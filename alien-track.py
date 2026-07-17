#!/usr/bin/env python3

import json
import requests
import time
import os
import sys
import socket
import hashlib
from concurrent.futures import ThreadPoolExecutor, as_completed
import phonenumbers
from phonenumbers import carrier, geocoder, timezone
import whois
from pyfiglet import Figlet

# ─── Colors ────────────────────────────────────────────────────────────────
Bl = '\033[30m'
Re = '\033[1;31m'
Gr = '\033[1;32m'
Ye = '\033[1;33m'
Blu = '\033[1;34m'
Mage = '\033[1;35m'
Cy = '\033[1;36m'
Wh = '\033[1;37m'
Rs = '\033[0m'

# ─── Banner ────────────────────────────────────────────────────────────────
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    clear()
    fig = Figlet(font="slant")
    logo = fig.renderText("ALIEN TRACK").splitlines()
    print(f"{Wh}╔════════════════════════════════════════════════════════════════════╗")
    for line in logo:
        # Pad each line to 66 chars (logo may have trailing spaces)
        line = line.rstrip('\n')
        if len(line) < 66:
            line = line.ljust(66)
        else:
            line = line[:66]
        print(f"{Wh}║ {Cy}{line}{Wh}║")
    print(f"{Wh}║{'':68}║")
    print(f"{Wh}║      {Gr}OSINT Framework • v2.0{'':37}{Wh}║")
    print(f"{Wh}║      {Cy}Author: IamG2{'':45}{Wh}║")
    print(f"{Wh}╚════════════════════════════════════════════════════════════════════╝")

def decorator_banner(func):
    def wrapper(*args, **kwargs):
        banner()
        func(*args, **kwargs)
    return wrapper

# ─── Core Functions ────────────────────────────────────────────────────────

@decorator_banner
def ip_tracker():
    ip = input(f"\n{Wh}Enter target IP : {Gr}")
    print(f"\n {Wh}============= {Gr}IP ADDRESS INFORMATION {Wh}=============")
    try:
        resp = requests.get(f"http://ipwho.is/{ip}", timeout=8)
        data = resp.json()
        if not data.get('success', True):
            print(f"{Re}Error: {data.get('message', 'Unknown error')}")
            return
        print(f"{Wh}\n IP target       :{Gr} {ip}")
        print(f"{Wh} Type            :{Gr} {data.get('type', 'N/A')}")
        print(f"{Wh} Country         :{Gr} {data.get('country', 'N/A')}")
        print(f"{Wh} Country Code    :{Gr} {data.get('country_code', 'N/A')}")
        print(f"{Wh} Region          :{Gr} {data.get('region', 'N/A')}")
        print(f"{Wh} City            :{Gr} {data.get('city', 'N/A')}")
        print(f"{Wh} Postal          :{Gr} {data.get('postal', 'N/A')}")
        print(f"{Wh} Latitude        :{Gr} {data.get('latitude', 'N/A')}")
        print(f"{Wh} Longitude       :{Gr} {data.get('longitude', 'N/A')}")
        lat = data.get('latitude')
        lon = data.get('longitude')
        if lat and lon:
            print(f"{Wh} Google Maps     :{Gr} https://www.google.com/maps/@{lat},{lon},8z")
        print(f"{Wh} Timezone        :{Gr} {data.get('timezone', {}).get('id', 'N/A')}")
        print(f"{Wh} Current Time    :{Gr} {data.get('timezone', {}).get('current_time', 'N/A')}")
        print(f"{Wh} ISP             :{Gr} {data.get('connection', {}).get('isp', 'N/A')}")
        print(f"{Wh} Organisation    :{Gr} {data.get('connection', {}).get('org', 'N/A')}")
        print(f"{Wh} ASN             :{Gr} {data.get('connection', {}).get('asn', 'N/A')}")
        print(f"{Wh} Domain          :{Gr} {data.get('connection', {}).get('domain', 'N/A')}")
        print(f"{Wh} EU Member       :{Gr} {data.get('is_eu', 'N/A')}")
        print(f"{Wh} Flag            :{Gr} {data.get('flag', {}).get('emoji', 'N/A')}")
        print(f"{Wh} Capital         :{Gr} {data.get('capital', 'N/A')}")
        try:
            resp2 = requests.get(f"http://ip-api.com/json/{ip}?fields=status,proxy,hosting", timeout=5)
            data2 = resp2.json()
            if data2.get('status') == 'success':
                print(f"{Wh} Proxy/VPN       :{Gr} {'Yes' if data2.get('proxy', False) else 'No'}")
                print(f"{Wh} Hosting/Cloud   :{Gr} {'Yes' if data2.get('hosting', False) else 'No'}")
        except:
            pass
    except Exception as e:
        print(f"{Re}Error: {e}")

@decorator_banner
def show_my_ip():
    try:
        resp = requests.get('https://api.ipify.org/', timeout=5)
        my_ip = resp.text.strip()
        print(f"\n {Wh}========== {Gr}YOUR PUBLIC IP {Wh}==========")
        print(f"\n {Wh}[{Gr}+{Wh}] Your IP Address : {Gr}{my_ip}")
        print(f"\n {Wh}=======================================")
    except Exception as e:
        print(f"{Re}Error retrieving IP: {e}")

@decorator_banner
def phone_tracker():
    phone_input = input(f"\n{Wh}Enter phone number (e.g., +6281xxxxxxxxx) : {Gr}")
    default_region = "ID"
    try:
        parsed = phonenumbers.parse(phone_input, default_region)
        if not phonenumbers.is_valid_number(parsed):
            print(f"{Re}Invalid phone number.")
            return
        region_code = phonenumbers.region_code_for_number(parsed)
        provider = carrier.name_for_number(parsed, "en")
        location = geocoder.description_for_number(parsed, "id")
        timezones = timezone.time_zones_for_number(parsed)
        tz_str = ', '.join(timezones)
        print(f"\n {Wh}========== {Gr}PHONE NUMBER DETAILS {Wh}==========")
        print(f" {Wh}Location          :{Gr} {location}")
        print(f" {Wh}Region Code       :{Gr} {region_code}")
        print(f" {Wh}Timezone          :{Gr} {tz_str}")
        print(f" {Wh}Carrier/Operator  :{Gr} {provider if provider else 'Unknown'}")
        print(f" {Wh}Valid number      :{Gr} {phonenumbers.is_valid_number(parsed)}")
        print(f" {Wh}Possible number   :{Gr} {phonenumbers.is_possible_number(parsed)}")
        print(f" {Wh}International fmt :{Gr} {phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL)}")
        print(f" {Wh}E.164 format      :{Gr} {phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.E164)}")
        print(f" {Wh}National number   :{Gr} {parsed.national_number}")
        print(f" {Wh}Country code      :{Gr} {parsed.country_code}")
        num_type = phonenumbers.number_type(parsed)
        if num_type == phonenumbers.PhoneNumberType.MOBILE:
            print(f" {Wh}Type              :{Gr} Wireless/Mobile")
        elif num_type == phonenumbers.PhoneNumberType.FIXED_LINE:
            print(f" {Wh}Type              :{Gr} Landline")
        elif num_type == phonenumbers.PhoneNumberType.VOIP:
            print(f" {Wh}Type              :{Gr} VoIP")
        elif num_type == phonenumbers.PhoneNumberType.PAGER:
            print(f" {Wh}Type              :{Gr} Pager")
        elif num_type == phonenumbers.PhoneNumberType.PERSONAL_NUMBER:
            print(f" {Wh}Type              :{Gr} Personal number")
        else:
            print(f" {Wh}Type              :{Gr} Other/Unknown")
    except Exception as e:
        print(f"{Re}Error: {e}")

@decorator_banner
def username_tracker():
    raw_input = input(f"\n{Wh}Enter username, email, or path to file (one per line): {Gr}").strip()
    # Determine if it's a file
    if os.path.isfile(raw_input):
        with open(raw_input, 'r') as f:
            lines = [line.strip() for line in f if line.strip()]
        if not lines:
            print(f"{Re}File is empty.")
            return
        print(f"\n{Wh}[{Gr}+{Wh}] Processing {len(lines)} entries...")
        for entry in lines:
            process_single_username(entry)
        return
    else:
        process_single_username(raw_input)

def process_single_username(entry):
    # If entry contains '@', treat as email -> use local part
    if '@' in entry:
        username = entry.split('@')[0]
        print(f"\n{Wh}▶ Checking email: {Gr}{entry}{Wh} → using username: {Gr}{username}")
    else:
        username = entry
        print(f"\n{Wh}▶ Checking username: {Gr}{username}")

    sites = [
        ("Facebook", "https://www.facebook.com/{}"),
        ("Twitter", "https://www.twitter.com/{}"),
        ("Instagram", "https://www.instagram.com/{}"),
        ("LinkedIn", "https://www.linkedin.com/in/{}"),
        ("GitHub", "https://www.github.com/{}"),
        ("Pinterest", "https://www.pinterest.com/{}"),
        ("Tumblr", "https://www.tumblr.com/{}"),
        ("YouTube", "https://www.youtube.com/{}"),
        ("SoundCloud", "https://soundcloud.com/{}"),
        ("Snapchat", "https://www.snapchat.com/add/{}"),
        ("TikTok", "https://www.tiktok.com/@{}"),
        ("Medium", "https://medium.com/@{}"),
        ("Quora", "https://www.quora.com/profile/{}"),
        ("Flickr", "https://www.flickr.com/people/{}"),
        ("Twitch", "https://www.twitch.tv/{}"),
        ("Dribbble", "https://dribbble.com/{}"),
        ("Ello", "https://ello.co/{}"),
        ("ProductHunt", "https://www.producthunt.com/@{}"),
        ("Telegram", "https://t.me/{}"),
        ("Reddit", "https://www.reddit.com/user/{}"),
        ("Keybase", "https://keybase.io/{}"),
        ("Patreon", "https://www.patreon.com/{}"),
        ("VK", "https://vk.com/{}"),
        ("GitLab", "https://gitlab.com/{}"),
        ("BitBucket", "https://bitbucket.org/{}"),
        ("HackerNews", "https://news.ycombinator.com/user?id={}"),
        ("Vimeo", "https://vimeo.com/{}"),
        ("DeviantArt", "https://www.deviantart.com/{}"),
        ("Steam", "https://steamcommunity.com/id/{}"),
        ("Spotify", "https://open.spotify.com/user/{}"),
        ("Roblox", "https://www.roblox.com/user.aspx?username={}"),
        ("Pastebin", "https://pastebin.com/u/{}"),
        ("HackerRank", "https://www.hackerrank.com/{}"),
        ("Codewars", "https://www.codewars.com/users/{}"),
        ("LeetCode", "https://leetcode.com/{}"),
        ("CodePen", "https://codepen.io/{}"),
        ("Replit", "https://replit.com/@{}"),
        ("Gravatar", "https://en.gravatar.com/{}"),
        ("About.me", "https://about.me/{}"),
        ("Imgur", "https://imgur.com/user/{}"),
        ("Codecademy", "https://www.codecademy.com/profiles/{}"),
        ("TryHackMe", "https://tryhackme.com/p/{}"),
        ("HackTheBox", "https://www.hackthebox.com/home/users/profile/{}"),
        ("Coursera", "https://www.coursera.org/user/{}"),
        ("Udemy", "https://www.udemy.com/user/{}"),
    ]

    found = []
    not_found = []

    def check_site(name, url_template):
        try:
            url = url_template.format(username)
            resp = requests.get(url, timeout=5, headers={"User-Agent": "Mozilla/5.0"}, allow_redirects=False)
            if resp.status_code == 200:
                found.append((name, url))
            else:
                not_found.append(name)
        except:
            not_found.append(name)

    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = [executor.submit(check_site, name, url) for name, url in sites]
        for _ in as_completed(futures):
            pass

    if found:
        for name, url in found:
            print(f" {Wh}[{Gr}+{Wh}] {name} : {Gr}{url}")
    else:
        print(f"{Ye}No profiles found for '{username}'.")
    if not_found:
        print(f"\n{Wh}[{Ye}!{Wh}] {Ye}Could not find on: {', '.join(not_found[:5])}...")

@decorator_banner
def email_tracker():
    email = input(f"\n{Wh}Enter email address : {Gr}")
    print(f"\n {Wh}========== {Gr}EMAIL INTELLIGENCE {Wh}==========\n")
    def check_gravatar():
        try:
            email_hash = hashlib.md5(email.strip().lower().encode()).hexdigest()
            url = f"https://www.gravatar.com/avatar/{email_hash}?d=404&s=1"
            resp = requests.get(url, timeout=5, allow_redirects=False)
            if resp.status_code == 200:
                return ("Gravatar", "Profile exists (has avatar)")
            else:
                return ("Gravatar", "No Gravatar found")
        except:
            return ("Gravatar", "Check failed")
    def check_hibp():
        try:
            url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
            resp = requests.get(url, timeout=10)
            if resp.status_code == 200:
                data = resp.json()
                breaches = [b['Name'] for b in data]
                return ("HaveIBeenPwned", f"Found in {len(breaches)} breaches: {', '.join(breaches[:3])}")
            elif resp.status_code == 404:
                return ("HaveIBeenPwned", "No breaches found")
            else:
                return ("HaveIBeenPwned", f"API error (status {resp.status_code})")
        except:
            return ("HaveIBeenPwned", "Check failed")
    def check_emailrep():
        try:
            resp = requests.get(f"https://emailrep.io/{email}", timeout=10)
            if resp.status_code == 200:
                data = resp.json()
                if data.get('status') == 'success':
                    rep = data.get('reputation', 'unknown')
                    susp = data.get('suspicious', False)
                    mal = data.get('malicious', False)
                    breaches = data.get('breaches', 0)
                    details = data.get('details', {})
                    first = details.get('first_seen', 'N/A')
                    last = details.get('last_seen', 'N/A')
                    return ("EmailRep", f"Reputation: {rep}, Suspicious: {susp}, Malicious: {mal}, Breaches: {breaches}, First: {first}, Last: {last}")
                else:
                    return ("EmailRep", "No data")
            else:
                return ("EmailRep", f"API error (status {resp.status_code})")
        except:
            return ("EmailRep", "Check failed")
    def check_domain_whois():
        try:
            domain = email.split('@')[1]
            w = whois.whois(domain)
            if w:
                created = w.creation_date
                expiry = w.expiration_date
                registrar = w.registrar
                return ("Domain WHOIS", f"Registrar: {registrar}, Created: {created}, Expires: {expiry}")
            else:
                return ("Domain WHOIS", "No WHOIS data")
        except:
            return ("Domain WHOIS", "Check failed")
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [
            executor.submit(check_gravatar),
            executor.submit(check_hibp),
            executor.submit(check_emailrep),
            executor.submit(check_domain_whois)
        ]
        for f in as_completed(futures):
            try:
                service, info = f.result()
                print(f" {Wh}[{Gr}+{Wh}] {service} : {Gr}{info}")
            except:
                print(f" {Wh}[{Re}!{Wh}] {Re}Error in one check")
    print()

@decorator_banner
def domain_whois():
    domain = input(f"\n{Wh}Enter domain (e.g., example.com) : {Gr}")
    print(f"\n {Wh}========== {Gr}WHOIS INFORMATION {Wh}==========")
    try:
        w = whois.whois(domain)
        if not w:
            print(f"{Re}No WHOIS data found.")
            return
        print(f"{Wh}Domain Name      :{Gr} {w.domain_name}")
        print(f"{Wh}Registrar        :{Gr} {w.registrar}")
        print(f"{Wh}Creation Date    :{Gr} {w.creation_date}")
        print(f"{Wh}Expiration Date  :{Gr} {w.expiration_date}")
        print(f"{Wh}Updated Date     :{Gr} {w.updated_date}")
        print(f"{Wh}Name Servers     :{Gr} {', '.join(w.name_servers) if w.name_servers else 'N/A'}")
        print(f"{Wh}Registrant       :{Gr} {w.registrant}")
        print(f"{Wh}Admin Email      :{Gr} {w.emails}")
        print(f"{Wh}Country          :{Gr} {w.country}")
    except Exception as e:
        print(f"{Re}WHOIS lookup failed: {e}")

@decorator_banner
def port_scanner():
    target = input(f"\n{Wh}Enter IP address or hostname : {Gr}")
    ports_input = input(f"{Wh}Enter ports (comma separated, e.g., 22,80,443) : {Gr}")
    try:
        ports = [int(p.strip()) for p in ports_input.split(',') if p.strip().isdigit()]
        if not ports:
            print(f"{Re}No valid ports provided.")
            return
        print(f"\n {Wh}========== {Gr}PORT SCAN RESULTS {Wh}==========")
        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f" {Wh}[{Gr}+{Wh}] Port {Gr}{port}{Wh} is {Gr}OPEN")
            else:
                print(f" {Wh}[{Re}-{Wh}] Port {Re}{port}{Wh} is {Re}CLOSED")
            sock.close()
    except Exception as e:
        print(f"{Re}Error: {e}")

# ─── Menu ──────────────────────────────────────────────────────────────────

options = [
    {'num': 1, 'text': 'IP Tracker (Geo, ISP, VPN check)', 'func': ip_tracker},
    {'num': 2, 'text': 'Show My Public IP', 'func': show_my_ip},
    {'num': 3, 'text': 'Phone Number Tracker', 'func': phone_tracker},
    {'num': 4, 'text': 'Username Tracker (45+ sites, supports file/email)', 'func': username_tracker},
    {'num': 5, 'text': 'Email Intelligence (Reputation + Breaches + WHOIS)', 'func': email_tracker},
    {'num': 6, 'text': 'Domain WHOIS Lookup', 'func': domain_whois},
    {'num': 7, 'text': 'Port Scanner (basic)', 'func': port_scanner},
    {'num': 0, 'text': 'Exit', 'func': exit},
]

def show_menu():
    banner()
    print(f"\n{Wh}Select an option:\n")
    for opt in options:
        print(f" {Wh}[ {opt['num']} ] {Gr}{opt['text']}")
    print()

def main():
    while True:
        show_menu()
        try:
            choice = int(input(f"{Wh}[ + ] Choose : {Gr}"))
            if choice == 0:
                print(f"\n{Wh}[{Gr}+{Wh}] Goodbye!")
                sys.exit(0)
            found = False
            for opt in options:
                if opt['num'] == choice and 'func' in opt:
                    opt['func']()
                    found = True
                    break
            if not found:
                print(f"\n{Re}Invalid option!")
            input(f"\n{Wh}[{Gr}+{Wh}] Press Enter to continue...")
        except ValueError:
            print(f"\n{Re}Please enter a number.")
            time.sleep(1)
        except KeyboardInterrupt:
            print(f"\n{Wh}[{Re}!{Wh}] Exiting...")
            sys.exit(0)

# ─── Entry Point ──────────────────────────────────────────────────────────

if __name__ == "__main__":
    try:
        import phonenumbers
        import whois
        from pyfiglet import Figlet
    except ImportError as e:
        print(f"{Re}Missing dependency: {e}")
        print(f"{Ye}Install: pip install requests phonenumbers python-whois pyfiglet")
        sys.exit(1)
    main()