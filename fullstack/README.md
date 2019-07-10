## Test Capture and Replay

### Goal

The main aim of the assignment is to develop a tool that allows manual quality analysts to capture a simple user flow for their webapp on browser, and then allow them to replay it back.The assignment is kept little open ended as we would love candidates to think about it and ask questions to form a proper bound around it.

### Directions

There are two separate components of this assignment

- A module responsible to capture the user flow on the web browser.

  One of the ways to solve this problem is to build a chrome extension, that let users start a capture session, then start recording whatever actions user is taking and store them as list of steps in the backend.

- A module to replay the user flow

  There are bunch of solutions that can be used for this -> for eg selenium, casperjs, puppeteer etc. You can use any of these tools to open the webapp, loop over the steps in the user flow and execute them using the api provided by these tools. I would recommend use Casperjs as its quite simple

### Features

- A user interface that allow users start a new test recording

- Automatically open that url in another window and let user interact with it normally

- Record user actions like "enter text", "scroll" and "click". The main challenge here is to identify the locator to be used for the element that is to be interacted with. Keep care that the locator you use, needs to be unique otherwise there will be conflicts during replaying. Some of the locator strategy that you can use is

  - id
  - name
  - other attributes
  - css selectors
  - xpath

- Let user stop recording and save the user flow with a name, description and any necessary settings

- A simple backend that provides an api to store the testcase. For now you can just store it as a json file on the file system

- A user interface that allows user to replay a recorded user flow.

- A backend api that initiates the run of user flow

- A casperjs/selenium/phantojs script that reads the saved test recording and executes it.

### Example Flow

An example user flow that you can record is google search.

    + Go to google.com

    + Enter text "Pirlo.io" in inbut box with name "q"

    + Click "Google Search" Button

    + Find the search result with heading "Pirlo.io" and click it

An example yaml file is given that represents this user flow at "google-search.yml". This is just an example format and you are free to use any representation that works for you.

### Deliverables

This is a fairly challenging task, so we are not expecting a full fledged solution. Rather our expectations is a working solution that can capture a simple user flow and then replay it back. We would love if you can document your expectations, the features that it supports and some thoughts on what are the major challenges to develop a full fledge solution and how you think you will approach it.

- A chrome extensions that records user actions

- A backend service that provides two api'

  - Store a user flow
  - Replay User Flow

- A script that replays the user flow.

- Readme file to let us know how to run the app

- Any other documentation that you want to share.

### Instructions

- Take 2-3 days to work on this assignment

- One of the key challenges of this assignment is identifying locators for elements that user interacts during the user flow

- We would like you to complete the entire flow and then optimize on individual components, in case you lack time

- Abstractions and code style is not most important but a well written code with good abstractions will definitely make the project more appealing

- Good Design / UI is not important but definitely has bonus points

- This will be followed by an interview where you will be asked to explain your decisions and asked to describe about challenges and opportunities with your solution

- Most importantly, have fun building it :) :)
