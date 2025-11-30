# Total Recall
## My TECS project to optimize learning.

## Weekly Notes ##
- [week 1 progress update](docs/week-one.md)

- [week 2 progress update](docs/week_two.md) 

- [week 3 progress update](docs/week_three.md)

- [week 4 progress update](docs/week_four.md)

- [images](/docs/img.md) where I provide the initial designes for Total Recall and updated designes as Total Recall changed throughout the month. 

- [Friction log](/docs/friction-log.md) where I treat it as like a diary updating every day/week with  more comprehensive explanations into what I am learning and the progress I'm making (something I cant really do that well on the weekly form).

----

Based on the science of "active recall", my project hopes to optimize ones abiity to learn by leveraging the [scientific research](https://pmc.ncbi.nlm.nih.gov/articles/PMC5126970/?). It works by a user entering in their notes and testing questions for that day, and after one day, week, month and three months, those notes and questions will be shown to the user to the test them and put learned information into their long term memory. Being in 6th year, this would be extremely helpful to me and being aware of the scientific research I attempted to find a tool to help me leverage it. After futile effort I decided to build it as my TECS project. 

 - Future enancements (if I had more time with TECS):
    - Ability to remove dynamically added questions (can add but cannot remove)
    - have the ability to edit notes
    - set up a daily cron to send an email to the user with their notes to look over for that day.
    - Set up user management to allow other to create an account and have their own notes

## -----------------------------------------------------------------------------------------------------

### Instructions on how set up Total Recall Locally ###

- install a virtual environment on your machine with these [libraries](requirements.txt).

- Run the database migration provided [here](db_schema.sql) to create the necessary tables into your chosen database.

- connect your API keys for the database and LLM following [.env.example](.env.example)

- To run the application locally input the following commands into your terminal. 
 - Mac OS: 
    - source venv/bin/activate
    - python app.py

- Windows: 
    - venv\Scripts\Activate
    - python app.py


- Finally go to http://127.0.0.1:5000 (could default to another port depending on your machine) and try out Total Recall for yourself!
 