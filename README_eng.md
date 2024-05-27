# Christmas Pop-Up Shop -dataproject - [Suomeksi](README.md)

## Table of Contents

1. [Team Members](#team-members)
2. [Project Overview](#project-overview)
   - [Summary](#summary)
   - [Methods and Technologies](#methods-and-technologies)
   - [Planning](#planning)
   - [Sprint 1](#sprint-1)
   - [Sprint 2](#sprint-2)
3. [How to Use](#how-to-use)

---

## Team Members

- **Kari-Matti Sillanpää**
  - Cloud database design and implementation 
  - [Linkedin](https://linkedin.com/in/kari-matti-sillanpaa) / [GitHub](https://github.com/sillaka1)
- **Maarit Ahlgren**
  - Local database design and implementation, PowerBI data-analysis
  - [Linkedin](https://linkedin.com/in/maarit-a-7a20b8197) / [GitHub](https://github.com/ahlanmaa)
- **Ville Naumanen**
  - Local database design and implementation, PowerBI data-analysis
  - [Linkedin](https://linkedin.com/in/villenaumanen) / [GitHub](https://github.com/NaumVi)
- **Sami Lappalainen**
  - Scrum Master/Project Manager, Streamlit and Webpage
  - [Linkedin](https://linkedin.com/in/sami-lappalainen) / [GitHub](https://github.com/stlgithub)

## Project Overview

### Summary

A practice project, done as part of BearIT's ICT-Camp, aimed to help learn and practice data related skills. The main goal of the project was to implement multiple databases and create various data analyses, while also getting acquainted with agile development methods.

The project lasted four weeks, divided into two sprints. During these weeks, participants also studied broader IT-related topics through courses offered by BearIT and lectures given by industry professionals.

### Methods and Technologies

The project utilized the Scrum methodology for project management. Version control was handled via GitHub, and GitHub Projects was used as a Kanban/sprint board. For team collaboration, tools such as Google Meet and Google Docs were used.

A local server was built using MySQL, and data analyses were conducted with Power BI. A cloud server was set up using AWS, and a web-based data app with dashboards and CRUD functionality was implemented using Python's Streamlit library. Project documentation was compiled into a website created with HTML and CSS.

### Planning

Before the first sprint, a project plan was created, along with user stories and a sprint board. The projects aim was to create a local database for a fictional pop-up Christmas shop, collecting information on customers, products, product categories, and transactions.

In addition to the local database, a cloud database would be created, to which the local data would be transferred. Sensitive customer data would not be transferred to the cloud database to maintain a high level of data security. The data was to be generated using artificial intelligence.

Once the databases were completed, the next phase of the project would be to create dashboards from the data. These dashboards would help visualize and analyze the data collected by the store. Additionally, a web-based interface would be developed to facilitate easy and visually appealing data analysis and presentation. The web interface would also allow for data deletion, modification, and entry.

The project would also have its own website and other documentation.

### Sprint 1

In the first sprint, the plan was to create the databases and their data, and study topics related to the second sprint and team project best practices. First, team members unfamiliar with GitHub and Git learned the basics of their use.

A two-person team designed and created the local database, with each member responsible for two tables. These tables were thoroughly tested, including data entry, deletion, and modification. The dependencies between tables were also tested to ensure the integrity and functionality of the database. The same design, creation, and testing processes were carried out for the cloud database.

Streamlit and Dash were studied and compared for data visualization. Based on the comparison, we chose to use Streamlit for its ease of use and versatility.

During the sprint, we also generally studied all the aforementioned areas.

The only things we didn't manage to complete in the first sprint were the rule ensuring that customers provide either an email address or a phone number, leaving the other field optional, and the data generation for the customer and sales tables, which had to be continued in the next sprint.

Overall, the sprint provided a good foundation for the continuation of the project and helped the team deepen their skills in the technologies and methods used.

### Sprint 2

During the second sprint, we finished the tasks left over from the previous sprint. After that, our main task was to learn to use Power BI and create dashboards for data analysis using the data created in the last sprint.

The data analysis was done in a two-person group. They first planned what data to analyze and why, and defined who would analyze what. After this, the group practiced using Power BI and created the dashboards.

On the cloud side, we finalized the method to ensure that sensitive data remained in the local database instead of being transferred to the cloud database. We also explored other features related to the cloud database, such as creating snapshots to ensure data security and integrity.

Streamlit web interface was created, capable of displaying analyses of customer and sales data. This interface also allowed reading the entire databases content and performing CRUD operations on each table. Additionally, an offline version of the interface was made, using CSV files instead of a database connection.

A website was also created for the project, providing an overview of the project, introducing the project team, and linking to necessary documentation, the GitHub repository, and the Streamlit application.

## How to Use

---
