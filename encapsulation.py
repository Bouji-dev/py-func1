class Manager():
    def __init__(self):
        self._adminFiles = "admin files"
        self.__managerFiles = "manager files"

    def access(self):
        print(self.__managerFiles)

    def print_files(self):
        print("public files")

    def __print_files(self):
        print("private files")

class Admin(Manager):
    def __init__(self):
        Manager.__init__(self)
        self.id = "1111"