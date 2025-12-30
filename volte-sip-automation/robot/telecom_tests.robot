*** Settings ***
Library    ../python/telecom_validations.py

*** Test Cases ***
Validate VoLTE Call Setup
    ${result}=    Run Volte Call
    Should Be True    ${result}

