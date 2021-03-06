# Teaching Notes

# March 10th, 2020

Just completed week eight, the end of the second session. I think we were really able to improve the course this time around and I look forward to continuing that.

## Kids Write Code Every Class

Having the kids do _anything_ themselves means committing a significant portion of the class time. Most of them are slow typers, and they get hung up on simple issues so they require constant attention to keep them moving. It asks more of the kids in terms of effort and focus, something not all of them are in the mood for after school. Still, my resolution to have them write code every day worked out really well, especially towards the later classes. They left the session with far more personally accomplished than in the last one.

Most classes, my volunteer assistant and I were able to get the class through an exercise so that everybody had a working program by the end. I wasn't sure that kids these days would find the same satisfaction in simple text programs that I did back in the day, but they did. They really enjoyed running their programs and watching them work, messing around with them and seeing what happened. It brings back memories of all the silly things I experimented with too - printing rude things to the screen, trying to make the biggest output or the largest number and seeing where it breaks.

Week eight was the most fun class in a session with quite a few highlights. Just like last session, we talked about secret codes (which sounds way more fun than cryptography,) and a couple of children were really drawn in by this subject.

## Hardcore Computer Science

Then we learned about recursion by writing a naive fibonacci implementation together. This was definitely more advanced than I could have done in the last session, and still I was probably pushing it a bit, but the kids already knew about the Fibonacci sequence from school so that was helpful. I introduced functions several classes earlier this time and I've been really hammering on those, so the basic understanding was out of the way.

We calculated some fibonacci numbers and, true to form, several kids punched in big numbers to see what happened. What happened was that the program froze as a massive number of calculations ticked away in the background, and I used this as an entrée to algorihmic complexity and optimization. Computers are crazy fast kids, but you can trick them into being slow really easily. :) Without explaining in detail, I optimized the function using memoization and had it quickly calculate the one millionth fibonacci number. As the digits rushed by on the screen I got all the oohs and ahhs I was hoping for.

## Notes for Next Time

  * Code every class is a good strategy. Let's stick with it.
  * Introduce functions even earlier. Bring out the "function as an I/O machine" slide as soon as possible, that clicked.
  * If I do Github again for the "something fun" section, wait until much later in the session. Kids either didn't see the appeal or didn't care.
  * Think of something better for the kids to do with lists. They should be introduced, I think, but I haven't been able to find a good simple application other than fiddling with them in the REPL.
  * Be prepared with resources and things they can do at home and next steps after the session. A bunch of kids and parents asked me about this and I didn't have much to offer them.


# February 4th, 2020
Week four complete. I introduced a new segment to the class today called You Write It. I run a program and show the class the *output*, and they have to write the code to make that program.

This is an exercise I tried out in weeks 7 and 8 during the last round of Coding Club, and I found the students were far less prepared than I thought to actually write code on a blank screen, even with access to all of the resources and code we'd already worked with.

So I'm bringing it into the class much earlier to get them started. The output of today's program looked like this (output from three runs.)

> What is your name? Simon
> 
> Hello, Simon.

> What is your name? Dinesh
>
> Hello, Dinesh.

> What is your name? James
>
> You stink.

I talked the kids through the ideas they would have to think about this and heavily accentuated the key words like *input*, *print*, *if* and *else*, hoping to jog their memories.

They did pretty well! Two children had a working program within about five minutes. I wrote out some pseudocode on the projector and progressively filled in more clues until everybody had it.

I'm definitely going to make You Write It a feature we do every week.

# January 14th, 2020
Time for coding club round 2! I've just completed the second class with a new batch of kids.

We've got two repeaters who signed up again - this is a good sign, right? I'm covering mostly the same material but they seem to be enjoying themselves anyway.

The class is bigger this time. The capacity is technically eight, but we had many more on the waiting list, and some of those showed up on the first day. By grabbing some chromebooks from the librarian we've been able to accomodate eleven kids. Surprisingly it hasn't been much more chaotic than last time.

My big goal for this time around is to have the children write more code. Last round I gave them some direct coding assignments in the last two classes, and I was disappointed how little they were able to do on their own. Looking back, I spent most of the eight weeks talking and explaining to them, and having us read code together. I'd like to see if they learn faster when we all write code together, every class. I think there's a danger that they'll just copy whatever code I put in front of them without really parsing it, but it still might be a more effective method than anything else ([Zed Shaw seems to think so.](https://learnpythonthehardway.org/python3/intro.html))

# October 30th, 2019

## Back to Basics
I've exhausted all of the ideas I had for the Back to Basics section, so today we did a Q&A. I was wondering if the kids were aware of any blind spots in their learning - terms or ideas that they were aware of but didn't understand, and so on. Most of the questions were about video games. How do real games get made? Can one person make a "real" game? We talked about "triple A" studio games and the hundreds of different people and roles that contribute to them, and the rise of indie games and people like Markus Persson, a.k.a. Notch, who single-handedly developed Minecraft.

