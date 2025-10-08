LangChain Fundamentals Covered in this project include: Prompt Templates, Chat Models, and Chains

SOME DETAILS ABOUT THIS PROJECT:  
Steps For Creating this Project:

Create a folder named Langchain-Text-Summarization in C drive.
Open it in VS Code. 
On the terminal type git status to check whether you have done cloning to GitHub already. Else no problem, later you can do.
Next do:
pip install uv
uv --help

uv init
- This creates and sets up the fundamental files for a new Python project.

uv add langchain
- You can notice that it also creates a .venv folder, which is a virtual environment. Now, when you run the code main.py, you can see that it is running in the virtual environment if seeing this (...) braces in the beginning of line in the terminal.

If Langchain package was already present (you can check this in Python by typing pip list), then you’ll have to create virtual environment by the below code:
python -m venv .venv
- So, python -m venv .venv command creates a .venv folder in your project.It is like creating a new virtual environment.

Activate the environment by typing:
& .venv/Scripts/Activate.ps1

This (venv) shows that we already created it!!
Then you can see (venv) PS C:\Langchain_TextSummarization> line in terminal.

Inside .env file, write google_api_key="API_KEY"
If you don't have the .env file in the file hierarchy, just create it: You can create .env file in VS CODE by File->New File-> .env-> Enter Key 

Now, note that you are inside the virtual environment. Install all the packages required for the project inside this virtual environment.
So, type:
uv add langchain-openai
-> If you are using OPENAI_API_KEY
uv add langchain-google-gemini
-> If you are using GOOGLE_API_KEY for gemini

NOTE that, you should use exactly the same variable names to store the API Keys (in the .env file) as they are defined by the respective providers. Else you may get errors like Your default credentials were not found in few programs.  

Inside .env file, write your API key:
GOOGLE_API_KEY="your_api_key_here"
You can see these dependencies which you installed in pyproject.toml file. YOU CAN HAVE MULTIPLE API keys in the same .env file on problem.

Next, type:
uv add python-dotenv
-> This helps us to load the environment variables from .env file, which is going to be very easy to load all the API keys which we are going to be using in this course.

uv add black isort
-> Black automatically formats Python code according to PEP8 style.
isort sorts import statements alphabetically and groups them properly.
Together, they keep your code clean and standardized.

Now write your code in main.py file and run it to get the output.

If you want to put this into GitHub, then:

Step 1:
Create a .gitignore file because there are a few things you don’t want to commit to the repository, such as venv, pycache, etc.

Step 2:
Add the following lines in .gitignore:

# Python-generated files
__pycache__/
*.py[cod]
build/
dist/
wheels/
*.egg-info

# Virtual environment
.venv

# Environment / Secret files
.env


Note that you are still inside the virtual environment of your project.
Go to the project folder path using the cd command (or deactivate command of venv):
C:\LangchainTextSummarization>

Go to your GitHub account in browser → create a new empty repository.
And Then type the following commands in VS Code terminal:

git init
git add .
git commit -m "Initial commit with Langchain project"
git branch -M main
git remote add origin https://github.com/<your-username>/LangchainTextSummarization.git
git push -u origin main

Once done, all your local project files will be uploaded to that GitHub repository.
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Summary of Tools Used:
---------------------------
uv → Manages Python project and dependencies

black → Code formatter

isort → Import sorter

.venv → Virtual environment

.env → API key or environment variable storage

Git + GitHub → Version control and repository hosting

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

🧩 1. pip install uv

Purpose: Installs the uv tool, which is a modern package and project manager for Python (faster than pip).

Use: You run this once to make sure uv is available in your environment.

🧩 2. uv --help

Purpose: Displays all available commands and options for uv.

Use: Just to verify uv installed correctly and see its usage instructions.

🧩 3. uv init

Purpose: Initializes a new Python project in your current folder.

Effect:

Creates important files like pyproject.toml, which tracks dependencies.

Sets up a virtual environment .venv.

Prepares the project structure for Python development.

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
🧩 Git Command Explanations
1. git init

Meaning: Initializes a new Git repository in your current project folder.

What happens:

It creates a hidden folder named .git/ inside your project.

This folder stores version history and configuration details.

When to use:
Run this once at the start of a new project to begin tracking your files with Git.

2. git add .

Meaning: Adds (or stages) all the files in your current folder for the next commit.

The . means “add everything in this directory.”

What happens:

Git now knows which files you want to include in your next commit.

When to use:
Run this after you create or modify files and before committing.

3. git commit -m "Initial commit with Langchain project"

Meaning: Saves your staged changes (from git add .) into Git’s local history.

The -m flag lets you write a commit message.

What happens:

Git records a snapshot of all staged files.

The message helps you remember what this commit was about.

When to use:
Every time you make meaningful changes to your project.

4. git branch -M main

Meaning: Renames your current branch to main (the new standard name replacing “master”).

The -M flag forces the rename even if the branch already exists.

What happens:

Your local working branch becomes main.

When to use:
Always before pushing to GitHub, since GitHub uses main as the default branch name.

5. git remote add origin https://github.com/<your-username>/LangchainTextSummarization.git

Meaning: Connects your local Git repository to a remote repository on GitHub.

Parts:

origin is a short name Git uses for the remote repository.

The URL is your GitHub repo’s address.

What happens:

Your local project now knows which GitHub repo to sync with.

When to use:
Only once per project (right after creating the GitHub repo).

6. git push -u origin main

Meaning: Uploads your local commits (the project files and history) to GitHub.

Parts:

origin = the remote repository name.

main = the branch you are pushing.

-u = sets “upstream” so that future pushes/pulls can use just git push or git pull without repeating branch names.

What happens:

Your project files appear in your GitHub repository.

When to use:
After your first commit, or whenever you want to update the remote repo with new changes.

✅ Summary Table

Command	Purpose	When to Use
git init	Start a new Git repository	Once at project creation
git add .	Stage files for commit	After creating or modifying files
git commit -m "message"	Save staged changes to Git history	After git add .
git branch -M main	Rename current branch to main	Before first GitHub push
git remote add origin <URL>	Link local repo to GitHub	Once per project
git push -u origin main	Upload local code to GitHub	After committing changes



