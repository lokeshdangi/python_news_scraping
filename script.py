import bs4 as bs
import urllib.request

#Latest News
with open("index.html", "w") as file:
    file.write(str('<html><head><title>Comprehensive up-to-date news coverage, aggregated from sources all over the world</title><style>p,h2{  font-size: 18px;line-height: 1.58;letter-spacing: -.004em;font-family: medium-content-serif-font,Georgia,Cambria,"Times New Roman",Times,serif;}h3,h2{font-family: medium-content-sans-serif-font,"Lucida Grande","Lucida Sans Unicode","Lucida Sans",Geneva,Arial,sans-serif; font-size: 20px;margin-left: -2.13px;line-height: 1.04;letter-spacing: -.015em;}.butn{a{  text-decoration:none;}</style> <script async src='+'"'+"//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"+'"'+'></script><script>(adsbygoogle = window.adsbygoogle || []).push({google_ad_client: '+'"'+'ca-pub-9964056295163738'+'"'+',enable_page_level_ads: true});</script>'))
    file.write(str("""  <meta name="description" content="latest news,news,scraped news">"""))
    file.write(str("""  <meta name="keywords" content="news, india news">"""))
    file.write(str('</head><body><ul>'))
for i in range(1,10):
    sauce = urllib.request.urlopen('http://indianexpress.com/latest-news/'+ str(i)).read()
    soup = bs.BeautifulSoup(sauce,'lxml')
    nation = soup.find_all('div',class_ = 'articles')
    for title in nation :
        try:
            z = title.find_all('a')[1].text
        except IndexError:
            z = title.find_all('a')[0].text
        z = z.replace(u'\xa0', u' ')
        z = z.replace(':','')
        z = z.replace('/','')
        z = z.replace(',','')
        z = z.replace('?','')
        z = z.replace(' ','-')
        sauce = urllib.request.urlopen(title.find_all('a')[0].get('href')).read()
        soup = bs.BeautifulSoup(sauce,'lxml')
        nation1 = soup.find('div',class_ = 'full-details')
        X = nation1.find_all('p')
        try:
            with open(z+".html", "a") as file:
                file.write(str('<html><head><title>Miner</title><style>p,h2{  font-size: 18px;line-height: 1.58;letter-spacing: -.004em;font-family: medium-content-serif-font,Georgia,Cambria,"Times New Roman",Times,serif;}h3,h2{font-family: medium-content-sans-serif-font,"Lucida Grande","Lucida Sans Unicode","Lucida Sans",Geneva,Arial,sans-serif; font-size: 20px;margin-left: -2.13px;line-height: 1.04;letter-spacing: -.015em;}.butn{a{  text-decoration:none;}</style> <script async src='+'"'+"//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"+'"'+'></script><script>(adsbygoogle = window.adsbygoogle || []).push({google_ad_client: '+'"'+'ca-pub-9964056295163738'+'"'+',enable_page_level_ads: true});</script></head><body>'))
                try:
                    file.write(str('<h2>'+ title.find_all('a')[1].text + '</h2>')) 
                except IndexError:
                    file.write(str('<h2>'+ title.find_all('a')[0].text + '</h2>')) 
                X = X[:-1]
                for x in X:
                    try:
                        file.write(str('<p>'+ x.text + '</p>'))
                    except UnicodeEncodeError:
                        pass  
        except OSError:
            pass
        with open("index.html", "a") as file:
            try:
                file.write(str('<li><h2><a target = '+"'"+'_blank'+"'"+' href ='+"'"+z+".html"+"'"+'>'+title.find_all('a')[1].text + '</a></h2></li>'))
            except IndexError:
                file.write(str('<li><h2><a target = '+"'"+'_blank'+"'"+' href ='+"'"+z+".html"+"'"+'>'+title.find_all('a')[0].text + '</a></h2></li>'))
          
            file.write(str('<p>'+ title.find_all('p')[0].text + '</p>')) 
