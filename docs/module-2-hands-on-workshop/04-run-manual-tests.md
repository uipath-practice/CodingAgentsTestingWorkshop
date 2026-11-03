# 04. Run Manual Tests

There are three ways to run a manual test case. Each records its results in Test Manager.


| | Who runs the steps | Apps it can test | Setup needed |
|---|---|---|---|
| **Delegate** *(used in this workshop)* | Delegate, on your machine | Web and desktop apps | None |
| **Manual execution assistant** | You | Any | None |
| **Run autonomously** | Autopilot, on a robot | Web apps | A robot in the project's default folder ([01. Import and Link the Test Manager Project](01-import-tm-project.md#link-the-project-to-your-folder)) |

See <a href="https://docs.uipath.com/test-manager/automation-cloud/latest/user-guide/executing-manual-tests" target="_blank">Executing manual tests</a>.

??? tip "Manual execution assistant"
    1. Go to **Test Sets**, open a test set, and select **Execute → Manually**. Allow pop-ups for Test Manager. The manual execution assistant opens in a new window.
    2. Perform each step, then select **Set Passed** or **Set Failed** (comment on failures). **Set Passed Until Here** passes several steps at once.
    3. At any step, capture a screenshot or upload related files as attachments.
    4. Check the postcondition, the state the app must be in after the test. Select **Condition Met** if it holds.
    5. Select **Next**, then **Done** after the last test case.
    6. Check the results in the project's **Execution** section.

    See <a href="https://docs.uipath.com/test-manager/automation-cloud/latest/user-guide/executing-test-sets-manually" target="_blank">Executing test sets manually</a>.

??? tip "Run autonomously"
    **Autonomous Test Execution** runs a manual test case with Autopilot, in one click, on a robot.

    1. Go to **Test Cases**, open a manual test case, and go to the **Manual Steps** tab. In the right-hand panel, select **Run Autonomously**.

        ![Run Autonomously in the Manual Steps tab](../assets/images/TM%20Run%20autonomously.png)

    2. Confirm the **Target Application URL**, for example `https://uibank.uipath.com`. Turn on **Live Streaming** to watch Autopilot drive the browser, and take over if needed. Leave **AI Model** as it is.
    3. Select **Run**.
    4. When it finishes, open the execution:
        ✅ **Logs** — each step's result, expected behavior, and screenshots. Expand a step to see what Autopilot did.

        ✅ **Execution Log** — Autopilot's reasoning, such as how it found an element or compared a result.

    See <a href="https://docs.uipath.com/test-manager/automation-cloud/latest/user-guide/running-autonomous-test-execution" target="_blank">Running Autonomous Test Execution</a>.

??? tip "No test case yet? Explore the requirement autonomously"
    **Autonomous Exploration** is exploratory testing with Autopilot: it learns the app, designs tests, and runs them within a time-box.

    1. Open a requirement → **+ Autonomous Exploration**.
    2. Enter the app URL, set a **time-box**, and select an AI model. Turn on **Live Streaming** to watch it explore.
    3. Select **Start**. When it's **Completed**, select **Show report**.

    Needs a Windows robot in the project's default folder (set up in [Prerequisites](../module-0-prerequisites/index.md#orchestrator-folder-and-robot)), with the UiPath browser extension set to **Allow in Incognito**. See <a href="https://docs.uipath.com/test-manager/automation-cloud/latest/user-guide/running-autonomous-exploration" target="_blank">Running Autonomous Exploration</a>.

## Run manual tests with Delegate

With Delegate, you can run a test case, add steps to an empty one, or create a new one from a business document. You review the work and decide what to save in Test Manager.

