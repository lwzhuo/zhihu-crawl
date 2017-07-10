# -*- coding: utf-8 -*-
import crawl_status,urlmanager,page_downloader,outputer,page_parser

if __name__ == '__main__':
    new_urlbase = set()
    old_urlbase = set()
    topicbase = []
    start_url = "https://www.zhihu.com/topic/19776749/hot"
    count = 1
    urlman = urlmanager.url_manager()
    downloader = page_downloader.download()
    outputer = outputer.output()
    parser = page_parser.parser()

    new_urlbase.add(start_url)
    while urlman.has_url(new_urlbase):
        try:
            report = crawl_status.status()

            url = urlman.get_url(new_urlbase)
            urlman.add_new_url(url,old_urlbase)

            html_content = downloader.download_page(url)
            htmlPageObj = parser.parse(html_content)

            urls = parser.download_new_urls(htmlPageObj)
            for aurl in urls:
                if aurl in new_urlbase or aurl in old_urlbase:
                    continue
                else:
                    urlman.add_new_url(aurl, new_urlbase)

            topicbase.append(parser.download_pagedata(htmlPageObj,url))
            print count,"add",len(urls),"urls","newurlbase:",len(new_urlbase)," oldurlbase:",len(old_urlbase)

            report.addStatus("crawl", "success")
            print report.showDetailList()
            print "*******************"
            if count == 1:
                break
            count = count + 1
        except:
            report.addStatus("crawl","failed")
            print report.showDetailList()
    print "crawl end,start output"

    if outputer.output(topicbase) :
        report.addStatus("output", "success")
    else:
        report.addStatus("output", "failed")
    print report.showDetailList()




