# Coding Agents for Test — Hands-On Workshop Guide

The learner's handbook for the UiPath **Coding Agents for Test** instructor-led workshop. It's an MkDocs site that walks testers through UiPath Test Cloud, from requirements to a go/no-go release report, using AI agents at every stage.

## What the workshop covers

Learners work on a ready-made **UiBank** Test Manager project. In eight hands-on steps, they take a loan application requirement all the way to an automated test run. Then they ask an agent for a release report in plain English.

| Phase | Steps | What learners do | Tools |
|---|---|---|---|
| **1 · Set up** | 1–2 | Import the project, and configure the Orchestrator folder and robot | Test Manager, Orchestrator |
| **2 · Plan & test** | 3–5 | Evaluate the requirement, generate test cases, and run them manually | Test Manager, Autopilot for Testers, Delegate |
| **3 · Build** | 6 | Connect Studio, build the Object Repository, automate the test cases, attach test data, and publish | Studio, Autopilot, Delegate, Data Fabric |
| **4 · Run & report** | 7–8 | Create a test set, trigger it, and get a go/no-go PDF in one prompt | Test Manager, Delegate |

By the end, learners have:

✅ Used the agentic features in Test Manager: requirement evaluation, test case generation, autonomous execution, and exploration

✅ Used **Delegate** at different stages of testing, from running manual tests to building release reports

✅ Turned manual test cases into automations with **Autopilot for Testers** in Studio

**Delegate** is the agent throughout.

## Trainer setup

The trainer checklist is in the guide, so trainers who only get the site URL can find it: [Trainer Setup](docs/trainer-setup.md) (`https://uipath-practice.github.io/CodingAgentsTestingWorkshop/trainer-setup/`).

## How the guide is organized

| Folder | Section |
|---|---|
| [`docs/module-0-prerequisites/`](docs/module-0-prerequisites/) | Accounts, access, and installing Studio and Delegate |
| [`docs/module-1-introduction/`](docs/module-1-introduction/) | A short tour of Test Cloud, Test Manager, and the agents |
| [`docs/module-2-hands-on-workshop/`](docs/module-2-hands-on-workshop/) | The eight hands-on steps |
| [`docs/module-3-troubleshooting-and-next-steps/`](docs/module-3-troubleshooting-and-next-steps/) | More prompts to try, and fixes for common problems |
| [`docs/assets/`](docs/assets/) | Images, CSS, scripts, and downloadable files |

The navigation is defined in [`mkdocs.yml`](mkdocs.yml).

## Preview the guide locally

On Windows, double-click [`start-guide.bat`](start-guide.bat). On first run, it creates a Python virtual environment and installs `mkdocs-material`. Then it opens the guide at <http://127.0.0.1:8000>.

On any other system, with Python 3 installed:

```bash
pip install mkdocs-material
mkdocs serve
```

The preview reloads automatically when you save a page.

## Publishing

Every push to `main` publishes the site to GitHub Pages through [`.github/workflows/deploy.yml`](.github/workflows/deploy.yml).

## Contributing

- **Branches:** `main` is the live site, and every push deploys it. Commit small fixes (typos, wording, a broken link) straight to `main`. For bigger changes, use a short-lived `feature/*` branch off `main`, preview it with `mkdocs serve`, then merge it to `main`. There's no `dev` branch.
- **Content standards:** every page is reviewed against the standards in [`CLAUDE.md`](CLAUDE.md): completeness, accuracy, styling, learning flow, clarity, and compliance, scored out of 15.
