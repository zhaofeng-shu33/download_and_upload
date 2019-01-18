import os
import oss2
import sys
if __name__ == '__main__':
    access_key_id = os.getenv('AccessKeyId')
    access_key_secret = os.getenv('AccessKeySecret')
    if(access_key_secret is not None):
        auth = oss2.Auth(access_key_id, access_key_secret)
        bucket = oss2.Bucket(auth, 'http://oss-cn-shenzhen.aliyuncs.com', 'freiwilliger')
        # open `main.pdf` and `clustering.pdf` and upload them to the oss server
        file = open(sys.arg[1], 'rb')
        research_base = 'tmp/'
        bucket.put_object(research_base + file, file)
