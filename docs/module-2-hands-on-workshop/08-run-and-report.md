# 8. Run, Triage, and Report

It's release night, and the release manager wants to know: **can we ship?** Run the test set, find out why anything failed, prove it, and write the go/no-go report.

!!! info "Check these first"
    ✅ **Your robot is available** — connected and not busy, in your Orchestrator folder.

    ✅ **UiBank Smoke Test Set** has your automated test cases, from [7. Add Test Cases to the Smoke Test Set](07-create-test-set.md).

## Run and triage

A failed test doesn't always mean a broken app: the test itself can be wrong. You made this call by hand in [4. Run Manual Tests](04-run-manual-tests.md#1-run-a-test-case). Now Delegate checks each failure against the requirement.

!!! example "It's your turn now!"
    1. Go back to your Delegate session.
    2. Paste:

        ```text
        Trigger the UiBank Smoke Test Set of my project in Test Manager and wait for it to finish. Then, for this run only, not earlier executions:
        - Give me the totals: passed, failed, none, and restricted.
        - For each failed test case and data row, compare its input data and expected outcome with the acceptance criteria of the Submit Loan Request requirement. Classify it as a UiBank defect (the app breaks the requirement) or a test defect (the test expects the wrong result), and quote the criterion you used.
        - List any manual test cases in the set separately as not run, not as failures.
        ```

    3. Approve Delegate's requests. The important one is the run itself, a **real execution** on your robot.
    4. Wait a few minutes while it runs the set and checks each failure.

??? tip "Run a single test case instead"
    ```text
    Run test case <YOUR_TEST_CASE_KEY> in my project in Test Manager, wait for it to finish, and tell me whether it passed. If it failed, explain why.
    ```

**Check it:** compare Delegate's totals with **Execution** in Test Manager. Delegate can be wrong, so check its triage against the requirement yourself.

!!! info "What you should find"
    ✅ Your test case with test data, from [6. Automate and Publish the Test Cases](06-automate-and-publish.md#attach-test-data), fails on the row with age **66**. The requirement rejects applicants over 65, but UiBank approves them. That's a **UiBank defect**.

    ✅ Its other rows pass.

    ✅ Any other failure comes from your own test cases. Check how Delegate classified it.

    Delegate calls the age-66 row a test defect? Ask it to check the row against the over-65 criterion, and share what happened in the workshop chat.

    The age-66 row passed? See [Troubleshooting](../module-3-troubleshooting-and-next-steps/02-troubleshooting.md#execution).

## Prove it

A defect report needs evidence a developer can reproduce. Delegate repeats the failed application in the browser.

!!! example "It's your turn now!"
    1. Keep only one UiBank tab open.
    2. Paste:

        ```text
        Reproduce the UiBank defect in the browser. Open https://uibank.uipath.com, apply for a loan with the data from the failed row, and take a screenshot of the result. Note the loan ID. Then look up that loan ID on the Loan Lookup page, and take a screenshot. Save both screenshots on my Desktop.
        ```

    3. Approve Delegate's requests. Don't use your browser while it works.

**Check it:** UiBank approves the age-66 application and shows a loan ID, Loan Lookup finds that loan, and both screenshots are on your Desktop.

## Write the report

!!! example "It's your turn now!"
    1. Paste:

        ```text
        Create a release manager report in PDF for this run, and save it on my Desktop. I need a go/no-go recommendation before tonight's sign-off meeting. Base it on UiBank defects only, and list test defects as follow-ups. Include the triage, and add the screenshots and loan ID as evidence for each UiBank defect.
        ```

    2. If Delegate asks where to save the report, choose your Desktop. Keep the default file name, and select **Submit**.

Delegate gives the path to the saved report and summarizes it in the chat. Always review its output before sharing. The report shows:

✅ **Scope** — the execution it covers

✅ **Totals** — passed, failed, none, and restricted

✅ **Success rate**

✅ **Triage** — each failure, whether it's a UiBank or a test defect, and the criterion it breaks

✅ **Evidence** — the screenshots and loan ID

✅ **Recommendation** — GO or NO-GO, and why

**Check it:** the right call is **NO-GO**, because UiBank breaks the age rule, not because of the success rate. Delegate recommends GO? Ask it why, against the over-65 criterion.

??? tip "Saved as .md instead of PDF?"
    Ask Delegate:

    ```text
    Create a PDF of the report and save it on my Desktop.
    ```

!!! question "Think about it"
    How did you know the failure was UiBank's, not the test's? Would the success rate alone have told you to stop the release? What does a developer need to fix it? How long would this take you by hand?

??? example "Optional: Draft the defect"
    ```text
    Draft a defect for the UiBank age defect: title, steps to reproduce, test data, expected and actual result, loan ID, and the screenshots. Save it on my Desktop.
    ```

    In a real project, log it in your defect tracker.

## Schedule it as a routine

A report you run once is useful. One that arrives every morning is better. You don't need to set this up today, but here's how it works.

**Save it as a routine.** Once Delegate has run a task, you can ask it to save the task as a reusable routine. For example: *"Save this run, triage, and report task as a routine called UiBank Release Report. Include my Test Manager project in the routine, so it works when it runs on a schedule."* The routine appears under **Routines** in Delegate's left panel, ready to run again on demand.

**Put it on a schedule.** Under **Scheduled routines**, a Day / Week / Month calendar shows every routine with a time slot. New routines wait in the **Not scheduled** list below it. Drop one onto a time slot or set it to recur, for example weekdays at 8:00 AM.

**Start from a ready-made routine.** The Test Cloud plugin includes **Summarize last night's execution of a test set**, already waiting in the **Not scheduled** list.

!!! warning "The machine must be on"
    A scheduled routine runs only if the machine it runs on is powered on and signed in at the scheduled time.

A routine suits a personal report. For the test set run itself, schedule the test set in Test Manager so it runs on the unattended robot, or trigger it from your CI/CD pipeline. Let the routine only fetch and summarise the results.

## Go further

Stay in the same session — it remembers the run:

✅ *"Summarize the failures in three bullet points I can paste into Slack."*

✅ *"Add a section to the report with recommended next steps for the developers."*

✅ *"Regenerate the same report for a Developer, with failure details and stack traces."*

More ideas in **[More Prompts to Try](../module-3-troubleshooting-and-next-steps/01-more-agent-prompts.md)**.

---

[Next → You did it!](you-did-it.md){: .md-button .md-button--primary}

---
