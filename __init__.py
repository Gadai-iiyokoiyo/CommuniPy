import requests
import json

class CommunityDocs():
    def __init__(self, URL, UserCode, debug_message):
        
        self.URL = URL
        self.debug_message = debug_message
        self.UC = UserCode
        
        if self.URL == "":
            self.URL = "https://communitydocs.gadaidev.repl.co/"
        if self.debug_message:
            print(f"[ API ] HELLO: CommunityDocs API 2.0")
            print(f"[ Info ] Start:Connect {self.URL}")
        
        self.apijson = requests.get(f"{self.URL}/API.txt")
        self.API_Json = json.loads(self.apijson.content.decode())
        self.SiteName = self.API_Json["Name"]
        self.APIBlock = self.API_Json["APIBlock"]
        

        if self.debug_message:
            print("[ OK ] Success:Connect")
            print(f"[ Info ] SiteName\t\t{SiteName}\nAPIBlock\t\t{self.APIBlock}")
            if self.APIBlock:
                print(f"[ Error ] API BLOCK")
        if self.APIBlock:
            exit()
            
    def debug_message_onoff(self, mode:bool):
        self.debug_message = mode

    def post(self, title:str, text:str):
        if self.debug_message:
            print("[ Info ] Start:Post")
            print(f"[ Info ] Data:[URL=\"{self.URL}\"\nUsercode=\"{self.UC}\"\nTitle=\"{title}\"\nText=\"{text}\"]")
        
        title = title.replace(">","≻")
        title = title.replace("<","≺")

        response = requests.post(f"{self.URL}bot/cr", {
            "uc":self.UC,
            "title":title,
            "text":text
        })
        
        response_str = response.content.decode()

        if self.debug_message:
            if response_str == "Invalid UserCode":
                print("[ Error ] UserCode:Invalid UserCode")
            print("[ OK ] Success:Post")
    def comment(self, PageID, title, text):
        if self.debug_message:
            print("[ Info ] Start:Post")
            print(f"[ Info ] Data:[URL=\"{self.URL}\"\nUsercode=\"{self.UC}\"\nTitle=\"{title}\"\nText=\"{text}\"\nPageID=\"{PageID}\"]")
        requests.post(f"{self.URL}/comment", {"code":PageID, "title":title, "text":text, "uc":self.UC})
        if self.debug_message:
            print("[ OK ] Success: Comment Post")

class Element_image():
    def __init__(url):
        return f"<img src='{url}'>"

class Element_link():
    def __init__(text, url):
        if text == "":
            text = url
        return f"<a href='{url}'>{text}</a>"
