import requests

def load_cookie() -> None:
    with open("cookie.txt", "r") as cookie:
        return cookie.readline()

def get_input(url: str, filename: str) -> None:
    cookie = load_cookie()
    response = requests.get(url, cookies={"session": cookie})
    with open(f"data/{filename}", "w") as f:
        f.write(response.text)