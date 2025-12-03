from tool.validators import is_url


print("~    Website Migration Tool    ~\n")

url = input("Enter a URL: ")

if not is_url(url):
    print("Invalid url:", url)
    quit()

print(url)