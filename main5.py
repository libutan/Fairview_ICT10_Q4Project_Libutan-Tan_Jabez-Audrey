import js #type: ignore

# Data list for your class activities
# You can easily add or remove events here
activities = [
    {"src": "Intrams (1).jpg", "caption": "Exciting Intramurals event where our class competed in various sports"},
    {"src": "Campout (1).jpg", "caption": "Fun Girls and Boys Camp Out under the stars"},
    {"src": "cat_graduation.jpg", "caption": "Proud moment at CAT Graduation ceremony"},
    {"src": "Image_20251207_154530_963.jpg", "caption": "Community service: River Clean Up activity"},
    {"src": "aj_kalinga.jpg", "caption": "Adventure trip to AJ Kalinga"},
    {"src": "photo6.jpg", "caption": "Joyful Christmas Party celebrations"},
    {"src": "Poetry (1).jpg", "caption": "Creative Poetry Festival showcasing talents"},
    {"src": "Peace Congress.png", "caption": "Important Peace Congress discussions"}
]

def render_gallery():
    # Target the gallery div
    gallery = js.document.getElementById("gallery")
    
    js.console.log("render_gallery called")
    
    if gallery:
        gallery.innerHTML = ""
        
        # Loop through each activity to create the card
        for activity in activities:
            # Create the container div for the photo
            photo_item = js.document.createElement("div")
            photo_item.className = "photo-card"

            placeholder_url = (
                "https://via.placeholder.com/600x360/06142e/ffd700?text="
                + activity["caption"].replace(" ", "+")
            )

            # Set the internal HTML structure
            photo_item.innerHTML = f"""
                <div class="photo-inner">
                    <img src="{activity['src']}" alt="{activity['caption']}" loading="lazy"
                        onerror="this.onerror=null;this.src='{placeholder_url}';">
                    <div class="caption-box">
                        <p>{activity['caption']}</p>
                    </div>
                </div>
            """

            gallery.appendChild(photo_item)

# Initialize the gallery on load
render_gallery()
