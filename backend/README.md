## Selenium Test Generation

As part of your assignment you are required to develop a test generator that takes the
test description as a yaml file and generates a `py.test` based project with test scripts for each
of the different tests specified inside the yaml file. An example test scenario file is provided
as a sample within this repoistory called test.yml. Given this as an input, we expect the `testgen`
project to generate a test project similar to "google_test" with a proper `requirements.txt` file as well a `conftest.py` and a tests folder with test scripts

The assignment is fairly open ended and we encourage you to ask as many questions as you want
The example test_script `test_no_result_found.py` is for your reference and has been handcrafted.
The code that you generate doesn't need to resemble this. As long as the generated test code works and
runs the desired test we should be fine. This is a fairly complex task and we
don't expect you to solve all the edge cases. Instead what we expect is a working solution
with ability to generate code for a subset of features that selenium supports with clear
documentation of what all features it lacks and some sense on how given time you would like
to solve other challenges.

Things to consider

- Only one project needs to be created no matter how many test scenarios are present in the input yaml file

- A Step can either be a user action like click or enter text or an assertion or a wait

- Different type of steps have different possible attributes. You are open to play along with the yaml spec and make any changes as you deem fit.

- You can specify multiple locators which will be checked in order

- If you specify a position within a locator then you indicate that you expect the locator to return multiple matching elements and you want to pick the one indicated by the position

- I have shown multiple different type of locators like attribute, css-selector, xpath, tag name etc. There can be many others. Again these are for examples and you can decide which locators to support

- Each step can have a config

- Entire test can have config

- For bonus point, implement a reporting mechanism that calculates how many test passed, failed or error out. For each test you can also calculate number of steps that passed/ failed/error out

- Try to identify common code patterns whcih can be then saved as utils inside helpers.py / or similar.

- Descriptions are added as comments to each step

### References

- You can use a (scaffolding)[https://github.com/audreyr/cookiecutter] tool to generate the project structure

- Use py.test test framework

### Directions

- Take 2-3 days to work on this assignment

- We are looking for a solution that is easily extensible and atleast have ability to incorporate more features in the future

- Abstractions and code style is not most important but a well written code with good abstractions will definitely make the project more appealing

- Call us if you have any trouble understading anything

- This will be followed by an interview where you will be asked to explain your decisions and asked to describe about challenges and opportunities with your solution

- Most importantly, have fun building it :) :)
