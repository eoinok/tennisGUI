class Member():
    def __init__(self,arg1,arg2,arg3,arg4,arg5):
        self.__name=arg1
        self.__age=arg2
        self.__smoker=arg3
        self.__memberType=arg4
        self.__gender

    def getName(self):
        return self.__name
    
    def getAge(self):
        return self.__age

    def getSmoker(self):
        return self.__smoker

    def getMemberType(self):
        return self.__memberType

    def getGender(self):
        return self.__gender

    def __str__(self):
        return self.__name
