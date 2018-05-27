# -*- coding: utf-8 -*-
import scrapy

from DouBanMovie.items import MovieItem


class DoubanSpider(scrapy.Spider):
    name = 'db'
    start_urls = ['file:///D:/douban.htm']
    print('Spider Starting...')

    def parse(self, response):
        print('Spider Downloading...')
        allMovie = response.xpath('// *[ @ id = "content"] / div / div[1] / div / div / table')
        for each_movie in allMovie:
            item = MovieItem()
            name = each_movie.xpath('./ tbody / tr / td[1] / a / img/@alt').extract()
            pic = each_movie.xpath('./ tbody / tr / td[1] / a / img/@src').extract()
            item['name'] = name
            item['pic'] = pic
            yield item

