<div id="top"></div>

![html-badge]
![css-badge]
![python-badge]
![django-badge]
![javascript-badge]
[![Contributors][contributors-shield]][contributors-url]
[![Stargazers][stars-shield]][stars-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/francinv/TDT4140-Middagsdeling">
    <img src="docs/logo.png" alt="Logo" width="200" height="80">
  </a>

<h3 align="center">MealShare</h3>

  <p align="center">
    MealShare is for sharing meals with others, if you for example have made to much food, or you just want to eat with someone else. 
    <br />
    <br />
    <a href="https://middagsdeling-staging.herokuapp.com">View Deployed App</a>
    ·
    <a href="https://github.com/francinv/TDT4140-Middagsdeling/issues">Report Bug</a>
    ·
    <a href="https://github.com/francinv/TDT4140-Middagsdeling/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][login-screenshot]](https://middagsdeling-staging.herokuapp.com)

***Test out the app by clicking the image***

MealShare (Middagsdeling) is an app created during the course Software Development (PU). During the development of this APP I got a good introduction to agile methods and TDD (test-driven development). We used Scrum as our framework, and followed it during the iterations. 

During this project I also got a good introduction to the django framework and have since fallen in love with it :heart_eyes:

In the section, ***Usage*** I will go more into depth on how you can use the APP. 

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Django](https://www.djangoproject.com)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

As mentioned the app is deployed to heroku. The APP can be accessed here:
[https://middagsdeling-staging.herokuapp.com](https://middagsdeling-staging.herokuapp.com). If you want to run the app locally, please follow the steps below. 

### Prerequisites

You must have python installed.
* pip
  ```sh
  pip install --upgrade pip
  ```

### Installation and running

1. Clone the repo
   ```sh
   git clone https://github.com/francinv/TDT4140-Middagsdeling.git
   ```
2. Initialize virtual environment
    ```sh
    pipenv shell
    ```
3. Install requirements
   ```sh
   pipenv install
   ```
4. Start App
   ```sh
   python manage.py runserver
   ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

The App can be used to create a community for meal sharing. First of all you have to create an user.

***Page 1: Register page***
![Register][register_screenshot]
To register an user, there are some fields to fill out (see attached picture):
- Username
- Full name
- Street address 
- Allergies
- ZIP code
- City
- Password

After user is successfully created, you can log in. (If any of the fields are incorrectly filled out, you will get an error message.)

***Page 2: Homepage***
![Homepage][homepage-screenshot]
As you can see on the image, you will see a homepage, with a navbar and available meals. 

_Navbar_

The Navbar consists of:
- MealShare logo:

      By clicking this item, you will be sent back to the HomePage. 
- Home (Hjem):

      By clicking this item, you will be sent back to the HomePage. 
- New dinner listing (Ny annonse):

      This item will take you to a form for creating and dinner.
- Messages (Meldinger):

      This item will take you to messages sent by you in addition to messages sent to you.
- Profile (Profil):

      This item leads to the profile page for logged in user.
- Log out (Logg ut):

      This button wil log you out of the app, and redirect you to a logout page.

_Available meals_

This section consists of several meals added by the community. The meals can be clicked on for more details. After a meal are clicked you will be shown meal details. If the meal is created by you, you will have the possibility to change and delete. If it is created by some other in the community you will have the possibility to sign up for this meal.

See the picture below:
![Meal Detail][meal_detail_screenshot]

***Page 3: New meal ad***
![Create Meal][create_meal_screenshot]
As seen in the picture, this is a page for creating a meal. After all of the fields are added correctly the meal will be created and you will see meal detail. 

The fields:
1. Title (Tittel)
2. Description (Beskrivelse)
3. Street (Gate)
4. ZIP Code (Postnr)
5. City (Poststed)
6. Allergies (Allergener)
7. Split the cost? (Dele utgifter)
8. Cost (NOK)
9. Date and time of dinner (Dato og tid)
10. Amount of guests (Antall gjester)

***Page 4: Messages***
![Inbox][inbox_screenshot]
This page is for messages sent by and to you. A message can be sent to a specific user by clicking `Send melding` button. You will be redirected to a simple form with 3 fields:
1. Title
2. To user: (Dropdown menu with users registered.)
3. Message

After submitting the message you will see that the new message has appeared. 

***Page 5: Profile***
![Profile][profile_screenshot]
This page is a simple profile page, that gives you the possibility to see your information. You will see _username_, _name_, _allergies_ and address.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Francin Vincent - [@francinvincent][linkedin-url] - francin.vinc@gmail.com

Project Link: [https://github.com/francinv/TDT4140-Middagsdeling](https://github.com/francinv/TDT4140-Middagsdeling)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/francinv/TDT4140-Middagsdeling.svg?style=for-the-badge
[contributors-url]: https://github.com/francinv/TDT4140-Middagsdeling/graphs/contributors
[stars-shield]: https://img.shields.io/github/stars/francinv/TDT4140-Middagsdeling.svg?style=for-the-badge
[stars-url]: https://github.com/francinv/TDT4140-Middagsdeling/stargazers
[license-shield]: https://img.shields.io/github/license/francinv/TDT4140-Middagsdeling.svg?style=for-the-badge
[license-url]: https://github.com/francinv/TDT4140-Middagsdeling/blob/master/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/francinvincent
[login-screenshot]: docs/login_page.png
[homepage-screenshot]: docs/home_page.png
[meal_detail_screenshot]: docs/meal_detail_page.png
[create_meal_screenshot]: docs/create_meal_page.png
[inbox_screenshot]: docs/inbox_page.png
[profile_screenshot]: docs/profile_page.png
[register_screenshot]: docs/register_page.png
[html-badge]: https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white
[css-badge]: https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white
[python-badge]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[django-badge]:https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white
[javascript-badge]: https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black
