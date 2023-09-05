import requests
class CommunityDocs():
    def __init__(self, URL, UserCode, debug_message):
        
        self.URL = URL
        self.debug_message = debug_message
        self.UC = UserCode


        if self.URL == "":
            self.URL = "https://communitydocs.gadaidev.repl.co/"
        if self.debug_message:
            print(f"[ Info ] Start:Connect {self.URL}")
        
        requests.get(self.URL)
        

        if self.debug_message:
            print("[ OK ] Success:Connect")
    
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
            print(f"[ Info ] Data:[URL=\"{self.URL}\"\nUsercode=\"{self.UC}\"\nTitle=\"{title}\"\nText=\"{text}\"\nPageID=\"{PageID}\"]"")
        requests.post(f"{self.URL}/comment/", {"code":PageID, "title":title, "text":text, "uc":self.UC})
        
