## Summary Of Week Three ##

 - I got a lot done this week, adding two major pieces of functionality that in my opinion, really tie the project together.

 - The First was dynamically generating extra questions with the click of a button. Before this I had hardcoded 5 questions but thats just not ideal from a UX perspective. To do this I had to use JS which was completely new to me. The code is probaly half broken but it does the job and I can always optimise it after TECS, but for now, time is of the essence. 

 - The second pice of functionality was an LLM intergration. This was easily the most fun I have had coding yet and the most satisfying. I use AI every day and I have coded in the past using AI but being able to call gemini (gemini-2.5-flash) with an API and recieveing a response has to be the coolest thing ever. The functionality isn't fully finished as its still buggy in terms of displaying but I have the main code finished where I am getting and parsing the response correctly.

 - The functionality of the LLM is to generate 5 new questions for the user based on the notes, subject, topic and the users questions. For Total Recall purposes, it helps the user get "mastery" of the content they wish to learn by having to answer questions they didnt already know the answers to. However the main reason I added the LLM was because I just really wanted to use one in the codebase and experiemnt with one.

 - **The Plan:** We're coming down to crunch time now so i need to get full functionality of Total Recall done by tomorrow. Next week is going to make the tool look somewhat presentable. I also need to get it up online hosted with render in which I was able to snag totalrecall.info (a perfect domain if I do say so myself).