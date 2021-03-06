import os
import csv
import requests
from bs4 import BeautifulSoup

os.system("cls")
alba_url = "http://www.alba.co.kr"

# 실행시키면 약 100개 가 넘는 csv 파일이 생겨서 마지막줄을 주석처리 해놓았음.


def extract_jobs(box_link, company_name):
    print(f"{company_name}is loading")
    jobs = []
    result = requests.get(box_link)
    soup = BeautifulSoup(result.text, "html.parser")
    tbody = soup.find_all("tbody")[-1]
    trs = tbody.find_all("tr", {"class": ""})
    for tr in trs:
        try:
            location = tr.find("td", {"class": "local"}).get_text(strip=True)
        except:
            location = "No information"
        try:
            title = tr.find("td", {"class": "title"}).find(
                "span", {"class": "company"}).get_text(strip=True)
        except:
            title = "No informaton"
        try:
            time = tr.find("td", {"class": "data"}).find(
                "span", {"class": "time"}).get_text(strip=True)
        except:
            time = "undecided"
        try:
            pay = tr.find("td", {"class": "pay"}).get_text(strip=True)
        except:
            pay = "No information"
        try:
            date = tr.find("td", {"class": "regDate"}).get_text(strip=True)
        except:
            date = "No information"
        jobs.append({"place": location, "title": title,
                     "time": time, "pay": pay, "date": date})
    return jobs


def get_brand_url():
    result = requests.get(alba_url)
    soup = BeautifulSoup(result.text, "html.parser")
    super_brand = soup.find("div", {"id": "MainSuperBrand"})
    good_box = super_brand.find_all('a', {"class": "goodsBox-info"})
    for box in good_box:
        box_link = box['href']
        box_company = box.find(
            "span", {"class": "company"}).get_text(strip=True)
        jobs = extract_jobs(box_link, box_company)
        save_to_file(jobs, box_company)
    return


def save_to_file(jobs, company_name):
    if '/' in company_name:
        company_name = company_name.replace('/', '-')
    file = open(f"{company_name}.csv", mode="w", encoding="utf-8-sig")
    writer = csv.writer(file)
    writer.writerow(["plcae", "title", "time", "pay", "date"])
    for job in jobs:
        writer.writerow(list(job.values()))
    return


def get_jobs():
    get_brand_url()
    return


# get_jobs()
