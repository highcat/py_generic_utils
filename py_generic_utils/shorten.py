# -*- coding: utf-8 -*-
# Сокращение строк и ссылок

def shorten(url, max_len=70):
    if max_len<30:
        max_len = 30 # меньше нет смысла - и неверно работает
    url_len = len(url)
    if url_len>max_len:
        # заменяем на многоточие, по возможности вторую треть адреса
        # сколько убрать
        to_remove = url_len-max_len+3
        # точка замены
        l = url_len/3*2 + url_len/6
        # минимальное число символов в конце
        min_end = 15
        visible_end = url_len-min_end
        # корректируем
        if l+to_remove/2 > visible_end:
            l -= (l+to_remove/2 - visible_end)
        
        return url[:l-to_remove/2]+'...'+url[l+to_remove/2:]
    return url

def shorten_span(s, max_len=40):
    """ сократить, полное имя показать в тайтле """
    return '<span title="%s">%s</span>' % (s, shorten(s, max_len))

def shorten_link(s, max_len=40):
    """ ссылка: сократить, полное имя показать в тайтле """
    href = s if s.startswith(("http://", "https://")) else "http://"+s
    return '<a href="%s" title="%s">%s</a>' % (href, s, shorten(s, max_len))

def shorten_noend(s, max_len=40):
    """ сократить, концовку не показывать """
    return '<span title="%s">%s%s</span>' % (s, s[:max_len], '...' if len(s)>max_len else '')
