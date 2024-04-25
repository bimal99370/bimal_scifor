import requests
def random_quote():
    url = "https://api.quotable.io/random"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        quote_text = data["content"]
        author = data["author"]
        return f'"{quote_text}" - By {author}'
    else:
        return "Failed to retrieve a random quote"

random_quote = random_quote()
print("Quote:",random_quote)
