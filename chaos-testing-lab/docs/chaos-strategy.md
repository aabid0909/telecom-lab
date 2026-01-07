# Chaos Testing Strategy

Chaos testing is used to validate resiliency and self-healing
of 5G Core and IMS CNFs running on Kubernetes.

## Principles
- Chaos is controlled and measurable
- One failure at a time
- Always establish baseline before chaos
- Always clean up after chaos

## Failure Categories
1. Pod-level failures
2. Deployment restarts
3. Network degradation

## Validation
- Robot Framework API tests
- VoLTE SIP call continuity
- Kubernetes recovery metrics
