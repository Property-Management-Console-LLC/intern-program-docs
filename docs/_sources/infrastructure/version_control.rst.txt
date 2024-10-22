Version Control
===============

We use Git, hosted on GitHub, for version control. Version control is a system that allows us to track changes to our code, collaborate with team members, and maintain a history of our work. Below is a guide on how to get started.

1. **What is Git?**
   Git is a distributed version control system. It allows you to:
   - Track changes to your codebase.
   - Work on new features or bug fixes in isolation using branches.
   - Merge changes back into the main codebase through pull requests.

2. **Setting Up Git:**
   - Install Git: https://git-scm.com/downloads.
   - Configure Git with your GitHub account:

   .. code-block:: bash
     
     git config --global user.name "Your Name"
     git config --global user.email "you@example.com"
     

3. **Basic Git Workflow:**
   1. **Cloning a Repository:**  
      Clone the repository to your local machine:

      .. code-block:: bash
      
        git clone https://github.com/your-company/repo-name.git
      

   2. **Creating a Branch:**  
      Create a new branch for your feature or bug fix:
      
      .. code-block:: bash
        
        git checkout -b feature/your-feature-name
      

   3. **Committing Changes:**  
      After making changes, stage and commit them:

      .. code-block:: bash
      
        git add .
        git commit -m "Your commit message"
      

   4. **Pushing Changes:**  
      Push your changes to GitHub:

      .. code-block:: bash
        
        git push origin feature/your-feature-name
      

   5. **Pull Requests:**  
      Open a pull request on GitHub to merge your changes into the main branch. This will trigger a code review by other team members.

4. **GitHub Features We Use:**
   - **Issues**: We track bugs and feature requests using GitHub issues.
   - **Pull Requests**: We review and discuss code changes before merging them into the main branch.
   - **Actions**: We automate tasks such as running tests and deploying code using GitHub Actions.
