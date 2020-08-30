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
<hr>
* As a site User:
    * As a user looking to purchase a service, I want to see what is included in that service.
    * As a user looking to purchase a service, I want to recieve an email confirming my purchase.
    * As a user looking to purchase a service, I want to see the purchase on my created profile.
    * As a user looking to purchase a service, I want to see my previous purchases if I have purchased before.
<hr>
* As a shopper:
    * As a user interested in the service I want to know as much about the information as possible.
    * As a user interested in the service I Want to know if people have used the service before.
    * As a user interested in the service I want to know about the individual or company providing the service.
    * As a user interested in the service I want to see what the service has to offer.
<hr>
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
Category | category | ForeignKey -> 'Category', null=True, blank=True, on_delete=models.SET_NULL
SKU | sku | CharField | max_length=254, null=False, blank=True
Description | description | TextField|()
Price | price | DecimalField | max_digits=6, decimal_places=2
Rating | rating|DecimnalField | max_digits=6, decimal_places=2, null=True, blank=True
Image URL | image_url | URLField | max_length=1024, null=True, blank=True
image | models.ImageField | null=True, blank=True

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
User | user_profile | ForeignKey -> UserProfile, on_delete=models.SET_NULL, null=False, blank=False, related_name='orders'
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
Order | order | ForeignKey -> Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems'
Product | product | ForeignKey -> Product, null=False, blank=False, on_delete=models.PROTECT
Total | lineitem_total | DecimalField | max_digits=6, decimal_places=2, null=False, blank=False, editable=False, default=0,


#### The Review App:
##### Review Model
Name|Key in db|Field Type|Arguments
:-----:|:-----:|:-----:|:-----:
User |user | ForeignKey -> User | on_delete=models.CASCADE, null=True, blank=True,related_name="reviews"
Product | product | ForeignKey -> Product | on_delete=models.CASCADE, null=True, blank=True,related_name="reviews"
Comment| comment | TextField | max_length=1000, blank=True, null=True
Rating|rating|Floatfield| default=1


#### The Profile App:
##### Profile Model
Name|Key in db|Field Type|Arguments
:-----:|:-----:|:-----:|:-----:
User | user | OneToOneField -> User | on_delete=models.CASCADE
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

### Features that will be developed in future releases:

* <p>A reset password link that will send the user a link to reset their password for the website.</p>
* <p>Services will be filtered by recently purchased or user favourites.</p>
* <p>Order confirmation emails to be sent to customer upon placing an order.</p>
* <p>A feedback section / Recommendations from past users.</p>
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
* <a href="https://fontawesome.com/icons?d=gallery" target="_blank">Font-Awesome</a>

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

Feature testing will go here.

## [Bugs](#Contents) 

#### Bugs During Development:

During the creation of the main page I was having issues / bugs with loading the background image from the media folder, at first the problem was I was not loading the directory into the settings.py file and joining to the basedir but I needed to resolve this by adding an additional param to the URLS.py file and import the settings from django config and import the static directory. This was added to the end of the URL patterns ```+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)``` After this it resolved the issue I was having with loading the images from the media directory.

I had issues with the products page passing in the correct variable to allow access to the media folder and display images, inside the variable ```{{ MEDIA_URL}}``` i noticed it was not passing correctly to the view and couldnt understand why this was occuring. I attempted to pass a different variable to see if the error was different and noticed in the error it was stating /products/noimage.png is not found, I knew from here the variable was not passing correctly and had something to do with the context processors. Once I added the .media processor it resolved the issue and the images began displaying.

On the cart page using the tables from bootstrap, I was using 5 table columns and when it came to using them on small screens it was not responsive enough for good UX, I began trying to adjust the styling of the bootstrap classes and the best solution to get this working smoothly on a small screen I utilized these classes ```d-none d-sm-table-cell``` on the child of tr, this removed the image of the item on small screens but kept it on medium and above screens.

I was having an issue with the products page styling, I added a background colour behind the image to cover where the anchor text was used, after doing this the class from bootstrap border-top was being clipped by the background colour and it looked like there was no rounded corners on the products I decided to try and add a gradient instead of a solid colour to the background. Doing this worked perfectly, the top was white like the background and the rounder corners could now be seen and the bottom was a solid colour.

