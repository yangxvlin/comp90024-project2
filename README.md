# comp90024-project2
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-5-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
![GitHub repo size](https://img.shields.io/github/repo-size/yangxvlin/comp90024-project2)
![GitHub](https://img.shields.io/github/license/yangxvlin/comp90024-project2)
![build](https://travis-ci.com/yangxvlin/COMP90024-2019SM1-Project1.svg?branch=master)

COMP90024 - Cluster and Cloud Computing - 2020 S1 - Project 2

## Contributors
<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://yangxvlin.github.io"><img src="https://avatars2.githubusercontent.com/u/26871369?v=4" width="100px;" alt=""/><br /><sub><b>XuLinYang</b></sub></a><br /><a href="https://github.com/yangxvlin/comp90024-project2/commits?author=yangxvlin" title="Code">💻</a></td>
    <td align="center"><a href="http://mrj9990123@gmail.com"><img src="https://avatars2.githubusercontent.com/u/36201915?v=4" width="100px;" alt=""/><br /><sub><b>rudy renjie meng</b></sub></a><br /><a href="https://github.com/yangxvlin/comp90024-project2/commits?author=BeginnerRudy" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/Sirius-ctrl"><img src="https://avatars0.githubusercontent.com/u/26541600?v=4" width="100px;" alt=""/><br /><sub><b>Morry Niu</b></sub></a><br /><a href="https://github.com/yangxvlin/comp90024-project2/commits?author=Sirius-ctrl" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/JasonSuMY"><img src="https://avatars3.githubusercontent.com/u/28706782?v=4" width="100px;" alt=""/><br /><sub><b>Mingyu Su </b></sub></a><br /><a href="https://github.com/yangxvlin/comp90024-project2/commits?author=JasonSuMY" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/Olivia0012"><img src="https://avatars3.githubusercontent.com/u/55537942?v=4" width="100px;" alt=""/><br /><sub><b>Olivia</b></sub></a><br /><a href="https://github.com/yangxvlin/comp90024-project2/commits?author=Olivia0012" title="Code">💻</a></td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->
<table>
  <tr>
  </tr>
</table>

<!-- ALL-CONTRIBUTORS-LIST:END -->

## Videos
https://www.youtube.com/playlist?list=PL3rzNLhlw3lEjaleheqtzTwldK0IhOWBx

## Repository Structure
```
| /.github 
      - github app configure file
  /ansible
      - ansible scripts
  /backend
      - backend server
  /crawler
      - twitter crawler
  /docs 
      - documentations
  /frontend
      - frontend application
  /sentiment-analysis
      - sentiment-analyser
  .all-contributorsrc 
      - all contributers infomation
  .travis.yml
      - travic.ci setup
```

## COVID-19 data resource
- https://github.com/covid-19-au/covid-19-au.github.io

## Due: Wednesday 20th May (by 12 noon!).

## The focus of this assignment
1. harvest tweets from across the cities of Australia on the UniMelb Research Cloud
2. and undertake a variety of social media data analytics scenarios that tell interesting stories of life in Australian cities
3. and importantly how the Twitter data can be used alongside/compared with/augment the data available within the AURIN platform to improve our knowledge of life in the cities of Australia.

## Implementation Requirements
<!-- exploits a multitude of virtual machines: 利用大量虚拟机 -->
1. develop a Cloud-based solution that exploits a multitude of virtual machines (VMs) across the UniMelb Research Cloud for harvesting tweets through the Twitter APIs (using both the Streaming and the Search API interfaces).
2. produce a solution that can be run (in principle) across any node of the UniMelb Research Cloud to harvest and store tweets and scale up/down as required.
3. may want to explore other sources of data they find on the Internet
    - e.g. information on weather, sport events, TV shows, visiting celebrities, stock market rise/falls, images from Instagram etc, however these are not compulsory to complete the work.
4. For the implementation, teams are recommended to use a commonly understood language across team members – most likely Java or Python.
5. Information on building and using Twitter harvesters can be found on the web, e.g. see https://dev.twitter.com/ and related links to resources such as **Tweepy** and **Twitter4J**.
<!-- deem: 认为 -->

- [x] expected to have multiple instances of this application running on the UniMelb Research Cloud 
  - together with an associated CouchDB database containing the amalgamated collection of Tweets from the harvester applications
  - [x] The entire system should have scripted deployment capabilities. 
    1. This means that your team will provide a script, which, when executed, will create and deploy one or more virtual machines and orchestrate the set up of all necessary software on said machines (e.g. CouchDB, the twitter harvesters, web servers etc.) to create a ready-to-run system. 
    <!-- orchestrate: 策划, populate the database: 给数据库增添数据 -->
    2. Note that this setup need not populate the database but demonstrate your ability to orchestrate the necessary software environment on the UniMelb Research Cloud. 
    3. Teams should use Ansible (http://www.ansible.com/home) for this task.
- [x] Teams are expected to develop a range of analytic scenarios. [Normally around 3-5](https://canvas.lms.unimelb.edu.au/courses/17514/discussion_topics/187247)
  - [x] scenerio 1
  - [x] scenerio 2
  - [x] scenerio 3
  1. Students may decide to create their own analytics based on the data they obtain. 
  2. Students are not expected to build advanced “general purpose” data analytic services that can support any scenario but show how tools like CouchDB with targeted data analysis capabilities like MapReduce when provided with suitable inputs can be used to capture the essence of life in Australia.
- [x] a version-control system such as GitHub or Bitbucket for sharing source code.
- [x] solution should include a Twitter harvesting application for any/all of the cities of Australia.
- [x] A front-end web application is required for visualising these data sets/scenarios.
  1. Teams are free to use any pre-existing software systems that they deem appropriate for the analysis and visualisation capabilities, e.g. Javascript libraries, Googlemaps etc.
- [x] The server side of your analytics web application may expose its data to the client through **a ReSTful design**. 
  1. Authentication or authorization is NOT required for the web front end
- [x] CouchDB setup may be a single node or based on a cluster setup
  - [x] MapReduce based implementations for analytics where appropriate, using CouchDB’s built in MapReduce capabilities.
- [x] **(Optional)** Teams may wish to utilise container technologies such as Docker, but this is not mandatory.

## Demo requirements
- A working demonstration of the Cloud-based solution with dynamic deployment – 25% marks
- A working demonstration of – 25% marks
  1. tweet harvesting and 
  2. CouchDB utilization for specific analytics scenarios
