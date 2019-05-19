#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-5-17 上午11:13
import  requests
from bs4 import BeautifulSoup
import xlwt

def main(page):
    url = 'https://movie.douban.com/top250?start='+ str(page*25)+'&filter='
    print(url)
    html=request_douban(url)
    soup=BeautifulSoup(html,'lxml')
    save_to_excel(soup)

def request_douban(url):
    try:
        response=requests.get(url)
        if response.status_code==200:
            return response.text
    except requests.RequestException:
        return None
    pass

def save_to_excel(soup):
    index=0
    movie_list=soup.find(class_="grid_view").find_all('li')#因为class是python的关键字，所以在写过滤时写成class_
    movie_book=xlwt.Workbook(encoding='utf-8',style_compression=0)
    movie_sheet=movie_book.add_sheet('豆瓣电影Top250',cell_overwrite_ok=True)
    if movie_sheet:
        movie_sheet.write(0, 0, '名称')
        movie_sheet.write(0, 1, '图片')
        movie_sheet.write(0, 2, '排名')
        movie_sheet.write(0, 3, '评分')
        movie_sheet.write(0, 4, '作者')
        movie_sheet.write(0, 5, '简介')

    for item in movie_list:
        index=index+1
        item_name=item.find(class_='title').string
        item_img=item.find('a').find('img').get('src')
        item_index=item.find(class_='').string
        item_score=item.find(class_='rating_num').string
        item_author=item.find('p').text #.get_text()
        #item_intr = item.find(class_='inq').string
        print('爬取电影：' + item_index + ' | ' + item_name  +' | ' + item_score  +' | ' + 'item_intr' )
        if movie_sheet:
            movie_sheet.write(index+1,1,item_img)
            movie_sheet.write(index+1,2,item_index)
            movie_sheet.write(index+1,3,item_score)
            movie_sheet.write(index+1,4,item_author)
            #movie_sheet.write(index+1,5,item_intr)
    movie_book.save('豆瓣电影250.xlsx')





if __name__=="__main__":
    for i in range(0,10):
       main(i)

