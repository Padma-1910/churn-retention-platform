# Problem Statement

## Business Problem

Acquiring a new customer costs significantly more than retaining an existing one — industry estimates put the ratio at 5–7×. When a customer churns, the company loses not just current revenue but the entire projected lifetime value of that relationship. The retention team currently has no systematic way to identify at-risk customers early enough to intervene effectively, so resources are spent reactively or spread too thin across the entire base.

## Objective

Build a system that:

1. **Predicts** the probability that a given customer will churn within the next billing cycle.
2. **Explains** the top drivers behind each individual prediction so the retention team understands *why* a customer is at risk.
3. **Recommends** a retention action (e.g., targeted discount, service upgrade offer, proactive support contact) tailored to each customer's risk profile and likely churn reason.

## Target Users

**Retention and marketing team** — analysts and campaign managers who will use model outputs to prioritise outreach and design targeted offers. They are not data scientists; outputs must be interpretable and actionable without requiring ML knowledge.

## Success Metrics

### ML Metrics

| Metric | Description |
|--------|-------------|
| ROC-AUC | Overall discrimination ability of the model across all thresholds |
| Recall on churners | Fraction of actual churners the model correctly flags |
| Precision @ top 20% risk | Of the customers ranked in the top 20% by churn probability, what fraction actually churn |

### Business Metric

**% of churners captured by targeting the top 20% risk customers** — the primary indicator of real-world utility. If the model is well-calibrated, targeting the highest-risk quintile should capture the majority of churners at a fraction of the cost of contacting everyone.

## Scope

### In Scope

- **Prediction**: batch churn probability scores per customer, refreshed on a regular cycle.
- **Explainability**: per-customer feature contributions (SHAP values) surfaced alongside the score.
- **Application**: a lightweight web UI for the retention team to browse scores, explanations, and recommended actions.

### Out of Scope

- **Real-time / streaming inference**: scores are batch-generated, not computed on live event streams.
- **A/B testing framework**: measuring the causal lift of retention offers is a future phase.
- **Automated offer fulfilment**: the app recommends actions; a human approves and executes them.

## Assumptions

| Assumption | Placeholder — to be confirmed in Phase 5 |
|------------|------------------------------------------|
| Average customer lifetime value (CLV) | TBD — needed to size the value of preventing one churn |
| Cost of a retention offer | TBD — sets the floor on model precision before outreach becomes unprofitable |
| Churn label definition | Customer did not renew / explicitly cancelled within the observation window |
| Data freshness | Features reflect the state of the account at the end of the most recent billing period |
| Class imbalance handling | Assumed ~26% churn rate based on initial data exploration; will be validated in Phase 2 |
