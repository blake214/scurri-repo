Before we proceed, just want to say thank you for the review.

1. Tell us about one thing you are proud of in your career. It could be a difficult technical problem you had to solve in your work or a personal project. There is no need to go into details; a short paragraph explaining the problem and why you are proud of it would be fine.

**Answer:**

A current issue i have been tackling that i think is a cool strategy:

**Problem Overview:**

I'm addressing a devops challenge involving the offloading of data from an overloaded in-memory caching service to better utilise the unused filesystem space available on nodes in my K8s clusters. The goal is to avoid introducing additional paid services, such as PVCs, by utlising the existing resources within the cluster.

**Key Issues:**

- The database is external to the cluster and the datacenter.
- The memory caching service is overwritting smaller data with the larger files, leading to the DB getting queried more that it needs.
- Im trying not to integrate a high memory usage service as like an internal mongoDB for this.

**My current solution i have been working on, That has been a bit more complex than i inticipated**

I'm implementing a solution that uses node-local storage with a mix of SQLite and lightweight services to manage file caching:

- Primary Service:

  - Maintains a SQLite database to track [nodes, file paths, and TTLs].
  - Uses a small PVC for the database to allow horizontal scaling.
  - Runs a cron job to enforce TTL and clean up expired files and query K8s for dead nodes.

- Node Services:
  - Deployed on nodes with available filesystem space.
  - Provide a basic API for crud operations on cached files.

**Current Status**
The solution effectively addresses the memory overload issue and makes use of "free" resources. However, the added spiderweb has introduced latency in retrieving cached data. Though despite this, the benefits of reduced memory load and cost savings outweigh the latency concerns.

Whether im going to integrate this into the custers, im not sure. Though if it works effciently enough i will.

2. Write a program that prints the numbers from 1 to 100. But for multiples of three print “Three” instead of the number and for the multiples of five print “Five”. For numbers which are multiples of both three and five print “ThreeFive”.

**Available at:** https://github.com/blake214/scurri-repo/numbers

3. Write a library that supports validating and formatting post codes for UK. The details of which post codes are valid and which are the parts they consist of can be found at https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Formatting. The API that this library provides is your choice.

**Available at:** https://github.com/blake214/scurri-repo/uk-postal-code-validations-package
