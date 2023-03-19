def min_max(li):
    str_li = []
    for i,data in enumerate(li):
        if '#' in data:
            str_li.append(i)
    if len(str_li) > 1:
        return str_li[0], str_li[-1]+1

    return str_li[0], str_li[0]+1

def solution(wallpaper):
    return sum(list(map(list,zip(min_max(wallpaper),min_max(zip(*wallpaper))))),[])