## I. Professional Self-Assessment/Introduction
### A. My Experiences

Hello and welcome to my ePortfolio! This page will serve as an introduction to various programming projects of mine, and will build over time to prove proficiency in the fundamentals of computer science. During my time at Southern New Hampshire University, I have worked in the following languages/technologies/databases: Python, Java, C++, Maven, OpenGL, MongoDB/RESTful API, MySQL and JMP for data mining. I also have an understanding of agile methodology, UML, and strong fundamentals in information technology and network security. Through the use of agile practices in combination with working on projects with Git, I have had experience working on a team and communicating with stakeholders. 

### B. My Capstone Project

As of summer 2020, the main focus of this ePortfolio will be my capstone project for the Computer Science program at Southern New Hampshire University. This project shows my proficiency in software engineering, algorithms and problem solving, database accessibility, and security. The entire project can be found and pulled from the latest commit at: 
  
https://github.com/hesscm/hesscm.github.io/tree/ZooProgram1.0

This capstone takes a project from one of my very first programming classes and improves it dramatically. The original program was written in Java and the final product is in Python with connectivity to a MongoDB database. 


## II. Code Review

This video shows the final project from my Java-based course IT-145: Foundations in Application Development. I introduce the project, talk about how the user interacts with the program, how the code works, and my plans for improving the weaknesses and vulnerabilities found in the code review.

Link to [code review] (https://www.youtube.com/watch?v=3tqgLBmKNVw)


## III. The Artifact and Narratives

###	A. Artifact Description and Inclusion Justification

As stated above, the artifact I am submitting was originally my final project for IT-145. This was originally a Java project. It was a basic authentication program for a zoo where users could input a user name and password to log in. The passwords were hashed using an MD5 hash. Once the users logged in, they would see a welcome screen and that was the end of the program. Users were assigned specific roles, and depending on their role (zookeeper, vet, admin) a different welcome screen would be presented.

I chose this as my artifact because I think it will easily show how much I have improved during my time at SNHU. I mostly wrote the code for the original project, and I am writing the entirety of the code for this new project. This project showcases my ability to write logical and concise code, write an algorithm to parse through a data file, write to and read from a database, and create an easy-to-use interface for the user. It also shows my ability to translate code from one programming language to another, as this project is written in Python. Next, I will summarize the improvements made in each area of programming to show that I have met the requirements to complete the Computer Science Program at SNHU.
  
### B. Communication and Collaboration

This project is completely contained in both a local and remote repository with the use of Github. Having skills with Git are crucial to any team. Version control and constant commits leave questions like “what did you change” an easy answer to find. Having great, concise, commit messages also leaves the “why did you change this” answer easy to find as well. These skills allow for easy collaboration with other team members. I also believe I have showcased my ability to communicate with potential stakeholders as shown in my code review above.
  
### C. Software Design and Engineering

The major aspect of my original project that was missing was a lack of organization. In the new zoo program, I have split the program into 6 different Python files with various methods. If I were not using a database for the animals or employees, I would have used classes as well to show my proficiency in OOP. I have included concise and easy to understand comments as well as method names that can be understood on their own. I have created a “main” file, so a person can understand the basic flow of the program by just looking at that one small file.
  
### D. Algorithms and Data Structures

Database inclusion limits the amount of data structures needed, so I decided to include a credentials file that can be parsed through to show my ability in solving algorithmic and logic puzzles. This credentials file includes the username, their SHA-256 password hash, and their role. An example of parsing a login attempt is here:

```
git status
git add
git commit
```

The method opens the file and checks for a successful username and hash match using a linear search algorithm and exits upon completion. Algorithmic thinking is not limited to the use of data structures, and evidence of problem solving can be seen in every module of this program.

### E. Databases

I have created a MongoDB zoo database with collections for both animals and employees. Basic users have limited CRUD capabilities while administrators have access to the full system. An example of the functionality from the user interface can be seen [here] (https://imgur.com/a/soReU8e). Databases are a critical tool for any software developer and this program proves my proficiency in creating an easy-to-use user interface that connects to a MongoDB database. 

### F. Security

The last category that needs to be addressed is security. To be honest, it is very easy to overlook security when writing a program. A developer needs to change their mindset from “how do I make this work” to “how do I make this work safely and efficiently”. Security is more than protecting the program from outside hackers. You must also protect the program from user attacks and from the program itself. I have used multiple iterations of try/except clauses to make sure the program does not crash in event of an incorrect input. An example of that, from ‘main.py’ is here:

```
git status
git add
git commit
```

I have also ensured users can only access their authorized data and cannot add, edit, or delete data that does not belong to them. The three pillars of security are confidentiality, integrity, and availability and I believe I have shown that I have thought of each pillar while developing this program. 


## IV. Reflection

My journey into computer science began two and a half years ago. I have over 20 years of experience as a musician and that has been my chosen career up until this point. I have decided it is best for myself and my family to make a change, and technology has always been my second love. At the beginning of my education, I felt lost and struggled to keep up with the course work. I think this is evident in my code review. However, since that point, I have become more confident as my skills have grown. 
	
As a professional musician, I would never say I have “mastered” anything. You develop your skills one day at a time and try your best to conquer the challenges that lie in front of you. It was not until this point in my journey that I realized how much I have learned since that moment two and a half years ago. I can confidently say now that I have a strong understanding of computer science fundamentals. I have the common sense and humility to know that, in this vast sea of technology, I know next to nothing. However, I have also learned enough that I feel capable of creating anything that I want. I have just enough know-how that I am able to find the resources I need and use them effectively. I know it is still a long journey ahead filled with lifelong learning, but I am certain that I would be an asset to any team.



You can use the [editor on GitHub](https://github.com/hesscm/hesscm.github.io/edit/master/index.md) to maintain and preview the content for your website in Markdown files.

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

### Markdown

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/hesscm/hesscm.github.io/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://help.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out.
