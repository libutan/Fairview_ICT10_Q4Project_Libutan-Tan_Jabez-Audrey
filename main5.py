import js #type: ignore

# Data list for your class activities
# You can easily add or remove events here
activities = [
    {"src": "Intrams(1).jpg", "caption": "Intramurals"},
    {"src": "Campout(1).jpg", "caption": "Girls and Boys Camp Out"},
    {"src": "cat_graduation.jpg", "caption": "CAT Graduation"},
    {"src": "Image_20251207_154530_963.jpg.jpg", "caption": "River Clean Up"},
    {"src": "aj_kalinga.jpg", "caption": "AJ Kalinga"},
    {"src": "photo6.jpg", "caption": "Christmas Party"},
    {"src": "Poetry(1).jpg", "caption": "Poetry Festival"},
    {"src": "Peace Congress.jpg", "caption": "Peace Congress"}
]

def render_gallery():
    # Target the gallery div
    gallery = js.document.getElementById("gallery")
    
    if gallery:
        gallery.innerHTML = ""
        
        # Loop through each activity to create the card
        for activity in activities:
            # Create the container div for the photo
            photo_item = js.document.createElement("div")
            photo_item.className = "photo-card"
            
            # Set the internal HTML structure
            photo_item.innerHTML = f"""
                <div class="photo-inner">
                    <img src="{activity['src']}" alt="{activity['caption']}" onerror="this.src='https://via.placeholder.com/300x200?text=Image+Not+Found'">
                    <div class="caption-box">
                        <p>{activity['caption']}</p>
                    </div>
                </div>
            """
            
            gallery.appendChild(photo_item)

# Initialize the gallery on load
render_gallery()