[Open Delegate](../module-0-prerequisites/01-installation-guide.md#step-2-meet-delegate).

### 1 — Run a test case

!!! example "It's your turn now!"
    1. Replace `<YOUR_TEST_CASE_KEY>` with a test case you created in [03. Generate Test Cases](03-generate-test-cases.md), then paste:

        ```text
        Run the manual test case <YOUR_TEST_CASE_KEY>. Open UiBank at https://uibank.uipath.com, follow the test case's manual steps in the browser, and check every expected result. Take a screenshot at the final validation step and upload it to the test case's assertions. Push the results to Test Manager. If any step failed, explain the reason.
        ```

    2. Approve when Delegate asks to push the result.
    3. For any failure, decide: **defect in UiBank**, or **problem with the test case**?

??? tip "Test data already used?"
    Tests like registering a new user fail if the data was used before. Ask Delegate:

    ```text
    Rerun test case <YOUR_TEST_CASE_KEY> with new registration data that hasn't been used before, and push the new result to Test Manager.
    ```

**Check it:** **Execution** → open the new execution → select your test case key. It shows the result, with the screenshot under **Assertions**.

!!! question "Think about it"
    Did Delegate stumble on a step? Autopilot automates these same steps in [05. Automate Test Cases with Studio Desktop and Delegate](05-automate-with-studio-and-delegate.md), so fix them now:

    ```text
    Rewrite the steps of test case <YOUR_TEST_CASE_KEY> that were unclear during this run, so each one has a single clear action and expected result. Show me the changes before you save them to Test Manager.
    ```

### 2 — Add steps to an empty test case

Your project has a test case, **Request Loan**, with no steps.

!!! example "Let's build it with Delegate!"
    1. Replace `<REQUEST_LOAN_KEY>` with its key, then paste:

        ```text
        Test case <REQUEST_LOAN_KEY> currently has no steps. Add test steps to it based on the linked requirement document and the navigation flow below.

        Navigation flow:

        Welcome page (https://uibank.uipath.com/welcome)
        Open the Products drop-down menu and select Loans.
        Expected result: The Loans page opens.

        Loans page (https://uibank.uipath.com/loans)
        Click the Apply for Loan button.
        Expected result: The loan application form is displayed.

        Loan application form (https://uibank.uipath.com/loans/apply)
        Fill in every required field with the values and rules from the requirement document.
        Click Submit.
        Expected result: The application is accepted, and the confirmation or result shown matches the acceptance criteria in the requirement.

        Instructions:

        Take all field names, valid test data, validation rules and expected outcomes from the requirement document. Don't make up any values.
        Give each step one action and one expected result.
        If the requirement leaves out details a step needs, such as a missing field value or an unclear acceptance criterion, list them as open questions. Don't guess.
        Add the label 'Coding Agent WS' to <REQUEST_LOAN_KEY>.
        Before saving the steps to <REQUEST_LOAN_KEY>, show them to me for review.
        ```

    2. Then follow Delegate:
        1. **No requirement linked** — ask it to link the **Submit Loan Request** requirement.
        2. **Test data** — choose the **approval path**.
        3. **Open questions** — answer them.
        4. **Save the steps** — give permission.
        5. **Run it** — say yes.

**Check it:** **Request Loan** has manual steps and the **Coding Agent WS** label, is linked to the requirement, and has a new result in **Execution**.

### 3 — Create a new requirement and test case (optional)

The business has documented a new process, **Loan lookup**, in a Process Design Document (PDD). It isn't in your requirements yet.

!!! example "It's your turn now!"
    1. Download the PDD, <a href="../../assets/Files/Loan%20lookup%20process%20to%20be%20tested.docx" target="_blank">Loan lookup process to be tested.docx</a>.
    2. Attach it in Delegate, then paste:

        ```text
        Analyze the attached PDD and create + save a requirement and a manual test case directly in UiPath Test Manager — no review pause, just create and save.

        Requirement: Create one new requirement for the process described in the PDD (don't create it if an existing requirement already covers this exact process — check first and tell me if you find one instead of creating a duplicate). Name it - infer from the PDD title; description should summarize the user flow (pages/actions) and any acceptance criteria from the PDD.
        Test case: Create one manual test case - infer name from the PDD, derived from the PDD's numbered steps/screenshots — one test step per documented UI action, each with an expected result.
        Final step: After the PDD's last action, add a step that verifies the loan details page shows the same loan ID that was entered, along with the rest of the loan's details.
        Link: Link the new test case to the new requirement.
        Report back: give me the created requirement key and test case key when done.
        ```

    3. Ask Delegate to run the new test case.

**Check it:** a new **Loan lookup** requirement, with a linked test case that has manual steps and a result in **Execution**.

??? example "Not quite right? Talk to Delegate"
    Open the new requirement and test case in Test Manager. Check the title, description, acceptance criteria, steps, and expected results.

    Then tell Delegate what to fix, in your own words, just as you'd tell a colleague. For example:

    ✅ *"The test case must check that the loan ID is the same, and that the loan's other details are displayed"*

    ✅ *"Don't use the data from the PDD in the test case"*

    ✅ *"Add the label 'Delegate' to this test case and requirement"*

    Keep going until you're happy with both.

!!! example "Go further — Organize test cases in bulk"
    1. Add a label to your test cases:

        ```text
        Add the label "Delegate" to every test case you created or ran in this session.
        ```

    2. Create a **Test Tier** custom field and set it on the labeled test cases:

        ```text
        Create a custom field definition for test cases in my project:
        - Name: Test Tier
        - Description: How often this test should run: every build, daily, or before release.
        - Object type: Test Cases
        - Data type: Label
        - Possible values: Smoke, Core, Extended

        Then, for every test case with the label "Delegate", set Test Tier to "Smoke".
        ```

    **Check it:** open a labeled test case. Its **Details** tab shows **Test Tier: Smoke**.

??? info "Beyond running tests — Delegate across the whole manual testing cycle"
    Ideas to try on your own project, in your own words:

    ✅ **Find test ideas** — from a requirement's acceptance criteria, or from a screenshot of a screen, including boundary and negative cases.

    ✅ **Write the steps** — turn those ideas into manual test cases and link them to the requirement.

    ✅ **Run them with you** — Delegate runs the steps and stops to ask when it needs input you have, such as login details.

    ✅ **Record the results** — create test results with screenshots of failed steps, and upload them to Test Manager.

## Nice work!

Your test cases are proven against the real application, with results in Test Manager. Next, you'll connect Studio to automate them.

---

[Next → 05. Automate Test Cases with Studio Desktop and Delegate](05-automate-with-studio-and-delegate.md){: .md-button .md-button--primary}

---
