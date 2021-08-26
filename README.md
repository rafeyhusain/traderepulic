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

To support 100K writes/sec, we could use AWS SNS, AWS API Gateway, AWS Lambda or AWS Fargate along with AWS DynamoDB to ingest stream. Fundamentally we need Streaming Architecture. Streaming data refers to data that is continuously generated, usually in high volumes and at high velocity.

#### AWS API Gateway
AWS API Gateway has 10K requests per second (RPS) capacity for single endpoint. So 10 endpoints could ingest 100K quotes/sec. AWS API provides necessary REST API infrastructure for request/response throttle and caching. 

#### AWS SNS
AWS SNS is a pub-sub system which helps to decouples API Gateway from other services in the system. As more and more services depending on incoming data, they could subscribe to SNS topic to do their part of work. SNS supports 30K transactions per second in AWS US-East region and it has a robust retry mechanism for situations when downstream targets are unavailable. AWS SQS could be used along with AWS SNS which scales elastically to persist messages, and there is no limit to the number of messages per queue. SQS service durably persists messages up to 14 days until they are processed by a downstream consumer. Not only it retains messages for up to 14 days but it is possible to batch up to 10 messages for processing.

#### AWS Lambda & Fargate
AWS Lambda, with concurrency limit of 1,000 functions per region could ingest data to AWS DynamoDB which has throughput of 40K read request units and 40K write request units. If AWS Lambda pose a limitation in ingestion, we could use AWS Fargate which allows 10K clusters each having 2K containers with 5,000 task and services per container. AWS SNS, AWS API Gateway, AWS Lambda or AWS Fargate comes under AWS free tier for certain time period and quota which is a cost saving. 

#### Cache
We could offer different Service Level agreement to 100M users regarding freshness of data. We could serve cached data from API Gateway cache. If enabled, API Gateway checks chache before invoking backend lambda, thus you save cost of lambda invocation for response which are served by cache.

#### AWS Cognito
API Gateway user authentication could be handled using AWS Cognito.

#### AWS Kinesis
If above event driven architecture is not sufficent for our requirements, we could use AWS Kinesis Services to easily collect, process, and analyze data streams in real time. Our data is being extracted from the 'Instrument API' by an AWS Lambda every 10 seconds, pushed to a Kinesis Data Stream, processed by Kinesis Data Analytics and sent to a new Kinesis Data Stream; then Kinesis Data Firehose pushes data to AWS S3 or DynamoDB from the Kinesis Data Stream. Kinesis Data Analytics consumes data from the Kinesis Data Stream instance and allows real-time SQL queries to run on the stream to analyze, filter, and process data.

#### Spark Streaming
Another option for real time analytics is Spark Streaming solution to configures the AWS services necessary to easily ingest, store, process, and analyze both real-time. Apache Spark is ideal for handling real-time data (the instruments streaming data in this case), with low latency and interactive data processing. Data could be stored in Amazon S3 object storage which is less expensive as compared to AWS DynamoDB or Hadoop.

#### Kafka Streaming architecture
Another option for streaming architecture is Kafka as stream processor, Spark Streaming as ETL tool, S3 as streaming data storage, Amazon Athena as Distributed SQL engine. The cost of maintaining and developing this kind of architecture is usually high as compared to AWS managed services.

There are pros and cons of each type of architecture and technology which should be calibrated and adjusted against business plans, short and long term needs and above all cost of implementation.

### 2. How would you change the system to support 100M users hitting each endpoint 10 times/day?

Maximum expected read load on system = 100M * 10 reads/day = 1000 Million reads/day

AWS API Gateway, AWS Lambda or AWS Fargate along with AWS DynamoDB provides necessary scalability for 1000 Million reads/day 

### 3. Our system is growing stale (the most recent price data we have is a few minutes old) and the fault is in our side. What would you do? How would you make sure this doesnt affects customers again?

It seems system is not ingesting data at the expected rate. We have to use scalable ingestion technologies like AWS API Gateway, AWS Lambda, AWS SNS. Also we should watch for critical usage alerts using AWS CloudWatch.