# Databricks Free

This is my databricks free edition environment.  I want to create demos and document the experience. 

# Local Setup
Several steps are needed on your local PC before you can accomplish anything.  This seems like an anti pattern, so I'll see if I still think so.

Sign up for Databricks free edition.  I associated my gmail to databricks years ago.  Most logins take multiple attempts where I paste the 6 letter 2FA.  I asked but am not on support, so each time I log in on my personal account getting back can take 10 minutes plus or minus.

Use your GitHub repo.  Those are free and have several well documented steps to follow.

Install some GitHub plugin specific to Databricks.  Antipattern? 

DABS CLI on your local machine.  The wall gets higher?  Maintaining these over time more complicated?  

Get your Databricks Personal Access Token.  



<div>
### Notes

I want to use Podman for both a development experience and to spin and kill my personal servers.
As I understand Podman is plug and play almost with Docker.  Docker has licensing issues that Podman does not.  

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
