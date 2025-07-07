import requests


class NewsFeed:
    base_url = "https://newsapi.org"
    api_key = "56d3f85d2e5f42c993f0f3877fa75e53"


    def __init__(self,interest,from_date, to_date, language="en"):
        self.interest = interest
        self.from_date = from_date
        self.to_date = to_date
        self.language = language
        

    def get(self):
        url = self._build_url()

        articles = self._get_articles(url)


        email_body=""
        for article in articles:
            email_body += f"{article['title']}\n{article['url']}\n\n"

        return email_body
    
    def _get_articles(self,url):
        response = requests.get(url)
        content=response.jsom()
        articles = content['articles']
        return articles
    
    def __build_url(self):
        url = f"{self.base_url}/v2/everything?q={self.interest}&from={self.from_date}&to={self.to_date}&language={self.language}&apiKey={self.api_key}"
        return url
    

    if __name__ == "__main__":
        news_feed = NewsFeed(interest="Python", from_date="2023-10-01", to_date="2023-10-02")
        print(news_feed.get())