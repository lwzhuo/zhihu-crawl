import urllib2

class download(object):
    def download_page(self,url):
        response = urllib2.urlopen(url)
        print 'status:', response.getcode()
        if response.getcode() != 200:
            return None
        return response.read()