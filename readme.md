### powershell Virtual Environments 
- `Set-ExecutionPolicy RemoteSigned -Scope Process`

#### virtualEnv
- `python -m venv myenv` this command makes that folder a a virtual env , not that it creates a folder named myenv ~
- along side this folder u will write ur python files , not inside it.
- after having a virtual environment , if do pip install anyPkg , it will be confined to that env , nnot globally 
- to use that package in other project ,u would have pip install again.

#### windows hidden files
  - Get-ChildItem -Force 

- explore Qt Widget designer