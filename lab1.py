import requests
import re


def main():
    url = input(
        "Δώσε το URL που θες να γίνει αναζήτηση(π.χ. www.example.com ή example.com): "
    )
    # url = "youtube.com"
    url = "https://" + url
    response = requests.get(url)
    text = str(response.headers)
    pattern = re.compile(r"Set-Cookie")
    matches = re.search(pattern, text)

    if "Server" in response.headers:
        print("\nServer used->", response.headers.get("Server"))
    else:
        print("No server detected")

    if matches is not None:
        print("Η σελίδα χρησιμοποιεί cookies")

        text = response.headers["Set-Cookie"]
        # print(text)
        pattern = r"(Expires=.*?;|expires=.*?;)"
        dates = re.findall(pattern, text)
        pattern = r"(^.*?=|,\s[a-zA-Z_].*?=)"
        cookie_names = re.findall(pattern, text)
        for i in range(len(dates)):
            name = cookie_names[i][:-1]
            date = dates[i]
            print(name + " " + date)
    else:
        print("Η σελίδα δεν χρησιμοποιεί cookies")


if __name__ == "__main__":
    main()
