"""All logic will live in here for now."""
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
        r = requests.get(f"{url}{token.strip()}")
        r.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(f"\n ERROR - please check token \'{token}\' is correct.\n")
        raise SystemExit(err) from err
    else:
        print("\nSuccess! Listing media libraries below.\n")
        return r

def main() -> None:
    """Main function where app logic is run."""
    print_title()

    token = input("\nPlease enter your plex token: ")
    print(get_plex_response("http://localhost:32400/library/sections?X-Plex-Token=", token).content)


# ===================EXECTUION STARTS HERE===================
if __name__ == "__main__":
    main()
