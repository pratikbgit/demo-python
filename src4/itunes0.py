import sys
import requests

if len(sys.argv) != 2:
    sys.exit("Usage: python script.py <search_term>")

try:
    response = requests.get(
        "https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1]
    )
    response.raise_for_status()  # Raises an error for bad status codes (e.g., 404, 500)
    print(response.json())
except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")
except ValueError as e:
    print(f"Error parsing JSON: {e}")