from gevent import monkey
import gevent
import time
import urllib.request
import re
import gzip

monkey.patch_all()

class Downloader():
    def __init__(self,url,file_type):
        self.url = url
        self.file_type = file_type
        self.file_name_list = []
        self.down_count = 0
        self.fail_count = 0
        self.i = 0
        # 变量i在循环方法外设置初始值，是因为download_file方法被gevent调用多次，如果多次调用，就会将i重新置零，循环就要多次执行。这样，多个协程就可以共享i变量，接力往下执行循环。这也是不能用for循环的原因。
    
    def download_file(self):
        while self.i < len(self.file_name_list):
            try:
                ret = urllib.request.urlopen(self.file_name_list[self.i])
            except Exception:
                self.fail_count += 1
            else:
                file_content = ret.read()
                self.write_file(file_content,self.i)
                print(self.i,end='>')
            finally:
                self.i += 1

    def search_file(self):
        import requests
        try:
            # 改用requests方法获取网页内容，可以成功获取sina sohu等网站信息，但是必须把协程相关的代码删除，否则报错，原因不明,报错提示如下
            '''
            gevent_pratice_03_downloader.py:9: MonkeyPatchWarning: Monkey-patching ssl after ssl has already been imported may lead to errors, including RecursionError on Python 3.6. It may also silently lead to incorrect behaviour on Python 3.7. Please monkey-patch earlier. See https://github.com/gevent/gevent/issues/1016. Modules that had direct imports (NOT patched): ['urllib3.util.ssl_ (C:\\Users\\Administrator\\Local Settings\\Application Data\\Programs\\Python\\Python37\\lib\\site-packages\\urllib3\\util\\ssl_.py)', 'urllib3.util (C:\\Users\\Administrator\\Local Settings\\Application Data\\Programs\\Python\\Python37\\lib\\site-packages\\urllib3\\util\\__init__.py)'].
            已查明原因，按照报错的提示打开网站，答复如下
           The problem is that you're importing requests before you monkey patch. You must monkey patch before importing anything else. 将patchall和import requests改变顺序就好了。 
            '''
            # 定义请求头的浏览器代理，伪装成浏览器
            headers = {'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
            res = requests.get(self.url,headers=headers)
            print('pagedata:',res)
            # res = urllib.request.urlopen(self.url)
        except Exception as e:
            print ('e',e)
        else:
            page_data = res.text
            #page_data = page_data.decode('utf-8')
            #print(page_data)
#            self.file_name_list = re.findall(r"https://.*?\.jpg", page_data)
            re_str = r'src="(.*?\.jpg)"'
            self.file_name_list = re.findall(re_str, page_data)
            if len(self.file_name_list) == 0:
                try:
                    page_data = res.text
                    page_data = gzip.decompress(page_data)
                    page_data = page_data.decode('gbk')
                except Exception as e:
                    print(e)
                else:
                    self.file_name_list = re.findall(re_str, page_data)
        print(len(self.file_name_list))

    def write_file(self,file_content,name):
        with open(f'.\html\pics\{name}.{self.file_type}','wb') as f:
            f.write(file_content)
        self.down_count += 1


def main():
    site = input('input site name:')
    url =f'https://{site}'
    #url = 'http://www.772586.com/tag/danai/'
    #url = 'edu.csdn.net'
    file_type = 'jpg'
    downloader = Downloader(url,file_type)
    downloader.search_file()
    downloader.download_file()
    gevent.joinall([
        gevent.spawn(downloader.download_file),
        gevent.spawn(downloader.download_file),
        gevent.spawn(downloader.download_file),
        gevent.spawn(downloader.download_file)
        ])
    print ('\ndownload files num:',downloader.down_count)
    print ('failed num:',downloader.fail_count)

if __name__ == '__main__':
    main()
