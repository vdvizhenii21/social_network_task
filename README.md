# Social Network Task

## _The Last Social Network, Ever_

## For deployment was used Docker.

## Features

- user signup

Send POST request with required fields:

 - email
 - username
 - password

[a link](http://localhost/users/auth/users/)

- user login

Send POST request with required fields:

 - username
 - password

[a link](http://localhost//users/token/)

Authorization was made with JWT.

On response we get access and refresh token, timo to life we can see on settings.py

- post like
Send POST request with credentials:

[a link](http://localhost/posts/api/posts/v1/likes/1/)

In this example we make like to post with id 1.

- post unlike

Send DELETE request with credentials:

[a link](http://localhost/posts/api/posts/v1/likes/1/)

In this example we make unlike to post with id 1.

- analytics about how many likes was made

[a link](http://localhost/posts/api/analitics/?date_from=2020-02-02&date_to=2020-02-15)


- user activity an endpoint which will show when user was login last time and when he mades a last request to the service.

GET request with id user we can see user activity.

[a link](http://localhost/users/usersactivity/1/)


