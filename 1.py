class login:
    def __init__(self, rid, pas):
        self.rid = rid
        self.pas = pas

    def check(rid, pas):
        print(self.rid)
        if self.rid == rid and self.pas == pas:
            print("Login success!")
        else:
            print("Hello")
f=input("Enter Login ID : ")
g=input("Enter Password : ")
log = login("admin", "admin")
log.check(f,g)
printf("Made By Ayon Roy for GitHub ")
