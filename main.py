import libCore.util_class as luC
import libCore.output_file_class as ofC
import keyboard
import pyperclip
import datetime

luC_ = luC.util()
ofC_ = ofC.output_file()

code_country = "fr"
is_clic = False 
list_un_authorized_account = set(ofC_.pipe_un_authorized_account())


pyperclip.copy("**[original2fx_link](https://github.com/LittleViewer/original2fx_link)**, provided by *[LittleViewer](<https://github.com/LittleViewer>)*, aims to simplify the use of the X (twitter) embed repair system via the [FxTwitter](<https://github.com/FixTweet/FxTwitter>)tool.")

while True:
        
        event = keyboard.read_hotkey(suppress=False)

        if event == "ctrl+x" :
            copy = pyperclip.paste()
            value = copy.split("x.com")
            copy_list = copy.split("/")
            if copy_list[3] in list_un_authorized_account:
                warn = "You have just attempted to convert a link from an unauthorized account. If this account needs to be authorized, please refer to the file: un_authorized_account.json"
                luC_.error_with_reason(warn)
                pyperclip.copy(warn)
            else:
                try:
                    new_formated_link = value[0]+"fxtwitter.com"+value[1]+f"/{code_country}"
                    print(new_formated_link)
               
                    date_hours_minute = str(datetime.datetime.now()).split('.')
                    pyperclip.copy(f"[ {date_hours_minute[0]} - [{copy_list[3]}](<https://x.com/{copy_list[3]}>) ]\n{new_formated_link} \n*[original2fx_link](<https://github.com/LittleViewer/original2fx_link>), provided by [LittleViewer](<https://github.com/LittleViewer>)*")
                
                    output_save =  {"date_time" :str(datetime.datetime.now()), "account": copy_list[3], "link_account" : f"https://x.com/{copy_list[3]}", "id_post" : copy_list[5], "original_link" : copy, "new_formated_link" : new_formated_link}
                    ofC_.pipe_output(output_save)
                except:
                    luC_.error_with_reason("Not good link format")

        elif event == "ctrl+h":
             pyperclip.copy(ofC_.pipe_copy_history())

        elif event == "ctrl+q":
            luC_.error_with_reason("Stop program", True)