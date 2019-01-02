## Что нужно уточнить перед началом тестирования?

- Requirements? -- corresponds or not?
- Specifications? -- what are typical usage scenarios? context?
- Authentication type
- Server type (development, testing, staging, production) -- performance and environment limitations

## Как вы будете ее тестировать?

#### Smoke testing

###### Positive
* check if server responds -- response code in [2xx, 3xx, 4xx]
* send required params only (=session) -- check json payload scheme

#### Functional testing

###### Positive
* send all=True&type=None -- check payload include non-active purchases
* send all=None&type=<type> -- check payload corresponds to purchases type
* send all=True&type=<type> -- check payload for activity AND type

###### Negative
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

## Это пост или гет запрос?
It is possible to combine POST with a query string, so we cannot say for sure without a method definition
https://stackoverflow.com/questions/14710061/is-it-valid-to-combine-a-form-post-with-a-query-string/14710450

## Какой тип данных может передаваться в параметре all?
Practically any data type that could be processed by a client or a server (depending encoding/decoding used)
The HTTP protocol is not restricted on length https://stackoverflow.com/questions/812925/what-is-the-maximum-possible-length-of-a-query-string