## Something Fun: Secret Codes
We talked about the idea of using a code to send and receive secret messages, and that computers are really good for this. I introduced the idea of a substitution cypher and we played with a python impelmentation of ROT13. Then we talked about much more powerful codes, and a quick bit about the history of signals intelligence, the Enigma machine, and modern government agencies like the CSE. In introduced the PGP project which is real encryption you can use that even governments have a hard time cracking.

## Coding Time! Implementing functions, debugging
I tried a new angle in getting the kids to write code. Coding from scratch in teams was pretty successful last week. This time I had them work singly on a partially completed program for a calculator. The body of the program was there, but there were three missing methods to do addition, subtraction and multiplication.

A couple of kids were able to complete this pretty quickly. Some read back through past weeks and were able to figure out what declaring a function looked like. Some were pretty lost and needed help to complete it.

Once we had all of our code created, we ran our programs and found a bug! Something was going wrong. The problem was that our program wasn't converting user input from text into a numeric type. A couple of the kids figured this out early, but I asked them to keep quiet.

We investigated this bug by using the IDLE debugger. This was our first look at a tool of this kind, and we talked for a minute about how programmers, like carpenters, can make their own tools.

By stepping through the program and examining the state of variables, we were able to observe the bug in action and then implement.

## Finishing Up

With a bit of time left at the end, I thanked the kids for taking part in the class and gave them some advice on how to keep learning coding. The kids said some really nice things about the class and how much they enjoyed it, which was pretty thrilling for me.

As we approach the next round of coding club in January, I'll start making a to-do list of things to keep and things to improve on. This was a great experience and I'm looking forward to the next one!

# October 23rd, 2019

## Back to Basics
Today we learned about files and folders, another element that is absent from mobile computing. We brought up the hard drive of our computer in Windows Explorer and poked around. We made some files and folders in our Documents folders and saw how they could nest inside each other.

## free-python-games

We took a look at Grant Jenks' great repo [Free Python Games](http://www.grantjenks.com/docs/freegames/). He makes a basic drawing API that is perfect for simple games, and provides a dozen or so implementations of games like Snake and Tic-tac-toe that are surprisingly short and easy to read.

We tried messing around with the source code for Snake to see if we could get double the length for every apple eaten. Instead the snake started growing out of control, which was also fun.

## Group Work!

After being defeated last week I resolved that these kids were going to write some more code. On the advice of some of my teacher friends I broke them into groups of two and three and gave them an assignment.

The content for week 7 was not a program, but a program output. The kids would have to read the output of that game and figure out how a program like that would work, then write it.

I kept the programs very simple, and used concepts we learned in past weeks. I encouraged the kids to look in the past weeks code from the club repo - copy/paste was completely allowed.

The results were excellent. Although I said it wasn't a competition, it quickly turned into one, and all the groups completed at least one program, some two. It was a challenge for everybody, but I think they gained some confidence by the time we were done. Writing your own program from scratch and watching it run is a great feeling!

The kids asked if we could do this again next week, and I think it's a great way to go out for the last lesson.

# October 15th, 2019

## Back to Basics
This week's Back to Basics was window management. A lot of kids have grown up on tablets and phones, so the basic concepts of opening and arranging windows, minimizing and restoring, are new ideas for some. Sure enough, there were a lot of surprised comments as some of the kids learned for the first time where that window "goes" when you minimize it.

## repl.it

For "Something Fun" we took a look at https://repl.it, a site where you can code in python (and other languages) right in your browser. We were able to connect it to our coding club git repo and run some of the games from earlier weeks. Cool!

## Lists and For Loops

Last week was great but we were mostly reading and explaining code, and I wanted this week to be mostly *writing* code. This did no go well.

We introducted the idea of a List in python and used the REPL to create lists and add items to them. Wrangling the room through this exercise took up a big part of the class and I wasn't able to get to For loops. We'll have to try a different approach next time.

## hangman.py

I put together another sample game that makes use of the things we've learned so far, and the kids had fun playing hangman. We had a good chat reading over the code - they thought it was pretty cool that my python script reached out to a list of 10,000 common words from some git repo in order to get the secret word.

Next week I'm trying a group exercise as a way to get these kids writing some code.

# October 8th, 2019

## Back to Basics
This week we learned about copying and pasting text, in our ongoing effort to get these kids up to speed on basic computing skills. We're now just about at a place where I can instruct the kids to grab a python file from the club github directory, copy it and paste it into a new file in IDLE... and in a few minutes, with a few desk visits, be up and running. Not too shabby.

## Neural Networks and Genetic Algorithms
We learned about the classic computer game "Snake" and how its simple rules and controls make it a great candidate for experimenting with machine learning.

