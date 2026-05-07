from js import document #type: ignore

# Data model for classmates
class Classmate:
    def __init__(self, name, section, favorite_subject):
        self.name = name
        self.section = section
        self.favorite_subject = favorite_subject

    def introduce(self):
        return f"Hello! I'm {self.name}, a student from {self.section}. My favorite subject is {self.favorite_subject}."

# Initial classmates list
classmates = [
    Classmate("Lucas", "Amethyst", "Math"),
    Classmate("Shia", "Topaz", "Science"),
    Classmate("Jairo", "Sapphire", "English"),
    Classmate("Adrian", "Ruby", "TLE"),
    Classmate("Gavin", "Jade", "Music and Arts"),
]

def get_input(id):
    return document.getElementById(id).value.strip()

def show_introductions(event=None):
    if event is not None:
        event.preventDefault()
    
    output = document.getElementById("output")
    message = document.getElementById("message")
    
    # Loop to build clear, multi-line cards
    cards = []
    for student in classmates:
        card_html = f"""
        <div class='intro-card'>
            <strong>{student.name}</strong>
            <span>📍 Section: {student.section}</span>
            <span>📚 Favorite Subject: {student.favorite_subject}</span>
            <hr style='border-color: rgba(96, 165, 250, 0.2); margin: 8px 0;'>
            <small><i>"{student.introduce()}"</i></small>
        </div>
        """
        cards.append(card_html)
    
    output.innerHTML = "".join(cards)
    
    if event is not None:
        message.innerText = "Classmate list refreshed."

def add_classmate(event=None):
    name = get_input("name")
    section = get_input("section")
    favorite_subject = get_input("favorite_subject")
    message = document.getElementById("message")

    if not (name and section and favorite_subject):
        message.innerText = "Please fill in every field."
        return

    # Add to list
    classmates.append(Classmate(name, section, favorite_subject))
    message.innerText = "Classmate added! Click 'Show List' to update."

    # Clear fields
    for field in ("name", "section", "favorite_subject"):
        document.getElementById(field).value = ""

def show_intro(event=None):
    show_introductions(event)

# Optional: Run on startup to show the initial list
show_introductions()