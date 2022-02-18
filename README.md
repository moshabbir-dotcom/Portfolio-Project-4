
# JA Therapies
## Background
JA therapies is the brainchild of S. Noor and J.Anand who was formed from a dream to offer holistic treaments to all that are rooted in recognised healthcare principles. They would like to have a professional looking website that exibits their level of expertise and professionalism.

As the team is quite small and all have their own specialisms they require a website with a level of automation that would suit their needs. They would need and automated way for customers to make provisional bookings and a function for user to ba able to contact the business at their leisure in order for the relevant treatment specialist to be able to respond further reinforcing the specialist fields catered for by the business and promoting trust in the business and people itself.

The aim is to build a website where only registered users may access the booking and messaging functions but where unregistered user may have enough information in order to be able to make an informed decision as to whether they would like to register or not as well as reducing the possibility of staff time being wasted by spoof contact requests and bookings.

## User Experience
### Site Owner Goals
* Make it easy for customer to make an appointment.
* Be able to confirm appointments.
* Be able to cancel appointments.
* Be able to amend an appointment details.
* Be able to access customer details.
* Allow customers to see the services on offer with prices.
* Be able to recieve a message from customers through a message form when logged in.
* Be able to recieve a booking from a customer through a booking form when logged in.
* Allow customers to know where the clinic is located.

