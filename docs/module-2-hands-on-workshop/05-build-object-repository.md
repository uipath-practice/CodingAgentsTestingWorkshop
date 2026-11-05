# 05. Set Up Studio and Build the Object Repository

Set up a Studio Test Automation project with Delegate, link it to Test Manager, and build the Object Repository that Autopilot uses in the next step.

!!! warning "Access required"
    You need an **App Test Developer** license to create and publish Test Automation projects.

## What you'll do

<span class="tool-badge tool-badge--delegate">Delegate</span>

You work in **Delegate** on this page: paste each prompt, then wait and watch it build in Studio. Click a step to jump to it.

<div class="flow">
  <div class="flow-part flow-part--delegate" style="--steps: 4">
    <span class="flow-part-label">Delegate</span>
    <div class="flow-part-steps">
      <a class="flow-step" href="#create-a-test-automation-project">Create a Test Automation project</a>
      <span class="flow-arrow"></span>
      <a class="flow-step" href="#install-the-ui-automation-package">Install the UI Automation package</a>
      <span class="flow-arrow"></span>
      <a class="flow-step" href="#link-studio-to-your-test-manager-project">Link Studio to your Test Manager project</a>
      <span class="flow-arrow"></span>
      <a class="flow-step" href="#build-the-object-repository">Build the Object Repository</a>
    </div>
  </div>
</div>

## Create a Test Automation project

<span class="tool-badge tool-badge--delegate">Delegate</span>

Replace `<YOUR_NAME>` with your name, for example `AlexS`, so your package is unique on the shared tenant. Then paste:

```text
Create a Studio Test Automation project named <YOUR_NAME>_UiBank Tests.
```

**Check it:** your project opens in Studio, in `Documents\UiPath\<YOUR_NAME>_UiBank Tests`.

## Install the UI Automation package

<span class="tool-badge tool-badge--delegate">Delegate</span>

```text
Install the latest stable UI Automation activities package in <YOUR_NAME>_UiBank Tests.
```

**Check it:** **Manage Packages → Project Dependencies** lists **UiPath.UIAutomation.Activities**.

## Link Studio to your Test Manager project

<span class="tool-badge tool-badge--delegate">Delegate</span>

Paste:

```text
Connect this project to my Test Manager project, then open Test Explorer to show its test cases.
```

**Check it:** the connection icon is green, and **Test Explorer** lists your test cases.

## Build the Object Repository

<span class="tool-badge tool-badge--delegate">Delegate</span>

The **Object Repository** stores the app's screens and UI elements for every test case to reuse. 


Building it by hand is usually one of the slowest parts of test automation: you capture every screen and element yourself. Tell Delegate what to capture, and it builds the repository for you. To cover every screen and element the test cases need, use the prompt below.


!!! example "Delegate"
    1. Prompt in Delegate:

        ```text
        Create an Object Repository in UiPath Studio Desktop for the UiBank web app running in Chrome.

        Application
        - Name: UiBankORForChrome
        - Browser: Chrome
        - Capture each element live in the browser
        - Prefer stable selectors (id, name, aria-label, visible text) over index-based ones
        - Avoid dynamic values in selectors
        - Name each element exactly as listed below

        Screens and elements

        1. Screen: Home (https://uibank.uipath.com/welcome)
           - Username (input)
           - Password (input)
           - Sign In (button)
           - Products (dropdown menu)
           - Loans (menu item in the Products dropdown; open Products first so Loans is visible when you capture it)

        2. Screen: Selection (https://uibank.uipath.com/loans)
           - Apply For A Loan (button; the one on the Loans page, not the Apply For Loan button on the Welcome page)
           - Already Have A Loan? (button)

        3. Screen: Form (https://uibank.uipath.com/loans/apply)
           - Email (input)
           - Amount (input)
           - Term (dropdown)
           - Income (input)
           - Age (input)
           - Submit (button)

        4. Screen: Quote (the results view shown after you submit the loan application)
           - Result Text: the full text block of the response
           - Rate: only the number shown below "With a fantastic rate of:", without the "%" sign
           - Loan ID: the value shown below "Your new loan ID is:"
           Anchor these elements to their label text, not to the changing values, so the selectors work for any result.
           To reach this screen, submit the form with sample valid values. Save the Loan ID for screen 6.

        5. Screen: Loan Lookup (https://uibank.uipath.com/loans/lookup)
           - Loan ID (input)
           - Retrieve Loan Details (button)

        6. Screen: Loan Lookup Result (the results view shown after you look up a Loan ID)
           - Result Text: the full text block of the response
           - Loan ID: the value shown beside its label, anchored to the label text
           To reach this screen, look up the Loan ID you saved from screen 4.

        Acceptance criteria
        - All 6 screens and 20 elements exist under UiBankORForChrome, named as above
        - Every selector validates (highlights the correct element) on its live screen
        - Report any element you could not capture reliably, and why
        ```

    2. Don't use your desktop or browser while it captures.

!!! tip "Using Edge?"
    The prompt uses Chrome. If you use Edge, change **running in Chrome** and **Browser: Chrome** to Edge. Keep the name **UiBankORForChrome**, so the next steps still match.

??? tip "Write your own Object Repository prompt"
    Describe what you need in plain language, such as the app, its screens, and the elements to capture. Delegate can also review and fine-tune your prompt, or fix it when something's missed.

??? tip "Check it"
    1. In Studio's **Object Repository** panel, expand **UiBankORForChrome**. It lists all 6 screens and their elements. If it's empty, reload the project.

        ![Object Repository panel](../assets/images/Object%20Repo.png){ width="300" }

    2. Open UiBank in your browser on the Home screen. Right-click an element, such as **Username**, and select **Highlight**.

        ![Highlight an element](../assets/images/Studio%20OR%20Highlight.png){ width="300" }

    3. In the browser, the element is outlined in **green**, and its label anchor in **blue**. Repeat for a few elements on each screen.

        ![Highlighted element in UiBank](../assets/images/UiBank%20Highlight.png)

    If an element doesn't highlight, ask Delegate to recapture it.

??? tip "Backup: import a ready-made Object Repository"
    1. Download <a href="../../assets/Files/Object%20Repository/UiBankORForChrome.Descriptors.1.0.1.nupkg" target="_blank">UiBankORForChrome.Descriptors.1.0.1.nupkg</a> and save it to a folder you can find.
    2. In Studio, click **Manage Packages** from the top ribbon.
    3. Go to **Settings**.
    4. Give the package source a unique name.
    5. Click the ellipsis (**...**), browse to the folder where you saved the library, and click **Add**.
    6. Select the new source in the left panel, select the library, click **Install**, then click **Save**.

        ![Custom Library Listing](../assets/images/custom%20library%20listing.png)

!!! warning "Complete this step before you continue"
    **Autopilot for Testers** builds your test cases from the Object Repository elements. Without them, it can't automate the test cases in the next step.

## Nice work!

Your project is set up, linked to Test Manager, and the Object Repository is built. This is a good point for a break.

---

[Next → 06. Automate and Publish the Test Cases](06-automate-and-publish.md){: .md-button .md-button--primary}

---
