# 07. Add Test Cases to the Smoke Test Set

A **test set** groups test cases that run together. Your project already has one: **UiBank Smoke Test Set**, with the existing loan test cases. Add the new test cases you automated, so the set runs them too.

## Add your test cases

1. In Test Manager, go to **Test Sets** and open **UiBank Smoke Test Set**.
2. Go to the **Test Cases** tab.

    ??? info "Static or Dynamic Assignment?"
        A test set gets its test cases in one of two ways:

        ✅ **Static Assignment** — pick test cases one by one. The set always runs exactly these.

        ✅ **Dynamic Assignment** — add labels. The set includes every test case with at least one of them.

3. Click **Add Test Cases** to see all the test cases in the project.
4. Select each new test case you automated in [06. Automate and Publish the Test Cases](06-automate-and-publish.md), and add them. Existing test cases you chose are already in the set.

## Configure the automation

1. On the **Test Cases** tab, click **Configure Automation**.
2. Check that the execution is set to your personal folder, the one you set as **Default Folder** in [01. Import and Link the Test Manager Project](01-import-tm-project.md#link-the-project-to-your-folder).
3. Set **Runtime Type** to the runtime you set on your machine: **App Testing** or **Testing**. The panel shows **1 Runtimes Available, 1 Connected**.
4. Under **Automation Packages**, select **Autoselect Packages**. Check that it lists your `<YOUR_NAME>_UiBank Tests` package, and click **Save**.

See <a href="https://docs.uipath.com/test-manager/automation-cloud/latest/user-guide/quickstart-assigning-test-cases-to-test-sets" target="_blank">Assigning test cases to test sets</a>.

**Check it:** **UiBank Smoke Test Set** lists every test case you automated.

!!! tip "Do a test run (recommended)"
    Do a test run now, so a missing package or robot shows up here, not in step 8.

    Open the test set → **Execute → Automated**, then check **Execution**. Every test case you automated should have a result. A failure is fine — you triage it in step 8.

## Nice work!

Everything is in place to run, triage, and report.

---

[Next → 08. Run, Triage, and Report](08-run-and-report.md){: .md-button .md-button--primary}

---
