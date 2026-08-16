import requests
from app.Config.constants import REQUEST_URL

def create_session():
    session = requests.Session()

    headers = {"User-Agent": "Mozilla/5.0",
           "Referer":"https://leetcode.com/",
           "Referer Policy":"same-origin",
           "Content-Type":"application/json"}
    
    session.headers.update(headers)
    request = session.get(url=REQUEST_URL)

    return session