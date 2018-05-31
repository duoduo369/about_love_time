#!/usr/bin/env python
# -*- coding: utf-8 -*-
import arrow

CONFIG = [
    (u'第一次相遇', '2018-01-29'),
    (u'第一次深聊', '2018-05-11'),
    (u'确认情侣关系', '2018-05-20'),
]

def main(config=CONFIG):
    now = arrow.now()
    print u'齐百慧'
    for each in config:
        key, date = each
        days = (now - arrow.get(date)).days
        print u'从我们{}至今 已经 {} 天了'.format(key, days)


if __name__ == '__main__':
    main()
