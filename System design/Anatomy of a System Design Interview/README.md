*How can you design a large scale distributed system during an interview?*
https://hackernoon.com/anatomy-of-a-system-design-interview-4cb57d75a53f

Over the last 2 years, I've taken 100s of System Design Interviews and helped engineers prepare for their interviews. Based on that experience, I've devised a set of steps that are helpful in approaching a system design interview problem. In this post, I'll focus on the following topics:


1. How to prepare for system design interviews?
2. How to approach a problem in a systematic way to maximize your chances of success?


EDIT: Also look at [Top 10 System Design Interview Questions for Software Engineers](https://hackernoon.com/top-10-system-design-interview-questions-for-software-engineers-8561290f0444).


I previously wrote a couple of blog posts listing the common mistakes in programming interviews: *h*[*ow not to design Netflix in your 45-minute system design interview*](https://hackernoon.com/how-not-to-design-netflix-in-your-45-minute-system-design-interview-64953391a054) and *h*[*ow not to succeed in your 45-minute coding interview*](https://hackernoon.com/how-not-to-succeed-in-your-45-minute-coding-interview-2eebd46bd6ec)*.*


I got a lot of feedback (and emails) on my earlier posts. The most common question was how should an interviewee approach the system design interviews. There are so many concepts, directions, components, pros and cons that one cannot describe all of them in 4 hours, let alone in 45 minutes.



> Unlike whiteboard coding interviews, there are very few "Aha" moments in system design interviews.
> 
> 
> 


In other words, System Design interviews are less about getting lucky and more about actually doing the hard work of attaining knowledge. At the end, your performance in these interviews depends on the following 2 factors.


1. Your knowledge --- gained either through studying or practical experience.
2. Your ability to articulate your thoughts.


When companies ask design questions, they want to evaluate your design skills and experience in designing large scale distributed systems. How well you do in such interviews often dictates your hiring level (and in some cases even salary). Hence, it's in your best interest to have a plan and prepare for these interviews.


*If you are looking for resources to prepare for system design and programming interviews, take a look at:*


1. [Grokking the System Design Interview](https://www.educative.io/collection/5668639101419520/5649050225344512)
2. [Grokking the Object-Oriented Design Interview](https://www.educative.io/collection/5668639101419520/5692201761767424)
3. [Coderust 3.0: Faster Coding Interview Preparation with Interactive Challenges & Visualizations](https://www.educative.io/collection/5642554087309312/5679846214598656)
4. [Data Structures for Coding Interviews](https://www.educative.io/d/data_structures)


### 7 steps to approach a System Design Interview


As you are studying, here's a 7-step framework that I recommend to approach each problem. For keeping the examples real, we will pick up a common interview question: Design a scalable service like Twitter and see how each step can be applied to designing Twitter.


#### Step 1: Requirement Gathering:


Many candidates think that system design interviews are all about "scale", forgetting to put required emphasis on the "system" part of the interview.



> You need to have a working "system" before you can scale it.
> 
> 
> 


As the first step in your interview, you should ask questions to find the exact scope of the problem. Design questions are mostly open-ended, and they don't have ONE correct answer. That's why clarifying ambiguities early in the interview becomes critical. Candidates who spend time in clearly defining the end goals of the system, always have a better chance of success.


Here are some questions for designing Twitter that should be answered before moving on to next steps:


1. *Who can post a tweet? (answer: any user)*
2. *Who can read the tweet? (answer:*any user --- as all tweets are public*)*
3. *Will a tweet contain photos or videos (answer: for now, just photos)*
4. *Can a user follow another user? (answer: yes).*
5. *Can a user 'like' a tweet? (answer: yes).*
6. *What gets included in the user feed (answer: tweets from everyone whom you are following).*
7. *Is feed a list of tweets in chronological order? (answer: for now, yes).*
8. *Can a user search for tweets (answer: yes).*
9. *Are we designing the client/server interaction or backend architecture or both (answer: we want to understand the interaction between client/server but we will focus on how to scale the backend).*
10. *How many total users are there (answer: we expect to reach 200 Million users in the first year).*
11. *How many daily active users are there (100 million users sign-in everyday)*


If you notice, some of these answers are not exactly similar to the real Twitter, and that's ok. It's a hypothetical problem geared towards evaluating your approach. You are just asking these questions to scope the problem that you are going to solve today. e.g. you now don't have to worry about handling videos or generating a timeline using algorithms etc.


#### Step 2: System interface definition


If you have gathered the requirements and can identify the APIs exposed by the system, you are 50% done.


Define what APIs are expected from the system. This would not only establish the exact contract expected from the system but would also ensure if you haven't gotten any requirements wrong. Some examples for our Twitter-like service would be:


*postTweet**(user\_id, tweet\_text, image\_url, user\_location, timestamp, ...)\**generateTimeline**(user\_id, current\_time)\**recordUserTweetLike**(user\_id, tweet\_id, timestamp, ...)*


#### Step 3: Back-of-the-envelope capacity estimation


It's always a good idea to estimate the scale of the system you're going to design. This would also help later when you'll be focusing on scaling, partitioning, load balancing and caching.


1. What scale is expected from the system (e.g., number of new tweets, number of tweet views, how many timeline generations per sec., etc.)
2. How much storage would we need? This will depend on whether users can upload photos and videos in their tweets?
3. What network bandwidth usage are we expecting? This would be crucial in deciding how would we manage traffic and balance load between servers.


#### Step 4: Defining the data model


Defining the data model early will clarify how data will flow among different components of the system. Later, it will guide you towards better data partitioning and management. Candidate should be able to identify various entities of the system, how they will interact with each other and different aspect of data management like storage, transfer, encryption, etc. Here are some entities for our Twitter-like service:


User: UserID, Name, Email, DoB, CreationData, LastLogin, etc.\
Tweet: TweetID, Content, TweetLocation, NumberOfLikes, TimeStamp, etc.\
UserFollows: UserdID1, UserID2\
FavoriteTweets: UserID, TweetID, TimeStamp


Which database system should we use? Would NoSQL like Cassandra best fits our needs, or we should use MySQL-like solution. What kind of blob storage should we use to store photos and videos?


#### Step 5: High-level design


Draw a block diagram with 5--6 boxes representing core components of your system. You should identify enough components that are needed to solve the actual problem from end-to-end.


For Twitter, at a high level, we would need multiple application servers to serve all the read/write requests with load balancers in front of them for traffic distributions. If we're assuming that we'll have a lot more read traffic (as compared to write), we can decide to have separate servers for handling reads v.s writes. On the backend, we need an efficient database that can store all the tweets and can support a huge number of reads. We would also need a distributed file storage system for storing photos (and videos) and a search index and infrastructure to enable searching of tweets.


#### Step 6: Detailed design for selected components


Dig deeper into 2--3 components; interviewers feedback should always guide you towards which parts of the system she wants you to explain further. You should be able to provide different approaches, their pros and cons, and why would you choose one? Remember there is no single answer, the only thing important is to consider tradeoffs between different options while keeping system constraints in mind. e.g.


1. Since we'll be storing a huge amount of data, how should we partition our data to distribute it to multiple databases? Should we try to store all the data of a user on the same database? What issues can it cause?
2. How would we handle high-traffic users e.g. celebrities who have millions of followers?
3. Since user's timeline will contain the most recent (and relevant) tweets, should we try to store our data in a way that is optimized to scan latest tweets?
4. How much and at which layer should we introduce cache to speed things up?
5. What components need better load balancing?


#### Step 7: Identifying and resolving bottlenecks


Try to discuss as many bottlenecks as possible and different approaches to mitigate them.


1. Is there any single point of failure in our system? What are we doing to mitigate it?
2. Do we've enough replicas of the data so that if we lose a few servers, we can still serve our users?
3. Similarly, do we've enough copies of different services running, such that a few failures will not cause total system shutdown?
4. How are we monitoring the performance of our service? Do we get alerts whenever critical components fail or their performance degrades?


In short, due to the unstructured nature of software design interviews, candidates who are organized with a clear plan to attack the problem have better chances of success.


One again, if you are looking for resources to prepare for system design and programming interviews, take a look at:


1. [Grokking the System Design Interview](https://www.educative.io/collection/5668639101419520/5649050225344512)
2. [Coderust 3.0: Faster Coding Interview Preparation with Interactive Challenges & Visualizations](https://www.educative.io/collection/5642554087309312/5679846214598656)
3. [Data Structures for Coding Interviews](https://www.educative.io/d/data_structures)


Happy interviewing!


If you liked this post, click the 💚 sign and follow me for more posts. If you have any feedback, reach out to me on [Twitter](https://twitter.com/fahimulhaq).


*Fahim is the co-founder of*[*Educative*](https://www.educative.io/)*. We are building the next generation interactive learning platform for software engineers and instructors. Learners learn by going through interactive courses. Instructors can quickly create and publish interactive courses using our course builder. If you are interested in publishing courses or knowing more, feel free to reach out.*


