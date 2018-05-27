# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import urllib3
import os


class DoubanmoviePipeline(object):
    i = 0

    def __init__(self):
        if os.path.exists('movie.txt'):
            os.remove('movie.txt')


    def process_item(self, item, spider):
        print('starting save...')
        for name in item['name']:
            print(name)
            for pic in item['pic']:
                print(pic)
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0'}
                req = urllib3.Request(url=pic, headers=headers)
                res = urllib3.urlopen(req)
                file_name = os.path.join(r'D:\my\down_pic'+ name + '.jpg')
                print('123')
                with open(file_name, 'wb') as  fp:
                    fp.write(res.read())