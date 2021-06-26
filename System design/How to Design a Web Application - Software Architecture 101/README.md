# How to Design a Web Application: Software Architecture 101


## Make the right decisions early in a project


[


![The Educative Team](img/2-sbwiz06-xw2lyq2srihw2q-png)


](<https://educative-inc.medium.com/?source=post_page-----df568b88da76-------------------------------->)


[The Educative Team](https://educative-inc.medium.com/?source=post_page-----df568b88da76--------------------------------)


[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F163aa84775f6&operation=register&redirect=https%3A%2F%2Fbetterprogramming.pub%2Fhow-to-design-a-web-application-software-architecture-101-df568b88da76&user=The%20Educative%20Team&userId=163aa84775f6&source=post_page-163aa84775f6----df568b88da76---------------------follow_byline-----------)


[Feb 6, 2020Â](https://betterprogramming.pub/how-to-design-a-web-application-software-architecture-101-df568b88da76?source=post_page-----df568b88da76--------------------------------)-Â 14Â min readÂ 



![](img/1-bqe960y3lak8ov671b-dpq-png)


So you've embarked on the entrepreneurial journey and you've decided to build your own web application. You have an idea but now it's crucial you get the architecture right.


In this post we'll walk through these key areas:


* What is software architecture?
* Why is software architecture important?
* The difference between software architecture and software design.
* Software architecture patterns.
* How to decide on the number of tiers your app should have.
* Horizontal or vertical scaling --- which is right for your app?
* Monolith or microservice?
* When should you use NoSQL or SQL?
* Picking the right technology for the job.
* How to become a software architect.
* Where to go from here.


Our goal is to give you a solid understanding of web architecture, the concepts involved, and how to pick the right architecture and technology when you design your app. By the end of this piece, you won't be sitting in the dark when you have to design an application from bare-bones.


If you're looking for a complete course on web application and software architecture, we recommend checking outÂ [Web Application and Software Architecture 101Â](https://www.educative.io/courses/web-application-software-architecture-101). This is a useful course for anyone looking to strengthen their overall knowledge of software architecture.


Let's dive in!


# What is Software Architecture?


The software architecture of a system describes its major components, their relationships, and how they interact with each other.


Essentially, it serves as a blueprint. It provides an abstraction to manage the system complexity; it establishes communication and coordination among components.


![](img/1-4zjv2tce9lkhepjwx6mcjq-jpeg)


Some key points:


* The architecture helps define a solution to meet all the technical and operational requirements, with the common goal of optimizing for performance and security.
* Designing the architecture involves the intersection of the organization's needs and the needs of the development team. Each decision can have a considerable impact on quality, maintainability, performance, etc.


One of my favorite definitions of software architecture is that of Ralph Johnson, co-author ofÂ *Design Patterns: Elements of Reusable Object-Oriented Software:*



> It's the decisions you wish you could get right early in a project.
> 
> 
> 


# Why is Software Architecture Important?


Constructing a building or making a pizza --- to successfully create anything, you need to get the base right. If you don't get the base right and something goes wrong, you just have to start over --- there's no way around it.


Building a web application is no different. The architecture is the base. It should be carefully thought out to avoid major design changes and code refactoring later.


Many engineers will tell you that: You don't want to have to re-design stuff. It eats up your time like a black hole. It has the potential to push your shipping date by months, if not longer.Â And that's not even counting the waste of engineering and financial resources.


Hasty decisions taken during the initial design phases can cause an impasse at any stage in the development process. So, before we even get our hands dirty with the code, we must make the underlying architecture right.


Software development is an iterative and evolutionary process --- we don't always get things perfect first go. But this is no excuse for not doing our homework.


# The Difference Between Software Architecture and Software Design


There's often confusion between software design and architecture. Let's break this down.


Software architecture is used to define the skeleton and the high-level components of a system and how they will all work together. For example, do you need a serverless architecture that splits the application into two components: BaaS (backend-as-a-service) and FaaS (functions-as-a-service)? Or do you need something like a microservice architecture where the different features/tasks are split into separate respective modules/codebases?


Choosing an architecture will determine how you deal with performance, fault tolerance, scalability, and reliability.


Software design is responsible for the code-level design --- what each module is doing, the classes scope, and the functions, purposes, etc. When used strategically, they can make a programmer more efficient, giving them methods that have already been refined by others, so they don't have to keep reinventing the wheel.


Also, when discussing with others or managing code in larger teams, they provide a useful common language to conceptualize repeated problems and solutions. Start leveraging software design patterns in your code with this helpful course:Â [Software Design Patterns: Best Practices for Software DevelopersÂ](https://www.educative.io/courses/software-design-patterns-best-practices).


Here's a good article on the importance of software design and tried and true patterns developers frequently use:Â [The 7 most important software design patternsÂ](https://www.educative.io/blog/the-7-most-important-software-design-patterns).


# Software Architecture Patterns


## Client-server


The architecture works on a request-response model. The client sends the request to the server for information and the server responds to it.


Every website you browse, whether it's a Wordpress blog, a web application like Facebook or Twitter, or your banking app, is built on the client-server architecture.


![](img/1-ui4ie7kasqdqeyetmrgeiw-jpeg)


![](img/1-ui4ie7kasqdqeyetmrgeiw-jpeg)


## Peer-to-peer


A P2P network is a network in which computers, also known as nodes, can communicate with each other without the need for a central server. The absence of a central server rules out the possibility of a single point of failure. All the computers in the network have equal rights. A node acts as a seeder and a leecher at the same time. So, even if some of the computers/nodes go down, the network & the communication is still up.


P2P is the base of blockchain technology.


![](img/1-ooemognlhvclz84nl8qhca-jpeg)


![](img/1-ooemognlhvclz84nl8qhca-jpeg)


## Model-View-Controller (MVC)


The MVC architecture is a software architectural pattern in which the application logic is divided into three components on the basis of functionality. These components are called:


* Models --- represent how data is stored in the database.
* Views --- the components that are visible to the user, such as an output or a GUI.
* Controllers --- the components that act as an interface between models and views.


The MVC architecture is used not only for desktop applications but also for mobile and web applications.


![](img/1-llvlumiuxqiad3btpzuc6g-png)


![](img/1-llvlumiuxqiad3btpzuc6g-png)


## Microservices


In a microservice architecture, different features/tasks are split into separate respective modules/codebases, which work in conjunction with each to form a whole large service.


This architecture facilitates easier and cleaner app maintenance, feature development, testing, and deployment compared to a monolithic architecture.


![](img/1-cpuarmtr8aqdb3nqzf0azw-jpeg)


![](img/1-cpuarmtr8aqdb3nqzf0azw-jpeg)


## Event-driven


Non-blocking architecture is also known as reactive or event-driven architecture. Event-driven architectures are pretty popular in the modern web application development.


They're capable of handling a big number of concurrent connections with minimal resource consumption. Modern applications need a fully asynchronous model to scale. These modern web frameworks provide more reliable behaviour in a distributed environment.


![](img/1-tgvffodrjamhnoda81llyg-jpeg)


![](img/1-tgvffodrjamhnoda81llyg-jpeg)


## Layered


This pattern can be used to structure programs that can be decomposed into groups of subtasks, each of which is at a particular level of abstraction. Each layer provides services to the next higher layer.


The most common layers are:


* Presentation layer
* Application layer
* Business logic layer
* Data access layer


## Hexagonal


The architecture consists of three components:


* Ports
* Adapters
* Domain


The focus of this architecture is to make different components of the application independent, loosely coupled and easy to test.


The architectural pattern holds the domain at its core --- that's the business logic. On the outside, the outer layer has ports and adapters. Ports act like an API, as an interface. All the input to the app goes through the interface.


![](img/1-cpgp9tjzxo2uxzqee3agca-jpeg)


![](img/1-cpgp9tjzxo2uxzqee3agca-jpeg)


# How Many Tiers Should Your App Have?


## Single tier application


Pros:


* No network latency.
* Data is quickly and easily available
* Data is not transferred over a network, ensuring data safety.


Cons:


* Little control over the application --- difficult to implement new features or code changes once it's shipped.
* Testing has to be extremely thorough with minimal room for mistakes.
* Single tier applications are vulnerable to being tweaked or reverse engineered.


## Two-tier application


Pros:


* Fewer network calls since the code and UI are in the same machine
* Database server and business logic are physically close, offering higher performance.


Cons:


* Since the client holds most of the application logic, problems arise in controlling the software version and re-distributing new versions.
* Lacks scalability as it supports only a limited number of users. When multiple client requests increases, application performance can slow down due to the fact that clients necessitate separate connections and CPU memory to proceed.
* Since the application logic is coupled with the client, it's difficult to re-use logic.


## Three-tier application


Pros:


* Data corruption through client applications can be eliminated as the data passed in the middle tier for database updations ensures its validity.
* The placement of the business logic on a centralized server makes the data more secure.
* Due to the distributed deployment of application servers, scalability of the system is enhanced since a separate connection from each client is not required whereas connections from a few application servers are sufficient.


Cons:


* Usually, more effort should be enforced when creating three-tier applications as the communication points are increased (client to middle tier to server, instead of directly from client to server) and the performance increased by tools like Visual Basic, PowerBuilder, Delphi will be reduced.


## N-Tier application


Pros:


* All the pros of three-tier architecture.
* The performance is increased due to off-load from the database tier and the client tier, enabling it to suit medium to high volume industries.


Cons:


* Due to the componentization of the tiers, the complex structure is difficult to implement or maintain.


## Conclusion


* You should choose a single-tier architecture when you do not want any network latency.
* Choose a two-tier application when you need to minimize network latency and you need more control of data within your application.
* You should choose a three-tier architecture when you need control over the code/business logic of your application, you want it to be secure, and you need control over data in your application.
* You should choose a N tier architecture when you need your application to scale and handle large amounts of data.


# Horizontal or Vertical Scaling --- Which is Right For Your App?


If your app is a utility or tool which is expected to receive minimal consistent traffic --- say, an internal tool in an organization --- you probably don't need to host it in a distributed environment. A single server is enough to manage the traffic and you know that theÂ *traffic load will not significantly increaseÂ*. In that case,Â go with vertical scalingÂ .


![](img/1-xatitzifinq3qmuejyvgzq-jpeg)


![](img/1-xatitzifinq3qmuejyvgzq-jpeg)


But if your app is a public-facing social app like a social network, a fitness app or something similar, then traffic is expected to spike exponentially in the near future. In this case, both high availability and horizontal scalability are important to you.


![](img/1-1mc-tea6squcvc4iqkcu6a-jpeg)


![](img/1-1mc-tea6squcvc4iqkcu6a-jpeg)


Build to deploy it on the cloud and always have horizontal scalability in mind from the start.Â [Here's a good website for learning more about scalabilityÂ](http://highscalability.com/).


# Monolith or Microservice?


Let's explore when you should choose one over the other.


![](img/1-uywvkwxpxytum1qywfcpjw-png)


## When to use monolithic architecture


Monolithic applications fit best when requirements are simple and the app is expected to handle a limited amount of traffic. For example, an internal tax calculation app for an organization, or a similar open public tool.


These are the use cases where the business is certain that thereÂ *won'tÂ*be exponential growth in the user base and traffic over time.


There are also instances where the dev teams decide to start with a monolithic architecture and later scale out to a distributed microservices architecture.


This helps them deal with the complexity of the application step-by-step, as and when required.Â [This is exactly what LinkedIn didÂ](https://engineering.linkedin.com/architecture/brief-history-scaling-linkedin).


## When to use microservice architecture


The microservice architecture fits best for complex use cases and for apps which expect traffic to increase exponentially in future, like a fancy social network application.


A typical social networking application has various components, like messaging, real-time chat, live video streaming, image uploads, liking and sharing features, etc. In this case, develop each component separately, keeping theÂ single responsibilityÂ andÂ separation of concernsÂ principles in mind.


Every feature written into a single codebase would take no time to become a mess.


Now, we have gone through three approaches to monolithic and microservices:


* Picking a monolithic architecture.
* Picking a microservice architecture.
* Starting with a monolithic architecture and then later scaling out into a microservice architecture.


Picking a monolithic or a microservice architecture largely depends on our use case. I suggest that you keep things simple and have a thorough understanding of the requirements. Get the lay of the land, build something only when you need it, and keep evolving the code iteratively. That's the right way to go.


# When Should You Use NoSQL or SQL?


## When to pick a SQL database?


If you are writing a stock trading, banking or a finance-based app, or you need to store a lot of relationships, for instance, when writing a social networking app like Facebook, then you should pick a relational database. Here's why:


## Transactions and Data Consistency


If you're writing software that has anything to do with money or numbers, that makes transactions, or has to comply with the ACID --- data consistency is incredibly important to you. Relational DBs shine when it comes to transactions and data consistency --- they comply with the ACID rule, have been around for ages and are battle-tested.


## Storing Relationships


If your data has a lot of relationships like which friends of yours live in a particular city? Which of your friend already ate at the restaurant you plan to visit today? etc. There is nothing better than a relational database for storing this kind of data.


Relational databases are built to store relationships. They have been tried & tested & are used by big guns in the industry like Facebook as the main user-facing database.


Popular relational databases


* MySQL
* Microsoft SQL Server
* PostgreSQL
* MariaDB


## When to pick a NoSQL database


There are a few reasons why you'd want to pick a NoSQL database.


## Handling a large number of read-write operations


Look towards NoSQL databases when you need to scale fast. For example, when there are a large number of read-write operations on your website and when dealing with a large amount of data, NoSQL databases fit best in these scenarios. Since they have the ability to add nodes on the fly, they can handle more concurrent traffic and large amounts of data with minimal latency.


## Running data analytics


NoSQL databases also fit best for data analytics use cases, where we have to deal with an influx of massive amounts of data.


## Popular NoSQL databases


* MongoDB
* Redis
* Cassandra
* HBASE


If you're curious about trying a NoSQL database like MongoDB, I highly suggest checking out Nikola Zivkovic's course,Â [The Definitive Guide to MongoDBÂ](https://www.educative.io/courses/definitive-guide-to-mongodb).


# Picking the Right Technology For the Job


## Real-time data interaction


If you're building an app that needs:


* To interact with the backend server in real-time, such as a messaging application, or an audio-video streaming app like Spotify, Netflix, etc.
* A persistent connection between the client and server, and a non-blocking technology on the back end.


Then some of the popular technologies which enable you to write these apps are NodeJS and the popular Python framework known asÂ [TornadoÂ](https://pypi.org/project/tornado/3.2.1/). If you're working in the Java Ecosystem you can look into Spring Reactor, Play, andÂ [Akka.ioÂ](https://akka.io/).


## Peer-to-peer web application


If you intend to build a peer to peer web app, for instance, a P2P distributed search engine or a P2P Live TV radio service --- something similar to LiveStation by Microsoft perhaps --- then you'll want to look into JavaScript protocols like DAT and IPFS. Check outÂ [FreedomJSÂ](https://www.freedomjs.org/), a framework for building P2P web apps that work in modern web browsers.


## CRUD-based regular application


If you have simple use cases such as a regular CRUD-based app, some of the technologies you can use are: Spring MVC, Python Django, Ruby on Rails, PHP Laravel, and ASP .NET MVC.


## Simple, small scale applications


If you intend to write an app that doesn't involve much complexity, like a blog, a simple online form, or simple apps that integrate with social media that and within the IFrame of the portal, use PHP.Â [Learn PHP for freeÂ](https://www.educative.io/courses/learn-php-from-scratch)today.


You may also consider other web frameworks like Spring boot, Ruby on Rails, which cut down the verbosity, configuration, development time by notches & facilitate rapid development. But PHP hosting will cost much less in comparison to hosting other technologies. It is ideal for very simple use cases.


## CPU and memory-intensive applications


Do you need to run CPU-intensive, memory-intensive, heavy computational tasks on the back end? Do you need to do big data processing, parallel processing, or running monitoring and analytics on large amounts of data?


Regular web frameworks and scripting languages aren't meant for number crunching. The tech commonly used in the industry to write performant, scalable, distributed systems is C++. It has features that facilitate low-level memory manipulation, providing more control over memory to the developers when writing distributed systems. The majority of cryptocurrencies are written using this language. This is aÂ [great courseÂ](https://www.educative.io/courses/learn-cpp-from-scratch)for learning C++ for free.


RustÂ is a programming language similar to C++. It is built for high performance and safe concurrency. It's been gaining in popularity lately amongst developers. Java, Scala, and Erlang are also good picks. Most large scale enterprise systems are written in Java.


GoÂ is a programming language by Google for writing apps for multi-core machines and handling a large amount of data.Â [Here's how you get started with Go developmentÂ](https://www.educative.io/courses/introduction-to-programming-in-go).


JuliaÂ is a dynamically programmed language built for high performance & running computations & numerical analytics.


LearnÂ [C++Â](https://www.educative.io/courses/learn-cpp-from-scratch),Â [RustÂ](https://www.educative.io/courses/learn-rust-from-scratch),Â [ScalaÂ](https://www.educative.io/courses/learn-scala-from-scratch), andÂ [JavaÂ](https://www.educative.io/courses/learn-java-from-scratch)for free today.


# How to Become a Software Architect


If this all sounds interesting, then you may aspire to be a software architect. But where do you start? Well, it's uncommon for anyone to start out as a software architect, so most software engineers work for a few years before they take on designing architecture.


One of the best ways to become familiar with software architecture is by designing your own web applications. This will force you to think through all the different aspects of your application --- from load balancing, message queueing, stream processing, caching and more. Once you start to understand how these concepts fit into your app, you'll be well on your way to becoming a software architect.


As an aspiring software architect, you need to constantly expand your knowledge and stay on top of the latest industry trends. You may start by learning one or more programming languages, work as a software developer, and gradually make your way.


Even though you can't get a software architect degree in college, there are other courses that you may find useful.Â [Web Application and Software Architecture 101Â](https://www.educative.io/courses/web-application-software-architecture-101)is a great place to start learning the best practices for designing and implementing web applications.


# Where to Go From Here


We've covered a lot in this piece, but we've only touched the surface of this topic. We have yet to explore REST APIs, high availability, and CAP theorem.


If you'd like a deep dive into software architecture, I highly recommendÂ [Web Application and Software Architecture 101Â](https://www.educative.io/courses/web-application-software-architecture-101). It walks you through different components and concepts involved when designing the architecture of a web application.


You'll learn about various architectural styles such as the client-server, peer-to-peer decentralized architecture, microservices, the fundamentals of data flow in a web application, different layers involved, concepts like scalability, high availability, and much more.


Additionally, you'll go through the techniques of picking the right architecture and the technology stack to implement your use case. I'll walk you through different use cases which will help you gain an insight into what technology and architecture are best for certain use cases when writing a web application. You'll come to understand the technology trade-offs involved.


If you're a beginner just starting your career in software development, this course will help you a lot. It will also help you with the software engineering interviews, especially for the full-stack developer positions.


Happy learning!


