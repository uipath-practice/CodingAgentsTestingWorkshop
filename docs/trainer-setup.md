# Trainer Setup

Learners complete their own [Prerequisites](module-0-prerequisites/index.md), but those rely on setup only an organization or tenant admin can do. Complete this checklist **before the workshop**, ideally a few days ahead, and do a dry run with a test user.

## Organization and tenant

✅ Create the workshop **tenant** in an organization.

!!! info "Test Cloud only"
    **Run autonomously** and **Autonomous Exploration** are only available in Test Cloud.

✅ Make sure the tenant has **Test Manager**, **Orchestrator**, and **Data Fabric** enabled.

✅ Make sure **Autopilot for Testers** is allowed for the tenant, in Test Manager and in Studio. Check that no AI Trust Layer or governance policy blocks it. To confirm, open a requirement in Test Manager → **Optimize Coverage**: **Evaluate Quality** is available.

✅ Make sure learners can use **Delegate** in the organization.

## Users and group

✅ Create a **group** for the workshop.

✅ Invite each learner to the organization, and add them to the group.

✅ Give permissions to the **group**, not to individual users, so late joiners get everything at once.

## Licenses and runtimes

Use the column for your organization type. Learners need the user license to create and publish Test Automation projects in Studio (steps 5 and 6), and the runtime for their machine (Prerequisites: folder and robot setup).

| | Test Cloud organization | Automation Cloud organization |
|---|---|---|
| Learner user license | **App Test Developer - Named User** (App Tester can't create or publish Test Automation projects) | **Automation Developer - Named User** (includes Tester for Test Manager) |
| Where to assign | Organization-wide, no tenant allocation | User license to the group or each learner |
| Robot runtime for the tenant | **App Test Robot**: at least one per learner machine | **Testing**: at least one per learner machine |
| Machine template runtime type | **App Testing** | **Testing** |
| Run autonomously, Autonomous Exploration (step 4 tips) | Available | Not available |

✅ **Optional:** for the **Run autonomously** and **Autonomous Exploration** tips in step 4, make sure a supported, non-serverless robot is available in each project's default folder. The robot machine must run Windows, and its UiPath browser extension must have **Allow in Incognito** turned on.

## Test Manager

✅ Give the group the **Project Creator** tenant role so learners can import the `.tmh` (step 1). The importer becomes **Project owner** of their project automatically, which covers Project Settings (Default Folder, step 1) and the Test Tier custom field (step 4). Autopilot's requirement evaluation needs requirement create and edit permissions, and Autonomous Exploration needs **Execute Automated Tests**.

✅ Learners download the **project file** (`.tmh`) from step 1. Check it imports into the workshop tenant.

## Orchestrator

✅ In the Prerequisites folder and robot setup, guide each learner to create a **personal folder**. Their machine is assigned to it, and it becomes their project's default folder.

✅ **Recommended:** do the Prerequisites folder and robot setup for each learner before the session, so learners don't need tenant-level rights.

✅ If learners do it themselves, give the group: **Personal Automation + Personal workspace**, the **Automation Developer** role, and **Custom Windows credentials** at tenant level, plus rights to create their own folder and add machines and users to it.

✅ If learners use credential assets in test cases, give them the **View** permission on **Assets**.

## Data Fabric

✅ Create the **UiBankTestData** entity from <a href="../assets/Files/Data%20Fabric%20files/Schema.json" target="_blank">Schema.json</a>.

✅ Import the test data from <a href="../assets/Files/Data%20Fabric%20files/UiBankLoanData.csv" target="_blank">UiBankLoanData.csv</a> into the entity. It has 3 rows. Imported an earlier version? Import it again.

✅ Before the workshop, check that UiBank still approves a loan for an applicant aged 66. The age-66 row relies on this defect, so step 6's test case fails and step 8 has a UiBank defect to triage. If UiBank now rejects it, remove the row, and tell learners to expect **GO** in step 8.

✅ Give the group the **Data Reader** role, so learners can read the test data (step 6).

## Learner machines and network

✅ Learners need **local admin rights** to install the Studio STS installer and the UiPath browser extension for Chrome or Edge.

✅ Learners can reach `cloud.uipath.com` and the UiBank app at `https://uibank.uipath.com`, without a proxy or firewall blocking them.

## On the day

✅ Share the **organization name** and **tenant name** with learners.

✅ Do a dry run of steps 01, 04, 05, 06, and 08 with a test user in the learner group, including setting the Default Folder (step 1) and creating the Test Tier custom field (step 4). These are the steps that depend most on permissions.

## After the workshop

✅ Clean up the imported projects, learner folders, the Data Fabric entity, and robot runtime assignments. Remove learners from the group, or delete the tenant.
