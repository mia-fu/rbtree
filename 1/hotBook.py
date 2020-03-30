# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup


def get_url(root_url, start):
    return root_url + "?start=" + str(start) + "&filter="


def get_review(page_url):
    movies_list = []
    response = requests.get(page_url)
    soup = BeautifulSoup(response.text, "lxml")
    # 书名
    allbook = soup.find_all('div', 'pl2')
    names = [b.find('a')['title'] for b in allbook]
    # 作者名
    allauthor = soup.find_all('p', 'pl')
    authors = [a.get_text() for a in allauthor]
    # 评分
    allscore = soup.find_all('span', 'rating_nums')
    scores = [s.get_text() for s in allscore]
    # 书评
    alldesc = soup.find_all('span', 'inq')
    descs = [d.get_text() for d in alldesc]
    for name, author, score, desc in zip(names, authors, scores, descs):
        dict = {}
        dict['name'] = str(name) + '\n'
        dict['author'] = str(author).split('/')[0] + '\n'
        dict['score'] = str(score) + '\n'
        dict['desc'] = str(desc) + '\n'
        movies_list.append(dict)
    return movies_list


if __name__ == "__main__":
    root_url = "https://book.douban.com/top250"
    start = 0
    filename = 'D:\DoubanBookTop250.txt'
    f = open(filename, 'w')
    while (start < 250):
        movies_list = get_review(get_url(root_url, start))
        for movie_dict in movies_list:
            print '图书名称：' + movie_dict.get('name')
            print '作者名称: ' + movie_dict.get('author')
            print '图书评分: ' + movie_dict.get('score')
            print('图书评词：' + movie_dict.get('desc', '无评词'))
            print('------------------------------------------------------')
            '''
            写入txt文件
            '''
            f.write('图书名称：' + movie_dict.get('name'))
            f.write('作者名称: ' + movie_dict.get('author'))
            f.write('图书评分: ' + movie_dict.get('score'))
            f.write('图书评词：' + movie_dict.get('desc', '无评词'))
            f.write('------------------------------------------------------' + '\n')
        start += 25
