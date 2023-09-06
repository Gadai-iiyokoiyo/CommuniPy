import CommuniPy as cp
import sys

instance = sys.argv[1]
usercode = sys.argv[2]
API = cp.CommunityDocs(instance, usercode, True)
if len(sys.argv)>=3:
    if sys.argv[3] == "-m":
        try:
            API.post(sys.argv[4], sys.argv[5])
        except IndexError:
            print("[ Error ] There are not enough arguments.")

    if sys.argv[3] == "-c":
        try:
            API.comment(sys.argv[4], sys.argv[5], sys.argv[6])
        except IndexError:
            print("[ Error ] There are not enough arguments.")

    if sys.argv[3] == "-mfile":
        try:
            API.post(sys.argv[4], open(sys.argv[5], "r", encoding="utf-8").read())
        except IndexError:
            print("[ Error ] There are not enough arguments.")
        
    if sys.argv[3] == "-cfile":
        try:
            API.comment(sys.argv[4], sys.argv[5], open(sys.argv[6], "r", encoding="utf-8").read())
        except IndexError:
            print("[ Error ] There are not enough arguments.")
