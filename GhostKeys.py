#!/usr/bin/env python3

"""
GhostKeys – Password Candidates Generation
Author: Techn0‑Genius
"""

from __future__ import annotations

import os
import re
import time
from pathlib import Path
from configparser import ConfigParser
from typing import List, Dict, Any

# ----------------------
# Optional Rich UI     ┃
# ----------------------

try:
    from rich.console import Console
    from rich.progress import Progress, SpinnerColumn, TextColumn
    from rich.prompt import Prompt
    from rich.text import Text
    from rich.panel import Panel
    from rich import box
    RICH_AVAILABLE = True

except Exception:  
    RICH_AVAILABLE = False

# ---------------------------------
# Configuration (ghostkeys.cfg)   ┃
# ---------------------------------
CONFIG_FILE = Path(__file__).with_name("ghostkeys.cfg")
DEFAULT_CFG = """[DEFAULT]
special_chars = !@#$%^&*()-_+=<>?~`[]{}|;':",./
leet_map = a=4,e=3,i=1,o=0,s=5,t=7,b=8,g=9,l=1,m=/\/\
"""

def _ensure_config() -> ConfigParser:
    """Create a default config file if missing and return a parser."""
    if not CONFIG_FILE.exists():
        CONFIG_FILE.write_text(DEFAULT_CFG.strip())
    parser = ConfigParser()
    parser.read(CONFIG_FILE)
    return parser

# --------------------
# Helper functions   ┃
# --------------------
def banner(console: Any) -> None:
    """Print the custom ASCII banner in bold blue (or plain text)."""
    art = (
        "____ _               _   _  __\n"
        "/ ___| |__   ___  ___| |_| |/ /___ _   _ ___\n"
        "| |  _| '_ \\ / _ \\/ __| __| ' // _ \\ | | / __|\n"
        "| |_| | | | | (_) \\__ \\ |_| . \\  __/ |_| \\__ \\\n"
        " \\____|_| |_|\\___/|___/\\__|_|\\_\\___|\\__, |___/\n"
        "                                    |___/"
    )
    if RICH_AVAILABLE and console:
        console.print(Text(art, style="bold blue"))
    else:
        print(art)

def prompt(console: Any, msg: str, allow_empty: bool = True, default: str | None = None) -> str:
    """Read a line from the user – re‑prompt if not allowed to be empty."""
    while True:
        try:
            if RICH_AVAILABLE:
                val = Prompt.ask(msg, default=default or "")
            else:
                raw = input(msg)
                val = raw.strip()

            if not val and not allow_empty:
                if RICH_AVAILABLE:
                    console.print("[red]Input cannot be empty – try again.[/red]")
                else:
                    print("Input cannot be empty – try again.")
                continue

            return val.strip()
        except EOFError:
            return ""

def leet_transform(word: str, leet_map: Dict[str, str]) -> str:
    if not leet_map:
        return word
    return "".join(leet_map.get(c.lower(), c) for c in word)

def alternate_caps(word: str) -> str:
    return "".join(c.upper() if i % 2 else c.lower() for i, c in enumerate(word))

def reverse_word(word: str) -> str:
    return word[::-1]

def numeric_range(start: int, end: int, width: int) -> List[str]:
    return [str(n).zfill(width) for n in range(start, end + 1)]

# ------------------
# Data container   ┃
# ------------------

class Victim:
    def __init__(self):
        self.first_name: str = ""
        self.surname: str = ""
        self.nickname: str = ""
        self.birthdate: str = "" 
        self.mobile: str = ""
        self.vehicle: str = ""
        self.location: str = ""
        self.fav_car: str = ""
        self.fav_food: str = ""
        self.partner: Dict[str, str] = {}
        self.child: Dict[str, str] = {}
        self.idol: Dict[str, str] = {}
        self.pet: str = ""
        self.company: str = ""
        self.keywords: List[str] = []
        self.patterns: List[str] = []
        self.use_leet: bool = False
        self.use_alt_caps: bool = False

