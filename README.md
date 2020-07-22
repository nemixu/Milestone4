# DN Fitness

<p>Welcome to DN Fitness this e-commerce website was developed by Stephen Seagrave as a final milestone project for the Code Institute Full-Stack Web development course. This application is aimed at targeting users who wish to purchase a variety of services that are available to help improve the individuals fitness / quality of life. If you would like to reach out to me please use my GitHub contact Details</p>

## Contents:

- [UX](#User-experience)
    - [Project Goals](#Project-Goals)
    - [Target Audience Goals](#Target-Audience-Goals)
    - [Site Owner Goals](#Site-Owner-Goals)
    - [User Stories](#User-Stories)
    - [User Requirements and Expectations](#User-Requirements-and-Expectations)
- [Design Choices](#Design-Choices) 
    - [Fonts](#Fonts)
    - [Icons](#Icons)
    - [Colours](#Colours)
    - [Styling](#Styles)
    - [Images](#Images)
- [Wireframes](#Wireframes)
    - [Database Design](#Database-Design)
    - [Data Models](#DN-Fitness-Data-Models)
- [Features](#Features)
    - [Features that have been developed](#Features-that-have-been-developed)
    - [Features that will be implemented in the future](#Features-that-will-be-developed-in-future-releases)
- [Technologies Used](#Technologies-Used)
- [Planning & Testing](#Planning-&-Testing) 
- [Bugs](#Bugs)
- [Deployment](#Deployment) 
	- [Deploying to Heroku](#Deploying-DN-Fitness-to-Heroku)
    - [Locally run this project](#Running-this-project-locally)
- [Credits](#Credits) 
- [Disclaimer](#Disclaimer)

## User Experience:

### Project Goals:
<p>The goal of this project is to offer a range of services and deals including merchandise. The user will be able to create an account, add a combination of services to a shopping basket, make payments and have their orders viewable on the profile dashboard.</p>

### Target Audience Goals:

* Browse various services and review information about that service.
* Purchase a service that is shown on the webstore.
* Create an account to track orders and purchase items on the webstore as a registered user.
* A visually appealing and intuitive design.
* A website that is navigable on any device (mobile/tablet/desktop).

### Site Owner Goals:

* Provide users with a safe and secure e-commerce platform in order to generate revenue from sales.
* Encourage user sales with promotions and discounts or possible group buys.
* Build awareness for the brand and attract more traffic on the site.

### User Stories:

* As a user looking to purchase a service I want to see what is included in that service.
* As a user looking to purchase a service I want to recieve an email confirming my purchase.
* As a user looking to purchase a service I want to see the purchase on my created profile.
* As a user looking to purchase a service I want to see my previous purchases if I have purchased before.
<hr>

* As a user interested in the service I want to know as much about the information as possible.
* As a user interested in the service I Want to know if people have used the service before.
* As a user interested in the service I want to know about the individual or company providing the service.
* As a user interested in the service I want to see what the service has to offer.
<hr>

* As a user who is new to fitness I want to ensure the information is clear and understandable.
* As a user who is new to fitness I want to know what kind of activites are covered in the services.
* As a user who is new to fitness I want to read about the service providers history to ensure they are certified.
* As a user who is new to fitness I want to see possible workout routines.

### User Requirements and Expectations:
<p>Shopping online has become a cornerstone to modern life, a user needs to feel safe and comfortable in order for them to continue with a purchase online. Especially when it comes to using a site / service that is not as well known as big companies / webservices. To tackle this and to ensure we can provide the best possible UX, proper authentication and secure payments through Stripe is necessary to offer peace of mind to the consumer.</p>

#### Requirements:
* Interact with a visually appealing and intuative website.
* Navigate the website on multiple devices with ease.
* Consume information about various products / services easily.
* Add products / services to a shopping cart in a safe and secure way.
* View orders in profile dashboard section.
* Ensure contact to the company / owner is easily accessible for the user.

#### Expectations:
* The website will not store payment information from customers orders on the websites database.
* The website will load with sufficient speed
* The website will ensure safe storage of user details.
* The content will be digestible on multiple devices, mobile, tablet, laptop, large screens.
* The website will have good contrast colours to ensure a user can digest the information easily.
* The website will have a navbar to ensure navigation around the site conforms to good UX.

## Design Choices:
<p>From the start the site design is extremely important to ensure a user is interested in the site, they will stay on the site and view what is to be offered and potentially purchase a product. The site will have a minimalistic theme to ensure the user is not distracted by too many colours, and also for colours to compliment the imagery used across the site.</p>

### Fonts: 
<p>I have chosen the # font for this project as the font family for this website made sense as it provided a clean and elegant & clean style to go along nicely with the colour scheme. And also helped to ensure the information on the site was readable to the user.</p>

### Icons:
<p>I have decided to use the collection of icons from font-awesome, as the collection they have are vast and easy to use. They have a wide range of icons that have come in handy for things such as the shopping cart and user icon</p>

### Colours:
<p>The colours I have chosen for this website will compliment the minimalistic feel and tones of the website, having a visually appealing contrast provides a more elegant user experience for those using / navigating the site website, below is a list of colours user across the website.</p>

-![#000](https://placehold.it/15/000/000000?text=+) Primary: #000;
"Black" - This Colour provides X and contrast to x colours.

-![#000](https://placehold.it/15/000/000000?text=+) Primary: #000;
"Black" - This Colour provides X and contrast to x colours.

-![#000](https://placehold.it/15/000/000000?text=+) Primary: #000;
"Black" - This Colour provides X and contrast to x colours.

-![#000](https://placehold.it/15/000/000000?text=+) Primary: #000;
"Black" - This Colour provides X and contrast to x colours.

-![#000](https://placehold.it/15/000/000000?text=+) Primary: #000;
"Black" - This Colour provides X and contrast to x colours.

### Styles:

DN Fitness Colours:

```css
$primary-color: #fafafa; // primary
$secondary-color: #fafafa; // secondary
$tertiary-color: #fafafa; // tertiary
$white-color: #ffffff; // white
$off-white-color: #fafafa; // off-white
$black-color: #fafafa; // black
$error-color: #fafafa; // error-red
$success-color: #fafafa; // success-green
```

Shadows:
```css
$panel-shadow: 1px 1px 2px rgba(0,0,0,0.4);
$text-shadow: 0.5px 0.2px 1px rgba(0,0,0,0.2);

```

Transitions:
```css
$slow-transition: 0.5s all ease-in-out;
```

### Images:
<p>The images used across the website have been sourced from royalty free image hosting websites such as <a href="https://unsplash.com/" target="_blank">Unsplash</a>. The images are related to gym / fitness in some way and helps invite the user to the site with visually appealing images.</p>

## Wireframes:
<p>The wireframes for this project were created using <a href="https://balsamiq.com/" target="_blank">balsamiq</a>. This tool helped to devlop the wireframes in a quick and easy manner and had mutliple components ready to use to speed up the development process. Once all the wireframes were completed for mobile, tablet, desktop it was extremely easy to export the .png files in order to save for this project.</p>

<p>The wireframes for this project can be found <a href="https://github.com/nemixu/Milestone4/tree/master/wireframes" target="_blank">here.</a></p>

### Database Design:

* During the development of DN fitness I worked with the standard sqlite3 database that is pre-installed with Django.
* In the production version of DN fitness the database is utilizing PostgreSQL and is hosted and provided by Heroku.

### DN Fitness Data Models:

User models used in this application is provided by Django. <a href="https://docs.djangoproject.com/en/3.0/ref/contrib/auth/" target="_blank">Click here to read more about it.</a>

#### The Product Model:

The product models will be showcased here.

#### The Order Model:

The order models will be showcased here.

#### The OrderItem Model:

Will be showcased here.

## Features:

### Features that have been developed:

* <p>Account creation, user can login and view orders on profile dashboard. </p>
* <p>User can update their details from their profile dashboard.</p>
* <p>A list of services / products the user can interact with and find more information about by clicking</p>
* <p>An active shopping cart that users can add or remove items from and also update the cart.</p>
* <p>User can complete a checkout purchase with shopping cart items through the Stripe API which will process the payment securely and place the order</p>
* <p>Users can get in touch with the site owner via email by sending the contact form on the contact page.</p>

### Features that will be developed in future releases:

* <p>A reset password link that will send the user a link to reset their password for the website.</p>
* <p>Services will be filtered by recently purchased or user favourites.</p>
* <p>Order confirmation emails to be sent to customer upon placing an order.</p>
* <p>A feedback section / Recommendations from past users.</p>
* <p>A forum / discussion section where users can talk about their journey in fitness</p>

## Technologies Used:
#### Languages:
* <a href="https://developer.mozilla.org/en-US/docs/Web/HTML">HTML</a>
* <a href="https://developer.mozilla.org/en-US/docs/Web/CSS">CSS</a>
* <a href="https://www.w3schools.com/js/">JavaScript</a>
* <a href="https://www.json.org/json-en.html">JSON</a>
* <a href="https://www.python.org/">Python</a>

#### Tools & Libraries: 
* <a href="https://www.djangoproject.com/">Django</a>
* <a href="https://code.visualstudio.com/">Visual Studio Code</a>
* <a href="https://stripe.com/">Stripe</a>
* <a href="https://pip.pypa.io/en/stable/installing/">PIP</a>
* <a href="https://jquery.com/">jQuery</a>
* <a href="https://git-scm.com/">Git</a>
* <a href="https://getbootstrap.com/">Bootstrap</a>
* <a href="https://fontawesome.com/icons?d=gallery">Font-Awesome</a>

#### Databases:
* <a href="https://www.postgresql.org/">PostgreSQL - Production</a>
* <a href="https://www.sqlite.org/index.html">SQlite3 - Development</a>


## Planning & Testing:

#### Planning:

<p>The planning for this project was extremely important, using new technology to create an application for the first time I knew would be time consuming and I would run into a lot of issues and problems to solve.</p>

<p>Part of my planning process was to use an agile styled system or ticket system to do hourly /daily / weekly tasks from a Todo List and move tasks into the in progress section, if completed they were moved to the completed block, and if i was having serious issues I would move them to the blocked section where I could do it when the rest of the tasks where done. Using this method helped me to ensure I was spending the right time on tasks and not wondering what to do next, when a job was done move it to completed and take a new ticket.</p>

<p>Having wireframes also helped build a base to the project fairly quickly and helped get the basics down, such as the nav bar, footer and image placement. It allowed me to spend more time with the functionality of the framework Django to ensure each app was working correctly.</p>

#### Feature Testing:

Feature testing will go here.

## Bugs 

#### Bugs During Development:

Bugs will go here

## Deployment:

### Running this project locally:

To run DN Fitness locally please follow these steps below.

Before we get started you will need to ensure you have the following:

* An Interactive development environment such as <a href="https://code.visualstudio.com/" targe="_blank">Visual Studio Code.</a>
* You must have the following installed on your machine
* * <a href="https://www.python.org/">Python3</a>
* * <a href="https://git-scm.com/">Git</a>
* You will need to create an account with the below to run this project and use it sucessfully.
* * <a href="https://stripe.com/">Stripe</a>

## Instructions:
<em>These instructions are for Windows 10, if you are using Mac or linux you may need to use different commands.
<a href="https://python.readthedocs.io/en/latest/library/venv.html">Read more here.</a></em>

* 1: Clone DN Fitness repository by either downloading from <a href="https://github.com/nemixu/Milestone4" target="_blank">Here</a> or type the following command into your desired terminal.
```bash
git clone https://github.com/nemixu/Milestone4"
```
* 2: Navigate to this folder in your terminal. (cd Milestone4 for e.g)
* 3: Enter the following command into your terminal.
```bash
python3 -m .venv venv
```
* 4: Initialize the environment by using the following command.
```bash
.venv\bin\activate
```
* 5: Install the requirements and dependancies from the requirements.txt file
```bash
pip3 -r requirements.txt
```
* 6: Inside your IDE create a file where you can store your secret information for the application. This can be done by creating an env.py file.
* 7: Enter the following command into the terminal to migrate models into the database.
```bash
python3 manage.py migrate
```
*8: Then you need to create a 'super user' for this project using the terminal. And follow the instructions.
```
python3 manage.py createsuperuser
```
*9: The application can now be ran locally using the following command.
```bash
python3 manage.py runserver
```

Well done, DN fitness is now running locally on your machine.

### Deploying DN Fitness to Heroku:

* 1: Create a requirements.txt file using the following command.
```bash
pip3 freeze > requirements.txt
```
* 2: Create a procfile with the following command. Please ensure the P is capital in Procfile
```bash
echo web: python3 app.py > Procfile
```
* 2.1: In some cases after creating the procfile the webdynos do not always spin up and this may needed to be done manually via the command line.
```bash
heroku ps:scale web=1
```
* 3: Push the newly created files to your repository.
* 4: Create an app for the project on the Heroku Dashboard, it can also be done by the command line.
* 5: Select your deployment method by clicking on the deployment method button in this case you can select GitHub.
* 6: On the dashboard, you will need to set config vars:

DATABASE_URL: <your_URL>
SECRET_KEY:<your_key>
STRIPE_PUBLIC_KEY:<stripe_key>
STRIPE_SECRET_KEY:<stipe_secret>

* 7: Click the deploy button on the heroku Dashboard.
* 8: Wait until the build has finished and click the view project link once it has done. If you get an error please refer to logs, and also check *2.1 above.

Congratulations you have deployed DN fitness to Heroku and it is live to be viewed by anyone!

## Credits:

* All credits will go here.

## Disclaimer:
The contents of this website are for educational purposes only.