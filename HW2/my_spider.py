import scrapy


class MySpider(scrapy.Spider):
    name = "my_spider"
    start_urls = ["https://www4.inservice.edu.tw/script/IndexQuery.aspx?school=10"]

    def parse(self, response):
        data_column_name = ["課程代碼", "研習名稱", "性質", "課程開始日期", "課程結束日期", "辦理研習單位", "開課地點"]

        # Extract data from the current page
        rows = response.css("table.csscts tr")
        for row in rows:
            row_data = row.css("td.wide-only::text").getall()
            if len(row_data) == len(data_column_name):
                yield dict(zip(data_column_name, row_data[1:]))

        # Follow to the next page if available
        next_page = response.css("#ImageButton8::attr(href)").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
