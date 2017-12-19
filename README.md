# wechat-pay
wechat pay sdk in python

This is an unofficial sdk for WeChat Pay

install by pip

    pip install wechat-pay-sdk

Usage:

```py
from wechatpay import WeChatScanPay

WECHAT_APPID = 'your_app_id'
WECHAT_MCH_ID = 'your_mch_id'
WECHAT_NOTIFY_URL = 'your_notify_url'
WECHAT_PAY_SECRET = 'your_pay_secret'

sp = WeChatScanPay(WECHAT_APPID, WECHAT_MCH_ID,
                   WECHAT_NOTIFY_URL, WECHAT_PAY_SECRET)

# 统一下单
result = sp.unifiedorder(body=body, out_trade_no=out_trade_no, total_fee=total_fee,
                             spbill_create_ip=client_ip)

# 查询订单
result = sp.query_order(out_trade_no=out_trade_no)

```

