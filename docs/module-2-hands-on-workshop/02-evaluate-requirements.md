# 02. Evaluate Requirements

Vague or incomplete requirements lead to gaps in testing. The **Evaluate Requirement Quality** built-in agent finds gaps in a requirement, such as undefined thresholds, ambiguous input formats, and missing edge cases or validation rules, and suggests fixes.

## Evaluate it with a built-in agent

1. Open **Requirements** → **Submit Loan Request**.
2. Click **Optimize Coverage**, and choose **Evaluate Quality**.
3. In **Provide additional context → Add documents**, select these project documents (marked **P**), so the agent checks the requirement against their rules:

    ✅ **UiBank Glossary of Terms.txt** — undefined banking terms

    ✅ **UiBank Security Guidelines.pdf** — input validation, data masking, sessions

    ✅ **UiBank Accessibility Guidelines.docx** — form labels, error messages, keyboard support

    ![Add documents tab in Provide additional context](../assets/images/Add%20Documents%20dialog.png){ .img-equal }

    ??? tip "Where do these documents come from?"
        They're the project's attachments, under **Dashboard → Attachments**:

        ![Attachments tab of the Test Manager project](../assets/images/Attachments%20in%20TM.png){ .img-equal }

4. On the next screen:
    1. **Select a prompt**: choose **Multifaceted Audit**.

        ??? info "Editing prompts and adding your own"
            The built-in prompts are editable, and you can add custom prompts of your own. Manage them in the **Prompt Library**, under **Project Settings**.

    2. Choose a model.
    3. Click **Evaluate quality**. The agent can takes a minute or so. You can close the dialog while it works.
5. On the requirement, click **Quality enhancements** under **Latest activity** to see the suggestions.

    ![Quality enhancements under Latest activity on the requirement](../assets/images/TM%20Quality%20enhancements.png)

6. Expand each suggestion. Select **Add to Requirement** for the ones you agree with. Each one you add appears at the end of the description: its title, with the suggestion below it.
7. Edit the requirement. Under each added title, replace the suggestion with the rule itself, and save.

**Check it:** each title you added has a rule under it, not the suggestion.

!!! question "Think about it"
    Can you spot gaps in the acceptance criteria — an applicant who is exactly 18 or 65, or a loan amount that matches two approval rules? Did the agent find them?

??? example "Sample: look beyond the suggestion"
    The agent's suggestions differ for each learner, so yours may not include this one.

    ![An enhancement suggestion: Add Rejection Criteria and Messages](../assets/images/TM%20Enhancement%20suggestion.png)

    The suggestion says rejection rules are missing, but not what UiBank shows. Try its examples in <a href="https://uibank.uipath.com" target="_blank">UiBank</a>, and write the exact rejection text as the rule:

    ```text
    Add Rejection Criteria and Messages
    Applicants requesting $150,000 for 3 years with $400,000 income: Reject with "You must be at least 18 years old for a loan and the loan must not exceed 100k."
    ```

## Check the requirement against UiBank

Test cases are generated from the requirement's text, so its messages must match what UiBank shows.

1. In <a href="https://uibank.uipath.com" target="_blank">UiBank</a>, go to **Products → Loans → Apply For A Loan**, and apply with an age of **17**.
2. Compare the message UiBank shows with the rejection message in the requirement's acceptance criteria, "Not approved due to age."

## Fix the requirement

1. Edit **Submit Loan Request**.
2. In the acceptance criteria, replace "Not approved due to age." with the message UiBank shows.
3. Save.

??? tip "Make every rule measurable"
    Edit the acceptance criteria themselves so each rule is measurable, with exact boundaries (18, 65, $100,000) and the exact message UiBank shows for approval and rejection. [03. Generate Test Cases](03-generate-test-cases.md) generates test cases from this text.

## Nice work!

Your requirement is clearer and more testable — ready for generating test cases.

---

[Next → 03. Generate Test Cases](03-generate-test-cases.md){: .md-button .md-button--primary}

---