Then we watched [a video of a simple AI learning to play the game](https://www.youtube.com/watch?v=zIkBYwdkuTk). We talked (at a very high level) about neural networks and genetic algorithms, which the kids seemed to understand once we watched generation after generation of AI "Snakes" improve their strategy incrementally.

We talked about how it would probably be easier to just write a program that plays Snake perfectly, but that this was an example of a different idea - a program that "learns" over time.

## Joke Telling and Dragon Realm
We got through the next two programs in the textbook.

[jokes.py](https://github.com/buzzcola/codingclub/blob/master/Week%2005/jokes.py) is a very simple program that tells a few jokes and just waits for the user to hit Enter to move to the next section. We learned some new tricks about string delimiters, escape characters, and the "end" optional parameter on the print() function.

[Dragon Realm](https://github.com/buzzcola/codingclub/blob/master/Week%2005/dragonrealm.py) taught us a few new ideas, the most important being how to define your own functions. I really tried to drive home how fundamental this is.

We managed to spend some time with both of these programs before time ran out for the day.

Next week I'd like to focus on writing some new code - we had great focus and made progress this week, but we only read and discussed code. Next is the point in the book that introduces debugging, which should be fun. And I really feel like it's time we played with some native data structures like lists.

## Highlights

I had some great questions and answers from the kids this week, indicating that they're really paying attention - 
  * I asked - why do you think python allows string qualification using interchangable single or double quotes?
  * The kids correctly guessed that it allowed you to make a string with a single or double quote inside.
  * I was then asked what to do when you need to define a string that contains both. Excellent question! This let right into the next topic of escape characters.
  * Once again a great question - how do you escape escape characters?

# October 1st, 2019

## Order and Chaos

I started the class by talking to the kids about our behaviour and expectations. Last week was pretty rough, and this was my attempt to get things back on track. I asked that we work together to make a good learning environment for everybody, and that we keep to one person talking at a time. This seemed to work and today went a lot better. I think I'll repeat this at the start of every class from now on.

## Back to Basics
I introduced a new section today called Back to Basics: quick lessons to get the kids up to speed on the general computing skills they will need to get started in programming.

This week it was about using the keyboard to edit a document. I had noticed a lot of kids hammering away at the arrow buttons to try and get the cursor where they wanted it, or having trouble inserting a line or a tab in the right place.

We talked about the Home, End and Delete keys, and how to use Ctrl-Home/Ctrl-End to move to the beginning/end of a document. There were a lot of "oohs" and "ahhs". Next week I'll show them about copying and pasting text.

## Squeakernet FLP
For our "Something Fun" segment, we looked at an [automated cat feeder project](https://github.com/buzzcola/squeakernet) that I built last year. Much like our earlier look at [shmup](https://github.com/kidscancode/gamedev/blob/master/shmup/shmup-24.py), most of the code was beyond the kids' level but we were still able to identify things that we recognized and learn about how the program worked. 

This was wildly popular, which is predictable since it includes videos of cats.

## Guessing Game
Our main task for the class was to complete our number guessing game that we started in Week 2. We had just enough time to get the final features in.

## Memorable Quotes
  * *"I'm looking at the code and I can see how it's going to work without running it."*
  * *"This is the coolest game I've ever made!"*
  * *"Hah! it's five fifteen, I'm not finishing my program, see you later losers!"*

# September 25th, 2019

I haven't taught in a classroom before, or taught children. So I have a lot to learn here. Here are some notes about my experiences so far.

## Class Structure
What's the best way to organize a one-hour weekly coding class? Here's what I've been trying:

  * Welcome, and please tell me your names again. I don't have a teacher's knack for memorizing the kids' names. I hope they're not too offended.
  * Review of previous weeks' material. There are a lot of details to learn on this subject, so I try to repeat myself as much as possible. After a few minutes of rehashing concepts I feel like the kids get back up to speed.
  * Something fun! We take some time to take a look at something interesting. So far we've looked at a real video game written in python and taken a tour of Github, the social coding site.
  * Then on to the main task: we pick up where we left off in the textbook and work on some code together to create or improve a game.

## Missing Required Skills (Children)

Although the new generation is often referred to as "digital natives", it appears the children's primary experiences with computing are the curated experiences of tablets and phones. I've found them surprisingly unprepared for real computer use in a few areas.

I'll try to incorporate an introduction to these topics in future classes.

### Window Management
Using an operating system like Windows, Linux or OSX often involves managing windows: rectangles that contain programs, like a web browser. They can be resized, maximized, minimized and closed.

### Typing
I don't expect the children to be able to touch-type 100 words per minute, but I was surprised that a number of them struggled with moving the cursor around a document and editing text.

### Files and Folders
This is the primary way that data is organized and accessed on a computer, and must be understood for the type of work we're doing in this class.

## Missing Required Skills (Me)
I didn't realize what a challenge it would be to manage eight children ages 9-12 for one hour. I have a new respect for elementary school teachers who teach much larger groups all day long.

When I move around around the room to help children with individual problems, I find that by the time I finish the room has gone out of control. Bringing everybody back to focus turns out to be a big job.

I've spoken to some of my friends who are school teachers and I have a few new strategies to try.