from gevent import monkey
import gevent
import time
import urllib.request

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
        self.file_name_list = ['https://upload4.hlgnet.com/baby/upload/2012/08/134431253157.jpg_t.jpg','https://upload4.hlgnet.com/uploadphoto/home/2014/2014-07-06/20140706082831_6714.jpg','abc']
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


    def write_file(self,file_content,i):
        with open(f'.\html\pics\{i}.{self.file_type}','wb') as f:
            f.write(file_content)
        self.down_count += 1


def main():
    url =''
    file_type = 'jpg'
    paraller_num = 5
    downloader = Downloader(url,file_type,paraller_num)
    downloader.download_file()

#    gevent.joinall([
#        gevent.spawn(func,10,'f1'),
#        gevent.spawn(func,10,'f2') ])

if __name__ == '__main__':
    main()
