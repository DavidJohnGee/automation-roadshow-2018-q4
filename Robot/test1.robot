*** Settings ***
Library  Collections
Library  String
Library  OperatingSystem
Library  RequestsLibrary


*** Test Cases ***

Get Requests

    ${headers}=    Create Dictionary
    Set To Dictionary    ${headers}    Accept    application/json
    Set To Dictionary    ${headers}    Authorization    Basic ZGVtbzpQYXNzdzByZA\=\=
    Create Session  demo01  http://demo01.ipengineer.net:8080  headers=&{headers}
    ${resp}=  Get Request  demo01  /rpc/get-route-information?table=VR1.inet.0  headers=&{headers}
    Should Be Equal As Strings  ${resp.status_code}  200
    # Dictionary Should Contain Value  ${resp.content.json()}  route-information
    # ${json}=    evaluate    json.loads('''${resp.content}''')    json
    ${jsondata}=  To Json  ${resp.content}
    # Log  Printing data  &{jsondata}  console=${True}
    ${json_string}=    evaluate    json.dumps(${jsondata})    json
    # Log  Printing data:  ${json_string}  console=${True}
    Dictionary Should Contain Key  ${jsondata}  route-information


