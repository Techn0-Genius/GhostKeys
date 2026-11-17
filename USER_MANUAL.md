GhostKeys – User Manual
---------------------
# 1. Installation   │
---------------------
   * Make sure you have Python 3.9+ installed.
   * Install the optional Rich dependency (used for UI):
        pip install rich
   * Clone this repository with command 'git clone https://github.com/Techn0-Genius/GhostKeys' or copy the three files (GhostKeys.py, GhostKeys.cfg, USER_MANUAL.md) into a folder.

-------------------------
# 2. Running the Tool   │
-------------------------
   python ghostkeys.py

-------------------------
# 3. Input Guidelines   │
-------------------------

   • For dates, if you do not know the day or month, type `00`.  
     If the year is unknown, type `0000`.  
   • Leave any optional field empty by just pressing Enter if you don't know anything.
   • When asked for “Add partner/child/idol”, answer `y` or `n`.  
     If `y`, you will be prompted for each sub‑field.
   • Leet mode and Alternate Caps are independent – you can enable both.

---------------
# 4. Output   │
---------------

   • The script will generate a text file in the current directory (or a custom location you choose).  
   • Each line of the file contains one password candidate.
   • If you enable hyerspeed mode, the console will continuously overwrite the same line with each new password.

----------------------
# 5. Customization   │
----------------------
   • Edit `ghostkeys.cfg` to change special characters or the leet mapping.
   • Feel free to add more transformation functions to `build_variants` if you need extra patterns.

------------------------
# 6. Troubleshooting   │
------------------------
  
   • If you see errors about missing modules, install the required packages (`rich`, `configparser` is built‑in).
   • The script is tolerant to missing optional UI libraries – it will fall back to plain text prompts.

Happy hacking! (Legally, of course)

-----------------
# 7. ALERT!!!   │
-----------------

GhostKeys is developed and provided strictly for educational purposes, authorized security testing, and legitimate cybersecurity research.

By using this tool, you acknowledge and agree that:

1. You are solely responsible for how you use this software and the data it generates.
2. You must obtain explicit permission from the respective owner before conducting any security testing or password-related assessments.
3. Unauthorized access, password attacks, privacy violations, or any illegal activity using this tool are strictly prohibited.
4. The developer does not endorse, encourage, or support any form of malicious or unlawful use of this software.
5. The developer assumes no responsibility or liability for damages, losses, legal consequences, or misuse arising from the use or distribution of this tool.

**Use responsibly. Stay ethical. Respect privacy and the law.**

By downloading, installing, or using GhostKeys, you agree that you understand and accept these terms.