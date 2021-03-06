import os
import requests
from bs4 import BeautifulSoup

os.system("cls")
url = "https://www.iban.com/currency-codes"


def extract_country(html):
    information = html.find_all("td")
    country_name = str(information[0].string)
    currency_name = str(information[1].string)
    code_name = str(information[2].string)
    nubmer_name = str(information[3].string)

    return {'country': country_name, 'currency': currency_name, 'code': code_name, 'number': nubmer_name}


def ask_country(countries):
    num = input("#: ")
    try:
        num = int(num)
        if int(num) >= len(countries):
            print("There is no country that has the number")
            ask_country(countries)
        else:
            print(f"You choose {countries[num]['country']}")
            print(f"The currency code is {countries[num]['code']}")
    except:
        print("That wasn't a number.")
        ask_country(countries)


def extract():
    countries = []
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    tbody = soup.find("tbody")
    results = tbody.find_all("tr")
    for result in results:
        country = extract_country(result)
        countries.append(country)
    print("Hello please choose select a country by number!")
    for value in countries:
        if value['currency'] == "No universal currency":
            countries.remove(value)
        else:
            pass
    for idx, val in enumerate(countries):
        print('#', idx, val['country'])
    return countries


if __name__ == "__main__":
    countries_list = extract()
    ask_country(countries_list)
