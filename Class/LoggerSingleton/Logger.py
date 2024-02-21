class Logger(object):
    instance = None
    # the rest of the class definition will follow here, as per the previous logging script
    def __new__(cls, filename):
        if not Logger.instance:
            Logger.instance = Logger.__Logger(filename)
        else:
            Logger.instance.file_name = filename
        return Logger.instance
    
    def __getattr__(self, name):
        return getattr(self.instance, name)
    
    def __setattr__(self, name):
        return setattr(self.instance, name)
    
    class __Logger():
        def __init__(self, file_name):
            """Return a Logger object whose file_name is *file_name*"""
            self.file_name = file_name

        def _write_log(self, level, msg):
            """Writes a message to the file_name for a specific Logger instance"""
            with open(self.file_name, "a") as log_file:
                log_file.write("[{0}] {1}\n".format(level, msg))
        
        def __str__(self):
            return "{0!r} {1}".format(self, self.file_name)
    
obj1 = Logger("FileName.txt")

print(obj1)
obj2 = Logger("FileName2.txt")
print(obj2)
#obj1.val = "FileName.txt"
# print("print obj1: ", obj1)
# print("-----")
# obj2 = Logger()
# obj2.val = "Object value 2"
# print("print obj1: ", obj1)
# print("print obj2: ", obj2)