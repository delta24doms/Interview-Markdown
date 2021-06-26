# The complete guide to crack the System Design interview


## Template to answer any system design question & links to all the system design questions attached.


[


![Harshith](img/2-psghik6uojneenlrnia7fw-jpeg)


](<https://medium.com/@shrshthreddy?source=post_page-----ba118f48bdfc-------------------------------->)


[


Harshith


](<https://medium.com/@shrshthreddy?source=post_page-----ba118f48bdfc-------------------------------->)


[


Jun 27, 2020 - 6 min read 


](<https://towardsdatascience.com/the-complete-guide-to-the-system-design-interview-ba118f48bdfc?source=post_page-----ba118f48bdfc-------------------------------->)



![](img/1-pku6-kojaknbdkkza-lsdq-jpeg)


source: modern analyst


## The article consists of 3 parts --- A preparation guide, a System design template, and Design questions with links.


For my system design interview with Amazon, I watched video lectures, read blog posts, and discussed with my friends' various approaches to design a system. After my extensive preparation, I came up with a template that I followed during my interview and wanted to share and hoping it would help anyone preparing for a system design interview.


## Preparation


Firstly it is important to learn the fundamental concepts before designing a system. Knowing all the concepts helps you in making the right decisions while designing a system.


This curated Yo u Tube playlist covers all the required concepts to understand the steps in designing a system.


System design concepts playlist


(Optional) For more comprehensive concepts, refer to the below Github repo.


[


## donnemartin/system-design-primer


### Learn how to design large-scale systems. Prep for the system design interview. Learning how to design scalable systems...


github.com


](<https://github.com/donnemartin/system-design-primer/blob/master/README.md>)


After learning all the fundamental concepts, it is now time for designing. First of all, you have to think of a use case (example: Instagram) and try designing all the components. Mainly think about how can you make your system, fault-tolerant (system is up and running at all times), and Scalable (to handle a growing amount of traffic). Brainstorm how the bottlenecks can be resolved. This entire process helps you to apply the concepts you learned in designing a system. If you face any difficulties with the steps to design a system then refer to the design template provided below.



> My advice to you would be to use the system and explore all the features
> 
> 
> 


Questions to ask yourself


* What are the different architectural components that can be used?
* How do these components interact with each other?
* How can we best utilize these components: what are the right tradeoffs ?


*Tip **: The more questions you ask your interviewer the more inputs you'll receive from the interviewer and the better your design will be�*.



> Key points for the interview:\
> Don't use any buzz words (tech stack), Don't get into details prematurely, Justify your design decisions
> 
> 
> 


# System design template for interviews


## 1. Requirements


Functional


What functionalities can the system or application provider to the user? Example: In Twitter, a user can follow another user, tweet, like a tweet, retweet other's tweet, and share a tweet (focus on the essential features and do not delve into the complex features of twitters)


Non-functional


*Mandatory to know **CAP theorem�**:�*[*Blog*](https://mwhittaker.github.io/blog/an_illustrated_proof_of_the_cap_theorem/)


For any distributed system, the following are the fundamental concepts to consider:


* High availability: Most of the systems must be highly available.
* Consistency: The systems with high availability will have eventual consistency. Any banking system favors consistency over availability as there cannot be discrepancies in data (account balance).
* Reliability: No loss of user data.
* Latency: Response time of a user action such as loading a web page, liking a post, etc.


## 2. Storage estimation


* Based on the data modality : A rough estimate of how much data must be stored --- To know what type of database can be used and file storage for storing images/videos.
* The number of requests to the service --- To know how to scale the services. A service that is read-heavy can be scaled to handle high traffic of requests.
* Read Write ratio --- Determines whether the system is read-heavy or not.


## 3. Database design


After discussing the data and the actions that a user can perform to interact with the system. The next step would be to talk about which type of DB will you use and why. For detailed differences SQL Vs NoSQL --- [Read](https://www.scylladb.com/resources/nosql-vs-sql/#:~:text=Scylla%20is%20a%20column%2Doriented,dynamic%20schema%20for%20unstructured%20data.&text=It%20is%20similar%20to%20Structured,tables%2C%20by%20columns%20and%20rows.)


## 4. High-level system design


Initially start with a very basic design


![](img/1-equzbs0s7lphn-6-xeyaiw-jpeg)


![](img/1-equzbs0s7lphn-6-xeyaiw-jpeg)


Source: writer's diagrams


Extending the design --- Creating specific components


* Isolating the services --- for easier scaling and traffic control


![](img/1-lfkwwikoeyktcdhn37qdvq-jpeg)


![](img/1-lfkwwikoeyktcdhn37qdvq-jpeg)


Source: writer's diagrams


* Replicate the services and databases - mention about a single point of failure --- [Video](https://www.youtube.com/watch?v=-BOysyYErLY)
* Load balancer --- Application side & Database side if needed --- [Video�](https://www.youtube.com/watch?v=K0Ta65OqQkY&list=PLMCXHnjXnTnvo6alSjVkgxV-VH6EPyvoX&index=3), [Blog](https://www.educative.io/courses/grokking-the-system-design-interview/3jEwl04BL7Q)
* Message Queues --- Tight coupling to loose coupling / Synchronous to Asynchronous communication --- Read [Message queues�](https://aws.amazon.com/sqs/), [Benefits of MQ](https://aws.amazon.com/message-queue/benefits/)
* Data Partitioning --- Location-based, UserID based --- [Video�](https://www.youtube.com/watch?v=5faMjKuB9bc&list=PLMCXHnjXnTnvo6alSjVkgxV-VH6EPyvoX&index=7), [Blog](https://www.educative.io/courses/grokking-the-system-design-interview/mEN8lJXV1LA)
* Content Delivery network --- To avoid round trips to the main server (reduces latency). [Video�](https://www.youtube.com/watch?v=Bsq5cKkS33I), [InterviewQs](https://www.youtube.com/watch?v=dzzPP87zUq4)
* Cache --- Distributed cache and client-side cache (For faster read access) --- [Video�](https://www.youtube.com/watch?v=U3RkDLtS7uY), [Blog�](https://aws.amazon.com/caching/), [Primer](https://github.com/donnemartin/system-design-primer/blob/master/README.md#cache)


## 5. Additional components (optional)


These components can be added to the design if you have time left in the interview. Knowing about these components helps you answer any in-depth follow-up questions. Generally, the components mentioned above will suffice and also take most of your time in the interview.


* Encryption (msgs) --- for messaging services to secure data --- [Blog](https://blog.storagecraft.com/5-common-encryption-algorithms/)
* Analytics service --- for analyzing requests and user data
* ML service --- recommendation/ news feed ranking ( if use case (Netflix) demands then add it to the basic components) --- talk about the data needed for your recommendation/ranking model.
* API gateway --- [Video�](https://www.youtube.com/watch?v=TYw-lzL3-Kc), detailed microservices, and API gateway --- [Playlist](https://www.youtube.com/watch?v=5OMx4R9VT-0&list=PLkQkbY7JNJuDqCFncFdTzGm6cRYCF-kZO&index=5)
* Service discovery --- to dynamically identify microservices --- [Video](https://www.youtube.com/watch?v=6dpcU3fnSBE)


By following this template, any system can be designed in an interview.


Disclaimer : The video links provided below are a detailed design of a system and can be referred to for an in-depth design of a real system. The educative blog links are succinct and cover the usage of the design concepts for a particular system.


# Design Questions


## General services


* Tiny URL : [Video�](https://www.youtube.com/watch?v=JQDHz72OA3c), [Blog](https://www.educative.io/courses/grokking-the-system-design-interview/m2ygV4E81AR)
* PasteBin : [Video�](https://www.youtube.com/watch?v=josjRSBqEBI&list=PLkQkbY7JNJuBoTemzQfjym0sqbOHt5fnV&index=30), [Blog](https://www.educative.io/courses/grokking-the-system-design-interview/3jyvQ3pg6KO)
* Search service : [Video�](https://www.youtube.com/watch?v=CeGtqouT8eA), [Blog](https://www.educative.io/courses/grokking-the-system-design-interview/xV9mMjj74gE)
* Type-ahead suggestion service : [Video�](https://www.youtube.com/watch?v=xrYTjaK5QVM&list=PLkQkbY7JNJuBoTemzQfjym0sqbOHt5fnV&index=8), [Blog](https://www.educative.io/courses/grokking-the-system-design-interview/mE2XkgGRnmp)
* Web crawler : [Video�](https://www.youtube.com/watch?v=BKZxZwUgL3Y), [Blog](https://www.educative.io/courses/grokking-the-system-design-interview/NE5LpPrWrKv)
* API rate limiter : [Video�](https://www.youtube.com/watch?v=xrizarXJgC8), [Blog](https://www.educative.io/courses/grokking-the-system-design-interview/3jYKmrVAPGQ)


## Social media systems


* Instagram : [Video�](https://www.youtube.com/watch?v=QmX2NPkJTKg), [Blog](https://www.educative.io/courses/grokking-the-system-design-interview/m2yDVZnQ8lG)
* Twitter : [Video�](https://www.youtube.com/watch?v=wYk0xPP_P_8), [Blog](https://www.educative.io/courses/grokking-the-system-design-interview/m2G48X18NDO)
* Facebook news feed : [Blog](https://www.educative.io/courses/grokking-the-system-design-interview/gxpWJ3ZKYwl)


## Cloud services


* Google drive : [Video�](https://www.youtube.com/watch?v=U0xTu6E2CT8), [Blog](https://www.educative.io/courses/grokking-the-system-design-interview/m22Gymjp4mG)
* Google docs : [Video](https://www.youtube.com/watch?v=2auwirNBvGg)
* Amazon S3 : [Video](https://www.youtube.com/watch?v=UmWtcgC96X8)


## Video streaming


Video is the main data and different formats of a video have to be stored. Recommendation service is key here.


* Netflix : [Video�](https://www.youtube.com/watch?v=psQzyFfsUGU&list=PLkQkbY7JNJuBoTemzQfjym0sqbOHt5fnV&index=5), [Blog�](https://www.educative.io/courses/grokking-the-system-design-interview/xV26VjZ7yMl),
* How Netflix onboards new movies: [Video�](https://www.youtube.com/watch?v=x9Hrn0oNmJM).


Similar systems: YouTube, Prime Video.


## Online shopping


* Amazon : [Video](https://www.youtube.com/watch?v=EpASu_1dUdE)


Similar systems: Walmart, Airbnb, eBay


## Messaging system


The difference between HTTP, long pooling, and WebSockets is important to know for a messaging system --- [Video](https://www.youtube.com/watch?v=GMlHsF1JmsE&list=PLpQ0aTOL-X-FqEaLF-nCzVRxICMlVNmwi&index=19&t=0s)


* WhatsApp : [Video](https://www.youtube.com/watch?v=vvhC64hQZMk)


## Cab use cases


* Uber : [Video�](https://www.youtube.com/watch?v=umWABit-wbk), [Blog](https://www.educative.io/courses/grokking-the-system-design-interview/YQVkjp548NM)
* Similar systems: Lyft


## Video conferencing


* Zoom : [Video](https://www.youtube.com/watch?v=G32ThJakeHk)
* Similar systems: Skype, Google Meet


## Restaurants review system


* Yelp : [Video�](https://www.youtube.com/watch?v=TCP5iPy8xqo), [Blog](https://www.educative.io/courses/grokking-the-system-design-interview/B8rpM8E16LQ)


## Dating apps


* Tinder: [Video](https://www.youtube.com/watch?v=tndzLznxq40)


## Payment services


What is a payment gateway: [Video](https://www.youtube.com/watch?v=GUurzvS3DlY)


* PayPal


## Gaming


* Online multiplayer: Videos [part1�](https://www.youtube.com/watch?v=EU81tjgoKoI), [part2](https://www.youtube.com/watch?v=K3Z1PY2vr3Q)


## Management systems


* Ticket master : [Video�](https://www.youtube.com/watch?v=lBAwJgoO3Ek), [Blog](https://www.educative.io/courses/grokking-the-system-design-interview/YQyq6mBKq4n)


Similar systems: Library management system, Movie booking, Hotel booking, & Flight booking.


Google maps : [Video](https://www.youtube.com/watch?v=jk3yvVfNvds)


Conclusion: I've written this blog from my own understanding and after preparing for the system design interview. This blog is to help software engineers with their interview preparation by consolidating all the important resources related to System design.


