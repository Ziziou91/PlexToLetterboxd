"""All logic will live in here for now."""
import requests

def print_title(line_length: int = 70) -> None:
    """prints the title of the application."""
    title = "Plex to Letterboxd"
    title_spacing = int((line_length / 2) - (len(title) / 2))

    print(f"{'=' * line_length}")
    print(f"{'-' * title_spacing}{title}{'-' * title_spacing}")
    print(f"{'=' * line_length}")

def validate_url(token: str) -> str:
    """calls a plex server with a given token and prints the response."""
    postcodes_req = requests.get("https://api.postcodes.io/postcodes/SK30DL")


def main() -> None:
    """Main function where app logic is run."""
    print_title()

# ===================EXECTUION STARTS HERE===================
if __name__ == "__main__":
    main()
