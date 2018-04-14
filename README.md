# How Git Works
## History of Git
Software engineers have been faced with the issue of how best to efficiently and effectively share code since the advent of their profession. Engineers have tried sending code through email or uploading their code to a storage for everyone else to see but this became impractical as code size changes [[2]](#ref2).In Linus Torvalds’ talk at Google, he talked about how it took a company three days to merge all the code from everyone and how everyone would have to stop working for those three days. Even though this inconvenient method worked, it still came with its drawbacks. For example, once all the code was published, it was tiring to rollback to a previous version if an error was detected. Engineers would have to manually detect what point that error was introduced to the code and then change the code back to its previous state if needed. This was obviously inconvenient and led to the creation of version control [[1]](#ref1). 

Version control is a system that tracks the changes to a file, or set of files over time so it can be rollbacked to a previous version. Version control systems were created and used but eventually they all became commercial and none of them supported free software. This was a problem for the development of the Linux Operating system because it was a free software and couldn’t afford to pay for version control. 


Fed up with then current systems, the developer of the Linux Kernel, Linus Torvalds, and his team wanted an alternative system to manage their project [[2]](#ref2). Their criteria specified that saving revisions should take no more than three minutes. Furthermore, they took preceding systems such as Concurrent Version System (CVS) as examples of what not to make. Consequently, the control system they would create was designed as a distributed version control architecture. Distributed revision control refers to copying an entire project including the history of all the changed rather than just copying the current version. Their solution came to be called Git and has since grown into the most popular version control system amongst developers. Git is a version control system (VCS) for managing electronic files and collaboration that is characterized by its distributed revision control design. 

## Examples of version control systems
The version control systems Concurrent Version System (CVS), Subversion, and Mercurial were all designed to address the issues of revision management that were plaguing software engineers. The designs of of each system reveal the evolution of revision control leading to Git with each system offering various features and limitations to the users.

CVS is the oldest of the three management systems, first released in 1990. The system was modeled around a client to server architecture, meaning that file changes are made on the user’s computer then stored on a central computer server. Although the decentralized design differs significantly from Git, it is often desirable to have a single source of revision on professional projects. Nevertheless, the system has become antiquated for usage on modern projects. Regardless, CVS pioneered version control technology and inspired newer software such as Subversion. 

Released in 2000, Subversion was a compatible successor to CVS. Like its predecessor, Subversion applies the centralized client-to-server storage technique and also provides the same single source benefits. Unlike its predecessor, Subversion was released as an open source software, meaning anyone could view, utilize, or contribute to the program. This decision encourages continuous improvements to be made and gives operational transparency which is favored by many software engineers. Being a free software also helped grow the popularity of Subversion among developers. To included the same Subversion benefits, Git was designed to be free and open source like Subversion. 

Mercurial, released 2005, strayed from the centralized approaches of CVS and Subversion to address the issue of revision control. Instead of single server storage, Mercurial deploys the idea of distributed version control. This alternative design does not rely on a central server to store all the old copies of a file. Rather, the system creates copies of the files locally to store the full history of the project. The decentralized version control systems currently possess the majority usage amongst professional developers because of the ability to make changes and maintain revision control running while not connected to the centralized server. Git and Mercurial operate under the same design concepts.
 

## Git compared to some popular version control systems
Centralized version control systems addressed the majority of early issues that software engineers experienced while sharing or saving code. A central server housed the storage of the version history for each file. Users would maintain the latest version of the file on their computer and could change their local copy to any older version by downloading the information from the central server. 

One downfall of this approach is that in the event of a breakdown of the central server, the entire history of the files would be lost. The only copies remaining would be the current version saved on each user’s computer. Therefore, the restoration of the full file history would be impossible. 

This issue encouraged the development of decentralized systems to offer a solution. With decentralized VCSs, such as Git, each user stores the entire history of the file locally. Consequently, each user’s computer operates similar to the central server in systems such as CVS or Subversion. As a result, the entire project can be restored by any one of the users.

## The snapshot concept
A repository is a folder that is being tracked by Git. Each step in the version history of a repository is called a commit. Most version control systems, such as Subversion, store a file and then the changes between each commit of that file. On the other hand, Git stores an entire snapshot of the repository in each commit. If a file hasn’t changed, Git uses a link to a previous version of that file rather than making an identical copy, to be more efficient. The data can be seen as a stream of snapshots with each snapshot being referenced by a commit. This way, Git can create branches from a snapshot and maintain several versions. The figure below shows an example of four different commits or versions inside a repository. The dashed line boxes indicate a file that has not changed between versions. The black arrows between identical files depicts how Git avoids making duplicate files when no changes are made by referencing back to the original file in the first commit that it appears.

![Snapshot concept](/snapshot.png)

## A Real world example of Git versioning stages
Files in a repository have to be selected before they are committed. This way, you can choose what files you want in the commit. Git manages this by having three levels: the working directory, the staging area and the local repository. A file can at one of these levels depending on what the current state of the file is. A file can either be in the untracked, committed, modified, or staged state.

### Working Directory
By default, a new file is in the working directory and not yet part of the git repository. The files in this level are in the untracked state and not yet tracked by Git.

### Staging Area
Whenever a file is added to a git repository, it is moved from the working directory to the staging area and is in the staged state. Multiple files can be added to the staging area. 

### Git Repository
The staging area can then be committed, which moves all the files from the staging area to the Git repository. All the previously staged files which were committed are now in the committed state. A new snapshot is created at this point.
Whenever a file that has already been staged is modified, it becomes in the modified state. This file can then be added to staging area and committed again. After the commit, a new snapshot is created, and the file is captured in the new snapshot. 

### Remote Repository
Think of a remote repository as a backup of your git repository that is stored online. When you want to share your repository with others, you upload it to a remote storage. A popular example of this is Github or BitBucket. After you upload your repository, it can be downloaded and viewed by other people. This is generally how people collaborate on a repository - they all have their individual local copies but share a remote version that they can upload to. In the event that you lose your local copy of your repository, you can always download it from the remote storage. We will not discuss this because it is out of scope on how git works.

![Git Workflow](/workflow.png)

## Using Git commands to see the Git workflow
We will go over some git commands and how they show the git workflow. These examples are done in a git terminal. Getting a git terminal is out of scope of this description as we focus on how it works, however, you can download the program and find installation instructions on Git’s website at www.git-scm.com/downloads.


### Git init
This is used to create a new Git repository. We will create a new folder and in the terminal, we will run “git init” to make it a Git repository.

```
git init
```

Now that we have a repository, we can add file(s) to our repository. We can create a new python file called `main.py` in our directory. Our program will be a change calculator that prompts the user for the price of the item and the amount given and will return the amount of $1 bills, dimes, nickels and pennies. This is what it should look like:


**<span>main.py</span>**
```python
# get the price from the user
price = float(raw_input('Please enter the transaction price.\n'))

# get the amount given from the user
given = float(raw_input('Please enter the amount the customer gave.\n'))

change = (given - price) * 100  # Multiply by 100 to prevent imprecisions

ones = int(change / 100)
change %= 100
dimes = int(change / 10)
change %= 10
nickels = int(change / 5)
change %= 5
pennies = int(change)

print '\nChange:'
print str(ones) + ' $1 bills'
print str(dimes) + ' dimes'
print str(nickels) + ' nickels'
print str(pennies) + ' pennies'

raw_input('\nPress Enter to close...')

```
Another file people tend to add in their Git repository is a `README` file. This is a file that describes what the repository is about. Let us create a new file and name it README. We can edit the file to this:

**README**:
```markdown
# Change Calculator

This is a repository for a change calculator program in python 
```

### Git status
A helpful command in Git is the `git status` command. It is used to check the state of the files in the repository. If you run git status, you will see that `main.py` and `README` are under the “untracked files” section in red.

```
git status
```

![git status](/git_status.png)

### Git Add

At this point, we want to actually add our file to the repository. We do this by first adding it to the staging area by using the `git add` command. Let’s add our `README` file first by running:

```
git add README
```

![git add](/git_add.png)

We can now check the status of our files using the  `git status` command.

![check git status](/check_status.png)

Now we can see our README in green which means it is in the staging area and ready to be committed. We can also see that `main.py` has remained in the untracked state.

### Git Commit
Since our README file is in the staging area, it is ready to be committed. We can run the `git commit` command to create a commit. We give our commit a name so we can look back at what we did in that commit without manually looking through the changes. 

```
git commit -m <name of commit>
```

![git commit](/git_commit.png)

We have just created out first commit (also known as the root commit). We can now check that the status of our files using `git status`.

![check git status](/check_status2.png)

Uh-oh! Our README file is gone! That’s actually a good thing. This means our README file has been committed and is no longer in the staging area.

We have just gone through a complete workflow of a git repository. Let’s add our `main.py` file to our repository and check the status of our repository.

![git add commit](/git_add_commit.png)

#### Modifying Files
We can see that our working tree is clean which means there are no uncommitted changes. Now let’s update our code to use quarters when calculating change. We do this by editing our `main.py` to this:

**<span>main.py</span>**
```python
# get the price from the user
price = float(raw_input('Please enter the transaction price.\n'))

# get the amount given from the user
given = float(raw_input('Please enter the amount the customer gave.\n'))

change = (given - price) * 100  # Multiply by 100 to prevent imprecisions

ones = int(change / 100)
change %= 100
# Use quarters as available change
quarters = int(change / 25)
change %= 25
dimes = int(change / 10)
change %= 10
nickels = int(change / 5)
change %= 5
pennies = int(change)

print '\nChange:'
print str(ones) + ' $1 bills'
print str(quarters) + ' quarters'
print str(dimes) + ' dimes'
print str(nickels) + ' nickels'
print str(pennies) + ' pennies'

raw_input('\nPress Enter to close...')

```

Let’s check our repository’s status by running git status. 
![status modified file](/modified.png)

Our `main.py` files is now in the modified state and is ready to be added and then committed. We can do that with the `git add` and `git commit` commands respectively.

![final commit](/final.png)

It’s always a good idea to run `git status` after every command so we can see the effects of the command we ran. As you can see, our file has been committed and our working tree is clean.

### Git Log

Another useful command is the `git log` command. It is used to check the history of our commits. This can show us every snapshot and the some information about the snapshot. We can see the hash of the commit, which is a unique string used to identify the commit; the author of the commit; the date of the commit; and the commit message.

```
git log
```

![git log](/git_log.png)

## Conclusion
There are many other git commands that you might find useful but these are the basic ones to help you understand how git works by showing you a complete git workflow. Git is an essential tool for software development and understanding how it works enables the users to work effectively in a team. It is used professionally for managing source control and even academically for smaller projects. 

## Authors
- Ashley Mace
- Ian Gottshall
- Tom Bjorlin
- Victor Amupitan

## References

- <span id="ref1">[1]</span> Git, "Getting Started - About Version Control," 2014. [Online]. Available:
     https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control. [Accessed 2018].
- <span id="ref2">[2]</span>
Google, Director, Tech Talk: Linus Torvalds on Git. [Film]. Youtube, 2007. [Accessed 2018].
- <span id="ref3">[3]</span>
L. Foundation, "10 Years of Git: An Interview with Git Creator Linus Torvalds," 22 August 2017. [Online]. Available: www.linuxfoundation.org/blog/10-years-of-git-an-interview-with-git-creator-linus-torvalds. [Accessed 2018].
- <span id="ref4">[4]</span>
Microsoft, "History in Git," 14 March 2018. [Online]. Available: docs.microsoft.com/en-us/vsts/git/concepts/history?view. [Accessed 2018].
- <span id="ref5">[5]</span>
Stack Overflow, "Stack Overflow Developer Survey 2018," 2018. [Online]. Available: https://insights.stackoverflow.com/survey/2018. [Accessed 2018].







