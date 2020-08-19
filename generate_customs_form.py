#!/usr/bin/env python3
"""
"""
import os
from dotenv import load_dotenv
from suds.client import Client
import suds

load_dotenv()
url="https://swsim.testing.stamps.com/swsim/swsimv90.asmx?wsdl"
client = Client(url)

credential=client.factory.create("Credentials")
print(credential)
credential.IntegrationID=os.getenv("INTEGRATOR_ID")
credential.Username=os.getenv("USERNAME")
credential.Password=os.getenv("PASSWORD")
print(credential)
'''
auth = client.factory.create('AuthenticateUser')
auth.Credentials=credential
print(auth)
'''
# <tns:Rate>
#         <tns:FromZIPCode>90405</tns:FromZIPCode>
#         <tns:ToZIPCode>90066</tns:ToZIPCode>
#         <tns:WeightLb>12</tns:WeightLb>
#         <tns:PackageType>Package</tns:PackageType>
#         <tns:ShipDate>2018-01-12</tns:ShipDate>
#         <tns:InsuredValue>100.00</tns:InsuredValue>
#       </tns:Rate>

# get_rate=client.factory.create("GetRates")
# print(get_rate)
# rate=client.factory.create("RateV33")
# rate.FromZIPCode=90405
# rate.ToZIPCode=90066
# rate.WeightLb=12
# rate.PackageType="Package"
# rate.ShipDate="2018-01-12"
# rate.InsuredValue=100.00
# print(rate)

if __name__ == "__main__":
    try:
        response = client.service.AuthenticateUser(credential)
        # response = client.service.GetRates(auth,rate)
        print(response)
    except suds.WebFault as e:
        print(e)
