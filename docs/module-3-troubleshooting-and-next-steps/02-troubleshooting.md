# Troubleshooting

## Delegate

| Symptom | Likely cause / fix |
|---|---|
| Delegate isn't in UiPath Assistant's top ribbon | Your Studio version may be too old. Install the latest STS version from the [Installation Guide](../module-0-prerequisites/01-installation-guide.md), and ask your trainer to confirm your access. |
| Delegate asks for approval on every step | The approval mode is **Cautious**. In **Settings → Security**, switch it to **Adaptive**. Delegate still asks before high-impact actions, such as starting the run in step 8. That's expected. |
| Delegate can't find your project | Delegate is signed in to the wrong tenant. Ask Delegate *"Run uip login status."* to see which tenant it uses. If it's wrong, ask *"Log me in with uip login."* and sign in to the tenant from your trainer. |
| `Authentication failed` or `401 Unauthorized` | Your `uip` sign-in has expired. Ask Delegate *"Log me in with uip login."* and sign in with your workshop account in the browser window that opens. |

## Execution

| Symptom | Likely cause / fix |
|---|---|
| *"We weren't able to locate a matching loan ID"* | The loan ID doesn't exist in UiBank. Use the loan ID from your own loan application in [04. Run Manual Tests](../module-2-hands-on-workshop/04-run-manual-tests.md#3-create-a-new-requirement-and-test-case-optional). |
| Publishing fails | UiPath Assistant isn't connected to Orchestrator. Reconnect it, then [publish the test cases](../module-2-hands-on-workshop/06-automate-and-publish.md#publish-the-test-cases) again. |
| Delegate can't start the test set run | The test set has no automated test case. [Publish the test cases](../module-2-hands-on-workshop/06-automate-and-publish.md#publish-the-test-cases) again, then check that the set lists them in [07. Create a Test Set](../module-2-hands-on-workshop/07-create-test-set.md). |
| `HTTP 400: Please assign folder to project level before executing testcases.` | The project has no default folder. Complete [01. Import and Link the Test Manager Project](../module-2-hands-on-workshop/01-import-tm-project.md#link-the-project-to-your-folder). |
| Test cases are skipped with no result | They're manual — not linked to a published automation. Complete [Publish the test cases](../module-2-hands-on-workshop/06-automate-and-publish.md#publish-the-test-cases) and check each test case shows an automation. |
| The run stays pending or hangs | The robot is busy or disconnected. In Orchestrator, check the machine in your folder is connected and has an **App Testing** or **Testing** runtime. |
| Tests fail with "Cannot communicate with the browser" | A robot-side problem with the UiPath browser extension, not a product defect. Check the extension is installed and enabled on the robot machine. |

## Report

| Symptom | Likely cause / fix |
|---|---|
| You can't find the report | Delegate shows the path when it finishes. If you chose **Current working directory**, the file is inside the Assistant install folder, which is hard to find. Ask Delegate *"Create a PDF of the report and copy to my Downloads folder"*. |
| The report numbers don't match Test Manager | Make sure you're comparing the **same execution**. Ask Delegate which execution ID it used. |

!!! info "Still stuck?"
    Ask your trainer, or ask in Delegate — for example *"Why did that last step fail, and how do I fix it?"*

---

[Back to Home](../index.md){: .md-button .md-button--primary}

---
