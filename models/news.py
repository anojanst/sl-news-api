from requests_html import HTMLSession


class News():

    def daily_mirror(self):

        session = HTMLSession()
        url = "https://www.dailymirror.lk/latest-news/342"
        r = session.get(url)

        articles = r.html.find('.lineg')

        all_news = []
        for a in articles:
            l = a.find('a', first=True)
            for val in l.absolute_links:
                news_link = val

            details = a.find('p', first=False)
            i = 0
            desc = ""
            for d in details:
                if i == 1:
                    desc = d.text
                i += 1
            news = {
                'title': a.find('h3', first=True).text,
                'time': a.find('.gtime', first=True).text,
                'description': desc,
                'link': news_link,
                'src': 'Daily Mirror'
            }

            all_news.append(news)

        return all_news

    def tamil_mirror(self):

        session = HTMLSession()
        url = "https://www.tamilmirror.lk/news/175"
        r = session.get(url)

        articleSection = r.html.find('.lineg')

        for section in articleSection:
            articles = section.find('.row')

            all_news = []
            for a in articles:
                l = a.find('a', first=True)
                for val in l.absolute_links:
                    news_link = val

                if a.find('.cat-hd-tx', first=True):
                    title = a.find('.cat-hd-tx', first=True).text

                if a.find('.gtime', first=True):
                    time = a.find('.gtime', first=True).text
                desc = ""
                if a.find('.ptext', first=True):
                    desc = a.find('.ptext', first=True).text

                news = {
                    'title': title,
                    'time': time,
                    'description': desc,
                    'link': news_link,
                    'src': 'Tamil Mirror'
                }

                all_news.append(news)

            return all_news

    def newswire(self):

        session = HTMLSession()
        url = "https://www.newswire.lk/category/news/"
        r = session.get(url)

        articles = r.html.find('article')

        all_news = []
        for a in articles:
            l = a.find('a', first=True)
            for val in l.absolute_links:
                news_link = val

            details = a.find('.entry-summary', first=False)
            desc = ""
            for d in details:
                if d.find('p', first=True):
                    desc = d.find('p', first=True).text

            news = {
                'title': a.find('h2', first=True).text,
                'time': a.find('.entry-published', first=True).text,
                'description': desc.replace("Continue Reading", ""),
                'link': news_link,
                'src': 'News Wire'
            }

            all_news.append(news)

        return all_news

    def newsfirstenglish(self):

        session = HTMLSession()
        url = "https://www.newsfirst.lk/latest-news/"
        r = session.get(url)

        articles = r.html.find('.desktop-news-block-ppd')

        all_news = []
        for a in articles:
            l = a.find('a', first=True)
            for val in l.absolute_links:
                news_link = val

            if a.find('h2', first=True):
                title = a.find('h2', first=True).text

            if a.find('p', first=True):
                time = a.find('p', first=True).text

            news = {
                'title': title,
                'time': time,
                'description': '',
                'link': news_link,
                'src': 'News First English'
            }

            all_news.append(news)

        return all_news

    def newsfirsttamil(self):

        session = HTMLSession()
        url = "https://www.newsfirst.lk/tamil/latest-news/"
        r = session.get(url)

        articles = r.html.find('.desktop-news-block-ppd')

        all_news = []
        for a in articles:
            l = a.find('a', first=True)
            for val in l.absolute_links:
                news_link = val

            if a.find('h2', first=True):
                title = a.find('h2', first=True).text

            if a.find('p', first=True):
                time = a.find('p', first=True).text

            news = {
                'title': title,
                'time': time,
                'description': '',
                'link': news_link,
                'src': 'News First Tamil'
            }

            all_news.append(news)

        return all_news

    def newsfirstsinhala(self):

        session = HTMLSession()
        url = "https://www.newsfirst.lk/sinhala/latest-news/"
        r = session.get(url)

        articles = r.html.find('.desktop-news-block-ppd')

        all_news = []
        for a in articles:
            l = a.find('a', first=True)
            for val in l.absolute_links:
                news_link = val

            if a.find('h2', first=True):
                title = a.find('h2', first=True).text

            if a.find('p', first=True):
                time = a.find('p', first=True).text

            news = {
                'title': title,
                'time': time,
                'description': '',
                'link': news_link,
                'src': 'News First Sinhala'
            }

            all_news.append(news)

        return all_news
