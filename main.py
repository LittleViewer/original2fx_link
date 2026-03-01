import libCore.util_class as luC
import libCore.output_file_class as ofC
import keyboard
import pyperclip
import datetime

luC_ = luC.util()
ofC_ = ofC.output_file()

code_country = "fr"
is_clic = False 

while True:
        event = keyboard.read_hotkey(suppress=False)

        if event == "ctrl+x" :
            copy = pyperclip.paste()
            value = copy.split("x.com")
            
            try:
                new_formated_link = value[0]+"fxtwitter.com"+value[1]+f"/{code_country}"
                print(new_formated_link)

                copy_list = copy.split("/")
                date_hours_minute = str(datetime.datetime.now()).split('.')
                pyperclip.copy(f"[ {date_hours_minute[0]} - [{copy_list[3]}](<https://x.com/{copy_list[3]}>) - {new_formated_link} ]")
                
                output_save =  {"date_time" :str(datetime.datetime.now()), "account": copy_list[3], "link_account" : f"https://x.com/{copy_list[3]}", "id_post" : copy_list[5], "original_link" : copy, "new_formated_link" : new_formated_link}
                ofC_.pipe_output(output_save)
            except:
                luC_.error_with_reason("Not good link format")



        elif event == "ctrl+q":
            luC_.error_with_reason("Stop program", True)