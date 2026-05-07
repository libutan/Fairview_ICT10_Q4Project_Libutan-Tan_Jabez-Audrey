
from js import document # type: ignore
from pyodide.ffi import create_proxy # type: ignore
from pyscript import display # type: ignore
import numpy as np
import matplotlib.pyplot as plt





plt.clf() # Clear any existing plots to ensure a clean slate for drawing the attendance plot.


class AttendanceData:
    def __init__(self):
        # This class initializes with default attendance data for the days of the week and their corresponding absences. It also includes a mapping to translate full day names to their abbreviated forms.
        self.days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
        self.absences = [0, 0, 0, 0, 0]
        
        # A simple mapping for translation
        self.day_map = {
            "Monday": "Mon",
            "Tuesday": "Tue",
            "Wednesday": "Wed",
            "Thursday": "Thu",
            "Friday": "Fri"
        }
# The update_day method takes a full day name and the number of absences, translates the day to its abbreviated form, and updates the attendance data accordingly. If the day is not already in the list, it adds it; otherwise, it updates the existing entry.
    def update_day(self, full_day: str, absences: int):
        # Translate "Monday" -> "Mon"
        short_day = self.day_map.get(full_day.strip(), full_day.strip())
        
        if short_day not in self.days:
            self.days.append(short_day)
            self.absences.append(absences)
        else:
            index = self.days.index(short_day)
            self.absences[index] = absences


class AttendanceTracker: # This class serves as a higher-level interface for managing attendance data, allowing for adding records and retrieving days and absences.
    def __init__(self):
        self.data = AttendanceData()




    def add_record(self, day: str, absences: int): # This method adds a new attendance record by updating the data for a specific day with the given number of absences.
        self.data.update_day(day, absences)




    @property
    def days(self): # This property allows access to the list of days from the attendance data.
        return self.data.days




    @property
    def absences(self): # This property allows access to the list of absences from the attendance data.
        return self.data.absences








def draw_attendance_plot(days, absences): # This function takes in the days and absences data and creates a line plot to visualize the attendance. It uses Matplotlib to create the plot and displays it in the web page.
    fig, ax = plt.subplots(figsize=(3.5, 3))
    ax.plot(days, absences, marker="o", color="#1f77b4", linewidth=2)
    ax.set_title("Weekly Attendance (Absences)")
    ax.set_xlabel("Day")
    ax.set_ylabel("Number of Absences")
    ax.set_ylim(bottom=0)
    ax.grid(True, linestyle="--", alpha=0.5)
    fig.tight_layout()




    document.getElementById("plot-area").innerHTML = "" # Clear the existing plot area before displaying the new plot
    display(fig, target="plot-area")








tracker = AttendanceTracker() # Create an instance of the AttendanceTracker class to manage the attendance data and interactions with the web page.








def submit_attendance(event): # This function is called when the attendance form is submitted. It prevents the default form submission behavior, retrieves the input values for the day and absences, validates the input, updates the attendance data, and redraws the attendance plot with the new data.
    event.preventDefault()




    day = document.getElementById("day-select").value # Get the selected day from the dropdown menu
    absences_text = str(document.getElementById("absences-input").value).strip() # Get the number of absences entered by the user and convert it to a string, stripping any leading or trailing whitespace
    status_element = document.getElementById("status") # Get the status element to display messages to the user




    if absences_text == "": # If the absences input is empty, display a message asking the user to enter the number of absences and return early from the function.
        status_element.innerText = "Please enter the number of absences."
        return




    try: # Attempt to convert the absences input to an integer. If the conversion fails (e.g., if the input is not a valid number), catch the ValueError and display an error message to the user.
        absences = int(absences_text)
    except ValueError: # If the input cannot be converted to an integer, display an error message indicating that absences must be a whole number and return early from the function.
        status_element.innerText = "Absences must be a whole number."
        return




    tracker.add_record(day, absences)  # Update the attendance data with the new record for the specified day and number of absences.
    status_element.innerText = f"Saved {absences} absence(s) for {day}." # Update the status element to inform the user that the attendance record has been saved successfully.
    draw_attendance_plot(tracker.days, tracker.absences) # Redraw the attendance plot with the updated data to reflect the new attendance record that was just added.








form = document.getElementById("attendance-form") # Get the attendance form element from the web page to attach an event listener for form submission.
form.addEventListener("submit", create_proxy(submit_attendance)) # Attach the submit_attendance function as an event listener for the "submit" event on the attendance form. The create_proxy function is used to create a proxy for the Python function so that it can be called from JavaScript when the form is submitted.




draw_attendance_plot(tracker.days, tracker.absences) # Initial drawing of the attendance plot with the default data when the page loads. This ensures that the user sees the initial attendance data visualized before making any updates.