One difficult issue I ran into was with the order checkout process when using webhooks. All orders where processing and adding to the database, but I noticed after 5 seconds it would add a second order of the same to the orderline item. I began debugging the code to see what was wrong with the code.
I tried many things one of the main things I noticed when i removed the ```form.submit()``` in the js it would still fire instantly, this was due to not correctly getting the element by ID for the button, as I was missing the # in the selector. Also there was a conflict on the checkout page with my class and ID as I had a class the same as my ID, once changing this I noticed something was still wrong. I was using ```document.getElementById``` I changed this to ```document.querySelector``` and it worked without issues. Inside the webhook handler it was time to resolve the issue with the webhook not finding the order and re-creating it. After countless times of reading the logic of the code, I finally noticed when the order is being saved it was not saving the stripe pid, this was because I had miss typed and was saving ```stripe_id =```, once I changed the code to ```stripe_pid``` the order was no longer sending a duplicate order and was finding the order in the database. This proved to be one of the most annoying bugs I was having during the duration of this project.

Issues with styling conflicts when a user added a product to their cart, i had it set that the ammount of the cart would show the ammount below the cart icon, but it was pushing the icons up and offset the bottom of the navbar, removing this and adding a counter with a circle to display how many items were in the cart was a better solution as the items on the site are quite big, having a counter for this type of site seemed like the best decision to make.

Issues with styling conflicts with the search icon on the icon header, I wanted to make the search icon like the netflix search bar, when clicked it slides left and opens an input field. I knew how to do this with jquery but wanted to limit the ammount of code written to achieve this. The simplist solution was to take the boostrap class ```.list-inline-item.dropdown.show ``` and added a margin left property to push the other nav anchors to the left. As a result it worked to what was needed but it intefered with other classes using the ``` .dropdown.show ``` class, the easiest fix was to add a custom class which I done ```.list-inline-item.icon-nav-spacer.dropdown.show``` and achieved the exact effect I was looking for.

On the profile page, I did not want a single page that displayed on the left and right, profile details and order history, I wanted to have it like there was a navigation button on the user profile. To get this concept working I created a profile nav with 3 list items, that would be controlled by jquery and remove and add ```display:none;``` when clicked on the navbar. I was originally having issues with the functionality of the jquery as I was on the variable name ```navIcon.on('click', function{})``` I was unable to get responses, so I changed the syntax slightly to ```$('#account-profile').click(function(){}``` which then housed the hide and show calls. This solution made a sleek and easily accessible user profile nav bar for the user.

I was having issues with the logout functionality that was built into the allauth package. on my user profile I had setup a sign out and are you sure you wish to sign out page on the profile, but when you click the url for signout on allauth it brings you to a provision page to ask if you wish to sign out which I did not want. The solution to this problem after reading the allauth documentation was simple, in settings.py in the project directory I added ```ACCOUNT_LOGOUT_ON_GET = True```, this has got one downfall tho which I am fully aware and does not effect this project direction. When you use the navicons to logout, it instantly logs you out now instead of having the provisonal page. This is something I can handle with a popup modal for logout if necessary.

I had issues when I split my css files into seperate components. I was getting errors in console when deployed to heroku that the MIME type was text type. To resolve this I attempted to add a ```type="css"``` but this did not resolve the issue and after discussing with a mentor, the best solution was to introduce the css into the base.css file. 

issues with bootstrap dropdown menu text blurry when using transform - only fix i could find was forcing dropdown class to transform unset and re-positioning the profile dropdown to match how it was with transition.


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
* 5: Install the requirements and dependancies from the requirements.txt file
```bash
pipenv -r requirements.txt
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
*10: To add any additional packages do so in the pipenv shell(you can set your python interpreter to use this shell), once any new package is installed
you will need to use the following command to freeze the new requirements.
```bash
pipenv lock -r > requirements.txt
```

Well done, DN fitness is now running locally on your machine.

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
```

* 7: Click the deploy button on the heroku Dashboard.
* 8: Wait until the build has finished and click the view project link once it has done. If you get an error please refer to logs, and also check *2.1 above.

Congratulations you have deployed DN fitness to Heroku and it is live to be viewed by anyone!

## [Credits](#Contents):

* This project was developed following Chris Lielinski and the Boutique Ado provided by [Code Institute](https://codeinstitute.net/), but was heavily customized and expanded to meet my needs.
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