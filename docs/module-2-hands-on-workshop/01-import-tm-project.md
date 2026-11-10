# 01. Import and Link the Test Manager Project

You start from a ready-made **UiBank** project: a requirement, test cases, a test set, results, and attachments.

## Download the project file

1. Download <a href="../../assets/Files/Agentic%20Testing%20Workshop%20-%20Sample%20Test%20Manager%20Project.zip" target="_blank">Agentic Testing Workshop - Sample Test Manager Project.zip</a>.
2. Unzip it. You'll import the `.tmh` file inside.

## Import it into Test Manager

1. Open **Test Manager** in the workshop tenant.
2. On **Projects**, select **Import Project** and drop the `.tmh` file.
3. Replace the **Name** and **Prefix** (project key) with your own, for example `UiBank_AlexS` and `UIBAS`, so your project is unique on the shared tenant.
4. Clear the **Include automation information for test cases** box.
5. Select **Import**.

!!! warning "Important"
    ✅ Clear **Include automation information for test cases** before you select **Import**.

    ✅ The import takes 3–15 minutes. Refresh the page to check: the project card shows **Import in progress…** until it's done, then **Created on**.

## Link the project to your folder

To run tests automatically, Test Manager needs to know which **Orchestrator folder** to use: the personal folder you set up in [Prerequisites](../module-0-prerequisites/index.md#orchestrator-folder-and-robot).

!!! example "It's your turn now!"
    In your Test Manager project, go to **Project Settings**, open the **Automation** tab, set **Default Folder** to your personal folder, and click **Save**.

!!! failure "Skipped this step?"
    Runs fail with `HTTP 400: Please assign folder to project level before executing testcases.`

    Your folder isn't in the **Default Folder** list? You're not assigned to it. Ask your trainer.

## Check it with Delegate

[Open Delegate](../module-0-prerequisites/01-installation-guide.md#step-2-meet-delegate) and ask, one at a time:

```text
List the Test Manager projects created by me, with their details. If there's more than one, ask me which one to use for this workshop. Remember that project, and use it whenever I ask about my project in this session.
```

```text
List the requirements in my project, with the test cases linked to each.
```

```text
Which test cases are in the UiBank Smoke Test Set of my project, and what were their latest results?
```

```text
Pick one test case in my project and show me its manual steps and expected results.
```

✅ Delegate finds your project: 1 requirement, **Submit Loan Request**, with 6 linked test cases, and 1 test set, **UiBank Smoke Test Set**, with the same 6. You use Submit Loan Request from step 2.

---

[Next → 02. Evaluate Requirements](02-evaluate-requirements.md){: .md-button .md-button--primary}

---
