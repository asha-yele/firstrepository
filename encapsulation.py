
class Dad:
    
        __accountPass = "1234"
        __superPass = "dfasdf"
        def __init__(self) -> None:
                print("Dad init")
        def hobby(self):
            print("News paper")

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


class Beta(Dad, Mom):          ## metthod order resolution # jo pahila base class hoga uska method call kiya jayega
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
print(obj.)
obj._accountPass = 443554
obj.bankAccount()

