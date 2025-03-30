"""Plex api user functionality."""
import xml.etree.ElementTree as ET
from .client import get_plex_response

def get_users(token: str) -> str:
    """Return list of users of Plex server.
    
    Args:
        token: The Plex authentication token
        
    Returns:
        Response object containing users
    """
    url = f"https://plex.tv/api/users?X-Plex-Token="
    users_response = get_plex_response(url, token)

    users = parse_users(users_response)
    return users

def parse_users(response) -> list:
    """Parse users XML response into a list of users.
    
     Args:
        response: Response object from get_users
        
    Returns:
        List of dictionaries with user information
    """

    root = ET.fromstring(response.content)
    users = []

    for child in root:
        if child.tag == "User":
            movie_data = child.attrib
            users.append({
                "username": movie_data.get("username"),
                "email": movie_data.get("email"),
                "id": movie_data.get("id"),
            })

    return users
