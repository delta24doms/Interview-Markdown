https://hackernoon.com/the-top-10-object-oriented-design-interview-questions-developers-should-know-c7fc2e13ce39
*(Some background: I've interviewed hundreds of candidates for software engineering jobs at Facebook and Microsoft. I've also failed several coding interviews myself when I wasn't prepared.)*


Object-Oriented Design (OOD) skills are a major plus for software engineers. They give interviewers an idea about the following:


1. Whether the candidate can translate a complex problem into a concrete set of objects and identify interactions among those objects to solve the problem at hand.
2. Whether the candidate can identify patterns while designing and, wherever applicable, effectively apply time-tested solutions instead of re-inventing the wheel.



> If you are looking for a complete course on Object-Oriented design for interviews, please take a look at following resources:
> 
> 
> [Grokking the Object-Oriented Design Interview](https://www.educative.io/collection/5668639101419520/5692201761767424).
> 
> 
> [Software Design Patterns: Best Practices for Software Developers](https://www.educative.io/collection/5307417243942912/5631943370604544).
> 
> 
> [Collection of interview preparation courses for software engineers.](https://www.educative.io/d/InterviewPrep)
> 
> 
> 


Object-Oriented Design Interviews are essential if you want to succeed as a software engineer, but plenty of engineers dread OOD interview questions (including myself when I was interviewing!). There are a few main reasons for this:


1. They can get very abstract, very quickly. OOD problems require the ability to "zoom out" of a problem and really think about the component parts on a high level (but not too abstract).
2. There isn't usually just one correct answer to a given question. Problems can be thought about or solved in a multitude of different ways.
3. Many beginner developers haven't yet had a chance to design a complex system from scratch.
4. Object-Oriented design is usually taught in colleges in a way that makes it look like a boring theoretical course, because you can't appreciate the value of such a design until the system is really complex --- and it's difficult to keep track of all the objects and interactions in your head.


![](img/1-3jomnwwry4fhtsyvw14khw-jpeg)


The good news is that at [Educative](https://www.educative.io/), we've talked to hundreds of candidates, and our authors have teamed up with hiring managers at top tech companies like Google, Amazon, Microsoft, and Facebook to tackle common interview problems in detail.


In addition to covering some of the most popular OOD interview questions these companies are likely to ask, I'll touch on what the general approach should be to solving such problems, so you can apply your skills to other questions as well.


### The approach to OOD interview questions:


In Object Oriented Design questions, interviewers are looking for your understanding of the nuances of complex problems and your ability to transform the requirements into comprehensible Classes.


In fact, OOD questions generally will all follow a very similar pattern. You will be provided with a vague problem and a set of constraints for a system to design, and very little else. It is then up to you, the candidate, to figure out the "level" of solution that the interviewer is looking for, what kind of functionality will be needed, and come up with a workable solution.


Interviewers are looking for one main thing: finding the right balance between a solution that works immediately and is also adaptable to change in the future.


To simplify things, you can take the following approach for any OOD question you encounter:


1. Clarify the requirements: Make sure you understand the expectations of the interviewer. Ask clarifying questions if at all necessary --- the interviewer will not mind, and will likely appreciate it. For example, "are you looking for me to demonstrate the structure of a solution, or to fully implement it?" Doing this here will take about 5--10 seconds, but save tremendous amounts of time later.
2. Hash out the primary use cases: Think about, and then *talk through,* use cases. Make sure you understand all the different functionality your system is expected to have. Talking about it out loud can also help you to come across expectations or ideas you might not have realized if you just jumped right in.
3. Identify key Objects: Now, identify all the objects that will play a role in your solution. For example, if you're designing a parking lot, these will be things like vehicles, parking spots, parking garages, entrances, exits, garage operators, etc.
4. Identify Operations supported by Objects: Work out all the behaviors you'd expect each object that you identified in the previous step to have. For example, a car should be able to move, park in a given spot, and hold a license plate. A parking spot should be able to accommodate a two-wheeled vehicle or a four-wheeled vehicle --- and so on.
5. Identify Interactions between Objects: Map out the relationships between the different objects that will need to interface with each other. This is where it all comes together. For example, a *car*should be able to park in a *parking spot*. *Parking garages* should be able to fit multiple *parking spots*, and so on.


I'll now walk through some of the top questions I'd recommend practicing. For each one, I'll also share some pointers about things the interviewer will probably be looking for in your answer to such a question.


To see detailed solutions, check out the course [Grokking the Object-Oriented Design Interview.](https://www.educative.io/collection/5668639101419520/5692201761767424)


### Design Amazon / Flipkart (an online shopping platform)


![](img/1-xfnsilp8rhwwvjtvznop8q-png)


Beyond the basic functionality (signup, login etc.), interviewers will be looking for the following:


* Discoverability: How will the buyer discover a product? How will the search surface results?
* Cart & Checkout: Users expect the cart and checkout to behave in a certain way. How will the design adhere to such known best practices while also introducing innovative checkout semantics like One-Click-Purchase?
* Payment Methods: Users can pay using credit cards, gift cards, etc. How will the payment method work with the checkout process?
* Product Reviews & Ratings: When can a user post a review and a rating? How are useful reviews tracked and less useful reviews de-prioritized?


### 2. Design a Movie Ticket Booking System


![](img/1-fcjwmc0sq2vsyebbzu2h-a-png)


Interviewers would be keen on seeing the following points in your answer:


* Duplication: How are you handling instances, such as the same cinema having multiple cinema halls showing different movies simultaneously? Or the same movie being shown at different times in the same cinema/hall?
* Payment Handling: What would be the process for a user to purchase a ticket?
* Selection: How would user a pick a seat, ensuring it's not already booked by someone else?
* Price Variances: How would discounted pricing be considered? For example, for students or children.


### 3. Design an ATM


![](img/1-9en453t9buruycszcwvnrg-png)


Interviewers would want to see you discuss things like:


* Overdrawing: What would you do when the ATM doesn't have any cash left?
* Pin Verification: What if a user enters a wrong PIN multiple times?
* Card Reading: How would you detect if the card has been correctly inserted or not?


### 4. Design an Airline Management System


![](img/1-llpevymmuxuczzllt9feoa-png)


A good answer from an interviewer's perspective would address:


* Itinerary Complexity: How would multi-flight itineraries work? How would multiple passengers on the same itinerary be handled?
* Alerts: How are customers notified if there's a change to the flight status?
* External Access: How would the system interact with other actors making reservations to the same flights, such as a front-desk operator for an airline?


### 5. Design Blackjack (a card game)


![](img/1-asfqq5wn5vajb3gd1acm1q-png)


Your answer should ideally consider the following:


* Scoring: On what level of the system is scoring handled? What are the advantages and disadvantages of this?
* Rules: What kind of flexibility exists for playing with slightly different house rules if needed?
* Betting: How are bet payouts handled? How are odds factored in?


### 6. Design a Hotel Management System


![](img/1-vatkx5nym0gm2zoiixe91g-png)


You'll want to make sure you cover:


* Room Complexity: How will the system support different room types within the same hotel?
* Alerts: How will the system remind users that their check-in date is approaching? What other alerts might be useful to factor in?
* Customization: How would users make special requests on their room? What kind of special requests would be supported?
* Cancellation / Modification: How would the system treat booking cancellation (within the allowed time period)? What about other changes? What types of modifications would be covered?


### 7. Design a Parking Lot


![](img/1-rf8k7w8yeazqhgj4bk9tkg-png)


This is one of the most common OOD interview questions and a must-know.


The interviewer will want to hear you discuss:


* Payment Flexibility: How are customers able to pay at different points (i.e. either at the customer's info console on each floor or at the exit) and by different methods (cash, credit, coupon)?
* Capacity: How will the parking capacity of each lot be considered? What happens when a lot becomes full?
* Vehicle Types: How will capacity be allocated for different parking spot types --- e.g. motorcycles, compact cars, electric cars, handicap vehicles, etc.?
* Pricing: How will pricing be handled? It should accommodate having different rates for each hour. For example, customers have to pay $4 for the first hour, $3.5 for the second and third hours, and $2.5 for all the remaining hours.


### 8. Design an Online Stock Brokerage System


![](img/1-jnvyjy4gxqaln1byqbhemg-png)


A good answer would cover these points:


* Watchlists: How would the system handle watchlists created by the user to save/monitor specific stocks?
* Transaction Types: How would the system handle different transaction types, e.g. stop loss and stop limit order? What types would be supported?
* Stock Lots: How will the system differentiate between different 'lots' of the same stock for reporting purposes if a user has bought the same stock multiple times?
* Reporting: How will the system generate reports for monthly, quarterly, and annual updates?


### 9. Design a Car Rental System


![](img/1-bqawrbzxbqwdd-cpsdfloq-png)


Candidates should be able to discuss the following:


* Identification: How will each vehicle be uniquely identified and located within the parking garage?
* Fees: How would the system collect a late fee for late returns?
* Logs: How would the system maintain a log for each vehicle and for each member?
* Customization: How would the system handle members' requests for additional services like roadside assistance, full insurance, and GPS?


### 10. Design Facebook --- a social network


![](img/1-s2rxf9ftkmqtdg8x-gow9a-png)


Your answer should ideally cover:


* Discoverability: How are users able to search other users' profiles?
* Following: How are users able to follow/unfollow other users without becoming a direct connection?
* Groups / Pages: How are members able to create both groups and pages in addition to their own user profiles?
* Privacy: How will the system handle privacy lists with certain content to be displayed only to specified connections?
* Alerts: How will users be notified for pre-selected events?


If you're looking for detailed answers to the above questions, including actual UML diagrams and code snippets, I highly recommend having a look at [Grokking the Object-Oriented Design Interview](https://www.educative.io/collection/5668639101419520/5692201761767424).


If you found this post helpful, please click the 👏 sign and follow me for more posts. If you have any feedback, reach out to me on [Twitter](https://twitter.com/fahimulhaq).


