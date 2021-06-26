# System Design Basics: Getting started with Load Balancer


## How popular sites handle huge number of requests


[


![Ashis Chakraborty](img/2-5a3odirjiyp4modhve2syg-jpeg)


](<https://ashchk.medium.com/?source=post_page-----adc4f602d08f-------------------------------->)


[Ashis Chakraborty](https://ashchk.medium.com/?source=post_page-----adc4f602d08f--------------------------------)


[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F577e2119c7f2&operation=register&redirect=https%3A%2F%2Fcodeburst.io%2Fsystem-design-basics-load-balancer-101-adc4f602d08f&user=Ashis%20Chakraborty&userId=577e2119c7f2&source=post_page-577e2119c7f2----adc4f602d08f---------------------follow_byline-----------)


[Nov 6, 2020�](https://codeburst.io/system-design-basics-load-balancer-101-adc4f602d08f?source=post_page-----adc4f602d08f--------------------------------)- 7 min read 



![](img/0-yiuede-yxaggc-bo)


Photo by [JOSHUA COLEMAN�](https://unsplash.com/@joshstyle?utm_source=medium&utm_medium=referral)on [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)


System design is one of the most important concepts of software engineering. When I started my associate architecture course, I had a hard time understanding how you design a system. One of the main problems was that the terminology used in the system design resources is hard to understand at first.


This article examines an important topic of system design, the Load Balancer. You may know about its characteristics and techniques of server selection here. Familiarizing yourself with the basic concepts and terminologies of system design would greatly help in designing a system.


# Load Balancer


A load balancer is a vital component of any distributed system. It helps to distribute the client requests within a cluster of servers to improve the responsiveness and availability of applications or websites.



> According to Wikipedia, " Load balancing refers to the process of distributing a set of tasks over a set of resources. "
> 
> 
> 


![](img/1-ykczh0ij9xf8ogt7zpzj5a-jpeg)


![](img/1-ykczh0ij9xf8ogt7zpzj5a-jpeg)


Image By [Author](https://medium.com/@ashchk)


For example, if one server can not serve a lot of requests at the same time, we need a load balancer. Its primary purpose is to optimize the response time of each task. Now let's assume a system has one server that is overloaded with the request of clients. The server has a limit of serving requests per second. So, we need to add more servers to handle large amounts of requests. But we may need a load balancer to balance the loads between the servers.


*The load balancer is a server that usually sits between client devices and a set of servers and distributes client requests across servers.�*Load balancers can be placed in various places of a system. The loads on the servers need to be distributed in a balanced way; that's why they are called a load balancer.


![](img/1-lsjnjmaqp69sftrly5luha-jpeg)


Figure 1: Add a Load balancer to distribute client requests to multiple servers(Image By [Author�](https://medium.com/@ashchk))


So, we may say that load balancing is the process of distributing client requests across multiple resources. If a server is not available to deal with new requests or is not responding, LB will stop sending requests to such a server.


As we already know, the load balancer prevents server overloads. Another essential task of load balancers is to carry out continuous health checks on servers to ensure they can handle requests. It ensures better use of system resources by balancing user requests. In system design, horizontal scaling is a common strategy to scale our system in case of a large number of users. A load balancer is a solution for horizontal scaling. Through balancing the incoming traffic of a system, an LB prevents a server from becoming overloaded. It also ensures better overall throughput of the system. Latencies should occur less often as requests are not blocked, and users don't need to wait for their requests to be processed.


Load balancers can be of two types of hardware LB and software LB. In this article, we are focused on the software load balancers.


## Where do we use a Load balancer?


Typically, we can put a load balancer between the client and the server to handle incoming network requests. Another very normal use of an LB is for distributing the network traffic across backend servers. A load balancer is used to reduce individual server load. And it prevents a single point of failure for any server. So, it improves the overall availability and responsiveness of the system. We may add LBs at various places in the system. Especially where we have multiple resources like servers or database or cache.


## Why do we use Load Balancing:


For any system design components, it's paramount that we know why and when to use a component. Load balancing is a vital component in case of availability and overall throughput of the system. Here is some example of load-balancing usage:


* When we design a system, one of its primary concerns creates a faster user experience and uninterrupted service. User requests should not wait for a single server that has not finished its previous task. In that case, client requests are immediately distributed to a responsive available server. That's when we need to use a load balancer; to balance out the tasks between multiple resources. Figure 1 is such an example:
* Availability is a key characteristic of a distributed system. In case of a full server failure scenario, this won't affect the user experience as the load balancer will simply send the client request to a healthy server.
* We can use predictive analytics in a load balancer to determine traffic bottlenecks before they happen. It can help in making business decisions.
* Instead of a single resource performing a lot of work, load balancing ensures that several devices perform a bearable amount of work.
* Another task of a load balancer is to defend the system from distributed denial-of-service (DDoS) attacks. Software load balancers can provide efficient and cost-effective protection from the DoS attack.


## Server selection:


We know a load balancer chooses a backend server out of multiple servers. How does it choose the server? There are two main factors that a load balancer considers before forwarding a client request to a server:


1. First, load balancers need to ensure that the chosen server is responsive; meaning that it is responding to its requests.
2. Secondly, the LBs use a pre-configured algorithm to select one from the set of responsive healthy servers.


*Health check:�*Load balancers need to forward traffic to healthy or responsive backend servers. To monitor the health, LBs constantly try to connect to backend servers to ensure that servers are listening. If a server fails to pingback in case of a health check, it is removed from the pool, and requests will not be forwarded to it until it is responsive again.


![](img/1-kbnngtn3z2yajwbt6opghw-jpeg)


Figure: Health check by the Load balancer (Image By [Author�](https://medium.com/@ashchk))


## Load Balancing Techniques:


There are various types of load balancing methods. Every type uses different algorithms for different purposes. These techniques are actually different types of strategy for server-selection. Here is a list of load balancing techniques:


* Random selection: In this method, the servers are selected randomly. There are no other factors calculated in the selection of the server. There might be a problem with some of the servers sitting idle, and some are overloaded with requests in this technique.
* Round Robin: This is one of the most common load balancing methods. It's a method where the LB redirects incoming traffic between a set of servers in a certain order. Check figure 2; there is a list of five servers; the first request goes to server 1, the second one goes to server 2, and so on. When LB reaches the end of the list, it starts over at the beginning, from server number 1 again. It almost evenly balances the traffic between the servers. But in this method, server specifications are not considered. The servers need to be of equal specification for this method to be useful. Otherwise, a low processing powered server may have the same load as a high processing capacity server.


![](img/1-fvu6kfrr4zacsketsv9o-g-jpeg)


Figure 2: Round Robin Method for load balancing (Image By [Author�](https://medium.com/@ashchk))


* Weighted Round Robin Method: This is the updated version of the previously described round-robin method. It's a bit more complex than the previous one. This method is designed to handle servers with different characteristics, which was a problem in the normal round-robin. A weight is assigned to each server. This weight can be an integer value that varies according to the processing power of the server. Higher processing servers get more connections to utilize their more powerful resources. So, here the traffic redirection depends on the processing power of the server.
* Least Connection: Here, the load balancer sends traffic to the server with the fewest active connections at the time when the client request is received. If the servers are busy in long computations, and the connections between client and server stay alive for a larger period of time, this approach is useful.
* Least Response Time: This algorithm sends the client requests to the server with the least active connections and the lowest response time (average). The backend server that responds the fastest receives the next request.
* Source IP Hashing: In this method, a hash of the client's IP address is generated which is used to select a server for a client. Even if the connection is broken, the client's next request will still go to the same server. So, this method can be used in a situation where clients need to be connected to a session that is still active after its disconnection. It can maximize our cache hits and improve performance.


## Conclusion:


The load balancer's task is to distribute [incoming client�](https://towardsdatascience.com/system-design-basics-getting-started-with-the-client-server-architecture-b02f9c9daae8?sk=d186470a4df5355b9f405010e8c4150e)traffic across multiple backend servers. Load balancing decreases wait time for users. When we are scaling a system, in the case of horizontal scaling, it is a crucial component. The more servers we add or remove, having a load balancer helps to maintain the change. When a new server is added or a server is removed from the server's pool, the load balancer needs to be updated; otherwise, it might be a waste of resources, or some requests might not be handled. While designing a system, we need to choose the server selection strategy according to the system's needs.



> Resource: Grokking the System Design Interview, [Load balancing techniques](https://kemptechnologies.com/load-balancer/load-balancing-algorithms-techniques/)
> 
> 
> This article is part of a series of system design for beginners. Here is a list of articles.
> 
> 
> 


