# User Testing

## Testing 

This project was tested thoroughly throughout the development process using chrome dev tools and user testing by me.


### Authentication 

#### Expectation

A normal user should not be able to access specific parts of the site.

#### Implementation

Using django template variables to remove certain options to anonymous users and login required decorators, this was to ensure if a user attempted to re-direct to the page via the address bar it would not be available to them. Redirect user to login page.

#### Test

* While not logged into session -
	* Paste / type into navbar ```/profile/``` after the site url, click enter.
* While not logged into session - 
	* redirct to user profile order history ```/profile/order_history/<order_id>``` after the site url, click enter.	


#### Result

Unregistered users are not given to oppertunity to view specific pages, if they attempt to access these pages there is logic in place to defer this.
Originally I did not have decorators for specific pages, when i Implemented this it removed this loophole.

#### Verdict

This test has met expectations.

------

### User Profile

#### Expectation

Users can register, login and have a personal profile that holds their contact details if they provide, access order history.

#### Implementation

Django-Allauth was used to handle the registration of users, User profile model has custom fields when registering. Account dashboard that has the features, Personal information, order history.
The user dashboard also has a logout section if the user decides to log out

#### Test

* While not logged into session -
	* Navigate to the sign up page
	* Create an account filling out all the required fields
	* Navigate to email to click confirmation email, confirm email
	* Navigate to sign in page - enter details
* While logged into session -
	* Navigate to profile page - click 3 tabs on the profile page to ensure all tabs work
	* Update contact information
	* Log out

#### Result

Users can sign up and a profile will automatically be created. There is a full functional dashboard with a navigation that gives users easy to digest information and improve their user experience.

#### Verdict

This test has met expectations

-----

### Classes(products)

#### Expectation

View a list of products, see information related to that product, sort products into categories.

#### Implementation

A products page was created displaying a list of cards that gave a brief overview of the product price and rating.
There is also a sub nav nested below the page title for easy access of switching between categories to improve user experience.

#### Test

* Navigate to the products page and check products are displaying 
* Click on the category nav to see if all links work
* Navigate to a specific product to see if it displays all the relevant information to the user

#### Result

All products have displayed as expected, filtering of the products displays the products related to the specific category chosen by the user, each product has its own detail page.

#### Verdict

This test has met the expectations

-----

### Reviews

#### Expectation

User can only add a review if they have purchased a product, they can only leave 1 review for a specific product, they can edit the review or delete the review.

#### Implementation

A featured review section on the product details page, which displays reviews left by users, and a link to edit if you have left a review and a delete button to remove the specific review. A review app that is built inside the products app as it was not going to be used else where for re-use. Once a user has made a purchase they are eligble to add a review, this is handled by template variables and if statements to ensure only once they have met all of the conditions will a review form display for them.

#### Test

* Whilst not logged in, navigate to any product details page, the product details page displays a message saying you can leave a review when you purchase.
* Ensure there are no product that I am able to leave a review without purchasing this product.
* Create an account / Login to an account, navigate to products detail page and see if I can leave a review. No review section is showing, displayed messages as above.
* Purchase a product using stripe card, revert to the product purchased, review form is now showing, review can be left.
* Reload site, check product detail page, review showing by user, user is me, edit and delete is showing for user, click edit -> directed to update page, update review.
* Delete review from page.
* confirmation of all actions edited / deleted resulted in a popup being shown throughout the app.

#### Result

Users can write a review only for products they have a confirmed purchase for, ensure their reviews are genuine and can inform potential clients. It is not possible to leave a review if you do not have a verified purchase.

#### Verdict

This test has met the expecatations

-----

### Cart & Checkout

#### Expectation

Select products and add them to cart, remove products from cart, adjust cart quantities, purchase selection through a secure checkout and recieve confirmation email.

#### Implementation

