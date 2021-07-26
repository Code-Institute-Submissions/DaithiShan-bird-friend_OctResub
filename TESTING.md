# Testing

## Table of Contents

  * [Functionality](#functionality)
    + [Navigation](#navigation)
      - [Navigation Bar](#navigation-bar)
    + [Main](#main)
      - [Landing Page](#landing-page)
      - [Gallery](#gallery)
      - [Contact](#contact)
    + [User Pages](#user-pages)
      - [Login / Register](#login---register)
      - [Avatar Selection](#avatar-selection)
      - [Reset Password](#reset-password)
      - [User Profile](#user-profile)
    + [Dog Pages](#dog-pages)
      - [Dog Page](#dog-page)
      - [Comments](#comments)
    + [Error](#error)
  * [Performance](#performance)
  * [Validators](#validators)
    + [HTML](#html)
    + [CSS](#css)
    + [JavaScript](#javascript)
  * [PEP8](#pep8)
  * [Compatibility](#compatibility)
    + [Hardware](#hardware)
    + [Browsers](#browsers)
  * [User Stories](#user-stories)
    + [New Visitor](#new-visitor)
    + [Repeat users](#repeat-users)
    + [All users.](#all-users)
    + [Website owner](#website-owner)
  * [Known Bugs](#known-bugs)
    + [Flask-Mail](#flask-mail)

<small><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></small>

## Functionality

### Navigation

- All links have been tested throughout the website with no broken links discovered
- Links throughout the website have hover and focus effects with no accessibiliity issues arising in testing.
- On attempting to access links that reguire a user login, page will redirect to login screen and successfuly flash to user that login is required
- On attempting to access pages the user does not have permission to, user is successfully redirected to home and a flash explaining to user that they cannot access that page

#### Navigation Bar

- Navigation successfully shows correct nav items whether user is logged out / logged in

	- Logged out: Login, Register, Contact
	- Logged in: My Profile, Gallery, Upload, Contact, Logout

- Once the user is logged in, on screens below 768px wide, navigation successfully switches from top navigation bar only to a mix of top and bottom nav bars 

### Main

#### Landing Page

- Landing page correctly displays:
	- Vertically, with text over the main image, if users are on a portrait viewport
	- Horizontally, with text to the left of the main image, on landscape viewports
- Landing page is successfully skipped if user is logged in, and any links leading to the landing page (such as the Hot Dogz icon in the top navigation) redirects to the main gallery page

#### Gallery

- Gallery page successfully displays all images in a small image of fixed size 525x350px
	- This image successfully auto-crops using Cloudinary AI
- Gallery page successfully displays a maximum of 6 photo cards per page
- Pagination successfully allows user to navigate between photo cards and see all uploaded photos, beyond the initial 6 shown on page 1
- Liking a photo of a bird successfully increases its count and alters its position in the displayed cards (if user is on the view sorted by popularity)
- Favouriting a bird photo successfully adds that photo to a user's profile
- Photo cards correctly display different data depending whether current user has uploaded that photo
	- If yes: displayes links to edit & delete bird photo pages
	- If no: displays the uploader's profile name

#### Contact

- Tested sending messages from contact form
- Messages successfully received in my/developer's linked gmail using Flask Mail

### User Pages

#### Login / Register

- Login & Register functionality has been extensively tested by both myself and real user sign-ups
	- as of writing this, there are XXX registered accounts with no reported issues of being unable to register or log in to the site

- Form validation works successfully, requiring
	- username between 2-12 characters
	- valid email address format e.g. email@domain.com
	- matching passwords on registration

- Validation message for any form input errors are clearly displayed to the user  

#### Avatar Selection
- On initial register, user is successfully directed to bird avatar selection screen
- If user exits out of this without selecting an avatar, a random bird avatar will be assigned to them 

#### Reset Password
- Reset password has been tested as working on my own registered user accounts
- Email is sent from david.shanahan.burns@gmail.com
- Link to reset user password works whether link is clicked directly from email, or pasted into browser address bar
- Reset password requires matching password validation, with any error messages clearly given to user  

#### User Profile

- All user uploaded bird photo cards and saved bird photo cards display successfully on the user's profile page

- User can successfully edit own profile
	- Existing information is pre-filled into edit profile form

- User can successfully delete their own profile
	- Password confirmation is requested prior to deleting own profile
	- Deletion of a profile successfully deletes any associated bird photos, along with any uploaded bird photos in admin's cloudinary account

	- Deletion of a profile successfully frees up that username and email for future user registration

### Bird Photo Pages

#### Bird Photo Page

- Bird photo image of fixed width 500px and original aspect ratio correctly displays on bird profile page

- Page correctly displays correct data depending on whether is a user uploaded photo:
	- if yes: edit and delete buttons
	- if no: no such functionality exists

### Error

- Successfully encountered 500 and 404 error pages during testing
- Back button successfully links user back to previous page

## Performance

## Validators

### HTML

### CSS

### JavaScript

## PEP8

## Compatibility

### Hardware

### Browsers

- **As site is built with Tailwind v2.0, it is not compatible with Internet Explorer**

## User Stories

### New Visitor

### Repeat users

### All users.

### Website owner


## Known Bugs
