*** Settings ***
Library    RequestsLibrary
Library    Collections

*** Variables ***
${PCSCF_URL}    http://pcscf-svc:5060
${SCSCF_URL}    http://scscf-svc:6060

*** Test Cases ***
Continuous IMS Health Check During Chaos
    FOR    ${i}    IN RANGE    1    60
        Create Session    pcscf    ${PCSCF_URL}
        ${resp1}=    GET On Session    pcscf    /health
        Log    P-CSCF Status: ${resp1.status_code}

        Create Session    scscf    ${SCSCF_URL}
        ${resp2}=    GET On Session    scscf    /health
        Log    S-CSCF Status: ${resp2.status_code}

        Sleep    3s
    END