# -------------------------------
# Interactive data collection   ┃
# -------------------------------

def collect_profile(console: Any, cfg: ConfigParser) -> Victim:
    v = Victim()

    def yes_no(msg: str) -> bool:
        return prompt(console, msg, default="N").lower() == "y"

    console.print("\n[bold cyan]=== Victim's Basic Info ===[/bold cyan]")
    v.first_name = prompt(console, "First name of victim:").strip()
    v.surname = prompt(console, "Surname :").strip()
    v.nickname = prompt(console, "Nickname :").strip()

    raw_dob = prompt(console, "Date of birth (DD/MM/YYYY or just YYYY):").strip()
    if raw_dob:
        clean = re.sub(r"[\/\-\s]", "", raw_dob)
        v.birthdate = clean

    v.mobile = prompt(console, "Mobile number (last 4 digits often used):").strip()
    v.vehicle = prompt(console, "Vehicle plate/number:").strip()
    v.location = prompt(console, "City or State:").strip()

    console.print("\n[bold cyan]=== Favorites ===[/bold cyan]")
    v.fav_car = prompt(console, "Favorite Car (Bugatti):").strip()
    v.fav_food = prompt(console, "Favorite Food (Pizza):").strip()

    console.print("\n[bold cyan]=== Partner's Info ===[/bold cyan]")
    if yes_no("Add partner? (y/N): "):
        v.partner = {
            "name": prompt(console, "  Partner's First Name:").strip(),
            "surname": prompt(console, "  Partner's Surname:").strip(),
            "nickname": prompt(console, "  Partner's Nickname:").strip(),
            "mobile": prompt(console, "  Partner's Mobile:").strip(),
            "vehicle": prompt(console, "  Partner's Vehicle:").strip(),
            "birthdate": prompt(console, "  Partner's DOB (DDMMYYYY or YYYY):").strip(),
        }

    console.print("\n[bold cyan]=== Child's Info ===[/bold cyan]")
    if yes_no("Add child? (y/N): "):
        v.child = {
            "name": prompt(console, "  Child's First Name:").strip(),
            "surname": prompt(console, "  Child's Surname:").strip(),
            "nickname": prompt(console, "  Child's Nickname:").strip(),
            "mobile": prompt(console, "  Child's Mobile:").strip(),
            "vehicle": prompt(console, "  Child's Vehicle:").strip(),
            "birthdate": prompt(console, "  Child's DOB (DDMMYYYY or YYYY):").strip(),
        }

    console.print("\n[bold cyan]=== Idol / Crush ===[/bold cyan]")
    if yes_no("Add idol? (y/N): "):
        v.idol = {
            "name": prompt(console, "  Idol's First Name:").strip(),
            "surname": prompt(console, "  Idol's Surname:").strip(),
            "nickname": prompt(console, "  Idol's Nickname:").strip(),
            "mobile": prompt(console, "  Idol's Mobile:").strip(),
            "vehicle": prompt(console, "  Idol's Vehicle:").strip(),
            "birthdate": prompt(console, "  Idol's DOB (DDMMYYYY or YYYY):").strip(),
        }

    v.pet = prompt(console, "\nPet name of the victim (optional):").strip()
    v.company = prompt(console, "Company name (optional):").strip()

    if yes_no("Enter custom keywords/patterns? (y/N): "):
        kw = prompt(console, "Comma‑separated list of words/patterns:").strip()
        v.keywords = [w.lower() for w in kw.split(",") if w.strip()]

    v.use_leet = yes_no("Enable leet mode for all passwords? (y/N): ")
    v.use_alt_caps = yes_no("Enable alternate caps mode? (y/N): ")

    return v

# -----------------------
# Password generation   ┃
# -----------------------

