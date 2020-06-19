from django.shortcuts import render
from .sz_spider.lib.spider.ershou_spider import *
from .sz_spider.lib.spider.zufang_spider import *
from .sz_spider.lib.spider.loupan_spider import *
# Create your views here.


def index(request):

    return render(request,'index.html',locals())

def search(request):
    if request.method == 'POST':
        house_type = request.POST.get('house_type')
        area = request.POST.get('area')

        if house_type == 'ershou':
            spider = ErShouSpider(SPIDER_NAME)
            spider.start(area)
        elif house_type == 'zufang':
            spider = ZuFangBaseSpider(SPIDER_NAME)
            spider.start(area)

        elif house_type == 'loupan':
            spider = LouPanBaseSpider(SPIDER_NAME)
            spider.start(area)
    return render(request,'serach.html')
