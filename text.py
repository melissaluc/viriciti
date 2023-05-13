import base64
from seleniumwire import webdriver 

username = "melissa.luc@metrolinx.com"
password = "CUgB4t9017ibkH^!"
auth = (
    base64.encodebytes(f'{username}:{password}'.encode())
    .decode()
    .strip()
)

def interceptor(request):
    if request.host == 'https://dashboard.viriciti.com':
        request.headers['Authorization'] = f'Basic {auth}'

## Set Request Interceptor
driver = webdriver.Chrome()
driver.request_interceptor = interceptor

