
WeChatPay
=========

.. py:class:: WeChatPay(appid, mch_id, notify_url, pay_secret, cert=None, key=None)

    .. py:method:: unifiedorder(device_info, sign_type, fee_type, trade_type, **kwargs)

       Form a new order. more information at
       `API <https://pay.weixin.qq.com/wiki/doc/api/native.php?chapter=9_1>`_

       :param device_info: exception type
       :param sign_type: sign method(MD5 or HMAC-SHA256)
       :param fee_type: currency type
       :param attach: attach data
       :param out_trade_no: order id (should be unique in your system)
       :param trade_type: `(JSAPI，NATIVE，APP) <https://pay.weixin.qq.com/wiki/doc/api/native.php?chapter=4_2>`_
       :param body: order description
       :param detail: item detail
       :param total_fee: the amount of fee
       :param spbill_create_ip: client ip address
       :param time_start: order generate time (format yyyyMMddHHmmss)
       :param time_expire: order expire time (format yyyyMMddHHmmss)
       :param goods_tag: `discount info <https://pay.weixin.qq.com/wiki/doc/api/tools/sp_coupon.php?chapter=12_1>`_
       :param product_id: item id
       :param limit_pay: no_credit
       :param openid: user wechat openid
       :param scene_info: scenario info
       :rtype: :py:class:`UnifiedorderResult`

    .. py:method:: random_str()

       Generate a random string

       :rtype: string

    .. py:method:: verify_notify(req)

       Verify WeChat payment notification

       :param req: Request object from requests
       :rtype: :py:class:`NotifyResult` or :py:class:`ErrorResult`

    .. py:method:: to_xml(dct)

       Transfer a dict to xml string
       :param dct: data dict to send
       :rtype: string

    .. py:method:: sendbox_sign()

       Generate sendbox secret key
       `API <https://pay.weixin.qq.com/wiki/doc/api/native.php?chapter=23_1>`_

       :rtype: :py:class:`SendBoxKey`


    .. py:method:: query_order(**kwargs)

       Query order from WeChat
       `API <https://pay.weixin.qq.com/wiki/doc/api/native.php?chapter=9_2>`_

       :param transaction_id: wechat order id
       :param out_trade_no: order id (transaction_id and out_trade_no only need one)
       :rtype: :py:class:`OrderResult`

    .. py:method:: downloadbill(bill_date, sign_type='MD5', bill_type='ALL', tar_type='GZIP')

       Download bills
       `API <https://pay.weixin.qq.com/wiki/doc/api/native.php?chapter=9_6>`_

       :param bill_date: the date of bill (format yyyymmdd)
       :param bill_type: the type of bill (ALL, SUCCESS, REFUND, RECHARGE_REFUND)
       :param tar_type: tar type(GZIP)
       :rtype: :py:class:`DownLoadBillResult`

    .. py:method:: close_order(out_trade_no, sign_type='MD5')

       Close order
       `API <https://pay.weixin.qq.com/wiki/doc/api/native.php?chapter=9_3>`_

       :param out_trade_no: order id
       :rtype: :py:class:`CloseOrderResult`

    .. py:method:: short_url(long_url, sign_type='MD5')

       Convert long url to short url and make the Qr code more recognizable
       `API <https://pay.weixin.qq.com/wiki/doc/api/native.php?chapter=9_9>`_

       :param long_url: long url
       :rtype: :py:class:`ShortUrlResult`

    .. py:method:: refund(out_trade_no, out_refund_no, total_fee, refund_fee, sign_type='MD5', refund_fee_type='CNY', **kwargs)

       Method for refund
       **this method need you to proide your cert.pem and key.pem file**
       `API <https://pay.weixin.qq.com/wiki/doc/api/native.php?chapter=9_4>`_

       :param transaction_id: wechat order id
       :param out_trade_no: order id (transaction_id and out_trade_no only need one)
       :param out_refund_no: refund id
       :param total_fee: total order fee
       :param refund_fee: refund total fee
       :param refund_fee_type:  currency type (CNY)
       :param refund_desc:  refund reason
       :param refund_account:   refund account
       :rtype: :py:class::`RefundResult`

    .. py:method:: refund_query(out_refund_no, sign_type='MD5', **kwargs)

       Query refund process
       `API <https://pay.weixin.qq.com/wiki/doc/api/native.php?chapter=9_5>`_
       :param transaction_id: wechat order id
       :param out_trade_no: order id
       :param out_refund_no: refund id
       :param refund_id: refund id from WeChat (transaction_id, out_trade_no, out_refund_no, refund_id only need to one)
       :param offset: query offset
       :rtype: :py:class::`RefundQueryResult`
