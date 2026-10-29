# sprint-retro-randomizer
A lightweight Python/Tkinter tool that randomly selects sprint retrospective feedback categories and records participant feedback during retrospectives.
The tool randomly selects one of three retrospective feedback categories:

What went well
What did not go well
What to improve
A facilitator can optionally enter a participant's name and maintain a running history of the feedback selections during the session.

Features
Randomly selects a retrospective feedback category
Simple graphical interface built with Tkinter
Optionally associates a participant with the selected category
Maintains a history of selections
Clear History button to reset the session
No external Python packages required
Requirements
Python 3
Tkinter
Tkinter is included with many standard Python installations.

Running the Application
Clone or download the repository.

From the project directory, run:

python sprint_retro_randomizer.py

How to Use
Launch the application.
Select Feedback Button.
The application randomly chooses:
What went well
What did not go well
What to improve
Optionally enter the name of the person providing feedback.
Select Feedback Person to add the entry to the history.
Select Clear History when you want to reset the session.
Example
A retrospective might produce a history similar to:

What went well
What to improve - Alex
What did not go well - Jordan
What went well - Taylor
Purpose
This application is intended to provide a simple and interactive way to facilitate sprint retrospective discussions. Rather than moving through retrospective categories in a fixed order, the randomizer can be used to select the next feedback topic.

Project Structure
sprint-retro-randomizer/ ├── sprint_retro_randomizer.py └── README.md

Technologies
Python
Tkinter
ttk
Python random module
License
Add the appropriate license for your organization or intended use before distributing the project.
