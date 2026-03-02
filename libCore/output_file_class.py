import libCore.util_class as luC
import json

class output_file:

    def pipe_output(self, content, link="..\save_output.txt"):
        handle = self.luC_.file_open(self.luC_.absolute_link(link),"a+")
        handle.write(f"{content}\n")
        handle.close()
    
    def pipe_copy_history(self, link="..\save_output.txt"):
        handle = self.luC_.file_open(self.luC_.absolute_link(link),"r")
        content = handle.read()
        handle.close()
        return content

    def pipe_un_authorized_account(self, link="..\\un_authorized_account.json"):
        handle = self.luC_.file_open(self.luC_.absolute_link(link),"r")
        content = handle.read()
        list_account = []
        for one_account in json.loads(content):
            list_account.append(one_account["name_account"])
        handle.close()
        return list_account
    

    def __init__(self):
        self.luC_ = luC.util()