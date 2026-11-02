# 02. Configure the Test Manager Folder

To run tests automatically, your project needs an **Orchestrator folder** with a **machine** that has an **App Testing** runtime, linked to the project.

## Part 1 — Set up your folder and robot

### Create your folder

1. Create a personal folder, as your trainer guides you. You'll assign your machine to it.
2. You get your permissions through a group your trainer sets up: **Personal Automation + Personal workspace**, with the **Automation Developer** role. You don't need to set them yourself.
3. In the Enterprise setup, use **Custom Windows credentials**: your `domain\username` and your system's Windows password.

    ![Personal automation and Enterprise robot setup settings](../assets/images/OC%20Settings%20Enterprize%20setup.png){ width="400" }

### Give your machine an App Testing runtime

1. Edit your machine template. Under **Runtime details**, set **App Testing** to **1**, and save.

    ![App Testing runtime in the machine template](../assets/images/OC%20App%20testing%20license.png)

2. Open your personal folder. In the **Manage Access** tab, check that your username is listed, with **Attended, Unattended** under **Robot Type**.

    ![Manage Access tab of the folder](../assets/images/OC%20Settings%20Folder%20Admin.png)

3. Open the **Machines** tab, next to **Manage Access**. Click **Manage Machines in Folder**, and select your machine to add it to the folder.

    ![Manage Machines in Folder button](../assets/images/OC%20Manage%20machine.png)

## Part 2 — Link the project to the folder

!!! example "It's your turn now!"
    In your Test Manager project, go to **Project Settings**, open the **Automation** tab, set **Default Folder** to the folder you created in Part 1, and click **Save**.

!!! failure "Skipped this step?"
    Runs fail with `HTTP 400: Please assign folder to project level before executing testcases.`

## Nice work!

Your project has a folder and a robot to run its tests.

---

[Next → 03. Evaluate Requirements](03-evaluate-requirements.md){: .md-button .md-button--primary}

---
