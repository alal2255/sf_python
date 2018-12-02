class sf_log:
    def __init__(self,username,passcode):
        self.username = username
        self.passcode = passcode

uname = input("Enter Username:")
pass1 = input("Enter Passcode:")

p1 = sf_log(uname,pass1)
print(p1.username)
print(p1.passcode)
    

