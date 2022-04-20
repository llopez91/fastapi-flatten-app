<p align="center">
  <a href="https://fastapi.tiangolo.com"><img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" alt="FastAPI"></a>
</p>
<p align="center">
    <em>FastAPI framework, high performance, easy to learn, fast to code, ready for production</em>
</p>

# Flatten App

Application to flatten array of integers or arrays of integers. This application has been deployed with serverless frameworks on AWS.

# URL AWS Deploy
[https://5fnjrlgys8.execute-api.eu-west-1.amazonaws.com/staging/docs#/][awsdeploy]


# Install python dependencies
```sh
pipenv shell
pipenv install
```

# Run application
```sh
uvicorn main:app --reload
```

You can see the docs application in
```sh
127.0.0.1:8000/docs
```

# Run Test
```sh
pytest
```



## License

MIT

**Free Software, Hell Yeah!**

[awsdeploy]: <https://5fnjrlgys8.execute-api.eu-west-1.amazonaws.com/staging/docs#/>