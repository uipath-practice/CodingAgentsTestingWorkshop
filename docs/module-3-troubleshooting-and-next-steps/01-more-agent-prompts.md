# More Prompts to Try

Try these in Delegate, in the same session, so it knows your project. Ask for outcomes, not commands.

## Morning standup brief

```text
Summarize today's test runs in my project — how many passed, failed, had no result, or were restricted?
```

In daily use, ask for yesterday's runs instead.

## Coverage check before a release

```text
In my project, what percentage of requirements are covered by test cases, and which requirements have no test cases at all?
```

## Triggering a targeted test set

```text
Run the UiBank Smoke Test Set in my project and let me know when it's done.
```

## Flaky or recurring failures

```text
For the failed test cases in the latest run of the UiBank Smoke Test Set in my project, look at their last 10 results and tell me which ones are new regressions and which keep failing.
```

## Read-only exploration

```text
List the test sets in my project and the test cases in each one. Don't change anything.
```

!!! warning "Prompts that write"
    Triggering runs or updating test cases changes Test Manager. Read each approval request before you approve it.

---

[Next → Troubleshooting](02-troubleshooting.md){: .md-button .md-button--primary}

---
