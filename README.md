# wechat-pay
wechat pay sdk in python

This is an unofficial sdk for WeChat Pay

[WeChat Pay official API doc](https://pay.weixin.qq.com/wiki/doc/api/index.html)

[Doc for this project](https://wechat-pay-sdk.readthedocs.io/en/latest/)

install by pip

    pip install wechat-pay-sdk

install from source

    python setup.py install

Usage:

```py
from wechatpay import WeChatPay

WECHAT_APPID = 'your_app_id'
WECHAT_MCH_ID = 'your_mch_id'
WECHAT_NOTIFY_URL = 'your_notify_url'
WECHAT_PAY_SECRET = 'your_pay_secret'
WECHAT_CERT = 'path/to/your_cert.pem'
WECHAT_KEY = 'patch/to/your_key.pem'


sp = WeChatPay(WECHAT_APPID, WECHAT_MCH_ID,
                   WECHAT_NOTIFY_URL, WECHAT_PAY_SECRET, WECHAT_CERT, WECHAT_KEY)

# 统一下单
result = sp.unifiedorder(body=body, out_trade_no=out_trade_no, total_fee=total_fee,
                             spbill_create_ip=client_ip)

# 查询订单
result = sp.query_order(out_trade_no=out_trade_no)

if result.success:
    # your code
    pass

```

