from simple_salesforce import Salesforce
import json,io
import pprint


#list []
sf=Salesforce(username='xxxxx@xxxxx.com',password=Salesforceaccountpasscode,security_token=securitotken)
#sf=Salesforce(instance_url='https://na85.salesforce.com',session_id='00D1U000000EVj3!AQ8AQMfhARMOhePr4kalZYFERLyRC5juwpqtZ0LiKuHiE57bckDLEyjE5FKXHs8P.bXpnr9Isv6_p7HjAKv8j32vAQvUy4V0') ##Salesforce OAuth Connection ###
r1 = sf.query("SELECT SourceIp from LoginIp") ##Salesforce SoSQL Query###
r2 = sf.query("SELECT Country from LoginGeo Limit 10")


r3 = [r1,r2]
#def merge(dict1,dict2):
#    dict3 = dict1.copy()
#    dict3.update(dict2)
    #res = {**dict1,**dict2}
#    return dict3
#dict1 = r1
#dict2 = r2
#dict3 = merge(r1,r2)
#print(dict3)
for obj in r3:
    print(json.dumps(obj,skipkeys='True',indent=4))

