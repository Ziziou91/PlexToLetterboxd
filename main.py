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

def get_lib_key(list_res: str, lib_type: str = "movie") -> str:
    """Return section key for a requested library. Defaults to 'movie' if no lib_type provided."""
    root  = ET.fromstring(list_res.content.decode("utf-8"))

    for child in root:
        if child.attrib["type"] == lib_type:
            return child.attrib["key"]

    return f"ERROR - No library found matching type {lib_type}"

def main() -> None:
    """Main function where app logic is run."""
    print_title()
    sys.stdout.reconfigure(encoding='utf-8')


    token = input("\nPlease enter your plex token: ")

    list_res = get_plex_response("http://localhost:32400/library/sections?X-Plex-Token=", token)
    lib_key = get_lib_key(list_res)

    print(lib_key)

# ===================EXECTUION STARTS HERE===================
if __name__ == "__main__":
    main()
