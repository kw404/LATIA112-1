import scrapy
from bs4 import BeautifulSoup


class FromwebSpider(scrapy.Spider):
    name = "fromweb"
    start_urls = ["https://www.cksh.tp.edu.tw/category/news/news_1/"]

    def parse(self, response):
        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.find("table", class_="nt_table").text

        print(title)

        rows = response.css("table tbody tr")

        for row in rows:
            post_date = row.css("td.nt_date::text").get()
            title = row.css("a.news_title::text").get()
            unit = row.css("td.nt_unit::text").get()

            yield {"Unit": unit, "Post Date": post_date, "Title": title}
