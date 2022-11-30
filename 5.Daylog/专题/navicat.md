
# Backgroud
## Why navicat？



## What is navicat？
[Navicat](https://www.navicat.com/)) is a muti-connections Databases tool allowing you to connect to MySQL，Oracle，PostreSQL，SQLite, SQL Server，MariaDB and/or MongoDB databases, making database adminstration to multiple kinds of database so easy. It can also manage cloud databases such as Amazon Redshift, Amazon RDS, Alibaba Cloud.
Navicat is avaliable on three platforms-Microsoft Windows, macOS, Linux. It can connect to local/remote servers,providing serveral utility tools such as Navicat Cloud Collaboration, Data Modeling, Data Transfer, Data/Structure Synchronization, Import/Export, Backup/Restore, Charts and Automation.
### Definitions
- "Non-commercial Version" means a version of the Software, so identified, for use by i) the individual who is a natural person and not a corporation, company, partnership or association or other entity or organization ii) the individual who is a student, faculty or staff member at an educational institution, and iii) staff of a non-profit oragnization or charity organization only. For purposes of this definition, "educational institution"means a public or private school, college, university, and other post secondary educational establishment. A non-profit organization whose primary objective is to support an issue or matter of private interest or public concern for non-commercial purposes.
- "Not For Resale(NFR) Version"means a version, so identified, of the Software to be used to review and evaluate the Software, only.
- "PremiumSoft"means PREMIUMSOFT CYBERTECH LTD. and its licensors, if any.
- "Unregistered version"means only the PremiumSoft software program(s) and third party software programs, in each case, supplied by PremiumSoft herewith, and corresponding documentation, associated media, printed materials, and online or electronic documentation.
- "Unregistered Version", ”Trial version“ or "Demo version" means an unregistered copy of the SOFTWARE ("UNREGISTERED SOFTWARE") which may be used by the USER for evaluation purpose for a period of fourteen days following the initial installation of the UNREGISTERED SOFTWARE. At the end of the trial period("TRIAL PERIOD"), the USER must either register the SOFTWARE or remove it from his system. The UNREGISTERED SOFTWARE may be freely copied and distributed to other users for their evaluation.
- "Navicat Essentials"means a version of the Software, so identified, to be used for commercial purpose.
- **Secure SHell(SSH)** is a program to log in into another computer over a network, execute commands on a remote server, and move files from one machine to another. It provides strong authentication and secure encrypted communications between two hosts, known as SSH Port Forwarding (Tunneling), over an insecure network. Typically, it is enployed as an encrypted version of Telnet. In a Telnet session, all communications, including username and password, are transmitted in plain-text, allowing anyone to listen-in on your session and steal passwords and other information. Such sessions are also susceptible to session hijacking, where a malicious user takes over your session once you have authenticated. SSH serves to prevent such vulnerabilities and allows you to access a remote server's shell without compromising security. **Note**:Avaiable only for MySQL, Oracle, PostgreSQL, SQL Server, MariaDB and MongoDB.
- **Port**:by default it is 22.
### Server Objects
#### MySQL/MariaDB
**Databases**:
To start working with the server objects, you should create and open a connection. If the server is empty, you need to create a new database.
- Create a new database
	- 1. In the Navicat pane, right-click your connection and select New Database.
	- 2. Enter the database properities in the pop-up window.
- Edit an existing database
	- 1. In the Navicat pane, right-click a database and select Edit Database.
	- 2. Edit the database properities in the pop-up window.
**Note**: MySQL does not support renaming database through its interface at this moment. Access the directory in which databases being stored. By default, all databases store within a directory called data under MySQL Installation folder. For example:C:\mysql5\data. You must stop MySQL before you can rename the database.

**Tables**：
Tables are database objects that contain all data in a database. A table is a set of ows and columns, and their intersections are fields. In the main window, click Table to open the table object list.
You can create a table shorcut by right-clicking a table in the Objects tab and select **Create Open Table Shortcut** from the pop-up menu. This option is used t oprovide a convenient way for you to open your table for entering data directly without activating the Navicat main window.
To empty a table, right-click the selected table and select **Empty Table** from the pop-up menu. This option is only applied when you wish to clear all the existing records without resetting the auto-increment value. To reset the auto-increment value while emptying your table, use **Truncate Table**.

**Table Designer**
It allows you to create, edit, and drop table's fields, indexes, foreign keys, and much more.
In the **Fields** tab, you can search a field name by choosing **Edit ->Find** or pressing CTRL+ F.
Note: The tabs and options in the designer depend on the server type and version.

**Table Viewer**
When you open a table, **Table Viewer** displays data as a grid. Data can be displayed in two modes: Grids View and Form View. 
Note: Transaction is only avaliable for INNODB tables.

**Views**
You can create a view shortcut by right-clicking a view in the Objects tab and select **Create Open View Shortcut** from the pop-up menu. This option is used to provide a convenient way for you  to opon your view directly without activating the Navicat mian window.

**View Designer**
You can choose to show the preview results bellow the editor or in a new tab by choosing **View -> Result -> Show Bellow Editor or Show in New Page**.

**Procedures/Functions**
Procedure and functions(stored routines) are supported in MySQL 5.0. A stored routine is a set of SQl statements that can be stored in the server. In the main window, click **Function** to open the function object list.
**Function Wizard**
Click **New Function** from the object toolbar. **Function Wizard** will pop up and it allows you to create a procedure/function easily.
1. Select the type of the routine:**Procedure** or **Function**.
2. Define the parameters. Set the **Mod, Name** and/or **type** under the corresponding columns.
3. If you create a function, select the **Return Type** from the list and enter the corresponding information: **Length, Decimals, Character set** and/or **Enum**.
Hint: Once uncheck the **Show wizard next time** option, you can go to **Options** to enbale it.
**Function Designer**
You can enter a valid SQL statement in the **Definition** tab. This can be a simple statement such as SELECT or INSERT, or it can be a compound statement written using BEGIN and END. Compound statements can contain declarations, loops, and other control structure statements. To customize the view of editor and find out more features for SQL editing.
**Results**
To execute the procedure/function, click **Execute** on the toolbar. If the SQl statment is correct, the statement will be executed and, if the statament is supposed to return data, the **Results** tab opens with the data return ed. If an error occurs while executing the procedure/function, execution tops, the appropriate error meessage is displayed. If the procedure/function requires input parameters, the **Input Parameter** dialog will pop up. Check the **Raw Mod** option to pass the inputted values to the procedure/function without quotation marks.
Note: Navicat supports to return 20 result sets.









## How to use？
### Installation
Installation for Download Version
1. Download Navicat Windows version.
2. Open the **.exe** file.
3. Click **Next** at the Welcome Screen.
4. Read the Licnese Agreement. Accept it and click **Next**.
5. Accpet the location of the program icons by clicking **Next**. If you wish to change the destination of the folder, click **Browse**.
Installation for CD Version
1. Load the Navicat CD Installation disk into the CD-ROM drive.
2. Open the **.exe** file.
3. Click **Next** at the Welcome Screen.
4. Read the License Agreement. Accept it and click **Next**.
5. Accept the loaction of the program icons by clicking **Next**. If you wish to change the destination of the folder, click **Browse**.
6. Follow the remaining steps.

