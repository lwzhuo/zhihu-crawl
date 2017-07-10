class url_manager(object):
    def add_new_url(self,url,targetbase):
        targetbase.add(url)
        return

    def add_new_urls(self,urls,targetbase):
        for url in urls:
            targetbase.add(url)
        return

    def get_url(self,sourcebase):
        if sourcebase != None:
            return sourcebase.pop()
        else:
            return None

    def has_url(self,sourcebase):
        if sourcebase == None:
            return False
        else:
            return True

    def reportStatus(self):
        pass
