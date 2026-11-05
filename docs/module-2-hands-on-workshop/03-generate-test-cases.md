# 03. Generate Test Cases

The **Generate Test Cases** built-in agent reads a requirement and proposes test cases with manual steps. It works from the requirement you improved in [02. Evaluate Requirements](02-evaluate-requirements.md). You review the test cases before they're saved.

## Generate them with a built-in agent

1. Open the **Submit Loan Request** requirement.
2. Click **Optimize Coverage**, and choose **Generate Tests**.
3. In **Provide additional context → Add documents**, select:

    ✅ **UiBank Regression Tests.xlsx** — matches the existing step style, avoids duplicates

    ✅ **UiBank Security Guidelines.pdf** — adds negative tests

    ✅ **UiBank Accessibility Guidelines.docx** — adds tests for labels, errors, and keyboard use

    ??? tip "Add documents or Leverage RAG?"
        | | Add documents | Leverage RAG |
        |---|---|---|
        | **What the agent reads** | The documents you select, **in full** | Only the **relevant passages** from a Context Grounding index |
        | **Best for** | Requirements whose rules live in a few known documents | Requirements with ambiguous terms or abbreviations whose meaning is spread across many sources |

        In this workshop, use **Add documents**.

        See <a href="https://docs.uipath.com/test-manager/automation-cloud/latest/user-guide/about-autopilot-chat" target="_blank">About Autopilot chat</a>.

4. On the next screen:
    1. **Select a prompt**: choose **Valid E2E Scenario Testing**. At the end of the prompt, add:

        ```text
        Add the label 'Coding Agent WS' to every test case you create.
        ```

        ??? info "Editing prompts and adding your own"
            ✅ **For this run only** — edit the prompt right here, as you just did.

            ✅ **For the whole project** — create new prompts or edit existing ones in the **Prompt Library**, under **Project Settings**.

    2. Below the prompt, add these instructions:

        ```text
        Generate 5 test cases. Give every step one action and an expected result, and add preconditions and postconditions.
        ```

    3. Choose a model.
    4. Click **Generate Tests**.
5. Expand each proposal and keep it only if it traces to one acceptance criterion, has one action per step, uses realistic data and expects what UiBank really shows. Otherwise sharpen the instructions and regenerate. Keep **2 or 3**, and create them.

    In production, turn on Testing Process Governance so a second reviewer signs off.

**Check it:** the requirement shows the new test cases as linked, each with manual steps and the **Coding Agent WS** label.

## Nice work!

You've gone from a requirement to reviewed, linked test cases in minutes.

---

[Next → 04. Run Manual Tests](04-run-manual-tests.md){: .md-button .md-button--primary}

---
