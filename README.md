# MarkovMe
Software Engineering Fall 2017 Final Project
By Krishna Gaire and Lucas Futch

The purpose of this project is to develop and refine the skills of implementing a Software Engineering project. Our project consists of Markov Chain natural language processing, where we the training data for the process will consist of personal user information, coming from places such as Facebook posts, Facebook Messenger messages, or play/movie scripts.  

Our goals for this project include creating a release deliverable that users can interact with, and easily obtain their desired output. In our case, output would be sentences that are developed from the training data. We also want to better understand the stochastic process behind the Markov Process, to better apply it on our models and project.

## Running The Code

Requirements:
  * Python 3.0 or greater  
  * Install flask for  python `sudo pip3 install flask`
  * Install markovify `sudo pip3 install markovify`

Now run the main.py. It will create and run a server. Then go on to http://0.0.0.0/5000 and have fun with the markov text generator. 

## v.01
For v.01 click on Login With Facebook Button. It will redirect you to login with facebook which will allow us to get your timeline posts. 

## v.02
When you open the page, you are greeted with four buttons to press. Login with Facebook to be able to pull your posts, done with the second button and which displays the posts. The third button provides a document upload form, which is intended to accept text files of data to be analyzed. This has been not implemented. Fourth button is intended to get data from your messenger. This also has not been implemented yet. 

## v.03

Finally, the app is approved by Facebook. We still have four buttons. Login with Facebook will ask you to login with your facebook and ask permission to allows us to use your timeline posts. Press OK to give us the permissions. Then you can click the Get My Predicted Posts button. It will take couple of seconds for us to collect your facebook posts. After that you will be presented with your predicted post on the webpage. 
