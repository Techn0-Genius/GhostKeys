# GhostKeys – Password Candidates Generation
Author: **Techn0‑Genius**

> GhostKeys is a lightweight, highly configurable password‑generation toolkit.  
> It collects victim data via an interactive terminal UI, then produces a massive list of possible password candidates that follow a wide range of patterns (leet, alternate caps, special‑char + number combos, `ilove<car>` prefixes, etc.).  
> The output is a plain text file ready for offline use or feeding into a brute‑force tool.

## Features

| Feature | Description |
|---------|-------------|
| **Interactive UI** | Rich‑based prompts, banners, progress spinners, and optional hyerspeed mode. |
| **Extensive Variants** | Includes leet, alternate caps, reversed names, numeric ranges, special‑char + number combos, `ilove<car>` prefixes, custom keywords/patterns, partner/child/idol data, pet/company, birthdate parts. |
| **Configurable** | `GhostKeys.cfg` lets you change special characters and leet mapping without touching code. |
| **Password Filtering** | Keeps only passwords that are 4‑32 chars long and contain at least one lowercase, uppercase, digit, and special character. |
| **Output** | One password per line in a `.txt` file. File name defaults to the victim’s first name, or `target.txt` if none provided. |
| **Hyerspeed Mode** | Prints each password |


# GhostKeys – Password Candidates Generator

> **⚡️ Fast, flexible, and fully‑configurable password‑generation tool.**  


## Features

- Collect victim data interactively (name, DOB, mobile, etc.).
- Generate dozens of password variants per entry.
- Customizable via `GhostKeys.cfg`.
- Export results to a plain‑text file.

## Installation

```bash

# Install dependencies

pip install -r requirements.txt

# Clone the repo

git clone https://github.com/Techn0-Genius/GhostKeys
cd GhostKeys
python Ghostkeys.py


