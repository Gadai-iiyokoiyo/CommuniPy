import CommuniPy

UserCode = "USERCODE"

API = CommuniPy.CommunityDocs("", UserCode, True)

texts = "1x1 ~ 9x9\n\n"+"\n".join([f"{a} x {b} = {a*b}" for a in range(1,10) for b in range(1,10)])

API.post(title = "SPL" text = texts)