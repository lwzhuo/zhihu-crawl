class output(object):
    def output(self,datasource):
        try:
            f = open('output.html','w')
            f.write('<html>')
            f.write('<head><style>table,th,td{border:2px solid #D0D0D0;border-collapse:collapse;}</style></head>')
            f.write('<body>')
            f.write('<table style="margin:auto;width:1300px;">')
            f.write('<tr style="background-color:#7FFFD4;width:100%;">')
            f.write('<td style="width:3%;"></td>')
            f.write('<td style="width:15%;">title</td>')
            f.write('<td style="width:35%;">URL</td>')
            f.write('<td style="width:10%;">followers</td>')
            f.write('</tr>')
            count = 1
            for data in datasource:
                try:
                    f.write('<tr style="width:100%;">')
                    f.write('<td style="width:3%%;">%d</td>'%count)
                    f.write('<td style="width:15%%;">%s</td>'%data['title'].encode('utf-8'))
                    f.write('<td style="width:35%%;"><a href="%s">%s</a></td>' % (data['url'],data['url']))
                    f.write('<td style="width:10%%;">%s</td>' % data['followers'])
                    f.write('</tr>')
                    count = count + 1
                except:
                    continue
            f.write('</table>')
            f.write('</body>')
            f.write('</html>')
            f.close()
        except:
            return False
        return True