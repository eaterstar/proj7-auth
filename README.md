# Project 7: Authenticated brevet time calculator service

Yite Zhao

for register:  http://localhost:5001/api/register
for get token: http://localhost:5001/api/token?username=aaaa&password=1234      (this is an example for username:aaaa 
																										password:1234)

for get data:  http://localhost:5001/user/eyJhbGciOiJIUzI1NiIsImlhdCI6MTUyMDY0MDk3NCwiZXhwIjoxNTIwNjQxNTc0fQ.eyJpZCI6MH0.VBZZ
			   Y80LM5Peqy_RfBwJoZOAagYkbyzYeSi2N8gnYXM
			   (this is an example for token = eyJhbGciOiJIUzI1NiIsImlhdCI6MTUyMDY0MDk3NCwiZXhwIjoxNTIwNjQxNTc0fQ.eyJpZCI6MH
												0.VBZZY80LM5Peqy_RfBwJoZOAagYkbyzYeSi2N8gnYXM)

duration are 600 sec for token.






- POST **/api/register**

    Registers a new user. On success a status code 201 is returned. The body of the response contains
a JSON object with the newly added user. Add a `Location` field to the response: it should contain the new user ID. On failure status code 400 (bad request) is returned. Note: The 
password is hashed before it is stored in the database. Once hashed, the original 
password is discarded. Your database should have three fields: id (unique index),
username and password. 

- GET **/api/token**

    Returns a token. This request must be authenticated using a HTTP Basic
Authentication (see password.py for example). On success a JSON object is returned 
with a field `token` set to the authentication token for the user and 
a field `duration` set to the (approximate) number of seconds the token is 
valid. On failure status code 401 (unauthorized) is returned.

- GET **/RESOURCE-YOU-CREATED-IN-PROJECT-6**

    Return a protected <resource>, which is basically what you created in project 6. This request must be authenticated using token-based authentication only (see testToken.py). HTTP password-based (basic) authentication is not allowed. On success the resources that you created in last project (for the authenticated user) is returned. On failure status code 401 (unauthorized) is returned.

## Tasks

You'll turn in your credentials.ini using which we will get the following:

* The working application with three parts.

* Dockerfile

* docker-compose.yml
