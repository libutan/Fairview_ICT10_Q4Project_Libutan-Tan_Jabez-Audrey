import js #type: ignore

# 1. The Data: Add as many students as you want here
classmates = [
    {"name": "Shia Cruz", "role": "Class Mayor"},
    {"name": "Xylee Goyenechea", "role": "Vice Mayor"},
    {"name": "Sofia Gueverra", "role": "Secretary"},
    {"name": "Ioana Haberia", "role": "Treasurer"},
    {"name": "Adrian Gavina", "role": "Eco Officer"},
]

def render_text_gallery():
    # Find the target <div> in the HTML
    container = js.document.getElementById("gallery-target")
    
    if container:
        # Clear any existing content
        container.innerHTML = ""
        
        for person in classmates:
            # Create a column for the Bootstrap grid
            col = js.document.createElement("div")
            col.className = "col-md-4 mb-3"
            
            # The HTML template for your text cards
            card_content = f"""
            <div class="card h-100 shadow-sm" style="background-color: #162a4d; border-left: 5px solid #ffd700; color: white; border-radius: 8px;">
                <div class="card-body">
                    <h5 class="card-title mb-1" style="color: #ffd700; font-weight: bold;">{person['name']}</h5>
                    <p class="card-text text-uppercase small" style="color: #cccccc; letter-spacing: 1px; font-size: 0.8rem;">{person['role']}</p>
                </div>
            </div>
            """
            
            col.innerHTML = card_content
            container.appendChild(col)
    else:
        print("Error: Could not find element with id 'gallery-target'")

# Execute the function to draw the cards
render_text_gallery()