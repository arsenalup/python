import requests
import base64
import time
import re


class xiaobing():
    def __init__(self):
        self.upload_url = 'https://kan.msxiaobing.com/Api/Image/UploadBase64'
        self.com_url = 'https://kan.msxiaobing.com/Api/ImageAnalyze/Process'

    def _get_raw_img_url(self, in_file):
        with open(in_file, 'rb') as f_stream:
            img_base64 = base64.b64encode(f_stream.read())
        resp = requests.post(self.upload_url, data=img_base64)
        # print(resp.json())
        return 'https://mediaplatform.msxiaobing.com' + resp.json()['Url']

    def _get_judgement(self, img_url):
        sys_time = int(time.time())
        paload = {'service':'yanzhi',
                  'tid':'093525ed49fc4c2ba97e022f7cf648fb'}
        form = {'MsgId':str(sys_time)+'731',
                'CreateTime': sys_time,
                'Content[imageUrl]': img_url,
                }
        resp = requests.post(self.com_url, params=paload, data=form)
        print(sys_time)
        print(resp.json())
        return resp.json()['content']['text']

    @staticmethod
    def _extract_point(text):
        match = re.search(r'\d.?\d?', text)
        point_str = match.group(0)
        return int(float(point_str)*10)

    def rank(self, input_, is_num=False):
        raw_url = self._get_raw_img_url(input_)
        judgement = self._get_judgement(raw_url)
        if is_num:
            return self._extract_point(judgement)
        return judgement


if __name__ == '__main__':
    xb = xiaobing()
    print(xb.rank(r'luxian.png', is_num=False))
