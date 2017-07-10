from bs4 import BeautifulSoup
import re
import urlparse

class parser(object):
    def parse(self,html_content):
        soup = BeautifulSoup(html_content,'html.parser',from_encoding='utf-8')
        return soup

    def download_new_urls(self,soup):
        urlset = set()
        tags = soup.find_all('a',class_="zm-item-tag")
        for tag in tags:
            rawurl = tag['href']
            fullurl = urlparse.urljoin("https://www.zhihu.com",rawurl)
            urlset.add(fullurl)
        return urlset

    def download_pagedata(self,soup,page_url):
        topic = {}
        title = soup.title
        followers = soup.find(class_ = "zm-topic-side-followers-info")
        try:
            followers = followers.contents[1].get_text()
        except:
            followers = None
        print title.get_text(),'followers:',followers,page_url
        topic['title'] = title.get_text()
        topic['url'] = page_url
        topic['followers'] = followers
        return topic