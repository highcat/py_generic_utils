# -*- coding: utf-8 -*-
# Сокращение строк и ссылок

def shorten(s, max_len=70):
    assert(isinstance(max_len, int))
    if max_len<30:
        max_len = 30 # меньше нет смысла - и неверно работает
    s_len = len(s)
    if s_len>max_len:
        # заменяем на многоточие, по возможности вторую треть адреса
        # сколько убрать
        to_remove = s_len-max_len+3
        # точка замены
        l = s_len/3*2 + s_len/6
        # минимальное число символов в конце
        min_end = 15
        visible_end = s_len-min_end
        # корректируем
        if l+to_remove/2 > visible_end:
            l -= (l+to_remove/2 - visible_end)
        
        return s[:l-to_remove/2]+'...'+s[l+to_remove/2:]
    return s

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
