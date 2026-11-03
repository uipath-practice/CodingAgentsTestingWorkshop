# Prerequisites

Complete this section **before the workshop**, then follow the **[Installation Guide](01-installation-guide.md)**.

## Accounts and access

!!! info "Access is provided by your trainer"
    Your trainer gives you access to the workshop **organization** and **tenant** and guides you through signing in.

Confirm that you can:

✅ Sign in to <a href="https://cloud.uipath.com" target="_blank">UiPath Automation Cloud</a> and open the workshop **organization** and **tenant**

✅ Open **Test Manager** and **Orchestrator** in that tenant

✅ Use an **App Test Developer** license, to create Test Automation projects

✅ **Create Data Fabric entities**, for test data in [05. Automate Test Cases with Studio Desktop and Delegate](../module-2-hands-on-workshop/05-automate-with-studio-and-delegate.md)

✅ Connect **UiPath Assistant** to your Cloud account

## Orchestrator folder and robot

Signing in to Automation Cloud lets you open Test Manager, but not run tests. Test Manager runs tests through **Orchestrator**, on a **robot**, in a **folder**. Your folder holds:

✅ **Your permissions**, which let you run tests in that folder

✅ **Your machine**, with an **App Testing** runtime, where the robot runs your tests

Later, in [01. Import and Link the Test Manager Project](../module-2-hands-on-workshop/01-import-tm-project.md#link-the-project-to-your-folder), you point your Test Manager project to this folder.

??? info "Trainer-led setup: your folder and machine"
    Your trainer guides you through these steps.

    **Create your folder**

    1. Create a personal folder, as your trainer guides you. You'll assign your machine to it.
    2. You get your permissions through a group your trainer sets up. You don't need to set them yourself.
    3. In the Enterprise setup, use **Custom Windows credentials**: your `domain\username` and your system's Windows password.

        ![Personal automation and Enterprise robot setup settings](../assets/images/OC%20Settings%20Enterprize%20setup.png){ width="400" }

    **Set up your machine and folder**

    1. Edit your machine template. Under **Runtime details**, set **App Testing** to **1**, and save.

        ![App Testing runtime in the machine template](../assets/images/OC%20App%20testing%20license.png)

    2. Open your personal folder. In the **Manage Access** tab, check that your username is listed, with **Attended, Unattended** under **Robot Type**.

        ![Manage Access tab of the folder](../assets/images/OC%20Settings%20Folder%20Admin.png)

    3. Open the **Machines** tab, next to **Manage Access**. Click **Manage Machines in Folder**, select your machine, then click **Update** to add it to the folder.

        ![Manage Machines in Folder button](../assets/images/OC%20Manage%20machine.png)

---

[Next → Installation Guide](01-installation-guide.md){: .md-button .md-button--primary}
