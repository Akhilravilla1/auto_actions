from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pyautogui
import time
import random
import math
import threading
import webbrowser

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Disable PyAutoGUI fail-safe (use with caution)
pyautogui.FAILSAFE = False

# Define duration of each movement
move_duration = 0.5

# Define screen boundaries to avoid moving the cursor out of the visible area
screen_width, screen_height = pyautogui.size()

# Control variable to manage continuous execution
running = False
initial_switch_count = 0  # Tracks how many Alt+Tab presses are needed to return to the initial app

def move_straight():
    directions = [(100, 0), (-100, 0), (0, 100), (0, -100)]
    direction = random.choice(directions)
    pyautogui.moveRel(direction[0], direction[1], duration=move_duration)

def move_diagonal():
    diagonals = [(100, 100), (-100, -100), (100, -100), (-100, 100)]
    diagonal = random.choice(diagonals)
    pyautogui.moveRel(diagonal[0], diagonal[1], duration=move_duration)

def move_circle():
    radius = 50
    for angle in range(0, 360, 45):
        x = radius * math.cos(math.radians(angle))
        y = radius * math.sin(math.radians(angle))
        pyautogui.moveRel(x, y, duration=0.1)

def move_zigzag():
    for _ in range(5):
        pyautogui.moveRel(50, 50, duration=move_duration / 10)
        pyautogui.moveRel(-50, 50, duration=move_duration / 10)

def scroll_randomly():
    scroll_amount = random.randint(-500, 500)
    pyautogui.scroll(scroll_amount)

def switch_application_randomly():
    global initial_switch_count
    num_tabs = random.randint(1, 5)
    initial_switch_count = num_tabs  # Record the number of switches
    pyautogui.keyDown('alt')
    for _ in range(num_tabs):
        pyautogui.press('tab')
        time.sleep(0.2)
    pyautogui.keyUp('alt')

def switch_application_in_order():
    global initial_switch_count
    initial_switch_count = 1  # One switch to the next application
    pyautogui.hotkey('alt', 'tab')

def return_to_first_application():
    global initial_switch_count
    if initial_switch_count > 0:
        pyautogui.keyDown('alt')
        for _ in range(initial_switch_count):
            pyautogui.press('tab')
            time.sleep(0.2)
        pyautogui.keyUp('alt')
        initial_switch_count = 0  # Reset the counter after returning

def perform_actions_continuously(actions):
    global running
    running = True
    while running:
        time.sleep(int(actions.get('delay', 168)))  # Delay between actions to control the speed of execution
        if actions.get('move_straight'):
            move_straight()
        if actions.get('move_diagonal'):
            move_diagonal()
        if actions.get('move_circle'):
            move_circle()
        if actions.get('move_zigzag'):
            move_zigzag()
        if actions.get('scroll_randomly'):
            scroll_randomly()
        if actions.get('switch_application_randomly'):
            switch_application_randomly()
        if actions.get('switch_application_in_order'):
            switch_application_in_order()

        # After actions, return to the initial application
        return_to_first_application()

@app.route('/')
def home():
    return render_template('control_panel.html')  # Render the HTML page

@app.route('/start', methods=['POST'])
def start_actions():
    data = request.json
    # Run actions in a separate thread to avoid blocking the response
    thread = threading.Thread(target=perform_actions_continuously, args=(data,))
    thread.start()
    return jsonify({"status": "success", "message": "Continuous actions started."})

@app.route('/stop', methods=['POST'])
def stop_actions():
    global running
    running = False
    return jsonify({"status": "success", "message": "Continuous actions stopped."})

if __name__ == '__main__':
    # Start the Flask app
    port = 5000
    url = f'http://127.0.0.1:{port}/'
    threading.Timer(1.25, lambda: webbrowser.open(url)).start()  # Open the browser after a slight delay
    app.run(host='127.0.0.1', port=port, debug=False)
