# 🤖 VIRTUAL-ASSISTANT 🤖

### 🔶🔶 One of my best completely self-built from scratch projects

>### This Project is the Virtual Assistant that's been created by using Libraries and end-to-end Customization

### ***`"Olivia"`*** is the name of my Assistant and does whatever you ask her to do!!

<br>

## ✅ IMPLEMENTATION ✅

Once the program is run, the microphone gets activated to listen to the voice commands.
The assistant gets activated only when the name assigned to her is called, otherwise it doesn’t respond.
Once the assistant is activated a number of tasks can be performed by her all with you’re beautiful voice like,

### As every Assistant out there it does the following :\
📅 Date, time and day can be asked.\
🔎 Search the web.\
🔓 Open various apps, sites.\
⏰ Sets a Reminder.\
📝 Open Word and write in it all with your voice.\
📰 Read out the latest news from NDTV without even opening it.\
🎼 Change the assistant's voice as per wish.\
😜 Crack some jokes.

<br>

## ⚡ ALGORITHM ⚡

1.  START
2.  Use get_audio() function to take audio input from the microphone.
3.  If "Olivia" in the input: Reply/Greet the user.
4.  Else: Ask the user to call the assistant's name in the input.
5.  Expect voice input/commands from the user.
6.  User asks to set a reminder.
7.  Call the reminder_seconds() function.
8.  Takes input as description/reason of reminder and time.
9.  Reminds you of your given description at a given time.
10. And also notifies you using the Windows System Notification with the reason.
11. User asks to open a word document.
12. Calls write_content() function which Opens a word document.
13. Takes live audio input for specified time.
14. Audio input is converted to a string.
15. This string is printed on the Word Document.
16. This function includes features like using Left, right, centre align, bold, underline and italics. All this is excluded from the text to be typed on the word document.
17. User asks to do a google search (search Elon Musk).
18. Here the keyword is search and the rest is searched on Bing.
19. Opens a browser and searches results and gives output.
20. User asks for a date/time.
21. Displays day, date, time accordingly
22. Other possible inputs
  a.  Runs its respective program/ calls function
  b.  Displays error on not recognizing input
  c.  Asks for the input again
23. Input to terminate the program.
24. STOP

<br>

## 🧊 WORKING 

### When the program executes the mic is enabled and is waiting for the user’s input for the name of the assistant to activate it. There are three possible outcomes:
***✒️  If no input, assistant asks politely for input***
\
***✒️ If the input is wrong, assistant reminds the user to call out it’s name***
\
***✒️ If the input is correct the assistant is activated*** 

<br>

### 💡 Now when the assistant is activated there is a list of functions available for use.  For Ex. : 


 ### ***📌 When the user asks for date, day or time :*** 
   Assistant replies to the user accordingly getting real time values with hardcoded name of days.


 ### ***📌 When the user asks for a reminder to be set :***
   Assistant asks what to remind and will remind the user at the specified time with the specified reason. Assistant also uses a system notification sent for reminding.


### ***📌 When the user asks to use a word :***
   Assistant opens a word file and does real time typing while the user is talking excluding the words like bold, italics, underline, centre. left, right align while providing    functions for the same.


### ***📌 When the user asks for latest news updates :***
   Assistant web scraps NDTV.com in the background for the latest news and prints it on the output panel of the IDE with a link provided for the same.


### ***📌 When the user asks for a web search :***
   Assistant searches the web for the same and opens the browser for us.


### ***📌 When the user asks for help in python :***
   Assistant gives the user a choice of three websites commonly used for programming related doubts. According to the user’s wish the assistant opens the chosen website.


### ***📌 When the user asks for some jokes :***
   Assistant gets jokes from a dataset of more than 60,000 jokes and speaks it out and after every joke accesses a .mp3 file in the computer directory for a crowd laughing effect.


### ***📌 When the user asks to change the voice :***
   Assistant changes its voice to male and asks the user if would like to be kept and do so accordingly. If the user doesn’t like that voice it changes to another voice and again sks the user for acceptance, and do so accordingly.


### ***📌 When the user asks to open any application :***
   Assistant opens the computer applications. These applications can be stored in a file with the applications shortcuts and this file path can be saved in the environment variables so that it can be accessed anywhere in the computer.
