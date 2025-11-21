# Friction Log: #

### 27/10 - 12:00: ###

 - Learning about databases, practicing using them with python ( basic CRUD functions)
 - Decided on using Supabase for database as I am familiar with other projects.
 - Need to figure out how to display table results on a HTML page (instead of terminal in VScode)
 - Going to leave “Auth” and “policies” to another day. I want to start displaying data on a screen.


### 1:00 ###

 - How do you show simple python outputs on the front end!? I have actually been at this for way too long. I just want to start off with something simple (“Hello World”) where I show the print(“Hello World”) on my python server to an index.html webpage. There seems to be a million ways to do it online like flask, pyscript, etc but I cant find the traditional way that its done.

### ---------------------------------------------------------------------------------------------------------------- ###

### 04/11 - 19:10 ###

  - Been a while since I’ve had time to work on total recall but we need to start building. Figured out I need to be using flask on my server side.

  - The plan for the next two hours is to learn and try and get my server and flask set up for development. 

### 21:00 ###

 - Flask env set up ready for development
 - Set up github repo
 - Took longer than I was hoping (never did this properly before)
 - Tomorrow I need to practice with Flask’s “@route” and parameters as well as calling functions for data retrieval from database (which I’m just realising i need to add the supabase client auth to my codebase)

 ### ---------------------------------------------------------------------------------------------------------------- ###

