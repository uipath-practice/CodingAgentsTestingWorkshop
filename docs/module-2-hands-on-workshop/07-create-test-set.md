# 07. Create a Test Set

A **test set** groups test cases that run together.

## Create it

1. In Test Manager, go to **Test Sets → Create Test Set**.
2. Name it **Regression Test Set**, and click **Create**.
3. Open the test set you just created, and go to the **Test Cases** tab. You can add test cases in two ways:

    ✅ **Static Assignment** — pick test cases one by one. The set always runs exactly these.

    ✅ **Dynamic Assignment** — add labels. The set includes every test case with at least one of them.

4. Choose **Dynamic Assignment**. In **Labels for dynamic assignment**, search for **Coding Agent WS** and add it.

    The set includes every test case with this label: the ones you've already created, and any you label later.

5. On the **Test Cases** tab, click **Configure Automation**.
6. Check that the execution is set to your personal folder, the one you set as **Default Folder** in [01. Import and Link the Test Manager Project](01-import-tm-project.md#link-the-project-to-your-folder).
7. Set **Runtime Type** to the runtime you set on your machine: **App Testing** or **Testing**. The panel shows **1 Runtimes Available, 1 Connected**.
8. Under **Automation Packages**, select **Autoselect Packages**. Check that it lists your `<YOUR_NAME>_UiBank Tests` package, and click **Save**.

See <a href="https://docs.uipath.com/test-manager/automation-cloud/latest/user-guide/quickstart-assigning-test-cases-to-test-sets" target="_blank">Assigning test cases to test sets</a>.

**Check it:** **Regression Test Set** lists every test case with the **Coding Agent WS** label.

!!! tip "Do a test run (recommended)"
    Do a test run now, so a missing package or robot shows up here, not in step 8.

    Open the test set → **Execute → Automated**, then check **Execution**. Every test case should have a result. A real failure is fine — that's what the report is for.

## Nice work!

Everything is in place to run and report.

---

[Next → 08. Run and Report](08-run-and-report.md){: .md-button .md-button--primary}

---
