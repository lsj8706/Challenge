import requests
from flask import Flask, render_template, request
base_url = "http://hn.algolia.com/api/v1"

# This URL gets the newest stories.
new = f"{base_url}/search_by_date?tags=story"
# http://hn.algolia.com/api/v1/search_by_date?tags=story

# This URL gets the most popular stories
popular = f"{base_url}/search?tags=story"
# http://hn.algolia.com/api/v1/search?tags=story

# This function makes the URL to get the detail of a storie by id.
# Heres the documentation: https://hn.algolia.com/api


def make_detail_url(id):
    return f"{base_url}/items/{id}"


db = {}
app = Flask("DayNine")


def get_text(n_or_p):
    articles = []
    result = requests.get(n_or_p)
    result = result.json()
    for hit in result['hits']:
        title = hit['title']
        url = hit['url']
        points = hit['points']
        author = hit['author']
        num_comments = hit['num_comments']
        object_id = hit['objectID']
        article = {'title': title, 'url': url, 'points': points,
                   'author': author, 'num_comments': num_comments, 'object_id': object_id}
        articles.append(article)
    return articles


def get_comments(id):
    comments = []
    result = requests.get(f"https://hn.algolia.com/api/v1/items/{id}")
    result = result.json()
    for child in result['children']:
        comment_author = child['author']
        if comment_author is None:
            comment_author = '[deleted]'
            comment_text = ''
        else:
            comment_text = child['text']
        comment = {'comment_author': comment_author,
                   'comment_text': comment_text}
        comments.append(comment)
    return comments


def get_title_by_id(id):
    result = requests.get(f"https://hn.algolia.com/api/v1/items/{id}")
    result = result.json()
    title = result['title']
    url = result['url']
    points = result['points']
    author = result['author']
    return {'id': id, 'title': title, 'url': url, 'points': points, 'author': author}


@app.route('/')
def index_page():
    order_by = request.args.get('order_by')
    if not order_by or order_by == 'popular':
        existing_pop = db.get('pop')
        if existing_pop:
            pop = existing_pop
        else:
            pop = get_text(popular)
            db['pop'] = pop
        return render_template("index.html", pop=pop)
    elif order_by == "new":
        existing_new = db.get('news')
        if existing_new:
            news = existing_new
        else:
            news = get_text(new)
            db['news'] = news
        return render_template("index.html", pop=news)
    return render_template("index.html")


@app.route('/<id>')
def get_with_id(id):
    comments = get_comments(id)
    article_info = get_title_by_id(id)
    return render_template("detail.html", comments=comments, article_info=article_info)


@app.route('/')
def paging():
    order_by = request.args.get('order_by')


app.run(host="0.0.0.0")
