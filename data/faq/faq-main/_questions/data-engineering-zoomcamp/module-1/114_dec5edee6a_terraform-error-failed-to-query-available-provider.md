---
id: dec5edee6a
question: 'Terraform - Error: Failed to query available provider packages │ Could
  not retrieve the list of available versions for provider hashicorp/google: could
  not query │ provider registry for registry.terrafogorm.io/hashicorp/google: the
  request failed after 2 attempts, │ please try again later'
sort_order: 114
---

This error typically occurs due to internet connectivity issues. Terraform is unable to access the online registry.

**Solution:**

- Check your VPN/Firewall settings.
- Clear cookies or restart your network.
- Run `terraform init` again after addressing the connection issues.