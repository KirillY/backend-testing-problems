## Что нужно уточнить перед началом тестирования? (What should be done before the testing begins?)

##### Learn project environment and risk oracles
- Familiarizing yourself with the product (probably taking UI tour)
- Ask PM (or a person for whom quality is a value) about potential concerns or risks -- i.e. clear quality criteria
- Study requirements documentation
- Study API specifications (paying attention at authentication type, error codes and messages list)
- Discuss typical use cases with developers
- Clear server type (development, testing, staging, production) -- performance and environment limitations

## Как вы будете ее тестировать? (What testing may include?)

#### 1. Smoke testing

1.1 check if server responds for request with or without params (just GET /purchases) -- response code in [2xx, 3xx, 4xx]

1.2 send required params only (GET /purcharses/?session=sessionId) -- check json payload scheme

1.3 if (1.1.2) is not working -- remove slash before query string https://stackoverflow.com/questions/1617058/ok-to-skip-slash-before-query-string

#### 2. Functional testing

##### 2.1 Positive
* send all=True&type=None -- check payload include non-active purchases
* send all=None&type=<type> -- check payload corresponds to purchases type
* send all=True&type=<type> -- check payload for activity AND type

##### 2.2 Negative
* Sending a request without the proper authorization -- high priority!!!
* Sending a request with the wrong HTTP verb
* Sending a request with the wrong endpoint
* Sending a request with the wrong headers
* Sending a request with missing headers
* Sending a request with a query with missing required fields
    eg. missing session
* Sending a request with a query with invalid field values
    eg. deprecated session, not existed type

#### Penetration testing
* Send SQL injection inside a params

#### Performance testing
* Use Locust https://habr.com/company/infopulse/blog/430502/

## Это пост или гет запрос? (Is it a POST or GET request?)
Technically it's a GET request.
Although it is possible to combine POST with a query string and GET with a body content, so the behavior can vary.
https://stackoverflow.com/questions/14710061/is-it-valid-to-combine-a-form-post-with-a-query-string/14710450

## Какой тип данных может передаваться в параметре all? (What data type could be transferred with 'all' parameter?)
Practically any data type that could be processed by a client or a server (depending encoding/decoding used)
The HTTP protocol is not restricted on length https://stackoverflow.com/questions/812925/what-is-the-maximum-possible-length-of-a-query-string


