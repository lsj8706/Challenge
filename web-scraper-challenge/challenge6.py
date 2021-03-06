import os
import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency
from challenge5 import extract_country, extract
os.system("cls")

"""
Use the 'format_currency' function to format the output of the conversion
format_currency(AMOUNT, CURRENCY_CODE, locale="ko_KR" (no need to change this one))
"""


def ask_country(countries):
    num = input("\n\nWhere are you from? Choose a country by number \n\n # ")
    try:
        num = int(num)
        if int(num) >= len(countries):
            print("There is no country that has the number")
            return ask_country(countries)
        else:
            print(f"{countries[num]['country']}")
            return num
    except:
        print("That wasn't a number.")
        ask_country(countries)


def ask_country2(countries):
    num = input("\n\nNow choose another country. \n\n\n # ")
    try:
        num = int(num)
        if int(num) >= len(countries):
            print("There is no country that has the number")
            return ask_country2(countries)
        else:
            print(f"{countries[num]['country']}")
            return num
    except:
        print("That wasn't a number")
        ask_country2(countries)


def ask_how_much(countries, from_num, to_num):
    num = input(
        f"\n\nHow much {countries[from_num]['code']} do you want to convert to {countries[to_num]['code']}?\n")
    try:
        num = int(num)
        return num
    except:
        print("That wasn't a number")
        ask_how_much(countries, from_num, to_num)


def convert(countries, from_num, to_num, how_much):
    f_country = countries[from_num]['code']
    t_country = countries[to_num]['code']
    result = requests.get(
        f"{url}{f_country}-to-{t_country}-rate?amount={how_much}")
    soup = BeautifulSoup(result.text, "html.parser")
    rate = soup.find("span", {"class": "text-success"}).get_text(strip=True)
    rate = float(rate)
    money = float(how_much * rate)
    formatted_how_much = format_currency(how_much, f_country)
    formatted_currency = format_currency(money, t_country)
    print(f"{formatted_how_much} is {formatted_currency}")


from_num = False
to_num = False
how_much = 0
countries_list = extract()
from_num = ask_country(countries_list)
if from_num is not False:
    to_num = ask_country2(countries_list)
if to_num is not False:
    how_much = ask_how_much(countries_list, from_num, to_num)
url = "https://transferwise.com/gb/currency-converter/"
convert(countries_list, from_num, to_num, how_much)

#print(format_currency(5000, "KRW", locale="ko_KR"))
