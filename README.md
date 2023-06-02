# Social Network Task

## _The Last Social Network, Ever_

## For deployment was used Docker.

## Features

- user signup

Send POST request with required fields:

 - email
 - username
 - password
[http://localhost/users/auth/users/][PlGd]

- user login

Send POST request with required fields:

 - username
 - password

[http://localhost//users/token/][PlGd]

Authorization was made with JWT.

On response we get access and refresh token, timo to life we can see on settings.py

- post like
Send POST request with credentials:

[http://localhost/posts/api/posts/v1/likes/1/][PlGd]

In this example we make like to post with id 1.

- post unlike

Send DELETE request with credentials:

[http://localhost/posts/api/posts/v1/likes/1/][PlGd]

In this example we make unlike to post with id 1.

- analytics about how many likes was made

[http://localhost/posts/api/analitics/?date_from=2020-02-02&date_to=2020-02-15 ][PlGd]


- user activity an endpoint which will show when user was login last time and when he mades a last request to the service.

GET request with id user we can see user activity.

[http://localhost/users/usersactivity/1/][PlGd]


