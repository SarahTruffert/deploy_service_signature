# Depuis /src : 
# python -m unittest 
import unittest
from hello_app.sign import *

class TestSignAndVerify(unittest.TestCase):
    def setUp(self):
        self.msg = b'hello world'
        self.fakemsg = b'world hello'
        self.privkey = b'-----BEGIN RSA PRIVATE KEY-----\nMIICXAIBAAKBgQCtTivjXYjJS8HUa+afOLTbBiejtktdpgRAJQqPqsYTkcDDKH4z\nC7zUyXjv7NBkVbCKDLbm9LvnQawfvoUG02gqQlbjKLYDfXVQ8cLWJGONeYwKInnw\nr+NBhnxoyI+tqRFLOnBPuCp4a/aoTcmb7dMK9ZQlTNYtdW/lVLdevSzyYQIDAQAB\nAoGAAL3TKe9YvEMAX8a0iV9NVYuyKij/u31QIse/ytmiTGOS+njJGbH/4U2RgI4L\n7hZ4ZW5QjuZamparMEV1AXCAj04n16XMTHctZ7GuTAO2si9lMUiS5ApqWM/gSmvU\nhInSSx8rO7vtfmvEnOdn8JO6c1FVOEUIEeDd/oTaNGj2UQECQQC1bGP2CBZzgGxA\nPW+9XugofjF4xUqN0Q8CGnD3jT2gTtO86W4rD8qNIQ/efT5J2uDIiEW786zKz6Gz\nKzB1ZE8BAkEA9IuAEX2rU9p6T+ZH5OZwc+MH3X/vYBzGJ/c49EzDqPAqqjHOt4xs\nhp354Eb9Mryx1Ziam48T0ytd0axZ8z4DYQJAF/QouppUxIlHQbAa6cj3JCmNRKHf\n9xuMPL3a/oRyh5EA2eeEOUFLgBjGbJzitYOlvDRp6KgCv4BsnChurIFDAQJBALr8\n8DBvp1G2/U+bBd5BVjtGnf0Alkknt11X7HThPbsv6W+6JhaziUhmA2s63OCu6Ewr\nJA1OmhoeTt7EqwMTqAECQGP616XH9tFt8cZZB/O/McITIPENr1qdvJ+zyEDALHyj\nYv46cyK4AZ3bKK1Tpjn8zThrSb32Uv9ndpfy06SUTBE=\n-----END RSA PRIVATE KEY-----'
        self.pubkey = b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCtTivjXYjJS8HUa+afOLTbBiej\ntktdpgRAJQqPqsYTkcDDKH4zC7zUyXjv7NBkVbCKDLbm9LvnQawfvoUG02gqQlbj\nKLYDfXVQ8cLWJGONeYwKInnwr+NBhnxoyI+tqRFLOnBPuCp4a/aoTcmb7dMK9ZQl\nTNYtdW/lVLdevSzyYQIDAQAB\n-----END PUBLIC KEY-----'
        self.goodsign = b'fehs9bk7oXCzsKzNytjazl8Q3n3PlYMwuuRF0aF+dyOLqr7s7yRspx+ni7z3H7ymC4pkjWoBuTSG\nHXD05tc3A0fBD5bYDNuRX/pVlLG0M/NcfCSG5qFn/lOEumyffHE8d5fAzlHZt6J2KBIyvXD5r+Tz\nPTDpPz9Le4WkD78mRDw=\n'

    def test_sign(self):
        self.assertEqual(sign(self.msg, self.privkey), self.goodsign)
        self.assertTrue(verify(self.msg, self.goodsign, self.pubkey))
        self.assertFalse(verify(self.fakemsg, self.goodsign, self.pubkey))
