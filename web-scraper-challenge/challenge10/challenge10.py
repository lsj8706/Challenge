import requests
from flask import Flask, render_template, request,redirect,send_file
from bs4 import BeautifulSoup
from so import get_jobs
from we import get_jobs_we
from remote import get_jobs_re
from exporter import save_to_file
"""
These are the URLs that will give you remote jobs for the word 'python'

https://stackoverflow.com/jobs?r=true&q=python
https://weworkremotely.com/remote-jobs/search?term=python
https://remoteok.io/remote-dev+python-jobs

Good luck!
"""
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}
app=Flask("JobSearch")
db={}

@app.route('/')
def home():
  return render_template("home.html")

@app.route('/search')
def search():
  word = request.args.get('word')
  if word:
    word=word.lower()
    existingJobs = db.get(word)
    if existingJobs:
      jobs = existingJobs
    else:
      jobs= get_jobs(word) + get_jobs_we(word) + get_jobs_re(word)
      db[word] = jobs
  else:
    return redirect('/')
  return render_template("search.html",searchingBy=word,resultsNumber=len(jobs),jobs=jobs)

@app.route('/export')
def export():
  try:
    word = request.args.get('word')
    if not word:
      raise Exception()
    word = word.lower()
    jobs = db.get(word)
    if not jobs:
      raise Exception()
    save_to_file(jobs)
    return send_file("jobs.csv",mimetype="application/x-csv", attachment_filename=f"{word}.csv",as_attachment=True)
  except:
    return redirect('/')
    

app.run(host="0.0.0.0")