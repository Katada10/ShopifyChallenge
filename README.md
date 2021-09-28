OVERVIEW & USE INSTRUCTIONS

This is an app which uses Flask, a Python framework, and Firebase to allow a user to add images to a repository.

The user chooses files on the main page, then adds them. The app will upload the images to the ImageKit Content Delivery Network, and will store their uploaded URL's in a Firebase Real Time Database. The user is then redirected to another page which displays the image by retreiving all the URL's from Firebase and loading them into an HTML <img> element. This was intended to be a global image repository, meaning all users can see what any user uploads. 

Use the file picker choose the images you want to add, then press "Add Images". This will take you to a new page where any images you add, as well as any images added by someone else will show. 

HOW TO RUN

-- This app requires flask and firebase. See instructions below on how to install --

1 - Open a command window in the root directory and use the command "FLASK_APP=main.py".
2 - Enter the command "flask run" or "python -m flask run". This should deploy the app on localhost and specify the port, usually 5000. 
3 - Open your web browser and type localhost:5000 or whichever port was used by flask, and the main page should show. 


INSTALLING FIREBASE AND FLASK

* This assumes your system already has Python 3.x installed *
 
1 - Open a command prompt and type "pip install Flask"
2 - Next, type "pip3 install firebase_admin"
3-  Type "pip3 install imagekitio"
4 - You should now have all required dependencies.
