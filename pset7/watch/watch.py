import re


def main():
    print(parse(input("HTML: ")))

# Extract the youtube link within an iframe element and pass it to the shorten_url function.
def parse(html):
    # Guard clause to determine that there is a valid youtube link within a valid HTML iframe element.
    if not re.search(r"<iframe src=\"http(s)?://(www\.)?youtube\.com/embed/[^\"]+\"></iframe>", html):
        return None
    else: 
        youtube_url = re.search(r"http(s)?://(www\.)?youtube\.com/embed/[^\"]+", html)
        return shorten_url(youtube_url.group())


# Shortens the url contained within an iframe element to a shareable, compact format.
def shorten_url(url):
    # Appends secure HTTP to any link without it.
    if not "https" in url:
        return url.replace("http", "https").replace("www.", "").replace("be.com", ".be").replace("embed/", "")
    return url.replace("www.", "").replace("be.com", ".be").replace("embed/", "")


if __name__ == "__main__":
    main()