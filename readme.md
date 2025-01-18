### powershell Virtual Environments 
- `Set-ExecutionPolicy RemoteSigned -Scope Process`

#### virtualEnv
- `python -m venv myenv` this command makes that folder a a virtual env , not that it creates a folder named myenv ~
- along side this folder u will write ur python files , not inside it.
- after having a virtual environment , if do pip install anyPkg , it will be confined to that env , nnot globally 
- to use that package in other project ,u would have pip install again.

#### windows hidden files
  - Get-ChildItem -Force 


### 🔥 Pending Exploration
- explore Qt Widget designer--pending
- progress bar logic in command line

- checking if we directly go to a folder deep inside and commit form there,  
  whether any changes from out side folder files will also get added and commited.


### the gitignore situation 


- The Problem:
    -  You are trying to ignore a folder (targetFolder/) using .gitignore, but it still appears in your GitHub repository.

 - The Explanation:
      - Git continues tracking the folder if it was added to the repository before .gitignore was configured.
      - `.gitignore` only prevents new files from being tracked, not files that are already committed.
      - A nested .gitignore file or misconfiguration could also affect the ignoring behavior.

 - The Solution:

    - Untrack the Folder:
        - Run `git rm -r --cached targetFolder/` to remove the folder from Git tracking while keeping it locally.
    - Ensure Correct .gitignore Configuration:
        - Make sure .gitignore contains targetFolder/ to ignore the folder.
    - Commit and Push:
        -  Commit the changes and push them to GitHub with git commit -m "Remove targetFolder from version control" and git push origin main.  

 This will remove the folder from GitHub and prevent it from being tracked.

- PS D:\python_repo> git rm -r --cached random/      
  fatal: pathspec 'random/' did not match any files

- `git rm -r --cached path/to/random/` --> `git rm -r --cached /d/python_repo/d_pyTkinter101/random/`

          PS D:\python_repo> git status
          On branch main
          Changes to be committed:
            (use "git restore --staged <file>..." to unstage)
                  deleted:    d_pyTkinter101/random/testJ101.txt

          Changes not staged for commit:
            (use "git add <file>..." to update what will be committed)
            (use "git restore <file>..." to discard changes in working directory)
                  modified:   .gitignore
                  modified:   readme.md

    - to check go to the tkinter --> and do git status
    - in vscode all folders named random will show up in faded fonts


- next topic