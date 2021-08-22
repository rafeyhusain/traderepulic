# Introduction
A service that read instrument price data from an external service.

## Setup

There are two ways to setup this service.

### Local Setup

Download and install Python, then run following command:

``` $ pip install -r requirements.txt ```

To start service

``` $ python api.py ```

### Docker Setup

For container based setup, simply run following command. It will few minutes for setup to finish.

``` $ docker-compose up ```

## Service URLs

### URL to Start Aggregator Task

To start aggregator task in background thread, use following URL

``` http://localhost:5001/ ```

Following message will appear

```"Aggregator thread is started..."```

### /instruments/{id}
Retrieve the aggregated Price history of the last 30 minutes of a given instrument to display a nice CancleStick chart (detailed below).

``` http://localhost:5001/instruments/{id} ```

e.g.

``` http://localhost:5001/instruments/4 ```

### /instruments/popular
List the 10 most popular and available instruments with their CandleStick data. Popularity is measured by number of calls to the prior endpoint.

``` http://localhost:5001/instruments/popular ```

## Follow up questions

### 1. How would you change the system to support 50k instruments each streaming one or more quotes every second?

Maximum expected write load on system = 50K * 2 quotes/sec = 100K quotes/sec

To support 100K writes/sec, we could use AWS SNS, AWS API Gateway, AWS Lambda or AWS Fargate along with AWS DynamoDB to ingest stream. 

### 2. How would you change the system to support 100M users hitting each endpoint 10 times/day?

Maximum expected read load on system = 100M * 10 reads/day = 1000 Million reads/day

AWS API Gateway, AWS Lambda or AWS Fargate along with AWS DynamoDB provides necessary scalability for 1000 Million reads/day 

### 3. Our system is growing stale (the most recent price data we have is a few minutes old) and the fault is in our side. What would you do? How would you make sure this doesnt affects customers again?

It seems system is not ingesting data at the expected rate. We have to use scalable ingestion technologies like AWS API Gateway, AWS Lambda, AWS SNS. Also we should watch for critical usage alerts using AWS CloudWatch.