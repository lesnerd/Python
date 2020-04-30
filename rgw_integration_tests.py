import unittest
import requests
import time
import logging
import json

logging.basicConfig(filename='pyrgw.log',
                    format='%(name)s %(levelname)s %(message)s')
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class Tools(object):

    @staticmethod
    def print_request(req):
        print('============ Request ============\n')
        print('HTTP/1.1 {method} {url}\n{headers}\n\n{body}'.format(
            method=req.method,
            url=req.url,
            headers='\n'.join('{}: {}'.format(k, v)
                              for k, v in req.headers.items()),
            body=json.dumps(json.loads(req.body.decode("utf-8")
                                       if req.body is not None else '{}'), indent=4),
        ))

    @staticmethod
    def print_response(res):
        print('============ Response ============\n')
        print('HTTP/1.1 {status_code}\n{headers}\n\n{body}'.format(
            status_code=res.status_code,
            headers='\n'.join('{}: {}'.format(k, v)
                              for k, v in res.headers.items()),
            body=json.dumps(json.loads(res.content.decode("utf-8")), indent=4),
        ))

# For reference https://requests.readthedocs.io/en/master/


class TestRGW(unittest.TestCase):

    def __init__(self, methodName):
        super().__init__(methodName)
        self.session_key = None
        self.transaction_id = None

    def test_create_tranaction(self):
        url = 'http://192.168.1.108/retailgateway/api/selling/v1/saletransactions/4801?createNew=true'
        headers = {'Retailer': 'Retailer',
                   'TouchPoint': 'MobileShopper',
                   'StoreID': '110'}
        r = requests.put(url, headers=headers)
        Tools.print_request(r.request)
        Tools.print_response(r)
        parsed = json.loads(r.text)
        assert parsed.get('SalesTransaction').get(
            'TransactionStatus') == 'InProcess'


if __name__ == '__main__':
    unittest.main()
