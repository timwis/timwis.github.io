---
title: Phila.gov Router
image: /img/phila-gov-router.png
date: 2018-07-01
role: Back-end Developer
tags:
  - Software
---
In order to serve the City of Philadelphia's website to users as quickly as possible,
we used a globally distributed cache. But in order to handle redirects and rewrites 
"at the edge," we had to build request middleware that would run in an AWS Lambda@Edge
function. This amounted to writing a request router from scratch, along with clever tests to
ensure basic human error in updating redirect rules does not bring down the City's website.

- [Source code](https://github.com/CityOfPhiladelphia/phila.gov-router)
