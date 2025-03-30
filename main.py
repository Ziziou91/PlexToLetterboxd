"""All logic will live in here for now."""
import xml.etree.ElementTree as ET
import sys
import requests

def print_title(line_length: int = 70) -> None:
    """prints the title of the application."""
    title = "Plex to Letterboxd"
    title_spacing = int((line_length / 2) - (len(title) / 2))

    print(f"{'=' * line_length}")
    print(f"{'-' * title_spacing}{title}{'-' * title_spacing}")
    print(f"{'=' * line_length}")

def get_plex_response(url: str, token: str) -> requests:
    """calls a plex server with a given token and prints the response."""
    token = token.strip()

    try:
        r = requests.get(f"{url}{token.strip()}", timeout=10)
        r.raise_for_status()
    except requests.exceptions.Timeout as err:
        print("\n ERROR - connection timed out.\n")
        raise SystemExit(err) from err
    except requests.exceptions.HTTPError as err:
        print(f"\n ERROR - please check token \'{token}\' is correct.\n")
        raise SystemExit(err) from err
    else:
        print("\nSuccess! Listing media libraries below.\n")
        return r

def get_librarySectionID(token: str, lib_type: str = "movie") -> str:
    """Return section key for a requested library. Defaults to 'movie' if no lib_type provided."""
    list_res = get_plex_response("http://localhost:32400/library/sections?X-Plex-Token=", token)
    root  = ET.fromstring(list_res.content)

    for child in root:
        if child.attrib["type"] == lib_type:
            return child.attrib["key"]

    return f"ERROR - No library found matching type {lib_type}"

def get_watch_history(token: str, accountID: str, librarySectionID: str) -> str:
    """Return list of media watched by a given user in a library."""
    list_res = get_plex_response(f"http://localhost:32400/status/sessions/history/all?accountId={accountID}&librarySectionID={librarySectionID}&X-Plex-Token=", token)

    return list_res

def main() -> None:
    """Main function where app logic is run."""
    sys.stdout.reconfigure(encoding='utf-8')

    print_title()

    token = input("\nPlease enter your plex token: ")

    librarySectionID = get_librarySectionID(token)

    # TODO - Get list of users - accountId
    # https://plex.tv/api/users?X-Plex-Token=

    watch_history = get_watch_history(token, 1, librarySectionID)

    root  = ET.fromstring(watch_history.content)

    for child in root:
        print(child.tag, child.attrib)



# ===================EXECTUION STARTS HERE===================
if __name__ == "__main__":
    main()
