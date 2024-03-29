# FastAPI-Auth0-Password-Flow-Base-App

## Project Title

FastAPI with Auth0 authentication base REST API using resource owner password flow

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need to have Python 3.9.6+ installed on your system. You can download it from [here](https://www.python.org/downloads/).

You need to have pip installed on your system. You can download it from [here](https://pip.pypa.io/en/stable/installation/).

You also need to have an Auth0 account. Register [here](https://auth0.com/signup?place=header&type=button&text=sign%20up)

#### Setup your Auth0 account for a Resource Owner Password Flow

- https://auth0.com/docs/get-started/authentication-and-authorization-flow/resource-owner-password-flow/call-your-api-using-resource-owner-password-flow#request-tokens

### Installing

First, clone the repository to your local machine:

```bash
git clone https://github.com/json2x/fastapi-auth0-base-app.git
```

Go to your project directory

```bash
cd fastapi-auth0-base-app
```

Install the required packages:

```bash
pip install -r requirements.txt
```

### Running the Application
You can run the application using the following command:

```bash
uvicorn main:app --reload
```

The application will be available at http://localhost:8000.

### Testing

Create a user in Auth0

![create user in Auth0](img/auth0-user.png)

Use created user's credentials to authenticate and authorize use of protected endpoint

![authenticate and authorize with auth0 user creds](img/auth0-Authorize.png)

Test protected endpoint

![test protected enpoint](img/auth0-test-protected.png)


### Built With
[FastAPI](https://fastapi.tiangolo.com/) - The web framework used

[Python](https://www.python.org/) - The programming language used

[Auth0](https://auth0.com/) - A platform that provides universal authentication and authorization services for web, mobile, and legacy applications.