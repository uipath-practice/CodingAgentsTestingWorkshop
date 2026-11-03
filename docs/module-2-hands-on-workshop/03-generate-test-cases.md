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
        | **Best for** | A few specific documents | Large document sets |

4. On the next screen:
    1. **Select a prompt**: choose **Valid E2E Scenario Testing**. At the end of the prompt, add:

        ```text
        Add the label 'Coding Agent WS' to every test case you create.
        ```

        ??? info "Editing prompts and adding your own"
            ✅ **For this run only** — edit the prompt right here, as you just did.

            ✅ **For the whole project** — create new prompts or edit existing ones in the **Prompt Library**, under **Project Settings**.

    2. Optionally, add instructions, for example *"Focus on the age and income rules in the acceptance criteria, and apply the security guidelines."*
    3. Choose a model.
    4. Click **Generate Tests**.
5. Review the proposals, keep **2 or 3**, and create them.

**Check it:** the requirement shows the new test cases as linked, each with manual steps and the **Coding Agent WS** label.

## Nice work!

You've gone from a requirement to reviewed, linked test cases in minutes.

---

[Next → 04. Run Manual Tests](04-run-manual-tests.md){: .md-button .md-button--primary}

---
