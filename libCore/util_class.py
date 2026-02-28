import datetime
import os
import sys
class util:

    def absolute_link(self, link):
        return os.path.join(os.getcwd(), link)
    
    def error_with_reason(self, reason, to_break = False, code = 1000):
        print(f"[{self.date_}] - Stop Reason: " + reason)
        if to_break == True:
            sys.exit(code)

    def file_open(self, link, mode = "r", encoding_would="utf-8"):
        handle = open(link, mode, encoding=encoding_would)
        return handle

    def __init__(self):
        self.date_ = datetime.datetime.now()