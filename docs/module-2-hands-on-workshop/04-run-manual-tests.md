# 4. Run Manual Tests

There are three ways to run a manual test case. Each records its results in Test Manager.


| | Who runs the steps | Apps it can test | Setup needed |
|---|---|---|---|
| **Delegate** *(used in this workshop)* | Delegate, on your machine | Web and desktop apps | None |
| **Manual execution assistant** | You | Any | None |
| **Run autonomously** | Autopilot, on a robot | Web apps | A robot in the project's default folder (set up in [Prerequisites](../module-0-prerequisites/index.md#orchestrator-folder-and-robot)) |

See <a href="https://docs.uipath.com/test-manager/automation-cloud/latest/user-guide/executing-manual-tests" target="_blank">Executing manual tests</a>.

??? tip "Manual execution assistant"
    1. Go to **Test Sets**, open **UiBank Smoke Test Set**, and select **Execute → Manually**.

        !!! info "Allow pop-ups for Test Manager"
            The manual execution assistant opens in a new window.

    2. Perform each step, then select **Set Passed** or **Set Failed** (comment on failures).
    3. At any step, capture a screenshot or upload related files as attachments.

        !!! info "Pass several steps at once"
            Select **Set Passed Until Here**.

    4. Check the postcondition, the state the app must be in after the test. Select **Condition Met** if it holds.
    5. Select **Next**, then **Done** after the last test case.
    6. Check the results in the project's **Execution** section.

    See <a href="https://docs.uipath.com/test-manager/automation-cloud/latest/user-guide/executing-test-sets-manually" target="_blank">Executing test sets manually</a>.

??? tip "Run autonomously"
    **Autonomous Test Execution** runs a manual test case with Autopilot, in one click, on a robot.

    1. Go to **Test Cases**, open a manual test case, and go to the **Manual Steps** tab. In the right-hand panel, select **Run Autonomously**.

        ![Run Autonomously in the Manual Steps tab](../assets/images/TM%20Run%20autonomously.png)

    2. Enter the **Target Application URL**, `https://uibank.uipath.com`. **Run** stays disabled until you do. Turn on **Live Streaming** to watch Autopilot drive the browser, and take over if needed. Leave **AI Model** as it is.

        **Run** still disabled? Open **Configure** and set **Runtime type** to your machine's runtime, **App Testing** or **Testing**.
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

With Delegate, you can run a test case or create a new one from a business document. You review the work and decide what to save in Test Manager.

Go back to your Delegate session.

### 1 — Run a test case

!!! example "It's your turn now!"
    1. Keep only one UiBank tab open. Delegate finds the window by its title, and the prompt names UiBank.
    2. Replace `<YOUR_TEST_CASE_KEY>` with the key of one of the test cases you chose in [03. Generate Test Cases](03-generate-test-cases.md). A key is your project prefix, a colon and a number, for example `UIBAS:43`. Then paste:

        ```text
        Run the manual test case <YOUR_TEST_CASE_KEY>. Open UiBank at https://uibank.uipath.com, follow the test case's manual steps in the browser, and check every expected result. Take a screenshot at the final validation step and attach it to that step's result. Push the results to Test Manager. If any step failed, explain the reason.
        ```

    3. If Delegate asks for permission to push the result, approve it. It records the result in a test set execution, which you'll find under **Execution**.
    4. For any failure, decide: **defect in UiBank**, or **problem with the test case**?

**Check it:** **Execution** → open the new execution → select your test case key. It shows the result and the step results, with the screenshot on the last step.

!!! question "Think about it"
    Did Delegate stumble on a step? Autopilot automates these same steps in [06. Automate and Publish the Test Cases](06-automate-and-publish.md), so fix them now:

    ```text
    Rewrite the steps of test case <YOUR_TEST_CASE_KEY> that were unclear during this run, so each one has a single clear action and expected result. Show me the changes before you save them to Test Manager.
    ```

### 2 — Create a new requirement and test case (optional)

The business has documented a new process, **Loan lookup**, in a Process Design Document (PDD). It isn't in your requirements yet.

!!! example "It's your turn now!"
    1. Download the PDD, <a href="../../assets/Files/Loan%20lookup%20process%20to%20be%20tested.docx" target="_blank">Loan lookup process to be tested.docx</a>.
    2. Attach it in Delegate, then paste:

        ```text
        Analyze the attached PDD and create + save a requirement and a manual test case directly in UiPath Test Manager — no review pause, just create and save.

        Requirement: Create one new requirement for the process described in the PDD (don't create it if an existing requirement already covers this exact process — check first and tell me if you find one instead of creating a duplicate). Name it Loan Lookup. Its description should summarize the user flow (pages/actions) and any acceptance criteria from the PDD.
        Test case: Create one manual test case - infer name from the PDD, derived from the PDD's numbered steps/screenshots — one test step per documented UI action, each with an expected result.
        Final step: After the PDD's last action, add a step that verifies the loan details page shows the same loan ID that was entered, along with the rest of the loan's details.
        Link: Link the new test case to the new requirement.
        Report back: give me the created requirement key and test case key when done.
        ```

    3. Ask Delegate to run the new test case.

**Check it:** a new **Loan Lookup** requirement, with a linked test case that has manual steps and a result in **Execution**.

??? example "Not quite right? Talk to Delegate"
    Open the new requirement and test case in Test Manager. Check the title, description, acceptance criteria, steps, and expected results.

    Then tell Delegate what to fix, in your own words, just as you'd tell a colleague. For example:

    ✅ *"The test case must check that the loan ID is the same, and that the loan's other details are displayed"*

    ✅ *"Don't use the data from the PDD in the test case"*

    ✅ *"Add the label 'Delegate' to this test case and requirement"*

    Keep going until you're happy with both.

??? example "Go further — Organize test cases in bulk"
    1. Replace `<YOUR_TEST_CASE_KEY>` with the key of the test case you ran in part 1, then paste:

        ```text
        Add the label "Delegate" to test case <YOUR_TEST_CASE_KEY> and to the Loan Lookup test case you created.
        ```

    2. Create a **Test Tier** custom field and set it on the labeled test cases:

        ```text
        Create a custom field definition for test cases in my project:
        - Name: Test Tier
        - Description: How often this test should run: every build, daily, or before release.
        - Object type: Test Cases
        - Data type: Label
        - Suggested values: Smoke, Core, Extended

        Then, for every test case with the label "Delegate", set Test Tier to "Smoke".
        ```

    **Check it:** open a labeled test case. Its **Details** tab shows the **Test Tier** dropdown set to **Smoke** (not a second Test Tier line).

    **Test Tier** is only a field. It doesn't add test cases to **UiBank Smoke Test Set**.

??? info "Beyond running tests — Delegate across the whole manual testing cycle"
    Ideas to try on your own project, in your own words:

    ✅ **Find test ideas** — from a requirement's acceptance criteria, or from a screenshot of a screen, including boundary and negative cases.

    ✅ **Write the steps** — turn those ideas into manual test cases and link them to the requirement.

    ✅ **Run them with you** — Delegate runs the steps and stops to ask when it needs a decision from you. Don't paste passwords into the chat: keep test logins in an Orchestrator Credential asset and give Delegate the asset name.

    ✅ **Record the results** — create test results with screenshots of failed steps, and upload them to Test Manager.

## Nice work!

Your test cases are proven against the real application, with results in Test Manager. Next, you'll connect Studio to automate them.

---

[Next → 05. Set Up Studio and Build the Object Repository](05-build-object-repository.md){: .md-button .md-button--primary}

---
