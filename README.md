# Flask REST Template

What's included?

- RESTful API with flask-restful
- SQLite database with flask-sqlalchemy
- Token authentication with flask-jwt-extended

## Routes

- /
- /protected
- /user
  - /login POST {email, password}
  - /register POST {username, password, email, \*profile_picture, \*description}
  - /update POST {\*newPassword, \*newEmail, \*newUsername, \*newDescription}
  - /information
  - /\<string:user_id>
