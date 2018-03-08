# coding:utf-8
import xmltodict
from requests import Response


class WeChatResult(object):
    def __init__(self, resp):
        # Response object
        self.resp = resp

        # 本次逻辑处理最终结果
        self.success = False

        # 结果字典
        self.result = self._parse_xml(resp)

        if self.result.get('return_code') == 'SUCCESS':
            self.success = True
        else:
            self.error_msg = {'return_msg': self.result.get('return_msg'),
                              'err_code': self.result.get('err_code', ''),
                              'err_code_des': self.result.get('err_code_des', '')}

    @staticmethod
    def _parse_xml(resp):
        if isinstance(resp, Response):
            # parse response
            return xmltodict.parse(resp.content).get('xml', None)
        else:
            # parse request
            return xmltodict.parse(resp.data).get('xml', None)


class UnifiedorderResult(WeChatResult):
    def __init__(self, resp):
        super(UnifiedorderResult, self).__init__(resp)

        if self.success and self.result.get('result_code', '') == 'SUCCESS':
            # 交易类型
            self.trade_type = self.result.get('trade_type')
            # 预支付交易会话标识
            self.prepay_id = self.result.get('prepay_id')
            # 二维码链接(trade_type为NATIVE时有返回)
            self.code_url = self.result.get('code_url', '')
        else:
            self.success = False
            self.error_msg = {'return_msg': self.result.get('return_msg'),
                              'err_code': self.result.get('err_code', ''),
                              'err_code_des': self.result.get('err_code_des', '')}


class SendBoxKey(WeChatResult):
    def __init__(self, resp):
        super(SendBoxKey, self).__init__(resp)

        self.key = self.result.get('sandbox_signkey', '')


class NotifyResult(WeChatResult):
    def __init__(self, resp):
        super(NotifyResult, self).__init__(resp)

        if self.success and self.result.get('result_code', '') == 'SUCCESS':
            map(lambda x: setattr(self, x, self.result.get(x)), self.result.keys())
        else:
            self.success = False
            self.error_msg = {'return_msg': self.result.get('return_msg'),
                              'err_code': self.result.get('err_code', ''),
                              'err_code_des': self.result.get('err_code_des', '')}


class OrderResult(WeChatResult):
    def __init__(self, resp):
        super(OrderResult, self).__init__(resp)

        if self.success and self.result.get('result_code', '') == 'SUCCESS':
            self.trade_state = self.result.get('trade_state')
            self.out_trade_no = self.result.get('out_trade_no')
            if self.trade_state == 'SUCCESS':
                # 支付成功
                self.total_fee = self.result.get('total_fee')
        else:
            self.success = False
            self.error_msg = {'return_msg': self.result.get('return_msg'),
                              'err_code': self.result.get('err_code', ''),
                              'err_code_des': self.result.get('err_code_des', '')}


class ErrorResult(WeChatResult):
    def __init__(self, resp):
        super(ErrorResult, self).__init__(resp)
        self.success = False
        self.error_msg = {'return_msg': self.result.get('return_msg'),
                          'err_code': self.result.get('err_code', ''),
                          'err_code_des': self.result.get('err_code_des', '')}


class DownLoadBillResult(object):
    def __init__(self, resp):
        self.text = resp.text
        self.content = resp.content


class CloseOrderResult(WeChatResult):
    def __init__(self, resp):
        super(CloseOrderResult, self).__init__(resp)
        if self.success and self.result.get('result_code', '') == 'SUCCESS':
            self.success = True


class ShortUrlResult(WeChatResult):
    def __init__(self, resp):
        super(ShortUrlResult, self).__init__(resp)
        if self.success and self.result.get('result_code', '') == 'SUCCESS':
            self.short_url = self.result.get('short_url')


class RefundResult(WeChatResult):
    def __init__(self, resp):
        super(RefundResult, self).__init__(resp)
        if self.success and self.result.get('result_code', '') == 'SUCCESS':
            map(lambda x: setattr(self, x, self.result.get(x)), self.result.keys())
        else:
            self.success = False
            self.error_msg = {'return_msg': self.result.get('return_msg'),
                              'err_code': self.result.get('err_code', ''),
                              'err_code_des': self.result.get('err_code_des', '')}


class RefundQueryResult(WeChatResult):
    def __init__(self, resp):
        super(RefundQueryResult, self).__init__(resp)
        if self.success and self.result.get('result_code', '') == 'SUCCESS':
            pass
        else:
            self.success = False
            self.error_msg = {'return_msg': self.result.get('return_msg'),
                              'err_code': self.result.get('err_code', ''),
                              'err_code_des': self.result.get('err_code_des', '')}


WECHAT_CLASS = {
    'unifiedorder': UnifiedorderResult,
    'getsignkey': SendBoxKey,
    'notify_result': NotifyResult,
    'orderquery': OrderResult,
    'error': ErrorResult,
    'downloadbill': DownLoadBillResult,
    'closeorder': CloseOrderResult,
    'shorturl': ShortUrlResult,
    'refund': RefundResult,
    'refundquery': RefundQueryResult
}
