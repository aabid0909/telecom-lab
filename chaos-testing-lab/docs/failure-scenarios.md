# Failure Scenarios

## AMF Pod Kill
Expected:
- New pod created
- UE re-registration
- No service blackout

## SMF Restart
Expected:
- Rolling restart
- PDU session recovery

## P-CSCF Pod Kill
Expected:
- SIP retry via Service
- No mass call drop

## Network Latency Injection
Expected:
- Increased call setup time
- No call drop below SLA threshold
