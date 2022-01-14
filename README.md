## Editor Project | Flask  | AWS EC2  | Apache & WSGI
##### Haris Nasir
###### Local Dev enviroment is Ubuntu 20.04 Oracle-VB VM

This is a flask project being hosted on AWS. The documentation below is a step-by-step walk through of hosting our flask application to AWS EC2.
We will use Ubuntu 20.04 server on the EC2 instance and set up Apache2 as the webserver. WSGI will be itigrated to allow webserver to forward requests to our flask app.

__We will begin by signing into AWS and creating our free tier EC2 instance.__\
For your EC2 instance, choose:
* Ubuntu 20.04 Server
* type: t2.micro
* Default settings except for Step #6 (Config Security Group)
  - Click "Add Rule" and Select HTTP (port 80).
  - You can name this security group inorder to reuse it for future instances.
* Download the key and save it to the local "~/"
* Click "Launch"

__Once the EC2 instance is initilized, lets apply a static public IP address to the instance.__\
Make your way to the EC2 console.
* Open navigation pane on the left.
* Under "Network & Security" Select "Elastic IP’s"
* If you don’t already have an Elastic IP
  - On the top right click "Allocate Elastic IP Address" 
* For Resource type, choose "instance"
* Now choose the EC2 instance we created in the previous section.
  - This will associate the Elastic IP address to that instance
* Click "Associate" at the bottom right.

_Now we have a static IP for our EC2 instance_
*	Navigate back to EC2 instances dashboard
*	Click on our EC2 instance to select it & click Connect at the top right 
*	Navigate to the SSH Client section

__Connect to EC2 Ubuntu Server from the local environment.__
*	Open terminal.
 - Navigate to the security key we downloaded.
* We must change the security key mode so it is not publicly viewable 
  - The SSH client window has the command for this
  - ```chmod 400 yourkey.pem```
* The Example command is given to connect to the EC2 Ubuntu Server through our terminal.
  - ```ssh  -I  “yourkey.pem”  ubuntu@ec2-yourElasticIP.compute-1.amazonaws.com```
*	You should now be in your EC2 Ubuntu server from your local terminal.

__Setting up EC2 Ubuntu Server for hosting flask app.__\
At first, we will download base packages required to host a simple flask app for testing, then we will set up git to pull our project from GitHub and host it. 
We will use Apache as the web server and WSGI so apache can forward requests to our flask application.

* ```sudo apt-get update```
*	```sudo apt-get install python3```
*	```sudo apt-get install python3-pip```
*	```sudo apt-get install apache2```
*	```sudo apt-get install libapache2-mod-wsgi-py3```
*	```sudo apt-get update```

___Now that the base requirement programs are installed lets quickly create a basic flask app to host and test.__\
_As a reminder we are still in our EC2 Ubuntu server._
* ```cd ~ ```
* ```mkdir FlaskDir```
* ```cd FlaskDir```
* ```sudo -H pip3 install flask```
* ```vi myApp.py```
  - ```from flask import Flask
	     app = Flask(__name__)
	     @app.route(‘/’)
	     def home():
		    return “<h1>Hello from Flask</h1>”
	     if __name__ == “__main__”:
		    app.run()```

* ```vi myApp.wsgi```
  - ```import sys
       sys.path.insert(0, “/var/www/html/FlaskDir”)
       from myApp import app as application```
* Delete any files or directories in /var/www/html/
  - ```sudo rm -r /var/www/html/*```
* Copy basic flask app files to /var/www/html/
  - ```cd ~```
  - ```sudo cp -r FlaskDir /var/www/html```

__Configure apache to host the flask app.__
*	```sudo vi /etc/apache2/sites-available/000-default.conf```
* Comment out the line beginning with  “DocumentRoot”
* Under the “DocumentRoot” line enter the following:
  - ```
       WSGIScriptAlias  /  /var/www/html/FlaskDir/myApp.wsgi
	   <Directory  /var/www/html/FlaskDir>
	     Order allow,deny
	     Allow from all
	   </Directory> 
     ```
* Restart apache server 
  - ```sudo systemctl restart apache2```
* Now from any web browser put in the public elastic ip address and you should see your basic flask app. 

__Getting git setup and pulling my flask application to host.__
* ```cd ~```
* ```sudo apt-get install git```
* ```sudo apt-get update```
* ```git config --global user.name "yourGitUserName"```
* ```git config --global user.email yourGitAccountEmail@email.com```
* ```git clone https://github.com/sirharis214/EditorProject.git```
* Now you should have a Directory in ~ called EditorProject

__Host the Flask Project by replacing the contents of our sample flask app from /var/www/html/FlaskDir/  
with the contents of our actual flask project in ~/EditorProject__\
* ```cd ~```
* ```sudo rm /var/www/html/FlaskDir/myApp.py ```
* ```sudo cp -r  ./EditorProject/*  /var/www/html/FlaskDir```
* ```cd /var/www/html/FlaskDir```
* ```sudo chmod 777 uploads/```
  - This is important so our python script can read the txt file the user uploads
* ```sudo systemctl restart apache2```







