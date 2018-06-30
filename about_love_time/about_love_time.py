#!/usr/bin/env python
# -*- coding: utf-8 -*-
import arrow

CONFIG = [
    (u'第一次相遇', '2018-01-29'),
    (u'第一次深聊', '2018-05-11'),
    (u'确认情侣关系', '2018-05-20'),
    (u'第一次去远方', '2018-06-02'),
    (u'第一次一起过生日', '2018-06-22'),
    (u'非正式吵架', '2018-06-30'),
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
