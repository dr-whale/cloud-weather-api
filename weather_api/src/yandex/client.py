import requests
from .errors import InvalidMethodError
from .errors import BadConfigError
from .errors import InvalidArgumentError

class Client():
    def __init__(self, url, key):
        if not key:
            raise BadConfigError('Key Not Found')
        if not url:
            raise BadConfigError('Url Not Found')    
        self.api_url = url
        self.api_key = key

    def __prv_request(self, method_req, address_req, params_req, body_req = None):
        headers_req = {'X-Yandex-API-Key':self.api_key}
        if method_req == 'get':
            response = requests.get(url = f"{self.api_url}{address_req}", params = params_req, headers = headers_req)
        elif method_req == 'post':
            response = requests.post(url = f"{self.api_url}{address_req}", params = params_req, data = body_req, headers = headers_req)
        else:
            raise InvalidMethodError('Invalid Method Error')
        response.raise_for_status()
        print('Request to Yandex')
        return response.json()

    def __get_prv(self, get_address, params):
        response = self.__prv_request('get', get_address, params)
        return response

    def __post_prv(self, post_address, params, body_req = None):
        response = self.__prv_request('post', post_address, params, body_req)
        return response

    def weather_req(self, address, params):
        if not address:
            raise InvalidArgumentError('No Address')
        response = self.__get_prv(address, params)
        return response
