import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}

def extract_job(html):
  title = html.find("td",{"class":"company_and_position"}).find("h2").get_text()
  company = html['data-company']
  apply_link=html.find("td",{"class":"company_and_position"}).find("a",{"class":"preventLink"})['href']
  apply_link ="https://remoteok.io"+ apply_link
  return {"title":title,"company":company,"apply_link":apply_link}

def extract_jobs(url):
  jobs=[]
  result = requests.get(url,headers=headers)
  soup = BeautifulSoup(result.text,"html.parser")
  results = soup.find_all("tr",{"class":"job"})
  for result in results:
    job = extract_job(result)
    jobs.append(job)
  return jobs

def get_jobs_re(word):
  url = f"https://remoteok.io/remote-dev+{word}-jobs"
  jobs = extract_jobs(url)
  return jobs