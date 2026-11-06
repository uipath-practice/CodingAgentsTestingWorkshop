# Prerequisites

Complete this section **before the workshop**, then follow the **[Installation Guide](01-installation-guide.md)**.

## Your machine

✅ A **Windows 10 or 11** laptop. The workshop uses Studio Desktop, and your machine runs your tests as a robot.

✅ **Local admin rights**, to install Studio and the UiPath browser extension

✅ A browser: **Google Chrome** or **Microsoft Edge**

✅ Access to <a href="https://cloud.uipath.com" target="_blank">cloud.uipath.com</a> and <a href="https://uibank.uipath.com" target="_blank">uibank.uipath.com</a>, with no proxy or firewall blocking them

## Accounts and access

!!! info "Access is provided by your trainer"
    Your trainer gives you access to the workshop **organization** and **tenant** and guides you through signing in.

    Trainers: see [Trainer Setup](../trainer-setup.md).

Confirm that you can:

✅ Sign in to <a href="https://cloud.uipath.com" target="_blank">UiPath Automation Cloud</a> and open the workshop **organization** and **tenant**

✅ Open **Test Manager** and **Orchestrator** in that tenant

✅ Use an **App Test Developer** license, to create Test Automation projects

✅ Connect **UiPath Assistant** to your Cloud account (see [Installation Guide, step 2](01-installation-guide.md#step-2-meet-delegate))

## Orchestrator folder and robot

Signing in to Automation Cloud lets you open Test Manager, but not run tests. Test Manager runs tests through **Orchestrator**, on a **robot**, in a **folder**. Your folder holds:

✅ **Your permissions**, which let you run tests in that folder

✅ **Your machine**, with a testing runtime, where the robot runs your tests


??? info "Trainer-led setup: your folder and machine"
    Your trainer guides you through these steps.

    **Create your folder**

    1. Create a personal folder, as your trainer guides you. You'll assign your machine to it.
    2. You get your permissions through a group your trainer sets up. You don't need to set them yourself.
    3. In the Enterprise setup, use **Custom Windows credentials**: your `domain\username` and your system's Windows password.

        ![Personal automation and Enterprise robot setup settings](../assets/images/OC%20Settings%20Enterprize%20setup.png){ width="400" }

    !!! tip "Workshop shortcut"
        Your own user runs the tests. In production, an admin assigns a dedicated **robot account** and a machine template to the folder.

    **Set up your machine and folder**

    1. In Orchestrator, select **Tenant** (top left) → **Machines**, and search for your name.

        ![Machines tab at the tenant level, with the search box](../assets/images/OC%20Tenant%20Machines.png)

    2. Edit your machine template. Under **Runtime details**, set **App Testing** or **Testing** to **1**, whichever you see, and save.

        ![App Testing runtime in the machine template](../assets/images/OC%20App%20testing%20license.png)

    3. Still at the **Tenant** level, go to **Folders** and open your personal folder. In the **Manage Access** tab, check that your username is listed, with **Attended, Unattended** under **Robot Type**.

        ![Manage Access tab of the folder](../assets/images/OC%20Settings%20Folder%20Admin.png)

    4. Open the **Machines** tab, next to **Manage Access**. Click **Manage Machines in Folder**, select your machine, then click **Update** to add it to the folder.

        ![Manage Machines in Folder button](../assets/images/OC%20Manage%20machine.png)

---

[Next → Installation Guide](01-installation-guide.md){: .md-button .md-button--primary}
