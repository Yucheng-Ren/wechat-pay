from setuptools import setup

setup(
    name='wechat-pay-sdk',
    packages=['wechatpay'],
    version='0.6.1',
    description='A sdk for wechat pay',
    author='Zack Ren',
    license='MIT',
    include_package_data=True,
    author_email='m6106918@gmail.com',
    url='https://github.com/Narcissist1/wechat-pay',
    download_url='https://github.com/Narcissist1/wechat-pay/archive/0.1.tar.gz',
    keywords=['wechat', 'pay'],
    classifiers=[],
    install_requires=[
    'xmltodict',
    'requests',
    'dicttoxml',
    ]
)
