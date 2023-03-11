
class Dad:
    
        __accountPass = "1234"          ## private attribute __ 
        __superPass = "dfasdf"          ## private attribute __ 
        _childPass = 'WhenYouAreFirstInClass'   ## Protected attribute  _
        passForAll = 'Public'               ## public attribute
        def __init__(self) -> None:
                print("Dad init")
        
        def __trip(self):
            print("Lets have vaction")

        def hobby(self):
            self.__trip()
            print("News paper")

        def getAccountPass(self):       ## if we want readonly attribute, make use of getter method
            return self.__accountPass

        def setAccountPass(self, oldPass, newPass):   # if you wnat to set value for private attribute use setter 
            if oldPass == self.__accountPass:
                self.__accountPass = newPass
            else:
                print("Enter valid old password..")

        def bankAccount(self):
            accountPassword = input("Enter bank pass")
            if(accountPassword != self.__accountPass):
                print("Pahila rank la.. tabhi milega..")
            else:
                print("Account is malamal")


class Mom:
    def __init__(self) -> None:
            print("Mom init")   
    def hobby(self):
        print("Cooking")
    def bankAccount(self):
        print("Account is super malamal")


class Beta(Dad, Mom):          ## method order resolution # jo pahila base class hoga uska method call kiya jayega
    def __init__(self) -> None:
            print("Beta init")
    def hobby(self):            ## method overriding  - requires inheritance, same method but differnt class
        print("Instagram")
    def khilone(self):          ## method overloading   - no requires inhertance, same method in same class
        print("cycle")
    def khilone(self):          ## method overloading  
        print("bike")

        ### python dont support method overloading, 
        ### if you wnat you can use default or optional parameters to achieve method overloading 


obj = Beta()

obj._accountPass = 443554
obj.bankAccount()