def build_variants(v: Victim, cfg: ConfigParser) -> List[str]:
    variants: List[str] = []

    # Load config
    try:
        special_chars = cfg["DEFAULT"]["special_chars"]
        leet_map_raw = cfg["DEFAULT"]["leet_map"]
        leet_map = {}
        for item in leet_map_raw.split(","):
            if "=" in item:
                k, val = item.split("=", 1)
                k = k.strip().lower()
                val = val.strip()
                if val:
                    leet_map[k] = val
    except Exception:
        special_chars = "!@#$%^&*()-_+=."
        leet_map = {"a": "4", "e": "3", "i": "1", "o": "0", "s": "5", "t": "7", "A":"4", "E": "3", "I": "1", "L": "1","O": "0", "S": "5", "T":"7"}

    # Base strings to transform

    base_strings = [
        v.first_name,
        v.surname,
        v.nickname,
        v.pet,
        v.company,
        v.fav_car,
        v.fav_food,
    ]

    # Add partner, child and idol names

    for person in [v.partner, v.child, v.idol]:
        for key in ("name", "surname", "nickname"):
            base_strings.append(person.get(key, ""))

    # Remove empties

    base_strings = [s for s in base_strings if s]

    # Transformations

    base_pool = set()
    for s in base_strings:

        base_pool.add(s.lower())
        base_pool.add(s.upper())
        base_pool.add(reverse_word(s).lower())
        base_pool.add(reverse_word(s).upper())

        if v.use_leet:
            base_pool.add(leet_transform(s, leet_map))
            base_pool.add(leet_transform(reverse_word(s), leet_map))

        if v.use_alt_caps:
            base_pool.add(alternate_caps(s.lower()))
            base_pool.add(alternate_caps(s.upper()))

    # Capital‑only first letter + alternative caps patterns
    
    capitalized_pool = {w[0].upper() + w[1:].lower() if len(w) > 1 else w.upper()
                        for w in base_pool if w}
    
    # Two “alternating‑caps” flavours:
    
    alt_start_lower = {alternate_caps(w.lower()) for w in base_pool if w}
    alt_start_upper = {alternate_caps(w.upper()) for w in base_pool if w}

    # Merge all three new pools into base_pool
   
    base_pool.update(capitalized_pool)
    base_pool.update(alt_start_lower)
    base_pool.update(alt_start_upper)
   
    # Numbers to append / prepend
   
    numeric_sources = set()

    # Current year and last 10 years
   
    yr = time.localtime().tm_year
    numeric_sources.update(str(y) for y in range(yr - 10, yr + 1))

    # Mobile last 4 digits
   
    mob = re.sub(r"\D", "", v.mobile)
    if len(mob) >= 4:
        numeric_sources.add(mob[-4:])

    # Birthdate full and parts
    bd = re.sub(r"\D", "", v.birthdate)
    if len(bd) >= 4:
        numeric_sources.add(bd[-4:])          # last 4
        numeric_sources.add(bd)               # full
        numeric_sources.add(bd[:2])           # DD
        numeric_sources.add(bd[2:4])          # MM
        numeric_sources.add(bd[4:])           # YYYY

    # Vehicle number (just digits)
    veh = re.sub(r"\D", "", v.vehicle)
    if veh:
        numeric_sources.add(veh)

    # Standard 2‑digit numbers
    numeric_sources.update(str(i) for i in range(10, 100))

    numeric_sources = list(numeric_sources)

    # Construct password list
    specials = list(special_chars)

    for base in base_pool:
        if not base:
            continue

        # 1. plain base
   
        variants.append(base)

        # 2. base + numeric (suffix)
   
        for n in numeric_sources[:15]:
            variants.append(f"{base}{n}")
            variants.append(f"{base}_{n}")
            variants.append(f"{base}.{n}")

   
        # 3. base + special + numeric
   
        for n in numeric_sources[:15]:
            for s in specials[:5]:
                variants.append(f"{base}{s}{n}")
                variants.append(f"{base}{n}{s}")

   
        # 4. numeric prefix
   
        for n in numeric_sources[:15]:
            variants.append(f"{n}{base}")

    # 5. base + single special (no number)
   
    for base in base_pool:
        for s in specials[:5]:
            variants.append(f"{base}{s}")
            variants.append(f"{s}{base}")

    # 6. “ilove” patterns for favourite car / food
   
    for fav in (v.fav_car, v.fav_food):
        if fav:
            base = f"ilove{fav.lower()}"
            variants.append(base)
            for n in numeric_sources[:10]:
                variants.append(f"{base}{n}")

    # 7. Custom keywords / patterns
   
    for kw in v.keywords:
        variants.append(kw)
        for n in numeric_sources[:10]:
            variants.append(f"{kw}{n}")
            variants.append(f"{n}{kw}")
        for n in numeric_sources[:10]:
            for s in specials[:5]:
                variants.append(f"{kw}{s}{n}")
                variants.append(f"{kw}{n}{s}")

    # Deduplicate while preserving order
   
    seen = set()
    unique = []
    for w in variants:
        if w not in seen and 4 <= len(w) <= 32:
            seen.add(w)
            unique.append(w)

    return unique

