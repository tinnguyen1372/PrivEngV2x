# PrivEngV2X

NTU Summer Project: Privacy-aware service provisioning in V2X networks. 

A website of a project on driver's behaviors using Machine Learning and Deep Learning techniques. With only the input data of starting location, heading, speed and acceleration in each second, this model can predict the location based on x and y direction in every second of the journey, without using GPS.

This web application make use of a backend system using NodeJS, MongoDB Database and Flask (Python) to receive location data continuously from a moving vehicle in real time, which will later be processed by deep learning model and displayed on frontend map with little delay.

For demo purpose, please find your data attached in the sample_data folder.

You will need to install the required Python libraries in order to run this project.


**Full guide:**

### Configure our project for the first time


You will need two machines: One for receiving data from the vehicle and uploading to the database, and one to retrieve data from the database and run the web page.

Once you are ready, please follow the instructions below:

- Download and extract the code from this repository.

- Make sure you have installed python3 and pip3 on both your machines. Then, in the project directory, run this command line:

### pip3 install -r requirements.txt

### This will install all the dependencies needed for all except live mode.

(In case of any error, please delete the requirements.txt file and run "pip3 freeze > requirements.txt". After that, run "pip3 install -r requirements.txt").


Please make sure you also have installed the latest version of node and npm on your machine.

If not, please download and follow the guides in this link.

Verify the installation by running npm -v.

Open a new terminal (we still keep anaconda terminal). Suppose you are in the main directory of this project. On the server machine, run these in the command line:


### cd mongodb

### npm install nodemon mongodb mongoose express path body-parser cors config fs (Only need to run in the first time)

### node server.js

If the terminal display: 'Listening on port 5000' and 'MongoDB Connected ...', then you are doing well. If not, please check the instructions again. You can close this terminal now.



### Run PrivEngV2X


Once you have completed the installation above, you can now start our web on our localhost.

Just type in the conda terminal this line:

### conda config --prepend channels conda-forge

### conda create -n ox --strict-channel-priority osmnx

### pip install flask

### pip install livereload

### python3 app.py 


If there is no error, you should be directed to the web now. If not, please try to access this link.

You can now use most of the functions, which include offline mode, except live mode.


### Run Live Mode


Last but not least, live mode. Please make sure you have completed all two previous steps.


You need to create a new terminal in the project directory. Just type in the terminal these lines:


### cd mongodb

### node server.js


If there is no error, you should see 'Listening on port 5000' and 'MongoDB Connected ...'.


Now, on the web, go to the Live Trajectory page (or you can go to localhost:5000).

Now, we would define the machine that receives data from the web as the server machine, and the machine that displays the web to the client as the client machine.


On your server machine, click the first green button: "Upload data to database".

On your client machine, click the second blue button: "Get data from database".

You should see the page is loading continuously, and the terminal is displaying a long list of "Uploaded!" and "Got data".

This terminal is solely for live mode trajectory.

If you don't use it, please stop the mongodb process by Ctrl + C in the terminal.



