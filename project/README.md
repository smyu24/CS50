# Sleep Monitor
## Video Demo:  https://www.youtube.com/watch?v=2MlL7K0ngUI&ab_channel=Seung-minYu
> Pardon my bad editing
## Description of Project:


**Explanation**
This was my final project that would complete my journey in CS50's Introduction to Computer Science. In this project, I used a blend of Python, Flask, Jinja2, HTML, CSS, and more. My final project is a website that takes in the sleep data that the user provides, and returns to the user with advice and helpful tips, in accordance with the data. I made this website because sleep is an important factor in maintaining a healthy lifestyle and it is a factor that is often overlooked. Sleep is something that I personally have struggled to maintain a healthy relation with, and I often slept too much or too little. As you can probably tell, this was a passion project of mine and I had a lot of fun developing and creating this website. I hope that one day, I can develop this idea to the point, where people use this to better themselves.

**Pages**
    -Register (Register User and gathers info such as username, password, email. Has additional features like hyperlinks to register, login)
    -Login (Logs user into their account. Has additional features like hyperlinks to register, login, recover account)
    -Rate (Users of the website can rate the website using a combination of comments and stars)
    -Layout (Basic landscape of the website. Every page will use its template)
    -Links (Filled with helpful links and advice)
    -Settings (Need to get the update password working. Also try to get unhashed password)
    -Index ("Main" page of the website that the user will first encounter when they login)
    -Quote/Quoted (Needs to receive user input correctly, save it into database, then give proper feedback, in both graphical and visual)
    -Compare (Needs to portray data in the form of a graph in order for the user to compare their sleep data to others if they wish to)

**Databases**
    -age (Structure: {id}, {age})
	-data (Structure: {id}, {day1}, {day2}, {day3}, {day4}, {day5}, {day6}, {day7})
	-datadump (Structure: {id}, {day1}, {day2}, {day3}, {day4}, {day5}, {day6}, {day7})
	-rate (Structure: {id}, {username}, {rating}, {comment})
	-users (Structure: {id}, {username}, {hash}, {email})

**Design Choices**
When creating a website, I had to go through several stages of development. A design choice that I debated on using a variable named pg, brought forth from my python backend code, and affect the variable to emulate pagination. I wanted to use this as a replacement for using three HTML files. Here is the code:
```
{% if pg == 0 %}{% endif %}
{% if pg == 1 %}{% endif %}
{% if pg == 2 %}{% endif %}
{% if pg > 0 %}<button type="button" name="previous">Previous Page</button> Previous -= pg {% endif %}
{% if pg < 2 %}<button type="button" name="next" >Next Page</button> Next += pg {% endif %}
```
Unfortunately, I was not able to use it this way, due to time constraints and school.



**Instruction to get and use my webpage in CS50 ide:**
- [ ] Get project file from Github and insert into CS50 ide
- [ ] In terminal type "cd project"
- [ ] In terminal type "flask run"
- [ ] Click link that pops up
- [ ] Enjoy!

Thank you for all CS50. Thank you, David J. Malan and the entire CS50 team!
For more information about the course visit [CS50](https://cs50.harvard.edu/x/2020/).