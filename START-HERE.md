# Install and hand off

1. Verify the target is the existing Content Studio computer in orgo/deployment.json. Inspect running jobs, installed Hermes commit and Slack connection metadata without printing credentials.
2. Back up the existing identity/configuration privately. Run orgo/setup.sh. It installs CSO identity and skill; it does not reinstall Hermes, copy credentials, stop unrelated services or enable schedules.
3. Verify with orgo/verify.sh. Run a harmless local identity response with the installed Hermes runtime.
4. Connect or repurpose the Content Studio Slack app only with the owner's authorization. Use slack-manifest.json if a new app is needed. Keep Socket Mode and an explicit user allowlist. Configure private tokens on the computer, never in Git or chat.
5. Fill the private integration contract with exact CRM, task, mailbox, call and proof-page mappings. Test reads and queue replay before writes. Publish no proof without verified evidence and consent.
6. Configure daily reminders for the selected Slack channel using the installed Hermes scheduler after reviewing existing jobs. Avoid duplicate schedules or idle model polling. Verify one reminder and one authorized Slack reply end to end.
7. Attach the computer to Boppy's independent chief-sales-officer instance. Verify health identity, desktop, task response, separate storage and switching.

The CSO is fully connected only when provider readbacks and end-to-end receipts verify all selected connections. Report missing connections plainly.
