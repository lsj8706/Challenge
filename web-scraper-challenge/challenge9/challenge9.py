import requests
from flask import Flask, render_template, request
from bs4 import BeautifulSoup
"""
When you try to scrape reddit make sure to send the 'headers' on your request.
Reddit blocks scrappers so we have to include these headers to make reddit think
that we are a normal computer and not a python script.
How to use: requests.get(url, headers=headers)
"""

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}


"""
All subreddits have the same url:
i.e : https://reddit.com/r/javascript
You can add more subreddits to the list, just make sure they exist.
To make a request, use this url:
https://www.reddit.com/r/{subreddit}/top/?t=month
This will give you the top posts in per month.
"""

subreddits = [
    "javascript",
    "reactjs",
    "reactnative",
    "programming",
    "css",
    "golang",
    "flutter",
    "rust",
    "django"
]

app = Flask("DayEleven")

@app.route('/')
def home():
  return render_template("home.html")

def get_post(html,subreddit):
  posts=[]
  anchor=html.find("a",{"class":"SQnoC3ObvgnGjWt90zD9Z"})
  if anchor is not None:
    url = anchor['href']
    title = html.find("h3",{"class":"_eYtD2XCVieq6emjKBH3m"}).get_text()
    vote = html.find("div",{"class":"_3a2ZHWaih05DgAOtvu6cIo"}).get_text().replace('k','000').replace('.','')
    post = {'vote':vote,'title':title,'subreddit':subreddit,'url':url}
    posts.append(post)
  else:
    pass
  return posts

def sort_list(reddit=[]):
  reddit.sort(key=lambda x:int(x['vote']),reverse=True)
  return reddit


@app.route('/read')
def read():
  reddit = []
  reading =[]
  for subreddit in subreddits:
    subject = request.args.get(subreddit)
    if subject=="on":
      reading.append(subreddit)
      result = requests.get(f"https://www.reddit.com/r/{subreddit}/top/?t=month",headers=headers)
      soup = BeautifulSoup(result.text,"html.parser")
      boxs = soup.find_all("div",{"class":"_1oQyIsiPHYt6nx7VOmd1sz"})
      for box in boxs:
        posts = get_post(box,subreddit)
        reddit = reddit + posts
    else:
      pass
  reddit = sort_list(reddit)
  return render_template("read.html",reddit=reddit,reading=reading)


app.run(host="0.0.0.0")