# MarkovMe
Software Engineering Fall 2017 Final Project
By Krishna Gaire and Lucas Futch

## Purpose and Goals

The purpose of this project is to develop and refine the skills of implementing a Software Engineering project. Our project consists of Markov Chain natural language processing, where we the training data for the process will consist of personal user information, coming from places such as Facebook posts, Twitter Tweets, or user provided text input.

Our goals for this project include creating a release deliverable that users can interact with, and easily obtain their desired output. In our case, output would be sentences that are developed from the training data. We also want to better understand the stochastic process behind the Markov Process, to better apply it on our models and project.

## Requirements:

  * Python 3.0 or greater  
  * pip3

## Running The Code

Run `pip3 install -r requirements.txt` to install all required python packages to run the server.

Run the main.py file. It will create and begin a server. Go to `localhost:5000` on a web browser and have fun with the markov text generator. 

## Using the Page

There main page has the instructions on how to use the page, as well as the buttons that are used for each different input. 

The Facebook flow will begin witht he first button, prompting the user to first log in. Once this is done, the user can generate a post, first waiting for their timeline to be parsed. The data is stores locally so that the user does not have to wait to get more Facebook posts while in the same session.

The Input flow requires a user to give enough text, and will be prompted if there is not enough data to generate a post. The text can come from any source, such as that of an essay, a book, or any other place the user can copy text from.

The Twitter flow has the option to enter two Twitter handles, but it still works with just one. The Twitter handles are taken and the users are parsed for their tweets, so both of the given users need sufficient data in their profiles to generate a tweet.

## Wiki Links

[User Stories and Use Cases](https://github.abudhabi.nyu.edu/lf1345/finalProject/wiki/User-Stories-and-Use-Cases)

[Release History](https://github.abudhabi.nyu.edu/lf1345/finalProject/wiki/Release-Library)