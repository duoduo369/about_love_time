#!/usr/bin/env python
# -*- coding: utf-8 -*-
import arrow

CONFIG = [
    (u'相遇', '2018-01-29'),
    (u'第一次深聊', '2018-05-11'),
    (u'确认情侣关系', '2018-05-20'),
    (u'第一次去远方', '2018-06-02'),
    (u'第一次给我过生日', '2018-06-22'),
    (u'非正式吵架', '2018-06-30'),
    (u'去你家见叔叔阿姨', '2018-09-16'),
    (u'去五莲', '2018-10-01'),
    (u'来我家看我妈妈', '2018-10-05'),
    (u'一起看话剧', '2018-10-06'),
]

def main(config=CONFIG):
    now = arrow.now()
    print u'齐百慧'
    for each in config:
        key, date = each
        days = (now - arrow.get(date)).days
        print u'从我们{}至今已经 {} 天了'.format(key, days)


if __name__ == '__main__':
    main()