### 5/11 ###
 
  - Finished building out what I want total recall to look like on excalidraw (love that tool by the way). I'm happy whith how the UI for the [form](<img/Screenshot 2025-11-07 at 19.35.08.png>) came out where the user will input their notes, aswell as the UI for where the user will see their notes/questions to look over for that [day](<img/Screenshot 2025-11-07 at 19.32.19.png>).

  - Also created a [mobile version](<img/Screenshot 2025-11-07 at 19.35.58.png>) for this more to give me a feel as to how it could look aswell as keeping in a similar style to the desktop version (won't be building the mobile version out for TECS but good to have for the future). 


  ### --------------------------------------------------------------------------------------------------------------- ###

### 7/11 ###

 - Forgot to mention what I have done over the last few days (hasn't been a whole lot - exam season). I have been learning about Flask's routes, parameters and arguments as that is how I'm going to be moving my data. Also learning about "GET", "POST" etc.
 - Learning is slow - my first time trying to figure any of this out without the help of AI. Hopefully progress speeds up more this weekend into next week as I start developing total recall properly. 

## End Of Week One ## 

### 9/11 ###

 - Working with looping through datasets from my supabase database to show on a webpage. Pretty basic stuff but crucial that I learned it now.
 - next step is to build out the imput form.
 - need to change how the "topic" field works. It needs to be a dropdown instead of a text field for organisational purposes and building out how the topics will work in the future. The topic dropdown will be populated by the subject the user has decided on. For now I will have to manually create/add the topics for each subject as I go, in future I could make some kind of topic config but under the time constraints this will have to do.

#### 17:30 ####
 - Spent some time working with and displaying the outputs of forms with flask routes etc. I can work it out fine in my head for the simple forms but trying to work out how I would do it in my case is more difficult. the form is going to be replaced with one with the subject argument when a dropdown is selected that will then populate the topic dropdown. Good practice though - nice to actually start building out *Total Recall*.

 ### 10/11 ###

 #### 13:40 ####
  - Ok, I've run into a problem. I want to dynamically reload the form when a subject is selectd from a dropdown menue. This would be to then make a call to the database with the subject selected and recieve the realevnt topics from that subject. I thought this might be possible to do with the ***action*** attribute on the ***select*** tag but this wont work (will only perform "action" when form is submitted).

 - From what I've seen, theres a couple of methods around this. The first is by using JS. I have no expereince with JS but the fix seems relatively simple, just code listening to whether or not the subject dropdown has been selected and sending the realavent data over to reload the form. I'm sure I could get this to work but I'm afraid of adding extra complexities such as introducing a new language I know nothing about.

 - The other way I could think to make this work is by having 2 seperate forms. Where the User would input their subject (pressing a submit button) and then the other form would appear with the correctly populated topic dropdown and with space for notes etc. This way is more clunky but removes the requirement for JS which is nice.

  - I'm going to try the second way but if it's too clunky I will rethink the first option.


#### 18:30 ####

 - Progress is slow, but progress is progress I guess. I have spent the day building out the form routes that will take place - hopefully I get them finished tonight. If I can thats a huge section of the input form finished. It doesnt look pretty, but it doesnt have to at the moment.

 - Hopefully over the course of the project I stop spending so long on silly mistakes (and learn how to clean up my code a bit, its pretty clunky but thats probably ok). 

 - Something else I need to consider is how I'm returning my HTML pages. I thought I was going to do it through building the page up with loops etc but the more I do it the more clunky and hard to follow it's becoming. My other option in jinga templates but I'm worried that's another can of worms. I'll research that option when I'm building up the entire page but for now I'll just continue building it up in python.
 


### 11/11 ###
 #### 15:15 ####

  - I have come to the conluction that jinga templating is the way to go. It isn't actually as complicated as I though and trying to build the html pages up through Python is already complicated with a simple form page.
  - Hopefully I can get everything sorted with the new html files and teplating today - glad I caught this early as this would have been awful to try and change later on with more complex pages.

#### 16:12 ####

 - Ok, that was much easier to chanage to jinja than I thought - good sign. Code is so much cleaner and easier to read now. 

 - next order of business is adding the notes and questions to the database

#### 19:50 ####
 - Just finishing up/cleaning up my code from today, updating routes, redirecting to a "submitted" page when the form submit button is pressed. Also added a calendar to the form and configured the database to accept the dates. 

 - This is in preperation for the next few days where I'll be working on the functionality to retrieve the relavent notes depending on the date where a function will compare the dates in the database and retrieve depening on the time between them (I dont exactly know how to do this yet, it might be easier then I'm making it out to be).

### 12/10/25 ###
#### 19:40 ####
 - After trying to understand the code that I wrote last night, I just realised i really need to comment on my code to actually explain to myself and the TECS mentors looking at it, what is actually going on. So I'll spend some time doing that. First order of business is to work out the functionality for retrival of data form the DB depending on the date.

 - I also need to change the names of html files and functions to be more descriptive because I can barely actually understand where my functions are pointing. 

### 13/11/15 ###
#### 10:00 ####
 - Spent last night working on the functionality for the retrieving of data depending on the date. I knew it would be operated under a script, but didnt know how that worked. Turns out scripts run entire py files, not specific functions (not sure why I didnt know that, that makes so much more sense). Therefore I did all the functiontionality inside a function making the code super clunky and error prone.

 - going to spend the next hour rewriting the logic (hopefully in a much better way) in the new file [script.py](/script.py)

#### 16:40 ####
 - Scratch that, I wrote the function inside a specific [db_client](/utils/db_client.py) file in a **utils** folder so that I can call it with my *script.py* file (which will send an email with the notes to the user) and my *app.py*. In summary, it's set up for an automatic cron call for the daily email, and a user call when a user goes to */todays_notes*.

#### 19:00 ####
 - Just had a thought while creating the jinja logic on my front end. A user will be adding their notes and questions into one input on the html form. But this just doesn't make sense (especially for the questions). The returning data will then be just one big paragraph of questions which doesnt make sense at all. I need to rethink the input of this to display the notes and questions as something like an unorderd list n the front end.

- The only option I have I think is to have seperate text fields for different questions i.e question 1, question 2 etc so that they're all added to the database seperately. For now I can hard code these inputs but ideally i'd like addition/deletion functionality on the form and for that I'll need to implement JS (could keep making calls to the backed and refresh the page with the extra text field but that feels too clunky). 

- Thats not to mention possible problems with the DB if some notes have 5 questions attatched and others have 8. How will that look on the database and retrieval? would I have to hard code 50 columns of questions and have them as "none" unless filled? There must be a better way then that. Regardless - food for though. The plan now is to go back and hardcode 5 text fields for notes and questions and I can look at the dynamic aspect later on. **Rant is over**


### 14/11/25 ###
#### 9:00 ####

 - Ok, need to do a big push today. My aim for the end of the weekend is to have all the basic functionality fully finished so I can start working on some stretch goals and making it look good.

 - might be worth also revising the style of the form as things have now changed with the addition of new questions.
 - the plan for this is to (for now) hard code a max of 5 questions to be sent and later today/tomorrow i'll implement the JS to do this dynamically. I also need to change my databse table from a flat file DB to a relational one, using foreign/local keys, etc. 

-  My advice from the TECS mentors was to keep everything implementation simple and make sure that I save time at the end for bug fixes, styleing etc, so i'll keep that in mind as I go through. 

- For this morning I think my first plan of action should be adding the five questions and sending them to the same table in the DB. Then I'll change the DB so it has its own questions table with id of "created_at" (the date). 

#### 10:00 ####
- well that was one frustrating hour. My names and routes were all messed up and I eneded up just completely confusing myself. I took that time to sort them out/renamining them going through the whole flow. Also spent the time commenting on my functions explaing what they do.


#### 13:00 ####
 - This is so frustrating. I'm trying to get my head around relational databases and I'm still trying to get my code to work as it did before. Really slow prgress, but I just have to power through.

### 15/11/25 ###
 - Ok, I finished the refactoring but I'm not iterating through my questions properly. i think I need to add the new question dictionary into the notes dictionary before sending it over. This means I'm not sending so many objects through to the todays_notes html page.

 - I'll do that tommorrow, for now I need to send in my weekly report to TECS


## End Of Week Two ## 

### 16/11/25 ###
#### 13:10 ####

 - Ok this is the problem. Due to the separation of the questions from the notes on the databse, theres nothing that ties the questions *to* the notes. This causes all the questions with that date to be shown on the font end, not the questions for the corresponding notes.

 - My way of solving this issue I think it to append the questions dictionary in the notes dictionary and loop through the notes dictionary as usual, but also then loop through the corresponding questions dictionary, now inside the notes dictionary. Not sure how much sense that makes in writing but it makes sense to me so that's all that matters...

### 17/11/25 ###
#### 16:00 ####
 - That was way to difficult then it should have been. I ended up breaking everything and not realising what was actually going on. I ended up having way too many variables, lists and for loops. I decided to rewrite the definition on db_client.py to include the get_notes function and get_questions. Now its all one function which I'm not sure is best practice but has dramatically cut down the amount of code I had to deal with. Now the function on app.py and db_client.py. is much cleaner and I only have one type of variable (day_prior_notes, etc) instead of the addition of day_prior_questions which called another function.

 - Regardless, questions from the date are correctly added to the relavent notes dictionary and are correctly being looped through - **Finally**

 - Now, I need to work on script.py that will be run by a daily cron for the email. If I get this done quickly I would love to have a look at a stretch goal of intergrating an LLM for extra question creation - need to keep an eye on timing for this dont want to corner myself time wise. 


### 19/11/25 ###
#### 14:30 ####
 - I haven't that much time to work on total recall over the last few days but I have gotten some stuff done. First of all I implemented the JavaScript on the front end for dynamic question creation. Admittedly I had pretty much 0 expereince with JS before this so I very quickly got everything I needed on stack overflow with basic learnings on different variables and acsessing a variable with a specific element id etc. 

 - I've also decided not to prioratise the daily email. Instead I want to intergrate AI in total recall (because I've wanted to work with LLM's for ages and I think it would be so cool). 

 - I want a button somewhere in the relavent notes section that when pressed, send the notes and questions to an LLM to then send back more AI created questions. This fits in the "total recall universe" quite well. My hypothisis is that when people write their own questions, they know the exact word or word answer (most likely in the notes also). But when different questions are given or frased differently, it requiers "mastery" of the content in your own words in order to correctly answer the question which helps you learn the content better. In short, this is my excuse to be able to work with LLM's in my code.

 - I have realised that I have been including my .env file in my github pushes (fine for now but could have been really bad if I had my private DB key or AI API key). So I need to sort that out. 

 -  I also bought totalrecall.info in preperating for production on Render. 


#### 17:30 ####
 - I have added the added the gemini model (gemini-1.5-flash as it appears to be free or at least of negligable price). I'm trying to figure out how I'm going to do this. There is two ways I can think of doing it. The first is by using python, when the button is pressed it does a HTTP call to the same page returning the value of the LLM's response but that will mean it will wait for the response meaning long page loads.

 - The second way is with JS. On button press, it would send a request to the Flask function and wait for the result. This is a way better UX because the entire page wouldn't be loading. However, I dont know how to do this. Also, Do I send it as JSON? the only things I need is the notes, subject, topic and questions as arguments to the flask function. I need to think about this.

 - I think I do it with something called an AJAX request? not 100 percent sure what that means but we'll give it a go....

 - Hold on this is a bit more complicated. The issue is that my todays_notes.html page is being dynamically built up with JINJA. Its easy to acsess a single div or form element with JS but how to you access the loop and send the correct notes?


#### 18:00 ####
 - I'm not experienced enough with Java Script to know what I'm doing. I cant think of how to do it at all. For now I'm going to try and get it to work in python first (I have an idea for this). This will at least get the function on flask working with the LLM and resposnses correctly. Then I can change it to JS. I need to get more familiar how JS works with Jinja, in terms of looping accessing variables etc. 


### 21/11/25 ###
#### 11:50 ####
 - Holy shit, after a days work I finally got a response from Gemini. This is rediculously cool. It's just printed to the console but that is acctually so satisfying. It wasn't all that difficult (I had some trouble with routes etc) but it is so cool to see it working. It now generates 5 questions on the notes provided when the button is pressed.

 - Now I need to parse the string to only get the questions