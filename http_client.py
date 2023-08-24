
from kivy.network.urlrequest import UrlRequest
import json

class HttpClient:

    def get_pizzas(self, on_complete, on_server_error, on_server_failure):
        url = "http://jrpizzamamadjango2.herokuapp.com/api/GetPizzas"
        pizzas_dict = []
        
        def data_received(req, result):
            data = json.loads(result)
            for i in data:
                pizzas_dict.append(i["fields"])
            if on_complete:
                return on_complete(pizzas_dict)
        
        def data_error(req, error):
            if str(error) == "[Errno 11001] getaddrinfo failed":
                on_server_error("Veuillez vérifier votre connexion Charlene internet")
            else:
                on_server_error(error)
            
        def data_failure(req, error):
            on_server_failure(str(req.resp_status))

        req = UrlRequest(url, on_success=data_received, on_error=data_error, on_failure=data_failure)

    



