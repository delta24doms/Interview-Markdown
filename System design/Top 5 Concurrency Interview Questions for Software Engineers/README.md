https://hackernoon.com/top-5-concurrency-interview-questions-for-software-engineers-x48i30qu
*(Some background: I've interviewed hundreds of candidates for software engineering jobs at Facebook and Microsoft. I've also failed several coding interviews myself when I wasn't prepared.)*


Concurrency and multithreading are some of the most advanced topics brought up in interviews, but a strong foundation in them can put interviewees at a considerable advantage over their peers. In short, these skills are a major plus for software engineers. They give interviewers an idea about the following:


* Whether the candidate has the ability to build performant programs


* Whether the candidate has the ability to efficiently utilize resources


* Whether the candidate displays expertise and technical depth




*If you are looking for a complete course on concurrency for interviews,*[*C.H. Afzal*](https://www.educative.io/profile/view/5307417243942912?ref=hackernoon.com)*, a Silicon Valley veteran and concurrency expert, has created courses in*[*Python*](https://www.educative.io/courses/python-concurrency-for-senior-engineering-interviews?ref=hackernoon.com)*,*[*Java*](https://www.educative.io/courses/java-multithreading-for-senior-engineering-interviews?ref=hackernoon.com)*,*[*C#*](https://www.educative.io/courses/c-sharp-concurrency-for-senior-engineering-interviews?ref=hackernoon.com)*, and*[*Ruby*](https://www.educative.io/courses/ruby-concurrency-for-senior-engineering-interviews?ref=hackernoon.com)*.*


Concurrency interviews are essential if you want to succeed as a software engineer, but plenty of engineers dread concurrency interview questions (including myself when I was interviewing!). There are a few main reasons for this:


* Concurrency is a very complicated topic, where many junior developers and even senior developers haven't had the chance to implement concurrent programs.


* The number of abstractions can be confusing. Choosing the right abstraction is difficult.


* The important lessons of encapsulation, separation of concerns, loose coupling, etc. all apply.


* Most of what was taught in introductory multithreading materials is technically correct but doesn't translate to the problems at hand.




*The good news is that at*[*Educative*](https://www.educative.io/?ref=hackernoon.com)*, we've talked to hundreds of candidates, and teamed up with C.H. Afzal, who's interviewed at some of the top tech companies in the world including: Microsoft, Netflix, Cloudera, and Oracle, to tackle some of the most common interview problems in detail.*


In addition to covering some of the most popular concurrency interview questions asked at top companies, I'll also provide some definitions to key terms, concurrency best practices, tips to solve the problem, and common pitfalls developers face when solving these problems.


# Concurrency Terminology: defining key terms


## Thread


A thread is the smallest unit of execution in a process that simply executes instructions serially. A process can have multiple threads running as part of it. Usually, there would be some state associated with the process that is shared among all the threads and in turn, each thread would have some state private to itself.


The globally shared state amongst the threads of a process is visible and accessible to all the threads, and special attention needs to be paid when any thread tries to read or write to this global shared state.





## Critical section


Critical section is any piece of code that has the possibility of being executed concurrently by more than one thread of the application and exposes any shared data or resources used by the application for access.


![image](img/image)


*You can think of the critical section as a bridge that can handle one car (i.e. thread) at a time*


## Mutex


Mutex as the name hints implies mutual exclusion. A mutex is used to guard shared data such as a linked-list, an array, or any primitive type. A mutex allows only a single thread to access a resource or critical section.


Once a thread acquires a mutex, all other threads attempting to acquire the same mutex are blocked until the first thread releases the mutex. Once released, most implementations arbitrarily (based on some heuristics) chose one of the waiting threads to acquire the mutex and make progress.


![image](img/image)


*The example in this illustration represents a mutex as a store fitting room stating one customer (i.e. thread) at a time*


## Semaphore


Semaphore, on the other hand, is used for limiting access to a collection of resources. Think of semaphore as having a limited number of permits to give out. If a semaphore has given out all the permits it has, then any new thread that comes along requesting a permit will be blocked till an earlier thread with a permit returns it to the semaphore.


Semaphores can also be used for signaling among threads. This is an important distinction as it allows threads to work towards completing a task cooperatively.


![image](img/image)


*The example here is a queue outside the Apple store stating only 50 customers can be in the store at a time*


# Best practices for concurrent programming


## Minimize data sharing of mutable data


You should minimize data sharing of mutable data for two reasons: performance (think Amdahl's Law) and safety. Safety is mainly about data races. A data race is a situation in which at least two threads access a shared variable at the same time. Within that, at least one thread tries to modify the variable.


If your program has a data race, it will have undefined behavior. This means all outcomes are possible and, therefore, reasoning about the program doesn't make sense.


## Minimize waiting


Waiting has at least two drawbacks. First, when a thread waits it cannot make any progress; therefore, your performance goes down. Even worse: if the waiting is busy, the underlying CPU will be fully utilized.


## Prefer immutable data


A requirement for getting a data race is mutable data. If you have immutable data, no data race can happen. You only have to guarantee that the immutable data will be initialized in a thread-safe way.


## Watchout for Deadlocks (and Livelocks)


While developing applications that rely on Mutexes and Semaphores to protect critical sections, you should look at your code carefully to ensure that there are no potential deadlocks (or livelocks).


I'll now walk through some of the top questions I'd recommend practicing.


*To see detailed solutions to these problems, you can check out our concurrency courses in*[*Python*](https://www.educative.io/courses/python-concurrency-for-senior-engineering-interviews?ref=hackernoon.com)*,*[*Java*](https://www.educative.io/courses/java-multithreading-for-senior-engineering-interviews?ref=hackernoon.com)*,*[*C#*](https://www.educative.io/courses/c-sharp-concurrency-for-senior-engineering-interviews?ref=hackernoon.com)*, and*[*Ruby*](https://www.educative.io/courses/ruby-concurrency-for-senior-engineering-interviews?ref=hackernoon.com)


# 1. ReadWrite Lock


![image](img/image)


## Problem statement


Imagine you have an application where you have multiple readers and a single writer. You are asked to design a lock which lets multiple readers read at the same time, but only one writer write at a time.


## Tips to help solve the problem:


1. Define the APIs your class will expose. In this case you'll need two for writer and two for reader. These are:


* acquireReadLock
* releaseReadLock
* acquireWriteLock
* releaseWriteLock


2. Think about each use case that you need to satisfy. These are: Before we allow a reader to enter the critical section, we need to make sure that there's no writer in progress. It is ok to have other readers in the critical section since they aren't making any modifications. Before we allow a writer to enter the critical section, we need to make sure that there's no reader or writer in the critical section.


Additional thoughts


Start by examining the Reader use case. You can have multiple readers acquire the read lock, and to keep track of all of them you'll need a count. You increment this count whenever a reader acquires a read lock and decrement it whenever a reader releases it.


Releasing the read lock is easy, but before you acquire the read lock, you need to be sure that no other writer is currently writing. Again, you'll need some variable to keep track of whether a writer is writing. Since only a single writer can write at a given point in time, you can just keep a boolean variable to denote if the write lock is acquired or not.


Additionally, you'll also need a condition variable for the readers and writers to wait while the other party is in progress. You can use a mutex lock with a condition variable to guard the sections of the code where you manipulate any shared variables.


## Common pitfalls


Avoid splitting the acquisition and release of the mutex variable across two methods. It may seem more efficient since a writer thread only acquires and releases the condition variable once during operation. But the Achilles' heel of this approach is that if the writer thread dies between the two method calls, the entire system would enter a deadlock.


Another common pitfall of the ReadWrite Lock problem is starvation. If a writer arrives while there are readers in the critical section, it might wait in queue forever while readers come and go. As long as a new reader arrives before the last of the current readers departs, there will always be at least one reader in the room. To help avoid this, you could add a mutex for the readers and allow writers to lock it.


# 2. Dining Philosopher


![image](img/image)


## Problem statement


Imagine you have five philosophers sitting around a roundtable. The philosophers do only two kinds of activities. One: they contemplate, and two: they eat. However, they have only five forks between themselves to eat their food with. Each philosopher requires both the fork to his left and the fork to his right to eat his food.


Design a solution where each philosopher gets a chance to eat his food without causing a deadlock.


## Tips to help solve the problem


1. Think about the circular wait condition and how to prevent it


* You could impose ordering on your condition variables to help prevent deadlocks


2. Think of each fork as a resource that two of the philosophers on either side can attempt to acquire. This intuitively suggests using a semaphore with a permit value of 1 to represent a fork. Each philosopher can then be thought of as a thread that tries to acquire the forks to the left and right of it.


3. When a philosopher wants to eat, he needs the fork to the left and right of him. So:


* Philosopher A(0) needs forks 4 and 0
* Philosopher B(1) needs forks 0 and 1
* Philosopher C(2) needs forks 1 and 2
* Philosopher D(3) needs forks 2 and 3
* Philosopher E(4) needs forks 3 and 4


4. Each thread (philosopher) will need to tell you what ID it is before you can attempt to lock the appropriate forks.


## Common pitfalls


A common pitfall that developers run into here is circular wait, which is one of the four Coffman conditions. Circular wait describes a condition where two or more processes are waiting for resources held by one of the other processes.


To avoid this pitfall, you should impose ordering on the condition variables (i.e. number the forks 0-4) and tell each of the philosophers to pick up the lower number fork.


Starvation is also another common pitfall. Imagine that you are trying to starve Philosopher 0. Initially, 2 and 4 are at the table and 1 and 3 are hungry. Imagine that 2 gets up and 1 sits down; then 4 gets up and 3 sits down.


Now you are in a mirror image of the starting position. If 3 gets up and 4 sits down, and then 1 gets up and 2 sits down, we are back where we started. We could repeat the cycle indefinitely and Philosopher 0 would starve.


# 3. Uber Ride problem


![image](img/image)


## Problem statement


Imagine at the end of a political conference, Republicans and Democrats are trying to leave the venue and ordering Uber rides at the same time. However, to make sure no fight breaks out in an Uber ride, the software developers at Uber come up with an algorithm whereby either an Uber ride can have all Democrats or Republicans or two Democrats and two Republicans. All other combinations can result in a fist-fight.


Your task as the Uber developer is to model the ride requestors as threads. Once an acceptable combination of riders is possible, threads are allowed to proceed to ride. Each thread invokes the method 



```
seated()

```

 when selected by the system for the next ride. When all the threads are seated, any one of the four threads can invoke the method 



```
drive()

```

 to inform the driver to start the ride.


## Tips to help solve the problem


1. First, model the problem as a class. You can use two methods: one called by a Democrat and one by a Republican to get a ride home. When either one gets a seat on the next ride it'll call the 



```
seated()

```

 method.


2. To make up an allowed combination of riders, you'll need to keep a count of Democrats and Republicans who have requested rides.


* You can create two variables for this purpose and modify them within a lock/mutex. In this problem, you can use an object of the Mutex class when manipulating counts for Democrats and Republicans.


3. If your first thread is a Democrat that invokes 



```
seatDemocrat()

```

 and there are no other riders available, it should be put to wait which you can do with a semaphore. You should refrain from using a barrier because it's not clear what the future party (i.e. Democrat or Republican) will be.


4. Use two different semaphores 



```
democratsWaiting

```

 and 



```
repulicansWaiting

```

. This will ensure your first Democrat thread will 



```
lock()

```

 the lock mutex variable, find that no other riders exist, release the lock object and go on to wait at the 



```
democratsWaiting

```

 semaphore.


5. Think about the use cases a Democrat thread has to check:


* If there are already 3 waiting democrats, then we signal the 



```
democratsWaiting

```

 semaphore three times so that all these four democrats can ride together in the next Uber ride.


* If there are two or more Republican threads waiting and at least two Democrat threads (including the current thread) waiting, then the current democrat thread can signal the 



```
republicansWaiting

```

 semaphore twice to release the two waiting republican threads and signal the 



```
democratsWaiting

```

semaphore once to release one more democrat thread. Together the four of them would make up the next ride consisting of two Republicans and two Democrats.


* If the above two conditions aren't true then the current democrat thread should simply wait itself at the 



```
democratsWaiting

```

 semaphore and release the mutex so that other threads can now enter the critical sections.




The key is to realize that each thread enters the critical sections 



```
seatDemocrat()

```

or 



```
seatRepublican()

```

 one at a time because of the lock at the beginning of the two methods. Whether a ride is evenly split between the two types of riders or consists entirely of one type of riders depends upon the order in which the threads enter the critical section.


## Common pitfalls


In this problem, it's possible that you could run into starvation, which could be attributed to scheduling errors where only Democrats or Republicans are getting to ride. To avoid this, you should keep a count of those who have requested rides.


Then, you can use two different semaphores to differentiate between Republicans waiting and Democrats waiting, this way the current thread that's waiting can signal the correct semaphore(s) to make up the next Uber ride.


# 4. Asynchronous to Synchronous problem


![image](img/image)


## Problem statement


Imagine we have an 



```
AsyncExecutor

```

 class that performs some useful task asynchronously via the method 



```
execute()

```

. In addition, the method accepts a function object that acts as a callback and gets invoked after the asynchronous execution is done. The asynchronous work is simulated using 



```
sleep

```

. A passed-in call is invoked to let the invoker take any desired action after the asynchronous processing is complete.


Your task is to make the execution synchronous without changing the original classes (imagine that you are given the binaries and not the source code) so that the main thread waits till the asynchronous execution is complete.


## Tips to help solve the problem


1. The requirement that the main thread should block until the asynchronous execution is complete hints at using some kind of notification/signaling mechanism.


* At first glance, you may want to use a semaphore, but instead you could use a condition variable and a mutex pair to achieve the same functionality


2. Since you're not able to modify the original code, you can extend a new class 



```
SynchronousExecutor

```

 from the given 



```
AsyncExecutor

```

 class and override the 



```
execute()

```

 method. The trick here is to invoke the original asynchronous implementation using 



```
super()

```

 inside the overridden method.


## Common pitfalls


In this problem, the shared resource might become unusable for both the asynchronous and synchronous code pieces. What if both keep on waiting for each other and the waiting loop never ends? This resembles a deadlock. You can avoid this by setting up a signaling mechanism to inform the main thread to continue execution.


# 5. Barber Shop problem


![image](img/image)


## Problem statement


A barber shop consists of a waiting room with n chairs, and a barber chair for giving haircuts. If there are no customers to be served, the barber goes to sleep. If a customer enters the barbershop and all chairs are occupied, then the customer leaves the shop.


If the barber is busy, but chairs are available, then the customer sits in one of the free chairs. If the barber is asleep, the customer wakes up the barber. Write a program to coordinate the interaction between the barber and the customers.


## Tips to help solve the problem


1. First, identify the different state transitions for this problem. Let's look at them piecemeal:


* A customer enters the shop and if all N chairs are occupied, he leaves. This hints at maintaining a count of the waiting customers.


* If any of the N chairs is free, the customer takes up the chair to wait for his turn. Note this translates to using a semaphore on which threads that have found a free chair wait on before being called in by the barber for a haircut.


* If a customer enters the shop and the barber is asleep it implies there are no customers in the shop. The just-entered customer thread wakes up the barber thread. This sounds like using a signaling construct to wake up the barber thread.




\


## Common pitfalls


A common pitfall here is for the program to enter a deadlock. The barber and the newly-arrived customer check each other's status at the same time so they deadlock because at that moment:


The barber sees no one sitting in a chair and thinks the waiting room is empty so goes to sleepThe customer thinks the barber is busy so doesn't try to wake up the barber and just patiently waits for the barber


Another pitfall that developers may run into is starvation. This is because in some solutions, there is no guarantee that customers are served in the order they arrive, so they will continually wait for a resource that is given to other processes.


You can avoid starvation by using a queue, where customers are added as they arrive, so that barber can serve them on a first come first serve basis.


# Put your concurrency skills to practice


The only way you can get better at concurrency problems is to practice them.


*If you're looking for detailed answers to the above questions, along with other top concurrency interview questions, including the Unisex Bathroom problem and thread-safe singleton, I highly recommend having a look at our concurrency interview courses in*[*Python*](https://www.educative.io/courses/python-concurrency-for-senior-engineering-interviews?ref=hackernoon.com)*,*[*Java*](https://www.educative.io/courses/java-multithreading-for-senior-engineering-interviews?ref=hackernoon.com)*,*[*Ruby*](https://www.educative.io/courses/ruby-concurrency-for-senior-engineering-interviews?ref=hackernoon.com)*, and*[*C#*](https://www.educative.io/courses/c-sharp-concurrency-for-senior-engineering-interviews?ref=hackernoon.com)*.*


Happy interviewing!


Additional reading:


* [Java Multithreading and Concurrency: Cracking Senior Interviews](https://www.educative.io/blog/java-multithreading-and-concurrency-what-to-know-for?ref=hackernoon.com)


* [Multithreading and Concurrency Fundamentals](https://www.educative.io/blog/multithreading-and-concurrency-fundamentals?ref=hackernoon.com)


* [Python Concurrency: Making sense of asyncio](https://www.educative.io/blog/python-concurrency-making-sense-of-asyncio?ref=hackernoon.com)




