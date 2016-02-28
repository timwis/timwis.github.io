---
title: SDE to Socrata
image: /img/sde-socrata.png
date: 2015-11-01
tags:
  - Software
links:
  - text: Source code
    url: https://github.com/timwis/sde-socrata
---
A command-line utility to create Socrata datasets from Arc SDE/Geodatabase feature classes 
and push their contents in using an efficient transfer process provided by Socrata's DataSync utility. 
Optionally, you can use a [list of pushes](https://github.com/timwis/sde-socrata/blob/master/config/datasets.yaml)
to create a recurring sync job that can run on a cron tab / Windows task. Supports proxy servers, 
logging, and email alerts.