Create a cart using session storage, user is notified of cart quantities via toas messages, cart summary page confirms their selection before checkout process. Form is created from the Order model and validates information before processing, informing the user of any issues. After successful submission a success page is shown with the order confirmation.
During the production of this app it was vital that non registered users could purchase without an account.

#### Test

Testing is carried out for both a user logged in and logged out, the only difference if a user is not logged in the order history is not added to their history in a profile as the user has no profile.
* Navigate to product page, click add to cart.
* Click on the same product again to add another to the cart
* Navigate to a second product, add 5 products to cart.
* Navigate to cart highlighting the number of products in your cart.
* Review cart selection, edit cart selection by adjusting the quantity of the 5 products to 1
* click go to secure checkout
* Fill out all details including the use of the stripe card ```4242 4242 4242 4242```
* Wait for payment to succeed or fail

#### Result

It is simple to add products and update the quanitity of the cart by minimum user clicks, the user has the ability to view at all times their cart quantity, and it is easy to digest and user friendly. Adjusting cart quantities works as expected and deleting a product from the cart removes it entirely from the selection. Checking out is simplified using crispy form fields with stripe animations and highlights to the user what ammount will be charged to the card. When completing a purchase a user is notified by a spinning loader to ensure the user does not refresh the page, they are visually aware of what is happening. The user is notified of the completion of the purchase and is given a review of their purchase and is notified they have been sent an email.
The application will send a confirmation email with a description of their order and details.

#### Verdict

This test has met expectations.

-----

### Toast Messages

#### Expectation

Users are notified of their actions and or errors via a popup message.

#### Implementation

Using bootstrap toast system and linking it to django messages module, users are notified of many different actions throughout the application, The messages use appropriate levels and the toasts are styled using conventional colours and match the theme of the site.

#### Test

* Add a product to the cart
* Update a product in cart
* Delete a product in cart
* Login as a user
* Log out as a user
* Submit the contact form


#### Result

Toast messages are displayed when all the above actions are performed and in further when all actions are performed on the site, an error success or info toast displays to the user constantly keeping them informed of their actions to follow linear usage of the site.

#### Verdict

This test has met expectations.

-----

### Contact Form

#### Expectation

Users can get in touch with the site owner by submitting a form to ask questions. A user who is not registered for this site should also be able to submit a contact form to the site owner.
#### Implementation

A dedicated contact page was created to house the contact form. This form has all required fields to ensure if a user makes a mistake when filling out a section of the form they can continue.

#### Test

* As an unregistered / logged out user, navigate to the contact form and fill out all the fields.
* Submit the form and confirm the content is processed and delivered.
* Checking if the email has been sent in the django console email backend.
* Checking if the email has been sent in the django smtp email backend.
* Wait for toast to notify of the submission of the form.

#### Result

Users can enter their email and write in the text area to contact the business and it is process successfully, as a backup the contact form is submitted to the db incase of a failure in sending.

#### Verdict

This test has met expectations.

-----

### Stripe Payments

#### Expectation

Payments are handled securely to protect sensitive user information

#### Implementation

Using the stripe package and creating webhooks to verify communication with stripe, Following the Boutique Ado project and reading the documentation of stripe.

#### Test

Test the checkout process by submitting an order, checking the stipe dashboard for webhooks ensure payment intent and payment success was present per order.
Check the admin panel to ensure there is no duplicate orders 


#### Result

The payments are handled securely using the systems provided by stripe.
No duplicate orders are created due to the webhook finding the order and submitting correctly.


#### Verdict

This test has met expecations


-----

### Browser Compatibility

#### Expectation

The application displays and functions on widely used browsers.

#### Implementation

Use modern code that is widely supported.#

#### Test

This application was developed using the chrome dev tools so is fully functional here, I have tested on Firefox and safari. Testing of IE has not been completed.
All tests outlined above have been performed on all browsers.


#### Result

The application functions as intended on major browsers.


#### Verdict

This test has met expecations