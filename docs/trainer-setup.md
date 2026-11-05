# Trainer Setup

Learners complete their own [Prerequisites](module-0-prerequisites/index.md), but those rely on setup only an organization or tenant admin can do. Complete this checklist **before the workshop**, ideally a few days ahead, and do a dry run with a test user.

## Organization and tenant

✅ Create the workshop **tenant** in an organization delivered through **Test Cloud**. Autonomous Test Execution and Autonomous Exploration (step 4) are only available in Test Cloud.

✅ Make sure the tenant has **Test Manager**, **Orchestrator**, and **Data Fabric** enabled.

✅ Make sure **Autopilot for Testers** is allowed for the tenant, in Test Manager and in Studio. Check that no AI Trust Layer or governance policy blocks it. To confirm, open a requirement in Test Manager: **Evaluate Requirement** is available.

✅ Make sure learners can use **Delegate** in the organization.

## Users and group

✅ Create a **group** for the workshop.

✅ Invite each learner to the organization, and add them to the group.

✅ Give permissions to the **group**, not to individual users, so late joiners get everything at once.

## Licenses and runtimes

✅ Assign an **App Test Developer** user license to the group or to each learner. Learners need it to create and publish Test Automation projects in Studio (steps 5 and 6).

✅ Allocate enough **App Testing** runtimes to the tenant: at least one per learner machine (Prerequisites: folder and robot setup).

✅ For **Run autonomously** and **Autonomous Exploration**, make sure a supported, non-serverless robot is available in each project's default folder. The robot machine must run Windows, and its UiPath browser extension must have **Allow in Incognito** turned on.

## Test Manager

✅ Give the group the **Project Creator** tenant role so learners can import the `.tmh` (step 1). The importer becomes **Project owner** of their project automatically, which covers Project Settings (Default Folder, step 1) and the Test Tier custom field (step 4). Autopilot's requirement evaluation needs requirement create and edit permissions, and Autonomous Exploration needs **Execute Automated Tests**.

✅ Learners download the **project file** (`.tmh`) from step 1. Check it imports into the workshop tenant.

## Orchestrator

✅ In the Prerequisites folder and robot setup, guide each learner to create a **personal folder**. Their machine is assigned to it, and it becomes their project's default folder.

✅ Give the group the roles it needs for the Prerequisites folder and robot setup. At tenant level, learners must be able to set up their own user: **Personal Automation + Personal workspace**, the **Automation Developer** role, and **Custom Windows credentials**. They also need rights to create their own folder and add machines and users to it. If you'd rather not grant these, do this setup for each learner before the session.

✅ If learners use credential assets in test cases, give them the **View** permission on **Assets**.

## Data Fabric

✅ Create the **UiBankTestData** entity from <a href="assets/Files/Data%20Fabric%20files/Schema.json" target="_blank">Schema.json</a>.

✅ Import the test data from <a href="assets/Files/Data%20Fabric%20files/UiBankLoanData.csv" target="_blank">UiBankLoanData.csv</a> into the entity.

✅ Give the group the **Data Reader** role, so learners can read the test data (step 6).

## Learner machines and network

✅ Learners need **local admin rights** to install the Studio STS installer and the UiPath browser extension for Chrome or Edge.

✅ Learners can reach `cloud.uipath.com` and the UiBank app at `https://uibank.uipath.com`, without a proxy or firewall blocking them.

## On the day

✅ Share the **organization name** and **tenant name** with learners.

✅ Do a dry run of steps 01, 04, 05, 06, and 08 with a test user in the learner group, including setting the Default Folder (step 1) and creating the Test Tier custom field (step 4). These are the steps that depend most on permissions.

## After the workshop

✅ Clean up the imported projects, learner folders, the Data Fabric entity, and robot runtime assignments. Remove learners from the group, or delete the tenant.
