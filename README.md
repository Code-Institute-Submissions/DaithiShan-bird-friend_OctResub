# Bird Friend

![AmIResponsive Mockup Screenshot](#)

## Project Outline

- [Bird Friend](#) is a photo sharing web app that allows users to create, search, and edit profiles for birds they've photographed, and comment on or like profiles from other users.
- All users, even those non-registered, can browse through uploaded photos of birds and read other people's comments to get a sense of the community.
- After browsing, users who want to get more involved by commenting or uploading their own photos will receive prompts to register to gain this functionality.
- This creates a deeper link between the user and the application, allowing the site developer to build a sense of community.
- This app features a visitor landing page, user registration and login, a photo gallery, a like feature, and the user ability to edit or delete their uploads and profile.
- The technologies used to build this app include HTML, [Tailwind CSS](https://tailwindcss.com/docs), JavaScript, Python, [Flask](https://palletsprojects.com/p/flask/), and [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)

## Project Goals

- To buid a fun community around casual bird spotting in cities and the countryside, as many people don't really take the time to stop and really see birds in the same way as other wildlife ; dogs, cats, foxes, deer.
- To sell cameras on behalf of a 3rd party through native advertisement. Camera is included as a data field on the Bird Object and, while many users select their iPhone, this field on Featured Photos all link back to that 3rd party supplier.

## Live project

**[View the live project here](#)**


## Table of Contents

  * [User experience](#user-experience)
    + [User Stories](#user-stories)
    + [Wireframes](#wireframes)
  * [Database Models and Schema](#database-models-and-schema)
    + [Database Models](#database-models)
    + [Database Schema](#database-schema)
    + [MongoDb](#mongodb)
  * [Design](#design)
    + [Colour Scheme](#colour-scheme)
    + [Typography](#typography)
  * [Features](#features)
    + [Main](#main)
      - [Landing page](#landing-page)
      - [Gallery page.](#gallery-page)
      - [Navigation](#navigation)
      - [Contact page.](#contact-page)
    + [User Pages](#user-pages)
      - [Register / Login](#register---login)
      - [Password Change Request](#password-change-request)
      - [Profile](#profile)
    + [Dog Pages](#dog-pages)
      - [Dog Profile Page](#dog-profile-page)
      - [Comments](#comments)
    + [Admin](#admin)
    + [Custom Error Pages](#custom-error-pages)
    + [Features left to Implement.](#features-left-to-implement)
  * [Technologies used.](#technologies-used)
    + [Flask](#flask)
      - [Flask extensions used](#flask-extensions-used)
    + [TailwindCSS](#tailwindcss)
    + [Cloudinary](#cloudinary)
      - [Cloudinary Upload API](#cloudinary-upload-api)
      - [Cloudinary Transformation URL API](#cloudinary-transformation-url-api)
    + [Other Tools, Libraries & Programs](#other-tools--libraries---programs)
  * [Testing](#testing)
  * [Deployment](#deployment)
    + [Requirements To Deploy:](#requirements-to-deploy-)
    + [Cloning This Project:](#cloning-this-project-)
      - [To Work With Your Local Clone:](#to-work-with-your-local-clone-)
    + [Deploying To Heroku](#deploying-to-heroku)
      - [Create a procfile:](#create-a-procfile-)
      - [For Deployment:](#for-deployment-)
  * [Credits](#credits)
    + [Code](#code)
    + [Content](#content)

<small><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></small>

## User Experience

#### User Goals

The first-time user is looking for:
- A web app that brings them closer to the everyday, almost invisible birds all around them.
- A fun, relaxed community that's casual, not as encyclopedia-like as other bird spotting sites.

The returning user is looking for:
- A community, where they can develop a new-found interest.
- A user-profile that makes them feel recognised, and where they can revisit favorite photos.

The frequent user is looking for:
- A way to measure the popularity of their own photo uploads.
- A way of taking sharper, higher quality photos to raise that popularity, once measurable.

#### Site Developer Goals
The Developer is looking to:
- Create an inviting, community-drive application to share their passion for birds.
- Develop a modest income flow from 3rd party camera sales whereby the site pays for itself monthly.

### User Stories

- New Visitor

  - I want to a colourful, vibrant landing page that grabs me.
  - I'd like to see all the site content, and some of the features, before registration.
  - I'll only register if it's the only way to comment, like and upload photos.
  - I'd like to eventually add my photos to the site, but it has to be simple.

- Repeat users

  - I'd like a nice profile page, easy login, and a quick fix if I forget my password.
  - I'd like my favorite photos logged to my profile.
  - I'd like to be able to comment on other people's uploads.
  - I want to be able to edit/delete my uploads, and comments.

- Frequent users

- I want to be able to see how many people have liked any of my photos.
- I'd like to see what camera is responsible for the highest quality images.
- I want uploads ranked in terms of popularity, as I grow more invested.
- I want to be able to delete my account if ever I feel frustrated, or finished with it.

-  All Users

   - I'd like to feedback on all my actions on this site.
   - I'd like to be able to contact the admin for any complaints/inappropriate content.
   - I'd prefer endless scrolling as a feature over pagination

- Site Developer

  - I want people to care more about birds, which seem invisible or meaningless to many others.
  - I want the site to pay for itself through 3rd party camera sales, to be sustainable.
  - I want the ability as admin to delete/edit any content that is inappropriate.

### Development Planes

In order to design and create a photo sharing app that would answer these user stories, the project was iterated through the **Five Development Planes**:

<strong>1. <u>Strategy</u></strong>

Broken into three categories, the app will focus on the following target audiences:

- **Roles:**
     - Bird enthusiasts of all levels
     - New Users (Non-Registered)
     - Return Users (Registered)

- **Persona:**
     - New interest in birds
     - Like taking photos casually
     - Enjoy social features when sharing media (likes/comments)

- **Psychographics:**
     - Personality & Attitudes:
          - Open-minded
          - Creative
     - Values:
          - Green / Environmentalist
          - Community
     - Lifestyles:
          - Casual photographer
          - Interested in world around them

The website needs to enable the **user** to:

- Register/login to an account

- Search Bird database by:
    - Bird Type
    - Camera Type
    - Name (frequent users)

- View Photo Gallery with the following information:
    - Bird Type
    - Camera Type
    - Location Spotted
    - Name (Optional)
    - User Name
    - Upload Time
    - Liked By

- Upload and edit their own Birds

- Like and view their favourite Birds from other users

- Get in contact with site owner

The website needs to enable the **site developer** to:
- Provide a community-driven photo-sharing app around birds
- Make 3rd party camera sales from users
- Edit/delete inappropriate content

With these goals in mind, a strategy table was created to determine the trade-off between importance and viability with the following results:

**Strategy Table for User Management:**
![Strategy Table for User Management](static/images/readme-files/user-management-st.png "User Management Strategy Table")

**Strategy Table for Bird Respository Management:**
![Strategy Table for Baking Respository Management](static/images/readme-files/baking-repo-st.png "Baking Repository Strategy Table")

<strong>2. <u>Scope</u></strong>

A scope was defined in order to clearly identify what needed to be done in order to align features with the strategy previously defined. This was broken into two categories:
- **Content Requirements**
     - The user will be looking for:
     - Fun, colorful landing page.
     - Easy navigation.
     - Searchable photo Gallery with following info:
        - Bird Type
        - Camera Type
        - Location Spotted
        - Name (Optional)
        - User Name
        - Upload Time
        - Liked By
     - Simple registration process
     - Customisable User Profile
        - Custom User Name/Password
        - Upload their own photos
        - Save favourite photos
     - Developer contact information

- **Functionality Requirements**
     - The user will be able to:
        - Register/Login to account
        - Customise their profile
            - Custom Username/Password
            - Upload their own photos
            - Save favourite photos
        - Navigate to the Photo Gallery:
            - Search by Bird Type, Camera Type or Name (for frequent visitors)
            - My Photos Page
            - My Favourites Page
        - Create Photo Uploads:
            - Bird Type
            - Camera Type
            - Location Spotted
            - Name (Optional)
            - Get in contact with the Developer

<strong>3. <u>Structure</u></strong>

The information architecture was organized in order to ensure that users could navigate through the site with ease and efficiency, with the following results: 

**Information Architecture for User Management:**
![Information Architecture for User Management](static/images/readme-files/user-management-ia.png "User Management Information Architecture")

**Information Architecture for Baking Respository Management:**
![Information Architecture for Baking Respository Management](static/images/readme-files/baking-repo-ia.png "Baking Repository Information Architecture")

<strong>4. <u>Skeleton</u></strong>

Wireframe mockups were created in a [Figma Workspace]( "Link to Bake It Figma Workspace") with providing a positive user experience in mind:

- Home Page:

     ![Strategy Table for Baking Respository Management](static/images/readme-files/.png "Baking Repository Strategy Table")


## Design

<strong>5. <u>Surface</u></strong>


- <strong>Colour Scheme</strong>

     - The soft, pastel colour scheme was picked to offset the most commonly occuring, vibrant background colors in casual photographs of birds.

    ![Colour Palette](static/images/readme-files/palette.png "Colour Palette")


- <strong>Typography</strong>

     - The primary font chosen is [Mallanna](https://fonts.google.com/specimen/Mallanna "Link to Mallanna Google Fonts page"). A sans-serif typeface, Mallanna stands out in comparison to more common typefaces like Open Sans and Roboto. It's thickness, and roundness is visually pleasing, and its individuality says this is something new, and out of the ordinary.

        ![Mallanna Typeface Example](static/images/readme-files/worksans-ex.png "Work Sans Typeface Example")

     - The Secondary font (headings font) is [Roboto Slab](https://fonts.google.com/specimen/Roboto+Slab "Link to Roboto Slab Google Fonts page"). This font was chosen to complements Mallanna with its mirroring thickness, and open friendly curves. It's also a less widely used typeface, and helps give the app extra character.

        ![Roboto Slab Typeface Example](static/images/readme-files/indieflower-ex.png "Indie Flower Typeface Example")

- <strong>Imagery</strong>

     - The imagery used was created by the developer using the application [Procreate](https://procreate.art/) in order to create a consistency of the elements while maintaining the look and feel of the application.

[Back to top ⇧](#table-of-contents)

### Wireframes

- [Mobile Wireframes](#)
- [Tablet Wireframes](#)
- [Desktop Wireframes](#)

## Database Models and Schema

### Database Models
- The database consists of four collections - User, Bird, Type, Comment
- User
	- This contains user's username, email address, hashed password string and avatar selection
	- The user ID acts as a reference field in various other collections
- Bird
	- This is where users enter; Bird Type, Camera Type, Location spotted and give a Name (optional).
	- User Id is not entered but is automatically set to the user that uploads the Bird object
	- liked_by is a one to many field automatically referencing IDs of Users that have liked a Bird object
	- img_url is the users uploaded image of the bird
		- img_url_card is the above image with transformations setting height to 350px, width to 525px, low quality on the image and automatically focusing on key part of image using cloudinary API
		- img_card_thumb is also optimized to lower quality and limited to a width of 500px (height remains at auto) 
	- upload_date is an automatically added datetime item
- Bird Type
	- This acts as a reference field for the Bird collection and contains a lists of types that users can choose from when uploading their Bird
- Camera Type
	- This acts as a reference field for the Camera collection and contains a lists of types that users can choose from when uploading their Bird
- Comment
	- author references the User.id that created the comment
	- bird references the Bird.id of the bird to which the comment is attached
	- content is text input of comment
    - datetime is another automatically added datetime item

### Database Schema

![database schema](#)

### MongoDb

- mongodb was used as the project database.

- I followed the following steps to set it up.
	- signed up to Mongodb and created a shared cluster
	- selected default AWS cloud provider
	- selected Ireland region
	- selected m0 cluster tier
	- chose name for cluster
	- once cluster was created I clicked 'CONNECT' button
	- Selected 'connect your application'
	- selected Python / 3.6 or later as my driver
	- copied the connection string for use in my application
	- set password / cluster name / collection name as enviuronmental variables to connect to my DB within flask
	- used Flask-MongoEngine to interact with my DB within the app

## Features

### Main

#### Landing page

- If user's are not signed in, then they are greeted with a fun, friendly landing page.
- There are clear links to the Photo Gallery and to Login or Register.
- If the user is already signed in, the landing page redirects to the Photo Gallery.
- The footer is viewable on scroll, but initially hidden off screen to focus the user on the main landing page design and image 
	
#### Gallery page.
-  Gallery page shows six uploaded birds per page
-  Pagination buttons are below pictures to easily navigate between pages
-  Options to view most popular or newly uploaded birds
-  Default view is to show the most popular bird
-  Clear distinction between 'Popular' and 'New' depending on which page the user is on
-  There is a different wallpaper depending on whether the user is in 'Popular' or 'New'
-  Each bird photo card on the gallery page contains links to:
	- Like the bird
	- See the main photo page of the bird with larger picture
	- Link to the person who uploaded the bird's photo (if user is not also the uploader)
	- Links to delete or edit the bird, if user is the uploader 

- There is a large button at the bottom of the gallery to upload a new bird photo 

#### Navigation

- There are two different navigations, depending on whether you are on mobile or tablet+
- On mobile there is a bottom navigation bar, making it easy to access the main links with your thumb (visible once the user has signed in)
- The top mobile navigation simply consists of a 'My Profile' button (or Login/Register buttons if a user has not yet signed in)
![bottom nav image](docs/screenshots/gallery_mobile.png)
- On desktop, the links that are present in the mobile bottom navigation are instead added alongside the 'My Profile' button in the top navigation bar
![top nav only](docs/screenshots/gallery_desktop.png)

#### Contact page.

- If user is not logged in:
	- Form has fillable Name/Email/Message fields
- If user is logged in
	- Form has read-only, pre-filled username/email fields for current user
	- Has fillable message form
- All messages sent from contact form send messages to site developer's email    

### User Pages

#### Register / Login

- Both the Register and Login pages have a simple, clean form asking for username / password
- Register form asks for email and password confirmation
- Both pages link to each other if user is already registered / not registered yet
- Both pages link to contact page
- Login page links to a password reset page, if user has forgotten their login password

#### Password Change Request

- Request page features a single email field for users to request a password reset link
- Feedback is given to check your email regardless of whether it is a registered email or not for security reasons (not identifying whether an email is registered or not)
- If it is a registered email, a link with a JWT token is sent to the user's email
- This link leads to a Password Change form with two password fields to type and confirm the users new password

#### Profile

- Displays user's chosen avatar
- Displays any bird photos user has uploaded
- Displays any birds this user has liked / favorited
- If user views their own profile, they see links to:
	- Change their avatar
		- Here you can choose from 10 bird themed user avatars
	- Edit your account
		- Here you can change your username or email 
	- Delete your account 
		- Presents a screen to confirm your password in order to delete your account, along with any of your uploaded birds/comments

### Bird Pages

#### Bird Profile Page

- Displays a larger thumbnail photo of the bird, without cropping to card aspect ratio
	- This image features a link to see original, user upload full-size image
- Displays photo info: Bird Type, Camera Type, User Name, Upload Date and Liked By
- If current user is photo's owner, then displays buttons to edit or delete photo of bird
	- Edit Bird Photo will load a form with any information pre-filled
	- Uploading a new photo will replace the previous Photo in Bird Friend's cloudinary database
	- Delete photo will ask user's to confirm before deletion

- Otherwise displays text prompting current user to leave a comment   

#### Comments

- Displays avatar of comment author and name, both of which act as a link to their user page
- Displays comment content and date comment was added
- If current user is author, it displays edit and delete comment buttons
	- Edit comment will navigate to a text entry, pre-filled witih the comment user is editing
	- Delete comment will display the comment text as a blockquote and ask user to confirm delete

### Admin

- There is an admin user account which has permissions to delete or edit any user, photo or comment on the site
- A preview of the admin account on the gallery home page will show edit/delete options for all uploaded photos of birds, which are normally hidden unless the uploader is the current user:
![admin_view](docs/screenshots/admin_view.png)
- Links for deleting/editing comments and users are also shown in this way for admins.

### Custom Error Pages

- I have created an error pages using the flask app_error handlers
- Each page contains a reason for the error and a navigation link to return to the previous page, along with a humourous image of a sad bulldog in a dress. Errors are:
	- 404 - not found an error
	- 403 - no permission error
	- 500 - server error.

### Features left to Implement.

## Technologies used.

### Flask

- The application was built on the Flask framework. 
- I followed [Corey Schafer's guide on YouTube](https://www.youtube.com/watch?v=Wfx4YBzg16s) in using Flask Blueprints to split my application up itno the following modules:
	- main
	- users
	- birds
	- errors
- This makes it easier to find routes and elements if they need to be updated or changed.
- The templates folder is also split into a similar structure.
	- base.html 
	- /main
	- /user
	- /bird
	- /email
	- /errors
- App configuration settings are contained within ``` config.py ```
- Inside the  ```__init__.py ``` file I've created the app as a [Flask application factory](https://flask.palletsprojects.com/en/1.1.x/patterns/appfactories/).
- Then in the ``` app.py ``` file, the application factory is imported and the function is the invoked ie. ``` app = create_app() ``` which creates the application.

#### Flask extensions used

- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
	- Flask micro framework was used to build the web app using python code.

- [Flask-login](https://flask-login.readthedocs.io/en/latest/)
	- Flask login was used to manage logged in users.

- [Werkzeug](https://werkzeug.palletsprojects.com/en/1.0.x/utils/#module-werkzeug.security)
	- Werkzeug Security Helpers were used to hash the user passwords before storing in the database

- [Flask-Mail](https://flask-login.readthedocs.io/en/latest/)
	- For sending emails relating to the contact and password reset forms
		- For the Heroku deployment, I used the Heroku Sendgrid extension instead, as Flask-Mail was giving me the error `SMTP AUTH extension not supported by server`, although it worked locally.

- [Flask-Mongoengine](http://docs.mongoengine.org/projects/flask-mongoengine/en/latest/)
	- For interacting with the MongoDB database

- [Flask-Wtf](https://flask-wtf.readthedocs.io/en/stable/)
	- For creating forms and adding validation

- [Gunicorn](https://gunicorn.org/)
	- To help deploy the app to Heroku

### TailwindCSS

- [TailwindCSS](https://tailwindcss.com/docs) was used extensively as the primary method of styling the application
- I installed Tailwind by initialising an NPM package within my static folder with `npm init`
- I then ran the following NPM installs within the terminal: `npm install -D tailwindcss@latest postcss@latest autoprefixer@latest postcss-cli` to install the necessary dependencies
- I ran `npx tailwindcss init -p` to create both my tailwind and postcss config files 
- I created two .css files - app.css & compiled.css
- Within app.css I placed the tailwind directives to inject Tailwind's styles into the CSS file:
```
@tailwind base;
@tailwind components;
@tailwind utilities;
```
- I then included a PostCSS command wihtin my package.json to compile the Tailwind libraries into a usable CSS file: `"build:css": "postcss css/app.css -o css/output.css"`
	- Any time that I made custom CSS changes or additions within my app.css or tailwind.config.js files, I would run this command to recompile my CSS file and then complete a hard refresh within my browser to update the changes
- Before deploying the site to Heroku, I ensured that `purge` was set to `true` within my tailwind.config.js file. This ensures that only the necessary classes are compiled in the final CSS file used by my web page, minimising the amount of CSS that the browser has to load as much as possible.

### Cloudinary

#### Cloudinary Upload API

- In adding user images to the website, I utilised the [Cloudinary Upload API](https://cloudinary.com/documentation/image_upload_api_reference)
- Within my Cloudinary account, I set up a hot_dogz folder.
- Within my Bird model I added a method to save uploaded user images into this folder under the format `hot_dogz/{user}/{pk}`
	- All of of a user's bird photos would be saved within one folder, named after the user's username
	- Each bird's photo would be named after it's primary key
- If a user deletes a bird photo or deletes their profile, then the bird photo is deleted from the cloudinary database using the built-in `uploader.destroy()` method. 

#### Cloudinary Transformation URL API

- Within each Bird collection, I added two additional image URLs which utlised the Cloudinary transformation API. These make on-the-fly changes in how the image is rendered on the web page.
	- One URL for displaying image thumbnails on the bird's profile page
	- One URL for displaying at a fixed aspect ratio within the bird card component
- For the `img_url_thumb` i added the transformations: `w_500,c_scale,q_auto:low`
	- Width: 500px
	- Crop: scale
	- Auto render in low quality for smaller file size  
	- These transformations dramatically reduce file size. Here is an example file size difference between clicking on the original full-size image vs what is rendered on a dog's profile page (from 2.95MB to 21.85kb)
		- [Before transformations](docs/screenshots/trans_before.png)
		- [After transformations](docs/screenshots/trans_after.png)

- For the `img_url_card` I wanted images to be a fixed size of 350px x 525px, so I used the transformations `c_fill,g_auto,h_350,w_525,q_auto:low`
	- Crop is set to fill
	- `g_auto` = Gravity set to 'auto'. The 'gravity' transformation determines which part of an image to focus on and decides where a crop should be made
	- Setting it to 'auto' leaves Cloudinary's AI decide where to crop the image, which generally focuses on a dog's face. An example can be seen here:

**Without gravity**:
![Without gravity](docs/screenshots/without_gravity.png)
**With gravity set to 'auto'**: 
![With Gravity set to 'auto'](docs/screenshots/with_gravity.png)


### Other Tools, Libraries & Programs

- [Font Awesome](https://fontawesome.com) - For icons used throughout the site
- [GIMP - GNU Image Manipulation Program](https://www.gimp.org) - For image editing
- [favicon.io](https://favicon.io) - For creating favicon .ico
- [Google Fonts](https://fonts.google.com) - for importing chosen fonts
- [Balsamiq](https://balsamiq.com) - For creating my wireframes
- [QuickDBD](https://app.quickdatabasediagrams.com) - For creating my DB schema diagram
- [Am I Responsive?](http://ami.responsivedesign.is) - For creating the mockup image at start of README
- [VSCode](https://code.visualstudio.com) - My primary code editor of choice for the project
- [PyCharm](https://www.jetbrains.com/pycharm/) - Secondary code editor, used particularly for additional PEP 8 compliance functionality

## Testing

**[Please see TESTING.md](TESTING.md)**

## Deployment

### Requirements To Deploy:
- Python3
- Github account
- MongoDB account
- Heroku account

### Cloning This Project:
To create a clone, follow the following steps.

1. Log in to GitHub and go to the repository.
2. Click on the button with the text “Code”.    
3. Click “Open with GitHub Desktop” and follow the prompts in the GitHub Desktop Application or follow the instructions from [GitHub](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to see how to clone the repository in other ways.

#### To Work With Your Local Clone:
1. Install all the requirements:
	- Go to the workspace of your local copy.
	- create a virtual environment with `python3 -m venv venv`
	- Activate your virtual environment with `source venv/bin/activate`
	- Install requirements from requirements.txt file with `pip install -r requirements.txt`

2. Create your database in MongoDB.
    1. Signup Or Login For [MongoDB](https://www.mongodb.com/)
    2. Create a cluster as well as a database.
    3. Create the following collections in the Database:
        1. bird type
        2. camera type
        2. comment
        3. bird
        4. user
3. Create a file in the root directory called ".flaskenv". This will contain all of your envornment variables. Your .flaskenv file should look similar to the following:
```
FLASK_APP=run.py
FLASK_DEBUG=[0 for off, 1 if you want to run flask debug mode locally]
SECRET_KEY=[random string]
MONGO_URI=mongodb+srv://[mongoDBusername]:[mongoDB password]@[clustername].wijab.mongodb.net/[database name]?retryWrites=true&w=majority
MONGO_DBNAME=[mongoDB database name]
CLOUD_NAME=[cloudinary username]
CLOUD_API_KEY=[cloudinary API key]
CLOUD_API_SECRET=[cloudinary API secret key]
CLOUDINARY_URL=[cloudinary connection URL]
MAIL_SERVER=[your mail smtp string, i.e. 'smtp.googlemail.com' if using gmail]
MAIL_PORT=[587 if using TLS, 465 if using SSL]
MAIL_USE_TLS=[1 if true, 0 if false (if false then set MAIL_USE_SSL=1 instead)]
MAIL_USERNAME=[email username, i.e. #####@gmail.com]
MAIL_PASSWORD=[login password for email]
```
4. Make sure that .flaskenv is included in your .gitignore file. It should be included already in cloned file
5. To read your environment variables from your .flaskenv file, you must ensure that you have installed Python-dotenv within your virtual environment: `pip install python-dotenv`. This should have alreayd happened when installing requirements earlier

### Deploying To Heroku

To deploy our application on Heroku, we are required to have a requirements.txt file as well as a Procfile. These files will allow Heroku understand 
what dependencies are required to run the application, as well as tell Heroku which file to run, to launch the application.

#### Create a procfile:
- Within your root folder, type in the terminal `touch Procfile` to create the Procfile
- In your IDE, insert the text `web: gunicorn run:app` in your Procfile and save
	- gunicorn should have been installed via pip earlier 

#### For Deployment:
1. Open [Heroku](http://heroku.com/).
2. Login or signup for Heroku.
3. Once logged in create a new app and select the desired region. 
4. Deployment method "GitHub" (if this section is accidentally missed, you can use the tab selection within your dashboard "DEPLOY")
5. Select "connect to GitHub" and follow the on screen instructions. Once connected to your Github:
   
    - Search for your repository using the form provided.
6. Once you have connected your GitHub repository:
    - Navigate to the "Settings" tab:
        - Scroll to the section "Config Vars" here you will have to tell Heroku what these variables are:
            - Input all data found in .flaskenv file into the config var section
    - Navigate back to the "Deploy" tab:
        - Scroll to the "Manual Deploy" tab:
            1. Select the branch you wish to deploy (master is default)
            2. Click the "Deploy Branch" button. (This may take some time as Heroku uploads the app to their servers.) 

- Once the build is complete, a "View App" button will appear just below the build progress box. You can click this to see immediately if the build was successful. If the app doesn't load first time, try refresh once prior to investigating further.

- Common issues include outdated requirements.txt and/or missing Procfile, if errors occur, check these are both correct before investigating further


## Credits

### Code
- HUGE CREDIT TO CJCON90 FOR PROJECT IDEA AND DESIGN INSPIRED COMPLETELY BY IT
- HUGE CREDIT TO REBECCATRACEYT FOR README.MD DESIGN, INSPIRED COMPLETELY BY IT
- My navbar designed was inspired by [this post on TailwindComponents by sebageounity](https://tailwindcomponents.com/component/bottom-and-header-nav-responsive)
- Form design was inspired by [this post on TailwindComponents by darkcris1](https://tailwindcomponents.com/component/facebook-login-page)
- Most of my Flask code and knowledge was inspired by Miguel Grinberg's [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
- Flask knowledge was also supplemented by Corey Schafer's [Python Flask Tutorial on YouTube](https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH), particularly the [use of Blueprints](https://www.youtube.com/watch?v=Wfx4YBzg16s&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&index=11)

### Content
