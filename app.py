from flask import Flask,render_template
from newsapi import NewsApiClient

app = Flask(__name__)

# creating the route function and render html  files that
@app.route('/')
def home():
      # creating the client id and api_key for authorization
      newsapi = NewsApiClient(api_key="1a7abb11a1f1404491e762c18fd25f3e")

      return render_template('home.html')

      top_headlines = newsapi.get_top_headlines(sources = 'bbc-news')
      
      t_articles = top_headlines['articles']
      # making a list of contents to store the values on the list
      news = []
      desc = []
      p_date = []
      url = []

     # fetching all the contents of the articles using loop
      for i in range(len(t_article)):
            main_article = t_articles[i]

            news.append(main_article['title'])
            desc.append(main_article['description'])
            img.append(main_article['urlToImage'])
            p_date.append(main_article['publishedAt'])
            url.append(main_article['url'])


if __name__ == '__main__':
    app.run(debug=True)

