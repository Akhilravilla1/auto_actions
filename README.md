# auto_actions
Control Actions Flask Application
This Flask application provides a web interface to control various actions on your computer, such as moving the mouse in different patterns, scrolling randomly, and switching between applications. The web interface automatically opens in your default browser when the application starts, and it supports dark and light modes.

Features
    Control mouse movements: straight, diagonal, circular, and zigzag patterns.
    Scroll the screen randomly.
    Switch between applications randomly or in order.
    Start and stop actions via an intuitive web interface.
    Dark and light mode toggle with a default dark mode setting.
    Automatically opens the control panel in your browser on startup.
    Prerequisites
    Python 3.x
    Pip (Python package installer)

Setup and Installation
    1. Clone the Repository
        Clone this repository to your local machine using:
            git clone https://github.com/Akhilravilla1/auto_actions.git
    
    2. Navigate to the Project Directory
        Change to the project directory:
            cd auto_actions

    3. Create a Virtual Environment
        Create a virtual environment to manage dependencies:
            python -m venv venv
    
    4. Activate the Virtual Environment
        On Windows:
            venv\Scripts\activate
        
        On macOS and Linux:
            source venv/bin/activate
    
    5. Install Dependencies
        Install the required dependencies using pip:
            pip install -r requirements.txt

    Ensure that your requirements.txt file includes the following packages:
        Flask
        Flask-Cors
        pyautogui
    
    Running the Application
        1. Start the Flask Application
            Run the Flask app using the command:
                python app.py

Access the Web Interface
    The control panel will automatically open in your default web browser.
    If it does not open automatically, manually navigate to http://127.0.0.1:5000

Usage
    Toggle Dark/Light Mode:
    Use the toggle button at the top right to switch between dark and light modes. The application starts in dark mode by default.
    Start Actions:
        Select the desired actions using the checkboxes.
        Set the delay between actions using the input field (in seconds).
        Click the "Start Actions" button to initiate the selected actions.
    Stop Actions:
        Click the "Stop Actions" button to stop all running actions.


Acknowledgements:
    Flask - For the web framework.
    PyAutoGUI - For mouse and keyboard control automation.
    


