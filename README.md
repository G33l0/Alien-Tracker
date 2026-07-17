# 🌐 Alien-Track

<p align="center">
  <a href="https://www.python.org/downloads/">
    <img src="https://img.shields.io/badge/python-3.7+-blue.svg" alt="Python 3.7+">
  </a>
  <a href="LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT">
  </a>
  <a href="https://ish.app/">
    <img src="https://img.shields.io/badge/iSH-compatible-brightgreen.svg" alt="iSH compatible">
  </a>
</p>

---

**Advanced OSINT Swiss Army Knife** – IP, phone, username, email, domain, and port intelligence all in one tool.

---

## 🛸 Overview

**Alien-Track** is a powerful, banner‑style information gathering tool designed for security researchers, penetration testers, and OSINT enthusiasts. It combines multiple public APIs and built‑in techniques to quickly extract valuable data about:

- **IP addresses** (geolocation, ISP, proxy/VPN detection)
- **Phone numbers** (carrier, location, type – wireless/landline/VoIP)
- **Usernames** (across 45+ social media and coding platforms)
- **Email addresses** (reputation, breach history, domain WHOIS)
- **Domains** (full WHOIS records)
- **Ports** (basic TCP scanning)

All within an interactive, user‑friendly terminal interface.

---

✨ Features

Module Capabilities
IP Tracker Geolocation, timezone, ISP, organisation, ASN, proxy/VPN flag, Google Maps link
Show My IP Quick public IP retrieval
Phone Tracker Country, region, timezone, carrier, validity, E.164 format, type classification (wireless, landline, VoIP, pager, personal)
Username Tracker 45+ platforms (social, coding, gaming, learning) – parallel multi‑threaded scanning
Email Intelligence Gravatar presence, HaveIBeenPwned breaches, EmailRep reputation, domain WHOIS
Domain WHOIS Registrar, creation/expiry dates, name servers, contacts
Port Scanner Quick TCP connect scan on user‑specified ports

---

🚀 Installation

Prerequisites

· Python 3.7 or higher
· pip package manager

Clone & Install

```bash
git clone https://github.com/G33l0/Alien-Track.git
cd Alien-Track
pip install -r requirements.txt
```

Note for iSH (iOS): Works seamlessly – install the same dependencies.

Requirements

Create a requirements.txt file with:

```
requests
phonenumbers
python-whois
```

Or install manually:

```bash
pip install requests phonenumbers python-whois
```

---

🎮 Usage

Run the script:

```bash
python alien_track.py
```

You'll be greeted with the Alien banner and a menu:

```
[ 1 ] IP Tracker (Geo, ISP, VPN check)
[ 2 ] Show My Public IP
[ 3 ] Phone Number Tracker
[ 4 ] Username Tracker (45+ sites)
[ 5 ] Email Intelligence (Reputation + Breaches + WHOIS)
[ 6 ] Domain WHOIS Lookup
[ 7 ] Port Scanner (basic)
[ 0 ] Exit
```

Simply enter the number of the desired module and follow the prompts.

---

🔧 Modules in Detail

IP Tracker

· Uses ipwho.is for core data and ip-api.com for proxy/hosting detection.
· Output includes: country, region, city, coordinates, timezone, ISP, organisation, ASN, EU membership, flag emoji, and a Google Maps link.

Phone Tracker

· Uses Google's phonenumbers library.
· Detects carrier, geographic location, timezone, and classifies the number as Wireless/Mobile, Landline, VoIP, Pager, or Personal.
· Validates and formats in international/E.164 standards.

Username Tracker

· Scans 45+ platforms concurrently using ThreadPoolExecutor.
· Platforms include: Facebook, Twitter, Instagram, GitHub, LinkedIn, Reddit, YouTube, Twitch, TikTok, Steam, Spotify, Roblox, HackerRank, TryHackMe, HackTheBox, Codecademy, and many more.

Email Intelligence

· Gravatar – checks if an avatar exists.
· HaveIBeenPwned – lists all known data breaches (public API, no key required).
· EmailRep.io – provides reputation score, suspicious/malicious flags, breach count, first/last seen dates.
· Domain WHOIS – extracts registrar, creation/expiry info for the email’s domain.

Domain WHOIS

· Fetches registrar, creation/expiration/update dates, name servers, registrant details, and administrative email.

Port Scanner

· Simple TCP connect scan on user‑specified ports (e.g., 22,80,443).
· Fast timeout (1 second) for quick checks.

---

📁 File Structure

```
Alien-Track/
├── alien_track.py       # Main script
├── requirements.txt     # Python dependencies
└── README.md            # This file
```

---

⚠️ Disclaimer

This tool is intended for educational purposes and authorised security testing only.
Unauthorised use against systems you do not own or have explicit permission to test is illegal. The author assumes no responsibility for any misuse or damage caused by this tool.

---

👨‍💻 Author

· IamG2 (@IamG2) – Creator & Maintainer

---

🙏 Credits

· APIs: ipwho.is, ip-api.com, EmailRep.io, HaveIBeenPwned
· Libraries: phonenumbers, python-whois, requests

---

📜 License

This project is licensed under the MIT License – see the LICENSE file for details.

---

“The truth is out there – track it with Alien-Track.” 🛸
