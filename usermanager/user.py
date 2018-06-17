import os
import pwd

class User():
    

    def __init__(self, name, passwd, uid, gid, lname, home, shell):
        self.name = name
        self._passwd = passwd
        self.uid = uid
        self.gid = gid
        self.lname = lname
        self.home = home
        self.shell = shell


    def __str__(self):
        info = '{0}, {1}, {2}, {3}, {4}, {5}'.format(self.name, 
            self.uid, self.gid, self.lname, self.home, self.shell)
        return info


    def __repr__(self):
        return self.__str__()
