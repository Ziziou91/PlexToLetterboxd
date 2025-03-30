"""Plex api user functionality."""
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

    return users_response.content