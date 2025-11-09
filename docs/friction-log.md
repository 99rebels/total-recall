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
 - Spent some time working with and displaying the outputs of forms with flask routes etc. I can work it out fine in my head for the simple forms but trying to work out how I would do it in my case is more difficult. the form is going to be replaced with one with the subject argument when a dropdown is selected that will then populate the topic dropdown. Good practice though - nice to actually start building out total recall.