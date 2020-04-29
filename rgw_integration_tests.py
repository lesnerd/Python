import unittest
import pip._vendor.requests
import time
import logging
import json

logging.basicConfig(filename='pyrgw.log',
                    format='%(name)s %(levelname)s %(message)s')
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# For reference https://requests.readthedocs.io/en/master/


class TestRGW(unittest.TestCase):

    def __init__(self, methodName):
        super().__init__(methodName)
        self.session_key = None
        self.transaction_id = None

    def test_create_tranaction(self):
        url = 'http://localhost/RetailGateway/api/selling/v1/saletransactions/4801?createNew=true'
        headers = {'Retailer': 'Retailer',
                   'TouchPoint': 'MobileShopper',
                   'StoreID': '110'}
        r = pip._vendor.requests.put(url, headers=headers)
        print_request(r.r)
        print_response(r.Response)
        # assert r.
        # print('============ Response Header ============\n')
        # for k, v in r.headers.items():
        #     print('key: ' + k + ' value: ' + v)
        # parsed = json.loads(r.text)
        # print('============ Response Body ============\n')
        # print(json.dumps(parsed, indent=4) + '\n')

    def print_request(self, req):
        print('HTTP/1.1 {method} {url}\n{headers}\n\n{body}'.format(
            method=req.method,
            url=req.url,
            headers='\n'.join('{}: {}'.format(k, v)
                              for k, v in req.headers.items()),
            body=req.body,
        ))

    def print_response(self, res):
        print('HTTP/1.1 {status_code}\n{headers}\n\n{body}'.format(
            status_code=res.status_code,
            headers='\n'.join('{}: {}'.format(k, v)
                              for k, v in res.headers.items()),
            body=res.content,
        ))


if __name__ == '__main__':
    unittest.main()
