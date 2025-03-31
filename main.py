#!/usr/bin/env python3
"""
Plex to Letterboxd - Export your Plex watch history as Letterboxd csv format.
"""
import sys
from utils.ui import print_title, print_token_instructions
from plex_api.libraries import get_librarySectionID
from plex_api.history import print_watch_history

def main() -> None:
    """Main function where app logic is run."""
    sys.stdout.reconfigure(encoding='utf-8')

    print_title("Plex to Letterboxd")
    print_token_instructions()

    token = input("\nPlease enter your plex token: ")

    ipaddress = input("\nPlease enter your plex ip address: ")

    librarySectionID = get_librarySectionID(ipaddress, token)

    print_watch_history(ipaddress, token, librarySectionID)

    # TODO: Add export to Letterboxd functionality


# ===================EXECTUION STARTS HERE===================
if __name__ == "__main__":
    main()
