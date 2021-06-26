#### 1. Design TinyURL or bitly (a URL shortening service)
https://hackernoon.com/top-10-system-design-interview-questions-for-software-engineers-8561290f0444

![](img/1-0tusmwh9fu7vd3ekxp5h2w-png)


Given a (typically) long URL, how would how would you design service that would generate a shorter and unique alias for it.


Discuss things like:


* How to generate a unique ID for each URL?
* How would you generate unique IDs at scale (thousands of URL shortening requests coming every second)?
* How would your service handle redirects?
* How would you support custom short URLs?
* How to delete expired URLs etc?
* How to track click stats?


#### 2. Design YouTube, Netflix or Twitch (a global video streaming service)


![](img/1-yo4vob7hdfdhcj9hhlactg-png)


Videos mean that your service will be storing and transmitting petabytes and petabytes of data.You should discuss how to efficiently store and distribute data in away that a huge number of users can watch and share them simultaneously (e.g. imagine streaming the latest episode of a hit TV show like Games of Thrones).


In addition, discuss:


* How would you record stats about videos e.g the total number of views, up-votes/down-votes, etc.
* How would a user add comments on videos (in realtime).


#### 3. Design Facebook Messenger or WhatsApp (a global chat service)


![](img/1-yjghws5gzspmj4avaexfmq-png)


Interviewers are interested in knowing:


* How would you design one-on-one conversations between users?
* How would you extend your design to support group chats?
* What to do when the user is not connected to the internet?
* When to send push notifications?
* Can you provide end-to-end encryption. How?


#### 4. Designing Quora or Reddit or HackerNews (a social network + message board service)


![](img/1-zbb6mn3n4e4j4htm2itfzg-png)


Users of the services can post questions or share links. Other users can answer questions or comment on the shared links. The service should be able to:


* Records stats for each answer e.g. the total number of views, upvotes/downvotes, etc.
* Users should be able to follow other users or topics
* Their timeline will consist of top questions from all the users and topics they follow (similar to newsfeed generation).


#### 5. Design Dropbox or Google Drive or Google Photos (a global file storage & sharing service)


![](img/1-ya6zgbwwcmlm-yxet8ukka-png)


Discuss things like:


* How would users be able to upload/view/search/share files or photos?
* How would you track persmissions for file sharing
* How would you allow multiple users to edit the same document


#### 6. Design Facebook, Twitter or Instagram (a social media service with hundreds of millions of users)


![](img/1-unzejgq6inp3tntpzrgx-q-png)


When designing a social medial service with hundreds of million (or billions of users), interviewers are interested in knowing how would you design the following components


* Efficient storage and search for posts or tweets.
* Newsfeed generation
* Social Graph (who befriends whom or who follows whom --- specially when millions of users are following a celebrity)


A lot of times, interviewers spend the whole interview discussing the design of the newsfeed.


#### 7. Design Uber or Lyft (a ride sharing service)


![](img/1-nabu7nflkrsuwxwu5nmqrw-png)


While designing a ride-sharing service, discuss things like:


* The most critical use case --- when a customer requests a ride and how to efficiently match them with the nearby drivers?
* How to store millions of geographical locations for drivers and riders who are always moving.
* How to handle updates to driver/rider locations (millions of updates every second)?


#### 8. Design a Web Crawler or Type-Ahead (search engine related services)


![](img/1-gehhemz6b2xr3kzpfzrrka-png)


For Type-Ahead, as the user types in their query, you need to design a service which would suggest top 10 searched terms starting with whatever the user has typed. Discuss things like:


* How to store previous search queries?
* How to keep the data fresh?
* How to find the best matches to the already typed string?
* How to handle updates and the user is typing too fast?


For Web Crawler, we have to design a scalable service that can crawl the entire Web, and can fetch hundreds of millions of Web documents. Discuss things like:


* How to find new web pages?
* How to prioritize web pages that change dynamically?
* How to ensure that your crawler is not infinitely stuck on the same domain?


#### 9. Design an API Rate Limiter (e.g. for Firebase or Github)


![](img/1-tqgqqzhbv0qfi0bwkpuflq-png)


You are expected to develop a Rate Limiter services that can:


* Limit the number of requests an entity can send to an API within a time window e.g., 15 requests per second.
* The rate limiting should work for a distributed setup, as the APIs are accessible through a cluster of servers.
* How would you handle throttling (soft and hard throttling etc.).


#### 10. Design Yelp or Nearby Places/Friends (a proximity server)


![](img/1-bkfacfpwmy3kvmygd8r5sg-png)


This service would need to store locations for millions of people/places. Discuss things like:


* How would the users of the service be able to search nearby friends or places
* How to rank places (based on the distance, user reviews).
* How to efficiently store location data according to the population density (e.g. a block in New York City might have more places/people than a small city).


### Software engineer Interview Preparation Resources


![](img/1-8in8p6ymf0e5cidv53bvra-png)


Following are some resources that can help you prepare for software engineering interviews.


1. System Design Interviews: [Grokking the System Design Interview](https://www.educative.io/collection/5668639101419520/5649050225344512).
2. Coding Interviews: [Coderust 3.0: Faster Coding Interview Preparation using Interactive Visualizations](https://www.educative.io/collection/5642554087309312/5679846214598656).
3. Data Structures: [Data Structures for Coding Interviews](https://www.educative.io/d/data_structures).


Happy interviewing!


If you found this post helpful, please click the 👏 sign and follow me for more posts. If you have any feedback, reach out to me on [Twitter](https://twitter.com/fahimulhaq).


*Fahim is the co-founder of*[*Educative*](https://www.educative.io/)*. We are building the next generation interactive learning platform for software engineers and instructors. Learners learn by going through interactive courses. Instructors can quickly create and publish interactive courses using our course builder. If you are interested in publishing courses or knowing more, feel free to reach out.*


* *All product names, logos, and brands are property of their respective owners.*


