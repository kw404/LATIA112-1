import scrapy
from bs4 import BeautifulSoup
from myproject.items import MyItem


class MySpider(scrapy.Spider):
    name = "myspider"
    start_urls = ["https://www4.inservice.edu.tw/script/IndexQuery.aspx?school=10"]

    def parse(self, response):
        soup = BeautifulSoup(response.text, "lxml")
        data_column_name = ["課程代碼", "研習名稱", "性質", "課程開始日期", "課程結束日期", "辦理研習單位", "開課地點"]

        while True:
            for row in self.get_data(response):
                item = MyItem()
                item["data"] = row[1:]
                yield item

            next_button = soup.find("input", {"id": "ImageButton8"})
            if not next_button:
                break

            yield scrapy.FormRequest.from_response(
                response,
                formdata={"__EVENTTARGET": "ImageButton8"},
                callback=self.parse,
            )

    def get_data(self, response):
        count = 0
        table = response.css("table.csscts")
        if table:
            for tr in table.css("tr"):
                row = tr.css("td.wide-only::text").extract()
                count += 1
                if count % 8 == 0:
                    yield row[1:]
