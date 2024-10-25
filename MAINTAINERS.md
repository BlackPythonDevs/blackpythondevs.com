---
layout: default
lang: en
title: BPD Website Maintainer's Guide
---

# BPD Website Maintainer's Guide

First off, thank you for considering contributing to Black Python Devs website. It's people like you that make Black Python Devs such a great community. Navigate through the following to understand more about contributing here.

- [Before You Get Started](#before-you-get-started)
- [How to Contribute](#how-to-contribute)
- [Accessibility](#accessibility)
- [Translations](#translations)
- [Styling](#styling)
- [Adding New Pages](#adding-new-pages)

# Before You Get Started

## Code of Conduct

Black Python Devs follows the following [Code of Conduct](https://github.com/BlackPythonDevs/.github/blob/main/CODE_OF_CONDUCT.md) . The comfort and safety of Black Python Devs community members are our priority. Please do well to adhere to the Code of Conduct to participate in the Black Python Devs community.

## Issues & Pull Requests

### Creating an issue

Before **creating** an issue i.e for `features`/`bugs`/`improvements` please follow these steps:

1. Search existing issues before creating a new issue (look to see if the issue has already been created).
1. If it doesn't exist create a new issue giving as much context as possible (please take note and select the correct issue type, for example `bug`, `documentation` or `feature`.
1. If you wish to work on the issue add this to the issue description.

### Working on an issue

Before working on an existing issue please follow these steps:

1. Comment asking for the issue to be assigned to you.
1. To best position yourself for issues assignment, we recommend that you:
   1. Confirm that you have read the CONTRIBUTING.md.
   1. Have a functional development environment (have built and are able to run the project).
   1. Convey your intended approach to solving the issue.
   1. Put each of these items in writing in one or more comments.
1. After the issue is assigned to you, you can start working on it.
1. In general, **only** start working on this issue (and open a Pull Request) when it has been assigned to you. Doing so will prevent confusion, duplicate work (some of which may go unaccepted given its duplicity), incidental stepping on toes, and the headache involved for maintainers and contributors alike as issue assignments collide and heads bump together.
1. Reference the issue in your Pull Request (for example `This PR fixes #123`), so that the corresponding issue is automatically closed upon merge of your Pull Request.

> Notes:
>
> - Check the `Assignees` box at the top of the page to see if the issue has been assigned to someone else before requesting this be assigned to you. If the issue has a current Assignee, but appears to be inactive, politely inquire with the current Assignee as to whether they are still working on a solution and/or if you might collaborate with them.
> - Only request to be assigned an issue if you know how to work on it.
> - If an issue is unclear, ask questions to get more clarity before asking to have the issue assigned to you; avoid asking "what do I do next? how do I fix this?" (see the item above this line)
> - An issue can be assigned to multiple people, if you all agree to collaborate on the issue (the Pull Request can contain commits from different collaborators)
> - Any issues that has no activity after 2 weeks will be unassigned and re-assigned to someone else.

## Reviewing Pull Requests

We welcome everyone to review Pull Requests. It is a great way to learn, network, and support each other.

### DOs

- Use inline comments to explain your suggestions
- Use inline suggestions to propose changes
- Exercise patience and empathy while offering critiques of the works of others.

### DON'Ts

- Do not repeat feedback, this creates more noise than value (check the existing conversation), use GitHub reactions if you agree/disagree with a comment
- Do not blindly approve Pull Requests to improve your GitHub contributors graph

## Discord Community

Join the [Discord](https://discord.gg/XUc3tFqCT3) to discuss suggested new features, possible bugs, enhancement in user experience, and any other aspects of the site. The comment section of each issue is our preferred method of communication as it retains conversations history for future contributors wanting to gain insights/updates on the topic in question, you can, however, inquire in the #community-discussion channel in the Black Python Devs Discord workspace.

# Accessibility

Accessibility (A11y) using the **FastPass** tests for A11y and the [Accessibility Insights for Web
][1] browser extension.

## 1: Reproduce the Tests

First, reproduce the **FastPass** tests for A11y using the [Accessibility Insights for Web
][1] browser extension. This extension is designed to help you identify and fix accessibility issues on your website.

![image](https://github.com/BlackPythonDevs/blackpythondevs.github.io/assets/44526468/222e6653-c963-4518-a297-262d656216a7)

## 2: Capture the issues

If the Accessibility Insights for Web extension identifies any issues, capture a screenshot of the issues on the [BPDevs](https://BlackPythonDevs.github.io/) website. You can do this by pressing <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>S</kbd> on your keyboard.

## 3: Make the Necessary Changes

Next, make the necessary changes to fix the identified issues. This might involve modifying the CSS of the website.

## 4: Test the Changes

After making the changes, run the **FastPass** test again and capture a screenshot showing no accessibility issues. This will serve as proof that the issues have been successfully resolved.

![image](https://github.com/BlackPythonDevs/blackpythondevs.github.io/assets/44526468/9a284f43-3cde-4370-9eab-1d302ed65e9e)

## 5: Check and Pass Other Tests

Finally, check and pass other tests, such as the rules with `pre-commit`. This ensures that your changes are in line with the existing codebase and do not introduce any new issues.

# Translations

We welcome translations for the Black Python Devs website in all languages! Here's how you can contribute:

The language code being used should be in the format [<ISO 639-1>](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes)

1. [**Fork the repository**](#2-fork-the-code): Make a copy of this project on your account.

2. **Create a new branch**: Make a new branch for your translation work to keep it separate from the main project: e.g. `es` .

3. **Translate**: Translate all the content in your preferred language. Please ensure that the translation is accurate and professional.

   - Copy `_data/locales/en.yml` to your target language file e.g. `_data/locales/es.yml` and translate all the strings.

   - Create a new directory in `_articles/` for your language e.g. `_articles/es/`, copy each guide from `_articles/` into that folder and translate the content in each guide.

   - Copy `index.html` to your target language index file e.g. [`_articles/es/index.html`](https://github.com/BlackPythonDevs/blackpythondevs.github.io/blob/HEAD/_articles/es/index.html) and update the `lang:` and add the `permalink:` fields. Example: `lang: es` and `permalink: /es/`.

4. **Submit a Pull Request**: You may send a pull request before all steps above are complete: e.g., you may want to ask for help with translations, or getting tests to pass. However, your pull request will not be merged until all steps above are complete.

Our maintainers will review your pull request and merge it if everything is in order. We appreciate your contribution to making Black Python Devs accessible to more people around the world!

[1]: https://microsoftedge.microsoft.com/addons/detail/accessibility-insights-fo/ghbhpcookfemncgoinjblecnilppimih

# Styling

Black Python Devs website uses [Pico CSS](https://picocss.com/) for styling. To maintain optimal performance:

1. **Optimize Color Profiles**:

   - Regularly review `pico.colors.min.css`
   - Remove unused color profiles to reduce file size
   - The color profiles file should be similar in size to `pico.min.css`

2. **Testing After Changes**:

   - Thoroughly test the website after removing unused colors
   - Ensure all necessary styles are still applied correctly

3. **Performance Monitoring**:

   - Monitor website load time after CSS optimizations
   - Report significant changes in performance to the team

4. **Framework Updates**:
   - When updating Pico CSS, re-evaluate and optimize color profiles

# Adding New Pages

When adding a new page to the website, follow these steps:

1. **Create Content**:

- Add a new Markdown file in the appropriate `_articles/` subdirectory.
- Include necessary front matter (layout, title, etc.) at the top of the file.

2. **Add Data (if needed)**:
   If your page requires new data, add a file in the `_data/` directory. Choose the appropriate format:

---

- **JSON (Preferred)**: Use for most structured data, especially when the data structure is complex or nested. JSON is the default choice for new data files.

- **YAML**: Can be used for configuration files or when the data structure is simple and human readability is a priority. YAML is particularly useful for data that doesn't require complex nesting.

- **CSV**: Use for large, tabular datasets, particularly when the data comes from or might need to be edited in spreadsheet software. Examples include:
  - Annual sponsorship numbers
  - Event attendance records
  - Membership statistics over time
  - Any data that is likely to be maintained or updated in a spreadsheet

---

When in doubt, prefer **JSON** for new data types unless there's a compelling reason to use **YAML** or **CSV**.

3. **Update Routes**:

- Open `tests/conftest.py`.
- Add your new page's route to the `ROUTES` list:

```python
ROUTES = [
    "",
    "blog",
    "about",
    "events",
    "community",
    "leadership",
    "book-club",
    "your-new-page",  # Add your new route here
]
```

4. **Create Navigation Links**:

- Update relevant navigation menus to include your new page.

5. **Test**:

- Make sure your new page renders correctly and all links work as expected.

---

Remember, when in doubt, don't hesitate to ask for help in our Discord community or in a GitHub issue!
