# Med Manager App
 
## Overview
 
This website was designed as a tool to help people manage medication. It can be used either for personal use or by a carer, to help them organise their patient's medications. 

It is often the case that when patients present to their medical practitioner, either GP or specialist, that they do not have a list of their medications at hand. Many people are not aware of what medications they take regularly, who prescribed them, why or when. This makes it difficult for medical practitioners to alter patient medication. Similiarly it is difficult for the patient to adhere to their treatment plan. People are at risk not only of missing vital medication but also of overdosing on medication. 

Read below to find out how the Med Manager App aims to reduce these risks and increase medication saftey and adherence. 

 
 

 
### UX

Megan: I am a 41yr old woman personal carer to my elderly mother, Mary, who has severe rheumatoid arthritis. Mary takes over 20 medications per day, with different medications due at different times each day. Her medication list changes frequently as she is in and out of hospital. It is difficult to keep track of her medications from one day to the next. The Med Manager app allows me to create a list of my mother's medications including doseage, administration time and even who the prescriber is. I can add and delete medications as needed and even change the doseage. The 'NOW' feature tells me exactly which medications Mary is due at any given time so it is less likely that I will give her the wrong medication or miss a dose. 

John: I am a 75yr old widower with some memory problems and heart troubles. I have to take lots of different medication every day for my high blood pressure. When i use my med manager app, it reminds me what day it is, what time it is and what medications i have to take at that time. I can check off my medications as i take them so i dont take the same medication twice by accident, which could be very dangerous for me. I can also check what date my prescription expires so i know in advance when i have to fill a new one. When i visit my GP or my cardiologist, I have an uptodate list of my medications with me. 
 
Sarah: I'm a 35yr old emergency doctor. Often patients arrive to the emergency department alone or confused. It can be impossile to get a list of a patients medications outside of normal working hours. If a patient is using the Med Manager app, I can see exactly what medications they are taking and have a good idea of what illnesses they have. This saves time and allows for quicker treatment. I can also update the list before the patient is discharged home to allow for any changes in hospital. 


## Features
 
### Existing Features
-Home page with clear, easy navbar links to website pages.
A large 'lets go!' button on the centre of the homepage which will bring you directly to your medications due at real time. 
The homepage describes some features of the app with links to these features and hover-sweep-to-bottom effect. 
Writing overlays a grayscale picture of an elderly gentleman using the app. 

The "NOW" link will bring the user to a page displaying real time date, day and time with a clear list of mediations due with doseage. The user can clear the list after they have taken the medication and click the 'show medication list' button if they wish to see the list again.

The 'Add Medication' link in the navbar will render a form to add a new medication. This includes a pop up calendar to save date prescribed and discontinued.

Edit Medications- this link will bring you to a list of all current medications. When each individual medication is clicked on, an accordian opens to reveal all details of that medicatiion. An edit and delete button will appear. The edit button will bring you to a form prefilled with that medications details. You can now change any details and save the form again to save the changes. Alternatively you can click the delete button to delete the medication from the list (and from the database).
This page also has a large red button which will bring you to the 'add medication' page. 

The "Week" link in the navbar will navigate to a list of medications by day and time. By clicking on each day and accordian will open with medications divided into subsections of time_of_day, morning, afternoon, evening and night. 

I used @media query to adjust text size according to VPW to make the website more responsive. 
### Features Left to Implement
- Ideally i would like to create a second collection in the database that would hold 'deleted medications' for future reference. 
- I would like to have a further collection which would hold a patient medication allergy list. 
- I would like to implement a function so that medications past 'date discontinued' would move to a separate collection, again for future reference. 

## Tech Used

### Some the tech used includes:
- **HTML**, **CSS** , **python**,  **JQuery**

[FLASK](http://flask.pocoo.org)
  - I used the framework flask and jinja2 templating for python. 
  - 
[PyMongo and MongoDB]
   - I used PyMongo to work with my database in MongoDB
 

[JQuery](https://jquery.com)
    - I used jquery  for the following functions:
    - sidebar nav which is collapsible
    - 'hide'and 'show' function to hide and display medication list onclick
    - 'datepicker' for the pop up calendar
    -'select' to select days of the week for drug administration
    

[Materialize]
    - I used Materialize as an alternative to bootstrap to give a simple responsive layout:
    (https://materializecss.com/about.html)


   
     
Libraries:

Fontawesome- (https://fontawesome.com/)
Hover.css- (http://ianlunn.github.io/Hover/)
Google Fonts- (https://fonts.google.com)


## Testing
- Prototype code was written and tested using jasmine
- All code used on the site has been tested to ensure everything is working as expected
- Site viewed and tested in the following browsers:
  - Google Chrome
  - Opera
  - Microsoft Edge
  - Mozilla Firefox

## Contributing


## Deployment
 
### Getting the code up and running
1. Firstly you will need to clone this repository by running the ```git clone <project's Github URL>``` command
2. After you've that you'll need to make sure that you have **npm** installed
  1. You can get **npm** by installing Node from [here](https://nodejs.org/en/)
4. After those dependencies have been installed you'll need to make sure that you have **http-server** installed. You can install this by running the following: ```npm install -g http-server # this also may require sudo on Mac/Linux```
5. Once **http-server** is installed run ```http-server -c-1```
6. The project will now run on [localhost](http://127.0.0.1:8080)
7. Make changes to the code and if you think it belongs in here then just submit a pull request

## Credits

### Media
- The photos used in this site were obtained from [Unsplash](https://unsplash.com/)

### Information

No external information sources were used. 

