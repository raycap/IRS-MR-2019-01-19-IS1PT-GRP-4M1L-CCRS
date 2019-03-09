### Worksop Project Submission Template: Github Repository & Zip File

**[Naming Convention]** CourseCode-StartDate-BatchCode-Group_or_Individual-TeamName_or_PersonName-ProjectName.zip
=======

* **[MTech Group Project Naming Example]** IRS-MR-2019-01-19-IS1PT-GRP-AwsomeSG-HDB_BTO_Recommender.zip

---

### <<<<<<<<<<<<<<<<<<<< Start of Template >>>>>>>>>>>>>>>>>>>>

---

## SECTION 1 : PROJECT TITLE
## 4M1L - Credit Card Recommendation System

<img src="SystemCode/clips/static/hdb-bto.png"
     style="float: left; margin-right: 0px;" />

---
## SECTION 2 : EXECUTIVE SUMMARY / PAPER ABSTRACT
A vibrant city located in the heart of Asia, Singapore offers global investors unparalleled access to global markets. Strategically located to serve Asia Pacific, one of the world’s fastest-growing regions, Singapore’s well-established business infrastructure, global connectivity and trade linkages enable investors to access the approximately 4 billion strong Asian market within a radius of 7 hours’ flight time. (MAS, 2017)

In Singapore, one of the first things people do after getting their first job is to apply for a credit card. It makes perfect sense that paying with a credit card allows them to enjoy many benefits that using cash wouldn’t provide. With the advancement of technology, the people nowadays could even embed the credit card with their phone with the various mobile payment introduced such as Apple Pay, Samsung Pay, Google Pay and etc.
In the past, carrying credit cards were considered one of the elusive “5Cs” (Cash, Car, Credit card, Condominium and Country club membership) that people in Singapore worked hard to attain. Today, owning a credit card is not only the norm, but the financially-savvy option. 
  
However, picking a credit card can be a very frustrating process and most of the people have went through a hard time in finding the best credit card. By trying to optimize the reward from credit card, they might have fallen into the pitfall of applying excessive credit card, resulting in burdened themselves with unnecessary late payment charge or principal annual fee. Overall, no single credit card is better than all others in all categories, but by asking the right questions, each person can find the card that best fit his spending habit and credit situation. 

Our team, comprising of 5 members from different nationalities, looking forward to achieve financial freedom in one day. As the first step toward the financial freedom, we have came out with a credit card recommendation system, with the aim to help all the first time credit card applicants  in optimizing the credit card selection and better their financial management.


---
## SECTION 3 : CREDITS / PROJECT CONTRIBUTION

| Official Full Name  | Student ID (MTech Applicable)  | Work Items (Who Did What) | Email (Optional) |
| :------------ |:---------------:| :-----| :-----|
| Desmond Chua | A1234567A | xxxxxxxxxx yyyyyyyyyy zzzzzzzzzz| A1234567A@nus.edu.sg |
| Chang Ye Han | A1234567B | xxxxxxxxxx yyyyyyyyyy zzzzzzzzzz| A1234567B@gmail.com |
| Chee Jia Wei | A1234567C | xxxxxxxxxx yyyyyyyyyy zzzzzzzzzz| A1234567C@outlook.com |
| Ganesh Kumar | A1234567D | xxxxxxxxxx yyyyyyyyyy zzzzzzzzzz| A1234567D@yahoo.com |
| Jeanette Lim | A1234567E | xxxxxxxxxx yyyyyyyyyy zzzzzzzzzz| A1234567E@qq.com |

---
## SECTION 4 : VIDEO OF SYSTEM MODELLING & USE CASE DEMO

TODO:
[![Sudoku AI Solver](http://img.youtube.com/vi/-AiYLUjP6o8/0.jpg)](https://youtu.be/-AiYLUjP6o8 "Sudoku AI Solver")

---
## SECTION 5 : USER GUIDE

Requirements
* nodejs and npm should be installed. Otherwise please download and install from the following website: https://www.npmjs.com/get-npm

``` bash
# install all front end dependencies
cd web/
npm install

# install all backend dependencies
pip install requests, flask, flask_cors, durable_rules

# locate the path of redis config and change set it in start_redis.bat
start_redis.bat :
redis-server "C:\Program Files\Redis\redis.windows.conf" <- change this

# run start.bat to start all application
start.bat

# access localhost:8000/home

```

`<Github File Link>` : <https://github.com/telescopeuser/Workshop-Project-Submission-Template/blob/master/UserGuide/User%20Guide%20HDB-BTO.pdf>


### [ 1 ] To run the system using iss-vm

> download pre-built virtual machine from http://bit.ly/iss-vm

> start iss-vm

> open terminal in iss-vm

> $ git clone https://github.com/telescopeuser/Workshop-Project-Submission-Template.git

> $ source activate iss-env-py2

> (iss-env-py2) $ cd Workshop-Project-Submission-Template/SystemCode/clips

> (iss-env-py2) $ python app.py

> **Go to URL using web browser** http://0.0.0.0:5000 or http://127.0.0.1:5000

### [ 2 ] To run the system in other/local machine:
### Install additional necessary libraries. This application works in python 2 only.

> $ sudo apt-get install python-clips clips build-essential libssl-dev libffi-dev python-dev python-pip

> $ pip install pyclips flask flask-socketio eventlet simplejson pandas

---
## SECTION 6 : PROJECT REPORT / PAPER

`<Github File Link>` : <https://github.com/telescopeuser/Workshop-Project-Submission-Template/blob/master/ProjectReport/Project%20Report%20HDB-BTO.pdf>

**Recommended Sections for Project Report / Paper:**
- Executive Summary / Paper Abstract
- Sponsor Company Introduction (if applicable)
- Business Problem Background
- Project Objectives & Success Measurements
- Project Solution (To detail domain modelling & system design.)
- Project Implementation (To detail system development & testing approach.)
- Project Performance & Validation (To prove project objectives are met.)
- Project Conclusions: Findings & Recommendation
- List of Abbreviations (if applicable)
- References (if applicable)

---
## SECTION 7 : MISCELLANEOUS

### HDB_BTO_SURVEY.xlsx
* Results of survey
* Insights derived, which were subsequently used in our system

---

### <<<<<<<<<<<<<<<<<<<< End of Template >>>>>>>>>>>>>>>>>>>>

---

**This [Machine Reasoning (MR)](https://www.iss.nus.edu.sg/executive-education/course/detail/machine-reasoning "Machine Reasoning") course is part of the Analytics and Intelligent Systems and Graduate Certificate in [Intelligent Reasoning Systems (IRS)](https://www.iss.nus.edu.sg/stackable-certificate-programmes/intelligent-systems "Intelligent Reasoning Systems") series offered by [NUS-ISS](https://www.iss.nus.edu.sg "Institute of Systems Science, National University of Singapore").**

**Lecturer: [GU Zhan (Sam)](https://www.iss.nus.edu.sg/about-us/staff/detail/201/GU%20Zhan "GU Zhan (Sam)")**

[![alt text](https://www.iss.nus.edu.sg/images/default-source/About-Us/7.6.1-teaching-staff/sam-website.tmb-.png "Let's check Sam' profile page")](https://www.iss.nus.edu.sg/about-us/staff/detail/201/GU%20Zhan)

**zhan.gu@nus.edu.sg**