# -------------------------------------
# Password filtering – relaxed rule   ┃
# -------------------------------------

def filter_passwords(pw_list: List[str]) -> List[str]:
    """
    Keep only passwords that are 4‑32 chars long and contain at least
    one digit or one special character.  If nothing survives, return
    a small set of safe defaults.
    """
    filtered = []
    for p in pw_list:
        if not (4 <= len(p) <= 32):
            continue
        if any(c.isdigit() for c in p) or any(not c.isalnum() for c in p):
            filtered.append(p)

    if not filtered:
        filtered = ["Password123", "Welcome1", "Admin123"]

    filtered.sort(key=lambda x: (len(x), x))
    return filtered

# ---------------
# I/O helpers   ┃
# ---------------

def write_to_file(passwords: List[str], path: str, console: Any = None) -> None:
    """Write the list to disk, one password per line."""
    if not passwords:
        if RICH_AVAILABLE and console:
            console.print("[red]No passwords generated – file will not be created.[/red]")
        else:
            print("[!] No passwords generated – file will not be created.")
        return

    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(passwords))

    if RICH_AVAILABLE and console:
        console.print(f"\n[bold green]Generated {len(passwords)} passwords → {path}[/bold green]")
    else:
        print(f"\n[+] Generated {len(passwords)} passwords → {path}")

def print_passwords(passwords: List[str]) -> None:
    """Print each password to stdout."""
    for p in passwords:
        print(p)

# --------------------
# Main entry point   ┃
# --------------------

def main() -> None:
    console = Console() if RICH_AVAILABLE else None
    cfg = _ensure_config()

    banner(console)

    victim = collect_profile(console, cfg)

    console.print("\n[bold yellow]Generating password list …[/bold yellow]")

    if RICH_AVAILABLE:
        with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), transient=True) as progress:
            task = progress.add_task("Processing", total=1)
            time.sleep(0.5)
            progress.update(task, completed=1)
    else:
        time.sleep(0.5)

    all_variants = build_variants(victim, cfg)
    passwords = filter_passwords(all_variants)

    # Default file name logic ──>
    default_name = victim.first_name or victim.surname or "target"
    output_dir = Path.cwd()

    if RICH_AVAILABLE:
        output_file = Prompt.ask("Enter output file name (without extension)", default=default_name)
    else:
        output_file = input(f"Enter output file name (without extension) [{default_name}]: ").strip()

    if not output_file:
        output_file = default_name

    full_path = output_dir / f"{output_file}.txt"
    write_to_file(passwords, str(full_path), console)

    # Optionally show passwords on screen

    if RICH_AVAILABLE:
        show = Prompt.ask("Show passwords on screen in hyperspeed mode? (y/N ):", choices=["y", "n"], default="n") == "y"
    else:
        show = input("\nShow passwords on screen in hyperspeed mode ? (y/N): ").lower() == "y"

    if show:
        print_passwords(passwords)

    if RICH_AVAILABLE:
        console.print("\n[bold green]Done! Good luck! HAPPY HACKING![/bold green]")
    else:
        print("\n[+] Done! Good luck! HAPPY HACKING!")

if __name__ == "__main__":
    main()