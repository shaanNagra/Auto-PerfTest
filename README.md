# *AUTOPERF - TESTING*
*(a work in progress title)*

## Table of Content

* ### ddp-sampler
  > atmosphere package to be bundled with meteorjs application that will be tested
  > 
* ### demo-Apps
  > demo meteor applications that were use for quick testing in devalopment of AutoPerf-Testing
* ### log2Test
  > API for creating jmx file(jmeter test plans) 
* ### logProcessing
  > proccess logs to build test/ id groups of function calls
* ### webservice
  > the API that ddp-sampler calls to save log of webapp 

## Links
| folders        | Content            |
| :------------- | ------------------ |
| ddp-sampler    |[github link](https://github.com/shaanNagra/AutoPerf-testing/tree/main/ddp-sampler)|

```
db.getCollection('sessions').aggregate([{
    '$lookup': {
        'from':"sessionsOps",
        'localField':'_id',
        'foreignField':'session_id',
        'as':'log'
        }
     }
     ])
```