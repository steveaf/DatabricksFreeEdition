#  CodeSpaces

Codespaces gives a VSCode environment in the cloud.   
<

My hopes
* Avoid installing locally so the codespaces environment can match the work.
* Run IAC 
* Use anywhere 
    * work
    * home
    * iPad? 
* Compare to bare metal
* Compare to Podman with VSCode
* See if I like the editor experience. 

## Steps

Log into your GitHub account. 
Find a branch to use.
Click <Code> button then, the "Codespaces"

**Create Codespace**
In your repo when you select codespace, use the "Configure and create codespace" button.
The default creates a codespace.  

You have options that are limited in the free codespace.  
Default is 4-core, 8GB RAM, 32 GB storage. 




## Configure
--- 
## Rant

 I want to avoid issues related to a local environment.  Using Windows at work, Linux at home, or wanting to switch computers in the future makes local configuration challenging.  Various needs also makes local configuration and versions challenging. 

Development:  Make a container for a scenario.
Container: Dev for Databricks and Python
* Install the best version of Python to use with your target version of Databricks. 
* Install CLI tools for GitHub, the above DABS plugin, and whatever else is needed.
* Have VS Code with Python, Databricks plugins, etc.  
* Have Mermaid plugins.  Learn to use its markdown for diagrams.

Container: Dev for SQL Server, Powershell

Container: Dev for Postgres (Including PGAdmin...)

Container: Server for Spark  (Run with Dev for Databricks, or ...)

BUT - if work doesn't also have containers, your containers are only for home. 

VS 

Install everything locally and lose everything when you get another computer, work at work, etc. 

## Resources

https://www.youtube.com/watch?v=SVaqUjBUdMA&list=PLmsFUfdnGr3wTl-NCblzcrEv2lFSX975-&index=3


