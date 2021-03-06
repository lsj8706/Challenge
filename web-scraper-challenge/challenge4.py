import requests
import os


def ask_url():
    print("Welcome to IsItDown.py!")
    url = input(
        "Please write a URL or URLs you want to check.(separated by comma)\n")
    url = url.lower()
    url_list = url.split(',')
    urls = []
    for url in url_list:
        url = url.strip()
        urls.append(url)
    urls_list = check_http(urls)
    check_legit(urls_list)
    ask_again()


def check_http(urls):
    urls_list = []
    for url in urls:
        if url.startswith('http://') or url.startswith('https://'):
            urls_list.append(url)
        else:
            url = f"http://{url}"
            urls_list.append(url)
    return urls_list


def check_legit(urls_list):
    for url in urls_list:
        try:
            if '.' not in url:
                print(f"{url} is invalid url")
                continue
            else:
                pass
            request = requests.get(url)
            if request.status_code == 200:
                print(f'{url} is up!')
            else:
                print(f'{url} is down!')
        except:
            print(f"{url} is down!")


def ask_again():
    again = input("Do you want to sart over? y/n ")
    if again == 'y':
        os.system('cls')
        # 윈도우에서는 cls 맥과 리눅스에서는 clear
        ask_url()
    elif again == 'n':
        print("Okay bye!")
        return 0
    else:
        print("That's not correct answer")
        ask_again()


ask_url()
