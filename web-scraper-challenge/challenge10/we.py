import requests
from bs4 import BeautifulSoup


def extract_job(html):
  title = html.find("span",{"class":"title"}).get_text()
  company=html.find("span",{"class":"company"}).get_text()
  apply_link = html.find("a")['href']
  apply_link = "https://weworkremotely.com"+apply_link
  return {"title":title,"company":company,"apply_link":apply_link}


def extract_jobs(url):
  jobs=[]
  result = requests.get(url)
  soup = BeautifulSoup(result.text,"html.parser")
  results = soup.find_all("li",{"class":"feature"})
  for result in results:
    job=extract_job(result)
    jobs.append(job)
  return jobs


def get_jobs_we(word):
  url = f"https://weworkremotely.com/remote-jobs/search?term={word}"
  jobs = extract_jobs(url)
  return jobs