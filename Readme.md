<a name="Steam Project"></a>

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
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Paniceres/PI_ML_OPS">
    <img src="/src/steam_project_logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Steam Project</h3>

  <p align="center">
    Machine Learning and Data Engineering
    <br />
    <a href="https://github.com/Paniceres/PI_ML_OPS"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Paniceres/PI_ML_OPS">View Demo</a>
    ·
    <a href="https://github.com/Paniceres/PI_ML_OPS/issues">Report Bug</a>
    ·
    <a href="https://github.com/Paniceres/PI_ML_OPS/issues">Request Feature</a>
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
    <li><a href="#methodology">Methodology</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)
Steam, a leading PC game distribution platform, has room for improvement in its recommendation system. This project aims to enhance the user experience by developing an effective and personalized game recommendation system using data analysis and machine learning techniques. The goal is to provide more relevant game suggestions, improve user satisfaction, increase engagement, and ultimately drive Steam's sales and revenue.

Here's a blank template to get started: To avoid retyping too much info. Do a search and replace with your text editor for the following: `github_username`, `repo_name`, `twitter_handle`, `linkedin_username`, `email_client`, `email`, `project_title`, `project_description`

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Pandas][Pandas-logo]][Pandas-url]
* [![Python][Python-logo]][Python-url]
* [![Scikit-Surprise][Scikit-Surprise-logo]][Scikit-Surprise-url]
* [![PyArrow][PyArrow-logo]][PyArrow-url]
* [![FastAPI][FastAPI-logo]][FastAPI-url]
* [![Render][Render-logo]][Render-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* pip
  ```sh
  pip install requirements.txt
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/Paniceres/PI_ML_OPS.git
   ```
2. Execute main.py
   ```sh
   python PI_ML_OPS/app/main.py
   ```
3. Enter your API in `localhost`
   ```
   https://localhost:8000
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

add photo

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- METHODOLOGY -->

## Methodology

### Data Collection

* Large sets of data were collected from Steam, including user information, game data, reviews, and recommendations.
* APIs and scraping tools were used to collect the data.

### Data Cleaning

* Once the data was collected, it was cleaned to remove any unwanted or redundant information.
* This included removing duplicate data, correcting errors, and removing data from users who did not meet the project's requirements.

### Data Transformation

* In this step, the data was transformed to make it easier to work with and analyze.
* This included converting data types, normalizing the data, and creating new variables from existing ones.

### Data Loading

* Once the data was ready, it was loaded into a destination dataset, such as a parquet file with gzip encryption.

### Data Exploration

* In this step, the data was explored to better understand the patterns and trends in user behavior.
* Data visualization tools and mining techniques were used to identify correlations and patterns in the data.

### Feature Engineering

* In this step, new variables were created from existing ones to improve the accuracy of the model.
* This included creating variables for user interactions with games, and game popularity and developers statistics.

### Modeling

* In this step, machine learning techniques were used to develop a model that could predict the probability of a user playing a particular game.
* Supervised learning algorithms, such as logistic regression and cosine similarity, were used to develop the model.

### Model Evaluation

* Once the model was developed, its accuracy was evaluated using appropriate evaluation metrics, such as precision, recall, and F1-score.
* Cross-validation techniques were used to ensure that the model would generalize well to new data.

### Model Deployment

* Finally, the model was deployed in a production environment where it could be used to make predictions in real-time.
* A microservices architecture was used to deploy the model in a scalable and efficient manner.


### Recommendation System Development

* Develop a system that can analyze Steam data and provide personalized game recommendations for each user based on their behavior and preferences.

### Testing and Validation

* Test and validate the recommendation system using appropriate evaluation metrics to measure its accuracy and usefulness.

Expected Outcomes
----------------

* A personalized game recommendation system for each Steam user based on their behavior and preferences.
* Improved user experience on the Steam platform through better game recommendations.
* Increased user satisfaction and engagement with the platform.
* Improved efficiency in the game recommendation process, leading to increased sales and revenue for Steam.


See the [open issues](https://github.com/Paniceres/PI_ML_OPS/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



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

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Your Name - [@twitter_handle](https://twitter.com/twitter_handle) - email@email_client.com

Project Link: [https://github.com/github_username/repo_name](https://github.com/github_username/repo_name)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/Paniceres/PI_OPS_ML.svg?style=for-the-badge
[contributors-url]: https://github.com/Paniceres/PI_OPS_ML/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Paniceres/PI_OPS_ML.svg?style=for-the-badge
[forks-url]: https://github.com/Paniceres/PI_OPS_ML/network/members
[stars-shield]: https://img.shields.io/github/stars/Paniceres/PI_OPS_ML.svg?style=for-the-badge
[stars-url]: https://github.com/Paniceres/PI_OPS_ML/stargazers
[issues-shield]: https://img.shields.io/github/issues/Paniceres/PI_OPS_ML.svg?style=for-the-badge
[issues-url]: https://github.com/Paniceres/PI_OPS_ML/issues
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/paniceres-lucio/
[product-screenshot]: src/screenshot.png

[Pandas-logo]: https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white
[Pandas-url]: https://pandas.pydata.org/
[Python-logo]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/
[SciKit-Surprise-logo]: https://img.shields.io/badge/Scikit--Surprise-F7931E?style=for-the-badge&logo=scikit--learn&logoColor=white
[SciKit-Surprise-url]: https://surprise.readthedocs.io/
[PyArrow-logo]: https://img.shields.io/badge/PyArrow-F63E02?style=for-the-badge&logo=apache-arrow&logoColor=white
[PyArrow-url]: https://arrow.apache.org/pyarrow/
[FastAPI-logo]: https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white
[FastAPI-url]: https://fastapi.tiangolo.com/
[Render-logo]: https://img.shields.io/badge/Render-FF6C37?style=for-the-badge&logo=render&logoColor=white
[Render-url]: https://render.com/
=====================================================