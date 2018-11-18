---
title: Socrata-to-Carto API translator
date: 2017-04-01
role: Back-end Developer
tags:
  - Software
---
In order for the City of Philadelphia's Open Data Program to migrate to a new API
provider, we had to make sure existing integrations didn't break and couldn't wait
for all of them to be updated. So we built a reverse proxy that translates incoming
old _Socrata-style_ requests into their equivalent new _Carto-style_ requests. This allowed
us to launch incrementally by employing the [Strangler Pattern](https://www.martinfowler.com/bliki/StranglerApplication.html).

- [Source code](https://github.com/CityOfPhiladelphia/soda-carto)
