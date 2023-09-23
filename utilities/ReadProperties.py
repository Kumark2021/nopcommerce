import configparser
config=configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig():
    @staticmethod
    def getApplicationURL(self):
        config.get('common info',baseurl)
        return url

    @staticmethod
    def getUseremail(self):
        config.get('common info', useremail)
        return username
    @staticmethod
    def getPassword(self):
        config.get('common info', password)
        return passsword
