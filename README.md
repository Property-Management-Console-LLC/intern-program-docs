
# Property Management Console Documentation

Welcome to the **Property Management Console LLC** intern-program documentation. This repository contains essential resources and guidelines for learning and contributing during your internship, focusing on development processes, infrastructure setup, and useful learning resources. Below are the key areas covered:

## Key Areas of Documentation

### 1. **Development Processes**
   - This section outlines the steps and practices followed during development. It includes coding standards, version control processes, and collaboration methods used within the project.

### 2. **Getting Started**
   - A comprehensive guide for new contributors and team members. This section includes resources to help you get up and running with the project:
     - **accessing_resources.rst** - Guide to accessing various resources needed for the project.
     - **intern_information_form.rst** - A form used to gather information from new interns for onboarding purposes.
     - **onboarding_checklist.rst** - A checklist to ensure all steps are completed during the onboarding process.
     - **workstation_setup.rst** - Instructions on setting up your workstation and configuring necessary tools for development.

### 3. **Infrastructure**
   - Detailed information on the infrastructure of the Property Management Console, including server setup, deployment configurations, and system architecture. This section helps you understand the technical backend of the project.

### 4. **Learning Resources**
   - A collection of resources and references to help you expand your knowledge on property management systems, software development best practices, and other related topics.

### 5. **Request Forms**
   - Templates and forms for requesting various services or information related to property management. These forms are used within the system for streamlining requests.

## Contribution Guidelines

We welcome contributions to improve this project! If you're interested in contributing, please follow these guidelines:

1. **Fork the Repository**: Start by forking this repository to create your own copy.
2. **Clone the Repository**: Clone your forked repository to your local machine:
   ```bash
   git clone https://github.com/your-username/intern-program-docs.git
   ```
3. **Create a New Branch**: For each feature or fix, create a new branch with a descriptive name:
   ```bash
   git checkout -b feature-description
   ```
4. **Make Your Changes**: Edit the files as needed, and commit your changes with a clear commit message.
5. **Push to Your Branch**: Push the changes to your forked repository:
   ```bash
   git push origin feature-description
   ```
6. **Submit a Pull Request**: Go to the original repository and submit a pull request from your branch. Describe your changes clearly for review.

For any questions, feel free to open an issue or reach out to the maintainers.

## Documentation Setup

We use **Sphinx** and the **Read the Docs** theme for generating documentation. Follow these steps to set up the documentation locally.

### Prerequisites

Ensure you have Python installed, then install Sphinx and the required theme:

```bash
pip install sphinx sphinx-rtd-theme
```

### Generating the Documentation

1. **Initialize Sphinx**  
   In the root of the project, run:
   ```bash
   sphinx-quickstart docs
   ```

2. **Configuration**  
   Update `docs/conf.py` with the following settings to integrate with GitHub Pages:

   ```python
   project = 'Intern Program Documentation'
   copyright = '2024, Property Management Console'
   author = 'Property Management Console'
   release = '1.0'
   extensions = ['sphinx_rtd_theme']
   html_theme = 'sphinx_rtd_theme'
   html_static_path = ['_static']
   html_context = {
       'display_github': True,
       'github_user': 'Property-Management-Console-LLC',
       'github_repo': 'intern-program-docs',
       'github_version': 'main/docs/',
   }
   html_css_files = ['custom.css']
   master_doc = 'index'
   ```

3. **Add Documentation Files**  
   Add `.rst` files (e.g., `accessing_resources.rst`) in `docs` and include them in `index.rst`:

   ```rst
   .. toctree::
      :maxdepth: 2
      :caption: Contents:

      accessing_resources
      onboarding_checklist
   ```

4. **Build the Docs**  
   In `docs`, run:
   ```bash
   make html
   ```
   This will generate HTML files in `docs/_build/html`. Open `index.html` in a browser to view.

## Contact

For any questions or inquiries, please reach out via the issue tracker or by contacting the repository maintainers.

---
