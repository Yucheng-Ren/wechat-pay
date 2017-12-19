from pay import WeChatScanPay

WECHAT_APPID = 'your_app_id'
WECHAT_MCH_ID = 'your_mch_id'
WECHAT_NOTIFY_URL = 'your_notify_url'
WECHAT_PAY_SECRET = 'your_pay_secret'

sp = WeChatScanPay(WECHAT_APPID, WECHAT_MCH_ID,
                   WECHAT_NOTIFY_URL, WECHAT_PAY_SECRET)


def unifiedorder(out_trade_no, body, total_fee, client_ip):
    '''
    :param out_trade_no: your order id, should be unique in your system
    :param body: order description
    :param total_fee: order price
    :param client_ip: request ip address
    :return:
    '''
    result = sp.unifiedorder(body=body, out_trade_no=out_trade_no, total_fee=total_fee,
                             spbill_create_ip=client_ip)
    if result.success:
        # Qr code url
        return result.code_url
    else:
        return result.error_msg


def query_order(out_trade_no):
    result = sp.query_order(out_trade_no=out_trade_no)
    if result.success:
        order_state = result.trade_state
        return order_state
    else:
        return result.error_msg
