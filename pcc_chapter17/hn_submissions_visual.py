from plotly.graph_objs import Bar
from plotly import offline

from datetime import date

from operator import itemgetter

import requests

# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    # Make a separate API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # Build a dictionary for each article.
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict['descendants'],
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                            reverse=True)

# Assemble data for visualization.
sub_urls, sub_comments = [], []
for submission_dict in submission_dicts:
    sub_title = submission_dict['title']
    sub_url = submission_dict['hn_link']
    sub_urls.append(f"<a href='{sub_url}'>{sub_title}</a>")
    
    sub_comments.append(submission_dict['comments'])

current_date = date.today()
title_date = current_date.strftime("%Y-%m-%d")

# Make visualization.
data = [{
    'type': 'bar',
    'x': sub_urls,
    'y': sub_comments,
    'hovertext': {'color': 'rgb(255, 255, 255)'},
    'marker': {'color': 'rgb(255, 102, 0)'},
    'opacity': 0.8,
}]

my_layout = {
    'title': f"Hacker News Popular Discussions {title_date}",
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Submissions',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Comments',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='hn_popular_discussions.html')