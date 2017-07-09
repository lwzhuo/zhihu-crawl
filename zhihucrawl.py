from bs4 import BeautifulSoup
import urllib2
import re
import urlparse

def download_page(url):
    response = urllib2.urlopen(url)
    print 'status:',response.getcode()
    if response.getcode()!=200:
        return None
    return response.read()

def parse(html_content):
    soup = BeautifulSoup(html_content,'html.parser',from_encoding='utf-8')
    return soup

def download_new_urls(soup):
    urlset = set()
    tags = soup.find_all('a',class_="zm-item-tag")
    for tag in tags:
        rawurl = tag['href']
        fullurl = urlparse.urljoin("https://www.zhihu.com",rawurl)
        urlset.add(fullurl)
    return urlset

def download_pagedata(soup,page_url):
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

def add_new_url(url,targetbase):
    targetbase.add(url)
    return

def add_new_urls(urls,targetbase):
    for url in urls:
        targetbase.add(url)
    return

def get_url(sourcebase):
    return sourcebase.pop()

def has_url(sourceebase):
    if new_urlbase == None:
        return False
    else:
        return True

def output(datasource):
    f = open('output.html','w')
    f.write('<html>')
    f.write('<head><style>table,th,td{border:2px solid #D0D0D0;border-collapse:collapse;}</style></head>')
    f.write('<body>')
    f.write('<table style="margin:auto;width:1300px;">')
    f.write('<tr style="background-color:#7FFFD4;width:100%;">')
    f.write('<td style="width:15%;">title</td>')
    f.write('<td style="width:35%;">URL</td>')
    f.write('<td style="width:10%;">followers</td>')
    f.write('</tr>')
    for data in datasource:
        f.write('<tr style="width:100%;">')
        f.write('<td style="width:15%%;">%s</td>'%data['title'].encode('utf-8'))
        f.write('<td style="width:35%%;"><a href="%s">%s</a></td>' % (data['url'],data['url']))
        f.write('<td style="width:10%%;">%s</td>' % data['followers'].encode('utf-8'))
        f.write('</tr>')
    f.write('</table>')
    f.write('</body>')
    f.write('</html>')
    f.close()
    return

if __name__ == '__main__':
    new_urlbase = set()
    old_urlbase = set()
    topicbase = []
    start_url = "https://www.zhihu.com/topic/19776749/hot"
    count = 1

    new_urlbase.add(start_url)
    while has_url(new_urlbase):
        try:
            url = get_url(new_urlbase)
            add_new_url(url,old_urlbase)

            html_content = download_page(url)
            htmlPageObj = parse(html_content)

            urls = download_new_urls(htmlPageObj)
            for aurl in urls:
                if aurl in new_urlbase or aurl in old_urlbase:
                    continue
                else:
                    add_new_url(aurl, new_urlbase)

            topicbase.append(download_pagedata(htmlPageObj,url))
            print count,"add",len(urls),"urls","newurlbase:",len(new_urlbase)," oldurlbase:",len(old_urlbase)
            print "*******************"
            if count == 1000:
                break
            count = count + 1
        except:
            print 'failed'
    print "end"

    output(topicbase)




