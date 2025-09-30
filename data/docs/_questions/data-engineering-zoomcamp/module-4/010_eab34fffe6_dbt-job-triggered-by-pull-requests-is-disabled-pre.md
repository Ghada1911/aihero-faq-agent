---
id: eab34fffe6
question: 'dbt: Job - Triggered by pull requests is disabled prerequisites when I
  try to create a new Continuous Integration job in dbt cloud.'
sort_order: 10
---

Solution:

Check if you’re on the Developer Plan. As per the [prerequisites](https://docs.getdbt.com/docs/deploy/ci-jobs#prerequisites), you'll need to be enrolled in the Team Plan or Enterprise Plan to set up a CI Job in dbt Cloud.

- If you're on the Developer Plan, you'll need to upgrade to utilize CI Jobs.

Note: A user mentioned that while on the Team Plan (trial period), the option was still disabled. In this case, you might try other troubleshooting steps for the Developer (free) plan.