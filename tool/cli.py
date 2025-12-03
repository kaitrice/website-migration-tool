"""Command Line Interface for migration tool."""
import sys
from tool.validators import is_url


print("~    Website Migration Tool    ~\n")

url = input("Enter a URL: ")

if not is_url(url):
    print(f"Invalid url: {url}\n")
    sys.exit()

print(f"{url}\n")
