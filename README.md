<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>

[![Issues][issues-shield]][issues-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/devpillow-org/patient-management">
    <!-- <img src="images/logo.png" alt="Logo" width="80" height="80"> -->
  </a>

<h3 align="center">patient-management</h3>


  <p align="center">
    <br />
    <a href="https://github.com/devpillow-org/patient-management"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/devpillow-org/patient-management">View Demo</a>
    ·
    <a href="https://github.com/devpillow-org/patient-management/issues">Report Bug</a>
    ·
    <a href="https://github.com/devpillow-org/patient-management/issues">Request Feature</a>
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
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#pull-requests">Pull Request</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
This layer of project is related to development of backend of patient management system.


#### (User case history) Backend Requirements Gathering

As `employee` i want to access the system using my private credentials, and recover my credentials if i don't remember clicking on "recovery password" button, after success reset password want to be redirected to login page.

When sucess logged want to see the respective page according to my function.

**Administrator**

As system `administrator` i want after login see a list of employees registred on the system ordered by function, want to see in that page a symbol to register new users, function, departments on the system. I want too that i be able to register new administrator users, designate a employee to specific department and manage work schedule.


**Receptionist**

As `receptionist` after login with my credentials, i want to be redirect to a page that can be able to see a queue of patients to be attended to, and in that page want to register new patient into data base or search for patient using name or document number. On click in a patient i want that be able to forward the patient to department to be attended to, put then in a queue of specific department.


**Doctor**

As `doctor` after login with my credentials, i want to see the patients to be attended ordinatin to priority. Want which when click on patient has to be able to see the previous appointments, patient data previous registred. Want when select a patient to be attended the status of patient changed and the same as removed from "waiting attendment" queue, when assist a patient, want that be able to register the patient complaint, write pescription for patient and give a record,  at the end i want that be able to forward the patient to another specialist (department) or end the attendment cicle writing and printing a sicknote with a sick ICD if available.


#### (Functional) Backend Requirements Gathering

As a clinic/hospital professional i want to login into the system with my credentials and:
1. manage/monitor the patient treatment cicle:
2. see the patient past procedures, when realized, who relized and where:
3. store the patient data in a relational database for max 5 years: and
4. designate patient for specific doctor.

#### (Technical) Backend Requirements Gathering
1. The backend project has to be develop using Python and Django Framework:
2. Provide a JSON in/out RESTful API:
3. Created endpoints has to have unit tests for their funcionalities:
4. The architecture used for the project app has to follow DDD principles with the following folder structure as base: and
  ```
  app_name/
  ├── api/
  │   ├── __init__.py
  │   ├── permissions.py
  │   ├── serializers.py
  │   ├── urls.py
  │   └── views/
  │       └── __init__.py
  ├── domain/
  │   ├── __init__.py
  │   ├── models/
  │   │   └── __init__.py
  │   └── services.py
  ├── infrastructure/
  │   ├── __init__.py
  │   ├── interfaces.py
  │   ├── repositories.py
  │   └── utils.py
  ├── tests/
  │   └── __init__.py
  ├── migrations/
  │   └── __init__.py
  ├── __init__.py
  ├── admin.py
  └── apps.py
  ```
  5. For coding format and styling the project has to use `black formater`, `flake8`, `typing hints`, `mypy` and `docstring` (for complex methods, function, class, modules).


<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

[![DRF][Django REST framework]][DRF-url] [![Python][Python.py]][Python-url] [![Django][Django]][Django-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started



### Prerequisites

* Python >= 3.12.2
* Docker >= 25.0.2

### Installation

1. Clone the repo
   ```sh
   git clone git@github.com:devpillow-org/patient-management.git
   ```
2. Create a virtual enviroment and access them
   ```sh
    $ python -m venv .venv
    $ source .venv/bin/activate
   ```
3. Install the requirements
   ```sh
   $ pip install -r requirements-dev.txt
   $ pip install -r requirements.txt
   ```


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Rename the `example.env` to `.env` and add the values of variables



<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Feature 1
- [ ] Feature 2
- [ ] Feature 3
    - [ ] Nested Feature

See the [open issues](https://github.com/devpillow-org/patient-management/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Pull Requests

1. Grant you have the repository cloned.
2. Create your action Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request to develop branch according to Git Flow.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License



<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Branch definitions

- Branchs with prefix "B" as B-login is related to backend-branchs
- Branchs with prefix "F" as F-login is related to frontend-branchs



<!-- CONTACT -->
## Contact

Pedro Augusto - [Linkedin](https://www.linkedin.com/in/pedro-augusto-b445b019b/)

William Elias - [Linkedin](https://www.linkedin.com/in/william-a-101694102/)

Project Link: [https://github.com/devpillow-org/patient-management](https://github.com/devpillow-org/patient-management)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* []()
* []()
* []()

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[Django REST framework]: https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray
[DRF-url]: https://www.django-rest-framework.org/

[Python.py]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=white&color=4FC08D&labelColor=gray
[Python-url]: https://www.python.org/

[Django]: https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white&labelColor=gray
[Django-url]: https://www.djangoproject.com/


[issues-shield]: https://img.shields.io/github/issues/devpillow-org/patient-management?style=for-the-badge
[issues-url]: https://github.com/devpillow-org/patient-management/issues
