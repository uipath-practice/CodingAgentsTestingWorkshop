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
Create a blank Studio Test Automation project named <YOUR_NAME>_UiBank Tests, with Windows compatibility.
```

**Check it:** your project opens in Studio, in `Documents\UiPath\<YOUR_NAME>_UiBank Tests`.

??? tip "Do it by hand in Studio"
    1. In Studio, go to **Home → New Project → Test Automation**.

        ![New Project → Test Automation in Studio](../assets/images/New%20Test%20Automation%20Project.png)

    2. Name it `<YOUR_NAME>_UiBank Tests`, choose **Windows** compatibility, and create the project.

## Install the UI Automation package

<span class="tool-badge tool-badge--delegate">Delegate</span>

```text
Install the latest stable UI Automation activities package in <YOUR_NAME>_UiBank Tests.
```

**Check it:** **Manage Packages → Project Dependencies** lists **UiPath.UIAutomation.Activities**.

??? tip "Do it by hand in Studio"
    1. Select **Manage Packages** in the Studio ribbon.

        ![Manage Packages in the Studio ribbon](../assets/images/Studio%20Manage%20Packages%20button.png)

    2. Select **All Packages** and search for `UiPath.UIAutomation.Activities`.

        ![Searching All Packages for UiPath.UIAutomation.Activities](../assets/images/Studio%20Manage%20Packages%20search.png)

    3. Select **UiPath.UIAutomation.Activities**, install the latest stable version, and select **Save**.

## Link Studio to your Test Manager project

<span class="tool-badge tool-badge--delegate">Delegate</span>

Paste:

```text
Connect this project to my Test Manager project, then open Test Explorer to show its test cases.
```

**Check it:** in **Test Manager Settings**, the status is **Connected** and **Default Project** is your project. **Test Explorer** lists your test cases.

??? tip "Do it by hand in Studio"
    1. Select **Test Manager** in the Studio ribbon.

        ![Test Manager in the Studio ribbon](../assets/images/Studio%20Test%20Manager%20button.png)

    2. Select **Test Manager Settings**.

        ![Test Manager Settings in the Test Manager menu](../assets/images/Studio%20Test%20Manager%20Settings%20menu.png)

    3. Check that the URL is your tenant's Test Manager, and select **Connect**. The status changes to **Connected**.
    4. In **Default Project**, type your project key and select your project from the list.

        ![Test Manager Settings, Connected, with the UiBank project selected](../assets/images/Studio%20Test%20Manager%20connected.png)

    5. Select **OK**.

## Build the Object Repository

<span class="tool-badge tool-badge--delegate">Delegate</span>

The **Object Repository** stores the app's screens and UI elements for every test case to reuse. 


Building it by hand is usually one of the slowest parts of test automation: you capture every screen and element yourself. Tell Delegate what to capture, and it builds the repository for you. To cover every screen and element the test cases need, use the prompt below.


!!! warning "This prompt is built for Chrome"
    Using Edge? Before you send the prompt, change **Chrome** to **Edge** in the two highlighted lines:

    ✅ The first sentence: **running in Chrome**

    ✅ Under **Application**: **Browser: Chrome**

    Keep the name **UiPath Banking App**, so the next steps still match.

!!! example "Delegate"
    1. Prompt in Delegate:

        ```text hl_lines="1 5"
        Create an Object Repository in UiPath Studio Desktop for the UiBank web app running in Chrome.

        Application
        - Name: UiPath Banking App
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
        - All 6 screens and 20 elements exist under UiPath Banking App, named as above
        - Every selector validates (highlights the correct element) on its live screen
        - Report any element you could not capture reliably, and why
        ```

    2. Don't use your desktop or browser while it captures, except to approve Delegate's requests. It asks before it submits the sample loan application.

    The prompt also captures **Username**, **Password** and **Sign In**. If a test signs in, read the login from a Credential asset with **Get Credential**.

??? tip "Write your own Object Repository prompt"
    Describe what you need in plain language, such as the app, its screens, and the elements to capture. Delegate can also review and fine-tune your prompt, or fix it when something's missed.

??? tip "Check it"
    1. In Studio's **Object Repository** panel, expand **UiPath Banking App**. It lists all 6 screens and their elements. If it's empty, reload the project.

        ![Object Repository panel](../assets/images/Object%20Repo.png){ width="300" }

    2. Open UiBank in your browser on the Home screen. Right-click an element, such as **Username**, and select **Highlight**.

        ![Highlight an element](../assets/images/Studio%20OR%20Highlight.png){ width="300" }

    3. In the browser, the element is outlined in **green**, and its label anchor in **blue**. Repeat for a few elements on each screen.

        ![Highlighted element in UiBank](../assets/images/UiBank%20Highlight.png)

    If an element doesn't highlight, ask Delegate to recapture it.

??? tip "Backup: import a ready-made Object Repository"
    1. On your Desktop, create a folder named **Custom Library**.
    2. Download the library for your browser and move it into **Custom Library**:

        ✅ Chrome: <a href="../../assets/Files/Object%20Repository/UiBankORForChrome.1.0.1.nupkg" target="_blank">UiBankORForChrome.1.0.1.nupkg</a>

        ✅ Edge: <a href="../../assets/Files/Object%20Repository/UiBankORForEdge.1.0.1.nupkg" target="_blank">UiBankORForEdge.1.0.1.nupkg</a>

    3. In Studio, click **Manage Packages** from the top ribbon.
    4. Go to **Settings**.
    5. Give the package source a unique name.
    6. Click the ellipsis (**...**), browse to **Desktop\Custom Library**, and click **Add**.
    7. Select the new source in the left panel, select **UiBankORForChrome** or **UiBankORForEdge**, click **Install**, then click **Save**.

        ![Custom Library Listing](../assets/images/custom%20library%20listing.png)

!!! warning "Complete this step before you continue"
    **Autopilot for Testers** builds your test cases from the Object Repository elements. Without them, it can't automate the test cases in the next step.

## Nice work!

Your project is set up, linked to Test Manager, and the Object Repository is built. This is a good point for a break.

---

[Next → 06. Automate and Publish the Test Cases](06-automate-and-publish.md){: .md-button .md-button--primary}

---
