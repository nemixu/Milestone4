# DN Fitness

<p>Welcome to DN Fitness this e-commerce website was developed by Stephen Seagrave as a final milestone project for the Code Institute Full-Stack Web development course. This application is aimed at targeting users who wish to purchase a variety of services that are available to help improve the individuals fitness / quality of life. If you would like to reach out to me please use my GitHub contact Details</p>

<p>This is a full stack website developed for Code Institute milestone project 4. For full functionality of this website registering for a profile is required to view profiles and order hisotry. To test card payments use Stripe test payments, use card number ``` 4242 4242 4242 4242 ```, CVC and expiry date 04 24 424242</p>
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
- [Planning & Testing](#Planning-and-Testing) 
- [Bugs](#Bugs)
- [Deployment](#Deployment) 
	- [Deploying to Heroku](#Deploying-DN-Fitness-to-Heroku)
    - [Locally run this project](#Running-this-project-locally)
- [Credits](#Credits) 
- [Disclaimer](#Disclaimer)

## [User Experience](#Contents):

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
* Encourage user sales with reasonable prices
* Build awareness for the brand and attract more traffic on the site.

### User Stories:
* As a store owner:
    * As a store owner, I want a site that is user friendly and is easy to navigate for the user.
    * As a store owner, I want users to purchase without being registered.
    * As a store owner, I want to show customers what my services are and what they include.
    * As a store owner, I want to be able to edit product prices, and upload and delete products.
    * As a store owner, I want to see users feedback on classes/services.

* As a site User:
    * As a user looking to purchase a service, I want to see what is included in that service.
    * As a user looking to purchase a service, I want to recieve an email confirming my purchase.
    * As a user looking to purchase a service, I want to see the purchase on my created profile.
    * As a user looking to purchase a service, I want to see my previous purchases if I have purchased before.

* As a shopper:
    * As a user interested in the service I want to know as much about the information as possible.
    * As a user interested in the service I Want to know if people have used the service before.
    * As a user interested in the service I want to know about the individual or company providing the service.
    * As a user interested in the service I want to see what the service has to offer.

* As a client:
    * As a user who is new to fitness I want to ensure the information is clear and understandable.
    * As a user who is new to fitness I want to know what kind of activites are covered in the services.
    * As a user who is new to fitness I want to read about the service providers history to ensure they are certified.


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

## [Design Choices](#Contents):
<p>From the start the site design is extremely important to ensure a user is interested in the site, they will stay on the site and view what is to be offered and potentially purchase a product. The site will have a minimalistic theme to ensure the user is not distracted by too many colours, and also for colours to compliment the imagery used across the site.</p>

### Fonts: 
* [Roboto](https://fonts.google.com/specimen/Roboto)
<p>I have chosen this font for this project as the font family for this website made sense as it provided a clean and elegant & clean style to go along nicely with the colour scheme. And also helped to ensure the information on the site was readable to the user.</p>

### Icons:
<p>I have decided to use the collection of icons from font-awesome, as the collection they have are vast and easy to use. They have a wide range of icons that have come in handy for things such as the shopping cart and user icon</p>

### Colours:
<p>The colours I have chosen for this website will compliment the minimalistic feel and tones of the website, having a visually appealing contrast provides a more elegant user experience for those using / navigating the site website, below is a list of colours user across the website.</p>

* Primary Colour - #ffffff - This colour was used for the navbar and overal site pages.
* Secondary Colour - #212529 - A Dark blue/grey colour used for the landing page about section and mobile nav slide menu.
* Tertiary Colour - #ff4500 - A vibrant orange red used to make buttons and important information pop out for the user.
* #000 - Black was used for text throughout the application
* #fafafa - Offwhite colour used on the footer and insets for profile navigation and order cards.

![alt text](https://github.com/nemixu/Milestone4/blob/master/media/colour_scheme.PNG "colour Palette")

### Styles:

DN Fitness Shadows and transitions:

Shadows:
```css
panel-shadow: 1px 1px 2px rgba(0,0,0,0.4);
text-shadow: 0.5px 0.2px 1px rgba(0,0,0,0.2);
```

Transitions:
```css
slow-transition: 0.5s all ease-in-out;
```

### Images:
<p>The images used across the website have been sourced from royalty free image hosting websites such as <a href="https://unsplash.com/" target="_blank">Unsplash</a>. The images are related to gym / fitness in some way and helps invite the user to the site with visually appealing images.</p>

## [Wireframes](#Contents):
<p>The wireframes for this project were created using <a href="https://balsamiq.com/" target="_blank">balsamiq</a>. This tool helped to devlop the wireframes in a quick and easy manner and had mutliple components ready to use to speed up the development process. Once all the wireframes were completed for mobile, tablet, desktop it was extremely easy to export the .png files in order to save for this project.</p>

<p>The wireframes for this project can be found <a href="https://github.com/nemixu/Milestone4/tree/master/wireframes" target="_blank">here.</a></p>

### Database Design:

* During the development of DN fitness I worked with the standard sqlite3 database that is pre-installed with Django.
* In the production version of DN fitness the database is utilizing PostgreSQL and is hosted and provided by Heroku.

### DN Fitness Data Models:

User models used in this application is provided by Django. <a href="https://docs.djangoproject.com/en/3.0/ref/contrib/auth/" target="_blank">Click here to read more about it.</a>

#### The Product App:
##### Product Model
Name|Key in db|Field Type|Arguments
:-----:|:-----:|:-----:|:-----:
Name | name | charfield | max_length=254, null=False, blank=False
Category | category | ForeignKey | 'Category', null=True, blank=True, on_delete=models.SET_NULL
SKU | sku | CharField | max_length=254, null=False, blank=True
Description | description | TextField|()
Price | price | DecimalField | max_digits=6, decimal_places=2
Rating | rating|DecimnalField | max_digits=6, decimal_places=2, null=True, blank=True
Image URL | image_url | URLField | max_length=1024, null=True, blank=True
image | image | models.ImageField | null=True, blank=True

#### The Category App:
##### Category Model
Name|Key in db|Field Type|Arguments
:-----:|:-----:|:-----:|:-----:
Name | name | charfield | max_length=254
Friendly | friendly_name | Charfield | max_length=254, null=True, blank=True,


#### The Order App:
##### Order Model
Name|Key in db|Field Type|Arguments
:-----:|:-----:|:-----:|:-----:
Order Number | order_number | CharField |max_length=32, null=False, editable=False
User | user_profile | ForeignKey | UserProfile, on_delete=models.SET_NULL, null=False, blank=False, related_name='orders'
Full Name | full_name | CharField | max_length=40, null=False, blank=False
Email|email | EmailField | max_length=254, null=False, blank=False
Phone Number | phone_number | CharField | max_length=20, null=True, blank=True
Date|order_date | DateTimeField | auto_now_add=True
Delivery Cost | delivery_cost | DecimalField | max_digits=6, decimal_places=2, null=False, default=0
Grand Total | grand_total | DecimalField |max_digits=10, decimal_places=2, null=False, default=0
Shopping Cart | original_cart | TextField | null=False, blank=False, default=''
Stripe PID | stripe_pid | CharField | max_length=254, null=False, blank=False, default=''

#### The OrderItem App:
##### Order LineItem Model
Name|Key in db|Field Type|Arguments
:-----:|:-----:|:-----:|:-----:
Order | order | ForeignKey | Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems'
Product | product | ForeignKey | Product, null=False, blank=False, on_delete=models.PROTECT
Total | lineitem_total | DecimalField | max_digits=6, decimal_places=2, null=False, blank=False, editable=False, default=0,


#### The Review App:
##### Review Model
Name|Key in db|Field Type|Arguments
:-----:|:-----:|:-----:|:-----:
User | user | ForeignKey | User, on_delete=models.CASCADE, null=True, blank=True,related_name="reviews"
Product | product | ForeignKey | Product, on_delete=models.CASCADE, null=True, blank=True,related_name="reviews"
Comment| comment | TextField | max_length=1000, blank=True, null=True
Rating|rating|Floatfield| default=1


#### The Profile App:
##### Profile Model
Name|Key in db|Field Type|Arguments
:-----:|:-----:|:-----:|:-----:
User | user | OneToOneField | User, on_delete=models.CASCADE
Full Name | default_full_name | CharField | max_length=40, null=True, blank=True
Email | default_email | EmailField | max_length=254, null=True, blank=True
Phone Number | default_phone_number | CharField | max_length=20, null=True, blank=True

#### The Contact App:
##### Contact Model
Name|Key in db|Field Type|Arguments
:-----:|:-----:|:-----:|:-----:
First Name | first_name | Charfield | max_length=50, blank=False, null=False
Last Name | last_name | CharField | max_length=50, blank=False, null=False
Email | email | EmailField | max_length=254, null=False, blank=False
Phone | phone | CharField | max_length=20, null=False, blank=False, default=''
Message | message | TextField | null=False, blank=False


## [Features](#Contents):

### Features that have been developed:

* <p>Account creation, user can login and view orders on profile dashboard. </p>
* <p>User can update their details from their profile dashboard.</p>
* <p>A list of services / products the user can interact with and find more information about by clicking</p>
* <p>An active shopping cart that users can add or remove items from and also update the cart.</p>
* <p>User can complete a checkout purchase with shopping cart items through the Stripe API which will process the payment securely and place the order</p>
* <p>Users can get in touch with the site owner via email by sending the contact form on the contact page.</p>
* <p>A user who has purchased and has an account are able to leave a review for a product.</p>

### Features that will be developed in future releases:

* <p>Fully functional review system, when a user updates it updates the overal rating for a product.</p>
* <p>A feedback section / Recommendations from past users.</p>
* <p>A booking system so a customer can book a specific session.</p>
* <p>A forum / discussion section where users can talk about their journey in fitness</p>

## [Technologies Used](#Contents):
#### Languages:
* <a href="https://developer.mozilla.org/en-US/docs/Web/HTML" target="_blank">HTML</a>
* <a href="https://developer.mozilla.org/en-US/docs/Web/CSS" target="_blank">CSS</a>
* <a href="https://www.w3schools.com/js/" target="_blank">JavaScript</a>
* <a href="https://www.json.org/json-en.html" target="_blank">JSON</a>
* <a href="https://www.python.org/" target="_blank">Python</a>

#### Tools & Libraries: 
* <a href="https://www.djangoproject.com/" target="_blank">Django</a>
* <a href="https://code.visualstudio.com/" target="_blank">Visual Studio Code</a>
* <a href="https://stripe.com/" target="_blank">Stripe</a>
* <a href="https://pip.pypa.io/en/stable/installing/" target="_blank">PIP</a>
* <a href="https://jquery.com/" target="_blank">jQuery</a>
* <a href="https://git-scm.com/" target="_blank">Git</a>
* <a href="https://getbootstrap.com/" target="_blank">Bootstrap</a>
* <a href="https://pipenv-fork.readthedocs.io/en/latest/" target="_blank">Pipenv</a>
* <a href="https://fontawesome.com/icons?d=gallery" target="_blank">Font-Awesome</a>
* <a href="https://marketplace.visualstudio.com/items?itemName=usernamehw.errorlens" target="_blank">Error Lens</a>

#### Databases:
* <a href="https://www.postgresql.org/" target="_blank">PostgreSQL - Production</a>
* <a href="https://www.sqlite.org/index.html" target="_blank">SQlite3 - Development</a>


## [Planning and Testing](#Contents):

#### Planning:

<p>The planning for this project was extremely important, using new technology to create an application for the first time I knew would be time consuming and I would run into a lot of issues and problems to solve.</p>

<p>Part of my planning process was to use an agile styled system or ticket system to do hourly /daily / weekly tasks from a Todo List and move tasks into the in progress section, if completed they were moved to the completed block, and if i was having serious issues I would move them to the blocked section where I could do it when the rest of the tasks where done. Using this method helped me to ensure I was spending the right time on tasks and not wondering what to do next, when a job was done move it to completed and take a new ticket.</p>

<p>Having wireframes also helped build a base to the project fairly quickly and helped get the basics down, such as the nav bar, footer and image placement. It allowed me to spend more time with the functionality of the framework Django to ensure each app was working correctly.</p>

<p>Future proofing this project was also something that was considered when planning this project, firstly I knew If I did not use the likes of AWS for hosting the static files, if the store owner created a new product and uploaded it via the admin panel, it would not have images attached. This is something I have taken into consideration and i have chosen not to use AWS as I would like to maintain the site myself, but I do understand it is something to strongly consider for projects and the future use of projects.</p>

#### Feature Testing:

A full write up of user testing can be found here

[Feature Testing](https://github.com/nemixu/Milestone4/blob/master/TESTING.md)

## [Bugs](#Contents) 

### Bugs During Development:

#### Issues with images not loading

##### Bug

Images not loading from media folder

##### Fix

Ensure settings file has correct routing to media files and on the URL patters ```+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)```

##### Verdict

This bug was resolved

#### Issues with products image when image is not available

##### Bug

When you direct to a products page when the product has no image, it would throw errors.

##### Fix

Ensure the view is being passed the correct context processors, adding .media processor and in the template use ```{{ MEDIA_URL}}```

##### Verdict

This bug was resolved

#### Stripe webhook duplicating order

##### Bug

When you would process the order everything would process correcly.
when checking the webhooks from stripe payment intent was failing.
This was causing 2 issues, 1. No email was being sent to a user 2. users order would be duplicated in the admin, 1 with stripe pid and 1 without.

##### Fix

Check spelling of all variables, stripe_pid was spelt incorrectly missing the "p" this was causing the error not to be found. Missing parentheses at the return was causing the email issue.

##### Verdict

This bug was resolved


### Other bugs to note 

On the profile page, I did not want a single page that displayed on the left and right, profile details and order history, I wanted to have it like there was a navigation button on the user profile. To get this concept working I created a profile nav with 3 list items, that would be controlled by jquery and remove and add ```display:none;``` when clicked on the navbar. I was originally having issues with the functionality of the jquery as I was on the variable name ```navIcon.on('click', function{})``` I was unable to get responses, so I changed the syntax slightly to ```$('#account-profile').click(function(){}``` which then housed the hide and show calls. This solution made a sleek and easily accessible user profile nav bar for the user.

I was having issues with the logout functionality that was built into the allauth package. on my user profile I had setup a sign out and are you sure you wish to sign out page on the profile, but when you click the url for signout on allauth it brings you to a provision page to ask if you wish to sign out which I did not want. The solution to this problem after reading the allauth documentation was simple, in settings.py in the project directory I added ```ACCOUNT_LOGOUT_ON_GET = True```, this has got one downfall tho which I am fully aware and does not effect this project direction. When you use the navicons to logout, it instantly logs you out now instead of having the provisonal page. This is something I can handle with a popup modal for logout if necessary.

Issues with bootstrap dropdown menu text blurry when using transform - only fix i could find was forcing dropdown class to transform unset and re-positioning the profile dropdown to match how it was with transition.
This was a know bug with bootstrap and was the easiest and quickest solution.


## [Deployment](#Contents):

### Running this project locally:

To run DN Fitness locally please follow these steps below.

Before we get started you will need to ensure you have the following:

* An Interactive development environment such as <a href="https://code.visualstudio.com/" targe="_blank">Visual Studio Code.</a>
* You must have the following installed on your machine
* * <a href="https://www.python.org/">Python3</a>
* * <a href="https://git-scm.com/">Git</a>
* You will need to create an account with the below to run this project and use it sucessfully.
* * <a href="https://stripe.com/">Stripe</a>

## [Instructions](#Contents):
<em>These instructions are for Windows 10, if you are using Mac or linux you may need to use different commands.
<a href="https://python.readthedocs.io/en/latest/library/venv.html">Read more here.</a></em>

* 1: Clone DN Fitness repository by either downloading from <a href="https://github.com/nemixu/Milestone4" target="_blank">Here</a> or type the following command into your desired terminal.
```bash
git clone https://github.com/nemixu/Milestone4"
```
* 2: Navigate to the terminal in vscode or your IDE of choice.
* 3: Enter the following command into your terminal.
```bash
pip3 install pipenv
```
* 4: Initialize the environment by using the following command.
```bash
pipenv shell
```
* 5: Install the required packages and start your virtual environment with these commands
```bash
pipenv install
```
* 6: Set up your environment variables
    * create a folder in project root called `.vscode`, inside this create `settings.json` and create this json object.
    ```
    terminal.integrated.env.windows": {
        "SECRET_KEY": "<your key>",
        "DEVELOPMENT": "1",
        "STRIPE_PUBLISHABLE": "<your key>",
        "STRIPE_SECRET": "<your key>",
        "STRIPE_WH_SECRET": "<your key>",
        "DATABASE_URL": "<your key>",
        "EMAIL_HOST" : "<your email host server> "
        "EMAIL_PASSWORD" : "<your email password key> "
        "EMAIL_HOST_USER": "dnfitness@example.com",
        "DEVELOPMENT_FROM_EMAIL": <email for dev>
        "ADMIN_EMAIL": <your admin email>
    }
    ```
* 7: Enter the following command into the terminal to migrate models into the database.
```bash
python3 manage.py migrate
```
*8: Then you need to create a 'superuser' for this project using the terminal. And follow the instructions.
```
python3 manage.py createsuperuser
```
*9: The application can now be ran locally using the following command.
```bash
python3 manage.py runserver
```

DN fitness is now running locally on your machine.

### Deploying DN Fitness to Heroku:

During the deployment of this project, I deployed the project early to ensure I could have time to iron out any issues I would have deploying a project. I was having issues with the intial deployment and was receiving H10 errors, and a number of things needed to be adjusted before the project would deploy correctly.

Firstly I needed to change settings in the settings.py file, I needed to migrate my db to postgres, dj_database_url and psycopg2-binary was installed using pip3. Next I had to ensure the allowed host was set to the herokuapp url. Gunicorn was installed and the procfile was adjusted from ```web:python3 app.py``` to ```web: gunicorn DN_fitness.wsgi:application ```

Next step was to check if the project would deploy without static files and was tested with ```DISABLE_COLLECTSTATIC = 1``` once the project deployed the settings with whitenoise were set in the project settings file in middleware and inside the config Variables on heroku ```DISABLE_COLLECTSTATIC = 0``` was set.

A re-deployment then deployed the project with the collected staticfiles.


* 1: Create a requirements.txt file using the following command. Ensure whitenoise is installed for staticfiles
```bash
pip3 freeze > requirements.txt
```
* 2: Create a procfile in your project main directory. Please ensure the P is capital in Procfile
```bash
web: gunicorn DN_fitness.wsgi:application
```
* 2.1: In some cases after creating the procfile the webdynos do not always spin up and this may needed to be done manually via the command line.
```bash
heroku ps:scale web=1
```
* 3: Push the newly created files to your repository.
* 4: Create an app for the project on the Heroku Dashboard, it can also be done by the command line.
* 5: Select your deployment method by clicking on the deployment method button in this case you can select GitHub.
* 6: On the dashboard, you will need to set config vars:

```
DATABASE_URL: <your_URL>
SECRET_KEY:<your_key>
STRIPE_PUBLIC_KEY:<stripe_key>
STRIPE_SECRET_KEY:<stipe_secret>
STRIPE_WH_SECRET:<stripe_wh_secret>
EMAIL_HOST <your email host server>
EMAIL_PASSWORD <your email/app password>
EMAIL_HOST_USER <your email>
EMAIL_PORT <your email host port>
```

* 7: Click the deploy button on the heroku Dashboard.
* 8: Wait until the build has finished and click the view project link once it has done. If you get an error please refer to logs, and also check *2.1 above.

Congratulations you have deployed DN fitness to Heroku and it is live to be viewed by anyone!

## [Credits](#Contents):

* This project was developed following Chris Zielinski and the Boutique Ado provided by [Code Institute](https://codeinstitute.net/), but was heavily customized and expanded to meet my needs.
* Loading spinner was taken from my previous project Trivia.
* During development I constantly referred to and used code from [Django](https://docs.djangoproject.com/en/3.1/) and [Stripe](https://stripe.com/docs) documentation

Massive thanks to [Simen Daehlin](https://github.com/Eventyret) for being a great mentor and teacher during my course, and for helping me keep ontop of my projects during the course.

Thanks to [Chris Zielinski](https://github.com/ckz8780) for his endless support with the django framework when things werent sinking in, and for his boutique ado project that basically thought me the structure of django and how to build an e-commerce site.

[James Gregory](https://github.com/asdfractal) for his feedback and troubleshooting during production, and for being always on hand to help with tricky logic.

[Andy Gorman](https://github.com/kangadrewie) for user testing the site, and highlighting bugs to me that were overlooked.

### Images
* [All images for this site came from Unspalsh](https://unsplash.com/)
* [Logo created using](https://hatchful.shopify.com/)

## [Disclaimer](#Contents):
The contents of this website are for educational purposes only.