
WeChatResult
============

.. py:class:: WeChatResult(resp)

    .. py:attribute:: resp

        resp is the instance of Response class from `requests <http://docs.python-requests.org/en/master/>`_

    .. py:attribute:: success

        success is used to determine whether this request is successful

    .. py:attribute:: result

        result is a python dict which contains the response data that parsed from xml

    .. py:attribute:: error_msg

        error_msg contains the error message if anything went wrong


.. py:class:: UnifiedorderResult(WeChatResult)

    .. py:attribute:: trade_type

        `(JSAPI，NATIVE，APP) <https://pay.weixin.qq.com/wiki/doc/api/native.php?chapter=4_2>`_

    .. py:attribute:: prepay_id

        generate by WeChat for more operation (valid in 2 hours)

    .. py:attribute:: code_url

        Qr code url for payment


.. py:class:: NotifyResult(WeChatResult)

    Every key in result dict refer to a attribute of this class
    `API <https://pay.weixin.qq.com/wiki/doc/api/native.php?chapter=9_7>`_


.. py:class:: ErrorResult(WeChatResult)

    .. py:attribute:: success

        in this case success is False

    .. py:attribute:: error_msg

        error message dict


.. py:class:: SendBoxKey(WeChatResult)

    .. py:attribute:: key

        send box secret key


.. py:class:: OrderResult(WeChatResult)

    .. py:attribute:: trade_state

        the state of this order

    .. py:attribute:: out_trade_no

        order id

    .. py:attribute:: total_fee

        amount of fee of this order

.. py:class:: DownLoadBillResult(WeChatResult)

    .. py:attribute:: text

        unicode of the bill content

    .. py:attribute:: content

        bill content

.. py:class:: CloseOrderResult(WeChatResult)

    pass


.. py:class:: ShortUrlResult(WeChatResult)

    .. py:attribute:: short_url

        short url


.. py:class:: RefundResult(WeChatResult)

    Every key in result dict refer to a attribute of this class

    `API <https://pay.weixin.qq.com/wiki/doc/api/native.php?chapter=9_4>`_


.. py:class:: RefundQueryResult(WeChatResult)

    `API <https://pay.weixin.qq.com/wiki/doc/api/native.php?chapter=9_5>`_

    Because there are some field need to access by index, so use the result dict to fetch the data you need
