import requests
import json

class VitakodConnector:
    def __init__(self):
        self.url = "https://vitakod-api.herokuapp.com/"
    
    def get_reports(self, limit = None, offset = None):
        reqUrl = self.url+"/get_reports"
        headersList = {
        "Accept": "*/*",
        "Content-Type": "application/json" 
        }
        if limit is not None and offset is not None:
            payload = json.dumps({
            "limit": limit,
            "offset": offset
            })
        else:
            payload = json.dumps({
            "limit": "ALL",
            "offset": 0
        })

        response = requests.request("GET", reqUrl, data=payload,  headers=headersList)
        return response.json()