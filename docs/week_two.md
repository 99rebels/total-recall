## Summary of week two ##

 - I have finished most of the functionality for Total Recall this week.

 - Building out the routes and logic was relatively easy. I can see myself getting more and more comfortable with code the longer I do it. 

 - However, the main troubleshooting of the week came after creating the main functionality. I realised my database isn't set up as it should be. I have been using it as a flatfile databse but shouldve been leveraging its relational qualities. To do this, I separated the questions column into its own table with the notes table's "id" as the primary key.

 - It certainly took a while to learn how to interact with a relational database such as this and the refactoring of my code to work with the new table took a while also. As of now, I am 99 percent of the way back to full functionality (I just need to add the questions dictionary into the notes dictionary before sending it over to todays_notes.html). This is to stop problems when looping through the dictionaries on the front end. Right now, all the questions are printing when it should just be the questions relating to the notes.

 - the plan for next week is to fully finish the refactoring procsess and create the functionality and set up the cron to send an email to the user with their notes and test questions every day. This will be done on script.py. I also need to look at the dynamic addition of questions with JS, a language I have not touched before. Also need to keep in mind the advice from the mentor on allowing sufficient time for bug fixes/styling, and keeping thins simple. 
