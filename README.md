# README
<!--
This README would normally document whatever steps are necessary to get the
application up and running.

Things you may want to c<!--
*** Thanks for checking out this README Template. If you have a suggestion that would
*** make this better, please fork the repo and create a pull request or simply open
*** an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
-->

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url] 
[![Forks][forks-shield]][forks-url] 
[![Stargazers][stars-shield]][stars-url] 
[![Issues][issues-shield]][issues-url] 
![Hireable](https://cdn.rawgit.com/hiendv/hireable/master/styles/default/yes.svg) 

# Django Rest Framework Auth Token

>  A very simple api with authorization token implementation.

Additional description about the project and its features.


## Built With

- DJANGO
- DJANGO REST FRAMEWORK
- HTTPie
- GITHUB ACTIONS
- VSCODE

## Getting Started
### Usage
To have this app on your pc, you need to:
* [download](https://github.com/javitocor/DRF_Auth/archive/main.zip) or clone this repo:
  - Clone with SSH:
  ```
    git@github.com:javitocor/DRF_Auth.git
  ```
  - Clone with HTTPS
  ```
    https://github.com/javitocor/DRF_Auth.git
  ```

* In the project directory, you can run:

Create virtual enviroment with:

``` bash
   py -m venv project-name
   project-name\Scripts\activate.bat
```

Run migrations:

``` bash
   py manage.py migrate
```
Run server:

``` bash
   py manage.py runserver
```
Create a superuser in the command line by typing:
``` bash
   python manage.py createsuperuser --username example --email example@example.com
```

Request you token with by sending a post request(with HTTPie):
``` bash
   http post http://127.0.0.1:8000/api-token-auth/ username=example password=123
```
Make a get request(with HTTPie) to get the info:
``` bash
   http http://127.0.0.1:8000/hello/ 'Authorization: Token 9054f7aa9305e012b3c2300408c3dfdf390fcddf'
```

You can access the page by typing in your web browser and login with your superuser credentials

``` bash
   http://127.0.0.1:8000/hello
```


## Author

👤 Javier Oriol Correas Sanchez Cuesta 
- Github: [@javitocor](https://github.com/javitocor) 
- Twitter: [@JavierCorreas4](https://twitter.com/JavierCorreas4) 
- Linkedin: [Javier Oriol Correas Sanchez Cuesta](https://www.linkedin.com/in/javier-correas-sanchez-cuesta-15289482/) 

## 🤝 Contributing

Contributions, issues and feature requests are welcome!

Feel free to check the [issues page](https://github.com/javitocor/DRF_Auth/issues).

## Show your support

Give a ⭐️ if you like this project!

## Acknowledgments 🚀

- [Django Docs](https://docs.djangoproject.com/en/3.2/)
- [Django Rest Framework Docs](https://www.django-rest-framework.org/)

## 📝 License

This project is [MIT](lic.url) licensed.

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/javitocor/DRF_Auth.svg?style=flat-square
[contributors-url]: https://github.com/javitocor/DRF_Auth/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/javitocor/DRF_Auth.svg?style=flat-square
[forks-url]: https://github.com/javitocor/DRF_Auth/network/members
[stars-shield]: https://img.shields.io/github/stars/javitocor/DRF_Auth.svg?style=flat-square
[stars-url]: https://github.com/javitocor/DRF_Auth/stargazers
[issues-shield]: https://img.shields.io/github/issues/javitocor/DRF_Auth.svg?style=flat-square
[issues-url]: https://github.com/javitocor/DRF_Auth/issuesover:
