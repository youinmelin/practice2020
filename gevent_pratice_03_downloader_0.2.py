from gevent import monkey
import gevent
import time
import urllib.request
import re
import gzip

monkey.patch_all()

class Downloader():
    def __init__(self,url,file_type,paraller_num):
        self.url = url
        self.file_type = file_type
        self.paraller_num= paraller_num
        self.file_name_list = []
        self.down_count = 0
        self.fail_count = 0

    def download_file(self):
        self.search_file()
        for i,self.file_name in enumerate(self.file_name_list):
            try:
                ret = urllib.request.urlopen(self.file_name)
            except Exception:
                self.fail_count += 1
            else:
                file_content = ret.read()
                self.write_file(file_content,i)
        print ('download files num:',self.down_count)
        print ('failed num:',self.fail_count)


    def search_file(self):
        try:
            ret = urllib.request.urlopen(self.url)
        except Exception as e:
            print (e)
        else:
            page_data = ret.read()
#            page_data = gzip.decompress(page_data)
            page_data = page_data.decode('utf-8')
            #print(page_data)
#            self.file_name_list = re.findall(r"https://.*?\.jpg", page_data)
            self.file_name_list = re.findall(r'<img src="(https://.*?.jpg)"', page_data)
#            print(self.file_name_list)

    def write_file(self,file_content,i):
        with open(f'.\html\pics\{i}.{self.file_type}','wb') as f:
            f.write(file_content)
        self.down_count += 1


def main():
    url ='https://www.hlgnet.com'
    file_type = 'jpg'
    paraller_num = 5
    downloader = Downloader(url,file_type,paraller_num)
    downloader.download_file()
    downloader.search_file()

#    gevent.joinall([
#        gevent.spawn(func,10,'f1'),
#        gevent.spawn(func,10,'f2') ])

if __name__ == '__main__':
    main()
