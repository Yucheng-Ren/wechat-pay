# coding:utf-8
from uuid import uuid4
import hashlib
import dicttoxml
import xmltodict
import requests
from collections import OrderedDict
from .models import WECHAT_CLASS


class WeChatPay(object):
    """
    documentation
    https://pay.weixin.qq.com/wiki/doc/api/native.php?chapter=6_1
    appid: 公众号id
    mch_id: 商户id
    notify_url: 通知URL
    pay_secret: 秘钥
    cert: path to your apiclient_cert.pem (download from wechat website)
    key: path to your apiclient_key.pem (download from wechat website)
    """

    def __init__(self, appid, mch_id, notify_url, pay_secret, cert=None, key=None):
        self.appid = appid
        self.mch_id = mch_id
        self.mch_base = 'https://api.mch.weixin.qq.com/'
        self.notify_url = notify_url
        self.pay_secret = pay_secret
        self.cert = cert
        self.key = key

    @staticmethod
    def random_str():
        """
        :return: 随机字符串
        """
        return str(uuid4()).replace('-', '')

    def _gen_sign(self, dct):
        """
        :param dct: 所需发送的所有数据的字典集合
            详情：https://pay.weixin.qq.com/wiki/doc/api/native.php?chapter=4_3
        :return: 签名
        """
        params = OrderedDict(sorted(dct.items(), key=lambda t: t[0]))
        stringA = ''
        for key, value in params.items():
            stringA += str(key) + '=' + str(value) + '&'
        stringSignTemp = stringA + 'key=' + self.pay_secret
        # stringSignTemp = stringA + 'key=7b3515d618d2f0ae70f6ac453983ea7e'  # send box
        return hashlib.md5(stringSignTemp.encode('utf-8')).hexdigest().upper()

    def _verify_sign(self, dct):
        sign = dct.pop('sign')
        if sign == self._gen_sign(dct):
            return True
        else:
            return False

    def unifiedorder(self, device_info='WEB', sign_type='MD5', fee_type='CNY', trade_type='NATIVE', **kwargs):
        """
        统一下单 所需的数据集合
        https://pay.weixin.qq.com/wiki/doc/api/native.php?chapter=9_1
        :param device_info: 设备号
        :param sign_type: 签名类型
        :param fee_type: 标价币种
        :param trade_type: 交易类型
        :param kwargs: 其他数据
        :return: 所需要发送数据的xml格式字符串
        """
        data = {
            'appid': self.appid,
            'mch_id': self.mch_id,
            'device_info': device_info,
            'sign_type': sign_type,
            'fee_type': fee_type,
            'trade_type': trade_type,
            'nonce_str': self.random_str(),
            'notify_url': self.notify_url
        }
        data.update(kwargs)
        data.update({
            'sign': self._gen_sign(data)
        })
        return self._request_post(self.mch_base + 'pay/unifiedorder', self.to_xml(data))

    def verify_notify(self, req):
        """
        :param req: wechat post request notify
        :return: NotifyResult instance
        """
        result = xmltodict.parse(req.data).get('xml')
        if self._verify_sign(result):
            return WECHAT_CLASS['notify_result'](req)
        else:
            return WECHAT_CLASS['error'](req)

    @staticmethod
    def to_xml(dct):
        """
        字典转换 xml
        :param dct: 字典
        :return: xml 字符串
        """
        return dicttoxml.dicttoxml(dct, custom_root='xml', attr_type=False, cdata=True)

    @staticmethod
    def _parse_result(resp, class_key):
        return WECHAT_CLASS[class_key](resp)

    def _request_post(self, url, data, is_cert=False):
        headers = {'Content-Type': 'application/xml'}
        if is_cert:
            if not self.cert or not self.key:
                raise ValueError
            resp = requests.post(url, data=data, headers=headers, cert=(self.cert, self.key))
        else:
            resp = requests.post(url, data=data, headers=headers)
        return self._parse_result(resp, url.split('/')[-1])

    def sendbox_sign(self):
        data = {
            'mch_id': self.mch_id,
            'nonce_str': self.random_str(),
        }
        data.update({
            'sign': self._gen_sign(data)
        })
        return self._request_post(self.mch_base + 'pay/getsignkey', self.to_xml(data))

    def query_order(self, **kwargs):
        """
        :param kwargs: out_trade_no 订单号
        :return:
        """
        data = {
            'appid': self.appid,
            'mch_id': self.mch_id,
            'nonce_str': self.random_str(),
            'sign_type': 'MD5'
        }
        data.update(kwargs)
        data.update({
            'sign': self._gen_sign(data)
        })
        return self._request_post(self.mch_base + 'pay/orderquery', self.to_xml(data))

    def downloadbill(self, bill_date, sign_type='MD5', bill_type='ALL', tar_type='GZIP'):
        '''
        下载对账单
        https://pay.weixin.qq.com/wiki/doc/api/native.php?chapter=9_6
        :param bill_date: 账单日期
        :param sign_type: 加密方式
        :param bill_type: 账单类型
        :param tar_type:  压缩账单
        :return:
        '''
        data = {
            'appid': self.appid,
            'mch_id': self.mch_id,
            'sign_type': sign_type,
            'nonce_str': self.random_str(),
            'bill_date': bill_date,
            'bill_type': bill_type,
            'tar_type': tar_type
        }
        data.update({
            'sign': self._gen_sign(data)
        })
        return self._request_post(self.mch_base + 'pay/downloadbill', self.to_xml(data))

    def close_order(self, out_trade_no, sign_type='MD5'):
        '''
        :param out_trade_no: 订单号
        :param sign_type: 加密类型
        :return:
        '''
        data = {
            'appid': self.appid,
            'mch_id': self.mch_id,
            'nonce_str': self.random_str(),
            'out_trade_no': out_trade_no,
            'sign_type': sign_type
        }
        data.update({
            'sign': self._gen_sign(data)
        })
        return self._request_post(self.mch_base + 'pay/closeorder', self.to_xml(data))

    def short_url(self, long_url, sign_type='MD5'):
        '''
        :param long_url: 长连接
        :param sign_type: 加密类型
        :return:
        '''
        data = {
            'appid': self.appid,
            'mch_id': self.mch_id,
            'nonce_str': self.random_str(),
            'sign_type': sign_type,
            'long_url': long_url
        }
        data.update({
            'sign': self._gen_sign(data)
        })
        return self._request_post(self.mch_base + 'tools/shorturl', self.to_xml(data))

    def refund(self, out_trade_no, out_refund_no, total_fee, refund_fee, sign_type='MD5', refund_fee_type='CNY', **kwargs):
        '''
        :param out_trade_no: 商户订单号
        :param out_refund_no: 商户退款单号
        :param total_fee: 订单总金额
        :param refund_fee: 退款总金额
        :param sign_type: 签名方法
        :param refund_fee_type: 退款币种
        :return:
        '''
        data = {
            'appid': self.appid,
            'mch_id': self.mch_id,
            'nonce_str': self.random_str(),
            'sign_type': sign_type,
            'out_trade_no': out_trade_no,
            'out_refund_no': out_refund_no,
            'total_fee': total_fee,
            'refund_fee': refund_fee,
            'refund_fee_type': refund_fee_type
        }
        data.update(kwargs)
        data.update({
            'sign': self._gen_sign(data)
        })
        return self._request_post(self.mch_base + 'secapi/pay/refund', self.to_xml(data), is_cert=True)

    def refund_query(self, out_refund_no, sign_type='MD5', **kwargs):
        '''
        :param out_refund_no: 商户退款单号
        :param sign_type: 签名方法
        :return:
        '''
        data = {
            'appid': self.appid,
            'mch_id': self.mch_id,
            'nonce_str': self.random_str(),
            'sign_type': sign_type,
            'out_refund_no': out_refund_no,
        }
        data.update(kwargs)
        data.update({
            'sign': self._gen_sign(data)
        })
        return self._request_post(self.mch_base + 'pay/refundquery', self.to_xml(data))

