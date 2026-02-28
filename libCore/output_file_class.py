import libCore.util_class as luC
class output_file:


    def pipe_output(self, content, link="..\save_output.txt"):
        handle = self.luC_.file_open(self.luC_.absolute_link(link),"a+")
        handle.write(f"{content}\n")
        handle.close()

    def __init__(self):
        self.luC_ = luC.util()