### Site User Goals
* I will know where the JA Therapy clinic is located.
* I will know what kind of services the practice offers.
* I want to be able to book an appointment.
* I will be able to find out about the company and the level of skill of staff.
* I will be able to message the company with a contact request. (Not live email, need to run <em>python -m smtpd -n -c DebuggingServer localhost:1025 in a new terminal while port 8000 is running to test functionality for marking.</em>)
Click [HERE](https://github.com/moshabbir-dotcom/Portfolio-Project-4/blob/7e0d5ed0f4a822b7f199c2e371234cfe7de6753f/static/mainsite/images/Port1025contact.png) for evidence of terminal output.
* I want to get a confirmation email with my appointment time. (Not live email, need to run <em>python -m smtpd -n -c DebuggingServer localhost:1025 in a new terminal while port 8000 is running to test functionality for marking.</em>)
Click [HERE](https://github.com/moshabbir-dotcom/Portfolio-Project-4/blob/7e0d5ed0f4a822b7f199c2e371234cfe7de6753f/static/mainsite/images/Port1025.png) for evidence of terminal output.
* I want to be able to view, amend or delete an appointment.

### Planning
* The project was planned using Github's project planning function and can be found [HERE](https://github.com/moshabbir-dotcom/Portfolio-Project-4/projects/1) or a screenshot [HERE](https://github.com/moshabbir-dotcom/Portfolio-Project-4/blob/39853abb1ee53aea7edad976d9eb1e1274e60a7f/media/images/ProjectPlan.png)

## Wireframe
* The basic wireframe design was put together with the client with a few preference as to how the site was visualised and on discussion it was possible to identify a few points to work towards with an element of flexibility around visuals to be reviewed at the end of every sprint. 

### Desktop
[Desktop1&2](https://github.com/moshabbir-dotcom/Portfolio-Project-4/blob/1c98200a9541fa5c0546035cc394269ee2562be2/media/images/Dsk1_Dsk2.jpg)

[Desktop3](https://github.com/moshabbir-dotcom/Portfolio-Project-4/blob/1c98200a9541fa5c0546035cc394269ee2562be2/media/images/Dsk3.jpg)

### Mobile
[Mobile1&2](https://github.com/moshabbir-dotcom/Portfolio-Project-4/blob/1c98200a9541fa5c0546035cc394269ee2562be2/media/images/Mob1_Mob2.jpg)

[Mobile3](https://github.com/moshabbir-dotcom/Portfolio-Project-4/blob/1c98200a9541fa5c0546035cc394269ee2562be2/media/images/Mob3.jpg)

The points pulled from the wireframes were:
* Every page to have a "hero" image with text overlay.
* The menu and logo would fit convention standards with a "burger" menu for smaller screen sizes.
* Quick link options at the bottom of each page with a Google maps link.

* Once these were defined it was a case of finding a few free bootstrap templates for the client to select from which was then customised to fit the requirements of the client and was primarily on the allauth template pages and booking/contact form pages which were designed and customised to fit the aesthetic of the selected template both in HTML design and CSS styling. There was one piece of JavaScript code that was written specifically for the UX on the Nabvbar which is discussed in the development summary below.

* The 2 designs that closest fit the clients requirements were:

Yogalax [Bootstrap1](https://github.com/moshabbir-dotcom/Portfolio-Project-4/blob/1c98200a9541fa5c0546035cc394269ee2562be2/media/images/Bootstrap1.png)

Physical Therapy [Bootstrap2](https://github.com/moshabbir-dotcom/Portfolio-Project-4/blob/1c98200a9541fa5c0546035cc394269ee2562be2/media/images/Bootstrap2.png)

## Design
* The design was chosen by the business owner from a free template (called physical therapy) available on [Colorlib](https://colorlib.com/wp/templates/). As the website is not currently being hosted the license for the template has not been purchased hence copyright information is still visible on the page until proof of concept is approved by the site owner. On approval this will continue to be a working project and will be cloned into a new respository.

### Fonts
* The fonts as per the template are "Rubik", "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif. Fonts would remain relatively consistent in the event the site is viewed on different devices with the fonts of Roboto, Arial & sans-serif being available on all devices and the typefaces of "Rubik", "Segoe UI" & "Helvetica Neue" being referred to as typefaces as they include all the glyphs used to display a character such as the "J" in the main title.
### Colours
* The font was chosen by the site owner due to its clean contrast between colour combinations which were simple & warm conveying the relaxing enviroment of the clinic itself. It will allow for the official trademarked branding to be added at a later date as well as copyrighted photographs whilst remaining aesthitically pleasing. This was tested as part of the template selection process however for this project stock images have been used to not infringe on copyright.

The contrast checking on the website showed 7 failed colour contrast pairs although this was an automated check and the checking site states <em>"Automatic programs such as this cannot analyze text embedded in images and may misdiagnose or ignore certain critical issues. We recommend that you combine contrast testing results from this website with a manual test performed by a trained accessibility expert."</em> With this in mind it is important to note that all issues raised were related to text within images so a recommendation would be to perform an accessibility analysis by a trained professional to ensure and prove digital compliance before the JA Therapies site is hosted in the public domain. [Bureau of Internet Accessibility](https://www.boia.org/)

However slightly adjusting the colour contrast by amending the css stylesheet allowed the test to pass:
* Before: [FAIL](https://github.com/moshabbir-dotcom/Portfolio-Project-4/blob/1c98200a9541fa5c0546035cc394269ee2562be2/media/images/ContrastFail.png)

* After: [PASS](https://github.com/moshabbir-dotcom/Portfolio-Project-4/blob/1c98200a9541fa5c0546035cc394269ee2562be2/media/images/ContrastPass.png)

## Technologies
### Languages
* [HTML](https://www.w3schools.com/html/)
* [CSS](https://www.w3schools.com/css/)
* [JavaScript](https://www.w3schools.com/js/)
* [Python](https://www.python.org/)

### Tools & Frameworks
* [GitHub](https://github.com/)
* [Gitpod](https://www.gitpod.io/)
* [Django](https://www.djangoproject.com/)
* [Heroku](https://www.heroku.com/home)
* [Postgres](https://www.postgresql.org/)
* [Google Fonts](https://fonts.google.com/)
* [W3C HTML Validation](https://validator.w3.org/)
* [H3C CSS Validation](https://jigsaw.w3.org/css-validator/validator.html.en)
* [http://pep8online.com/](http://pep8online.com/)
* [a11y](https://color.a11y.com/Contrast/)
* [TinyPNG](https://tinypng.com/)
* [Cloudinary](https://cloudinary.com/)
* [ES6 Syntax Checker](https://www.piliapp.com/syntax-check/es6/)
* [W3C CSS Checker](https://jigsaw.w3.org/css-validator/)
* [W3C HTML Checker]()

## Features
### Navigation
* The navigation bar was designed as a full size menu right aligned as per convention for the desktop version although the menu did not show which page the user was on reulting in poor UX. To address this the handleActivNavLink.js file was written so that an "addClass" would be added to the navlink of the viewed page allowing for the corresponsing CSS to take effect.
* As per the clients request the menu was a "burger" menu on smaller devices and a concious decision was made by the client to not utilise a collapsible menu on the site to not have the site seem overly "busy".

## Rendering on different screen sizes
### Home
* [HomeMobile](https://github.com/moshabbir-dotcom/Portfolio-Project-4/blob/f025bd9ce3a4e3b0937b0760025543538582e92c/media/images/Mob1REAL.png)
* [HomeDesktop](https://github.com/moshabbir-dotcom/Portfolio-Project-4/blob/f025bd9ce3a4e3b0937b0760025543538582e92c/media/images/HomeDsk1.png)
* [FooterMobile](https://github.com/moshabbir-dotcom/Portfolio-Project-4/blob/f025bd9ce3a4e3b0937b0760025543538582e92c/media/images/FooterMob.png)
* [FooterDesktop](https://github.com/moshabbir-dotcom/Portfolio-Project-4/blob/f025bd9ce3a4e3b0937b0760025543538582e92c/media/images/FooterDsk.png)

### About
* [TestemonialMobile](https://github.com/moshabbir-dotcom/Portfolio-Project-4/blob/f025bd9ce3a4e3b0937b0760025543538582e92c/media/images/TestemonialMob.png)
* [TestemonialDesktop](https://github.com/moshabbir-dotcom/Portfolio-Project-4/blob/f025bd9ce3a4e3b0937b0760025543538582e92c/media/images/TestemonialDsk.png)
* [AboutMobile](https://github.com/moshabbir-dotcom/Portfolio-Project-4/blob/f025bd9ce3a4e3b0937b0760025543538582e92c/media/images/AboutMob.png)
* [AboutDesktop](https://github.com/moshabbir-dotcom/Portfolio-Project-4/blob/f025bd9ce3a4e3b0937b0760025543538582e92c/media/images/AboutDsk.png)

### Treatments & Prices
* [TherapiesMobile](https://github.com/moshabbir-dotcom/Portfolio-Project-4/blob/f025bd9ce3a4e3b0937b0760025543538582e92c/media/images/TherapiesMob.png)
* [TherapiesDesktop](https://github.com/moshabbir-dotcom/Portfolio-Project-4/blob/f025bd9ce3a4e3b0937b0760025543538582e92c/media/images/TherapiesDsk.png)

### Contact
* This is a page that was set to only be viewed when the user is logged in and was set using the allauth decorator of "login_required" in the views.py file to ensure that it coulds not be accessed by writing the url directly in the address bar. The links for this page across the website were embedded in "if" statements where the links to this page would only be visible in the event the user was authenticated. Otherwise the user would be directed to the signup page to first make an account.
As the email settings were causing a "port not found error" when attempting to submit a contact request; I believe from doing research online that this may be caused by firewall/security settings for the learning provider so a dubug server has been used to prove functionality for which the output is evidenced [HERE](https://github.com/moshabbir-dotcom/Portfolio-Project-4/blob/7e0d5ed0f4a822b7f199c2e371234cfe7de6753f/static/mainsite/images/Port1025contact.png) and in the user story section.

### Booking
* This is a page that was set to only be viewed when the user is logged in and was set using the allauth decorator of "login_required" in the views.py file to ensure that it coulds not be accessed by writing the url directly in the address bar.The links for this page were as the homepage in that across the website they were embedded in "if" statements where the links to this page would only be visible in the event the user was authenticated. Otherwise the user would be directed to the signup page to first make an account.
As the email settings were causing a "port not found error" when attempting to make a booking; I believe from doing research online that this may be caused by firewall/security settings for the learning provider so a dubug server has been used to prove functionality for which the output is evidenced in the user story section and [HERE](https://github.com/moshabbir-dotcom/Portfolio-Project-4/blob/7e0d5ed0f4a822b7f199c2e371234cfe7de6753f/static/mainsite/images/Port1025.png).
There was a user story for client to be able to select the therapist they require but with the niche specialisms that the therapists offer customers would only have a very restricted choice in 1 or 2. As a result this was left as a "To Do" action to be added as part of an incremental function additon to the site once everyone is upskilled in multiple other areas. This was done to adhere to the principle of adding value to a development cycle in that this would not have provided an immediate benefit to the site user or owner and other tasks that would were prioritised.

## Code validation & Testing
### Testing
* The TestCase module imported from Django.test was used to test each page load and redirect. Whilst writing my test code I was informed by my new mentor that this was no longer an assessment criteria for Portfolio Project 4, so form testing was not done although would have been completed if it were.

### HTML
* All HTML pages were tested via URL input and passed validation before submission. Links to validation evidence is below.
* [Home](https://github.com/moshabbir-dotcom/Portfolio-Project-4/blob/5e60e111a5041675f93b33352599d8254d0fefc0/media/images/HomePASShtml.png)
* [About](https://github.com/moshabbir-dotcom/Portfolio-Project-4/blob/5e60e111a5041675f93b33352599d8254d0fefc0/media/images/AboutPASShtml.png)
* [Prices](https://github.com/moshabbir-dotcom/Portfolio-Project-4/blob/5e60e111a5041675f93b33352599d8254d0fefc0/media/images/PricesPASShtml.png)
* [Booking](https://github.com/moshabbir-dotcom/Portfolio-Project-4/blob/5e60e111a5041675f93b33352599d8254d0fefc0/media/images/BookingPASShtml.png)
* [Contact](https://github.com/moshabbir-dotcom/Portfolio-Project-4/blob/5e60e111a5041675f93b33352599d8254d0fefc0/media/images/ContactPASShtml.png)
* [Login](https://github.com/moshabbir-dotcom/Portfolio-Project-4/blob/5e60e111a5041675f93b33352599d8254d0fefc0/media/images/LoginPASShtml.png)
* [Logout](https://github.com/moshabbir-dotcom/Portfolio-Project-4/blob/5e60e111a5041675f93b33352599d8254d0fefc0/media/images/LogoutPASShtml.png)
* [Signup](https://github.com/moshabbir-dotcom/Portfolio-Project-4/blob/5e60e111a5041675f93b33352599d8254d0fefc0/media/images/SignupPASShtml.png)
### CSS
* The bulk of the CSS was from the bootstrap template itself however custom code was written in order to fulfill marking criteria and passed validation which is evidenced [HERE](https://github.com/moshabbir-dotcom/Portfolio-Project-4/blob/5e60e111a5041675f93b33352599d8254d0fefc0/media/images/CSSValidation.png).
### JavaScript
* The bulk of the Javascript was from the bootstrap template itself however custom code was written in order to improve the UX on the navigation menu when exploring the site and passed validation which is evidenced [HERE](https://github.com/moshabbir-dotcom/Portfolio-Project-4/blob/5e60e111a5041675f93b33352599d8254d0fefc0/media/images/JSValidation.png).
### Python
* All Python code was tested through a PEP8 validator and passed even though the pylint module in some occasions reported errors. The evidence of validation is below:
* [Admin.py](https://github.com/moshabbir-dotcom/Portfolio-Project-4/blob/39853abb1ee53aea7edad976d9eb1e1274e60a7f/media/images/Admin.png)
* [Forms.py](https://github.com/moshabbir-dotcom/Portfolio-Project-4/blob/39853abb1ee53aea7edad976d9eb1e1274e60a7f/media/images/Forms.png)
* [Models.py](https://github.com/moshabbir-dotcom/Portfolio-Project-4/blob/39853abb1ee53aea7edad976d9eb1e1274e60a7f/media/images/Models.png)
* [Settings.py](https://github.com/moshabbir-dotcom/Portfolio-Project-4/blob/39853abb1ee53aea7edad976d9eb1e1274e60a7f/media/images/Settings.png)
* [Tests.py](https://github.com/moshabbir-dotcom/Portfolio-Project-4/blob/39853abb1ee53aea7edad976d9eb1e1274e60a7f/media/images/Tests.png)
* [Urls.py](https://github.com/moshabbir-dotcom/Portfolio-Project-4/blob/39853abb1ee53aea7edad976d9eb1e1274e60a7f/media/images/Urls.png)
* [Views.py](https://github.com/moshabbir-dotcom/Portfolio-Project-4/blob/39853abb1ee53aea7edad976d9eb1e1274e60a7f/media/images/Views.png)

## Deployment & setting up Postgres DB
* On the home screen click on create new app
* Enter project name & select region
* Under resources add database to the app resources by selecting Herku Postgres and adding it to env.py in the follwing steps
* Select settings and go to config vars and then reveal config vars
* Set the secret key and database url in heroku config vars and env.py and finalise the connection in settings to ensure sensitive data is not visible in the settings.py file
* Deploy to Heroku by selecting Github as the method and connecting via the prompt
* Click into the search box type project name and then connect
* Click deploy branch. (Before final deployment staticfiles were collected via CLI and debug set to "False" in settings.py file.)
* Once complete the view button will allow the app to be shown in a browser

The program is set to be deployed automatically after each push from gitpod.

### Credits
* Django tutorial videos from Codemy.com
* Bim Williams, Daisy McGirr, Charlie Mallon & Matt Bodden who between them helped me with understanding areas I struggled to grasp.
* Allauth templates were provided to me by Daisy as my initial ones caused button clicks to go to the wrong urls.
* The bootstrap template came with CSS and JS files which were adapted however bespoke code that was written has been marked seperately in the ActiveNavLink.js file and at the bottom of the style.css file.
* Business name and treatment offers belong to JA Therapies.
* Lastly my new mentor Chris Quinn.