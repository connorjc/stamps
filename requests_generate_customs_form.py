#!/usr/bin/env python3
"""
"""
import os
from dotenv import load_dotenv
import requests
import xml.dom.minidom

load_dotenv()

url="https://swsim.testing.stamps.com/swsim/swsimv90.asmx?wsdl"

# url="https://www.w3schools.com/xml/tempconvert.asmx"
headers = {'content-type': 'application/soap+xml; charset=utf-8'}

# tutorial="""<?xml version="1.0" encoding="utf-8"?>
# <soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
#   <soap12:Body>
#     <CelsiusToFahrenheit xmlns="https://www.w3schools.com/xml/">
#       <Celsius>36</Celsius>
#     </CelsiusToFahrenheit>
#   </soap12:Body>
# </soap12:Envelope>"""

# FOMAT ACCORDING TO SOAP1.2 at https://swsim.testing.stamps.com/swsim/swsimv90.asmx?op=AuthenticateUser
auth = """<?xml version="1.0" encoding="utf-8"?>
<soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                 xmlns:xsd="http://www.w3.org/2001/XMLSchema"
                 xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
  <soap12:Body>
    <AuthenticateUser xmlns="http://stamps.com/xml/namespace/2018/03/swsim/swsimv90">
      <Credentials>
        <IntegrationID>{}</IntegrationID>
        <Username>{}</Username>
        <Password>{}</Password>
      <Credentials>
    </AuthenticateUser>
  </soap12:Body>
</soap12:Envelope>""".format(os.getenv("INTEGRATOR_ID"),os.getenv("USERNAME"),os.getenv("PASSWORD"))

# <tns:Rate>
#         <tns:FromZIPCode>90405</tns:FromZIPCode>
#         <tns:ToZIPCode>90066</tns:ToZIPCode>
#         <tns:WeightLb>12</tns:WeightLb>
#         <tns:PackageType>Package</tns:PackageType>
#         <tns:ShipDate>2018-01-12</tns:ShipDate>
#         <tns:InsuredValue>100.00</tns:InsuredValue>
#       </tns:Rate>

if __name__ == "__main__":
    headers["Content-Length"] = str(len(auth))
    print(headers)
    print(auth)
    response = requests.post(url,data=auth,headers=headers)
    print(response.content)
    # dom = xml.dom.minidom.parseString(response.content) # or xml.dom.minidom.parseString(xml_string)
    # pretty_xml_as_string = dom.toprettyxml()
    # print(pretty_xml_as_string)
