# chaos-testing-lab

This project focuses on chaos engineering and resiliency validation
for cloud-native 5G Core and IMS Network Functions.

## Scope
- Kubernetes-based CNFs (AMF, SMF, IMS)
- Pod failure, restart, and network chaos
- Validation using Robot Framework and SIP automation

## Out of Scope
- CNF feature development
- SIP protocol implementation
- UE simulation logic

## Dependencies
- Running 5g-cnf-lab Kubernetes cluster
- Active VoLTE / SIP automation
- kubectl access to cluster

## Goal
Prove carrier-grade resiliency under controlled failures.
