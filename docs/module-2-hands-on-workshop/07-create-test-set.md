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

See <a href="https://docs.uipath.com/test-manager/automation-cloud/latest/user-guide/quickstart-assigning-test-cases-to-test-sets" target="_blank">Assigning test cases to test sets</a>.

**Check it:** **Regression Test Set** lists every test case with the **Coding Agent WS** label.

??? tip "Do a test run (optional)"
    Open the test set → **Execute → Automated**, then check **Execution**. Every test case should have a result. A real failure is fine — that's what the report is for.

## Nice work!

Everything is in place to run and report.

---

[Next → 08. Run and Report](08-run-and-report.md){: .md-button .md-button--primary}

---
