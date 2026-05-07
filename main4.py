import js #type: ignore
from pyscript import display #type: ignore

# 1. Your Data
students = {
    "boys-area": [
        {"name": "ADRIAN GAVINA", "email": "gavina.ade@obmontessori.edu.ph"},
        {"name": "Shia Adam Jayzen Cruz", "email": "cruz.sp@obmontessori.edu.ph"},
        {"name": "Fateh Singh", "email": "singh.f-@obmontessori.edu.ph"},
        {"name": "ALEXANDER JOEL JANAYAN", "email": "janayan.aam@obmontessori.edu.ph"},
        {"name": "Matthew Banaag", "email": "banaag.md@obmontessori.edu.ph"},
        {"name": "MIGUEL BUO", "email": "buo.mge@obmontessori.edu.ph"},
        {"name": "MIKKO ALAIZA", "email": "alaiza.ma@obmontessori.edu.ph"},
        {"name": "NASER A AL HAZMI", "email": "alhazmi.na@obmontessori.edu.ph"},
        {"name": "RYCOB PAGTALUNAN", "email": "pagtalunan.ryd@obmontessori.edu.ph"},
        {"name": "TYRONNE JAIHO SUBAAN", "email": "subaan.tb@obmontessori.edu.ph"},
        {"name": "ZALDIVAR JAMES GUILE", "email": "zaldivar.jm@obmontessori.edu.ph"},
        {"name": "GAVIN FRANCISCO", "email": "francisco.gw@obmontessori.edu.ph"},
        {"name": "Jairo James Agudo", "email": "agudo.js@obmontessori.edu.ph"},
        {"name": "JABEZ LIBUTAN", "email": "libutan.jm@obmontessori.edu.ph"},
        {"name": "LUCAS REYES", "email": "reyes.lt@obmontessori.edu.ph"},
        {"name": "EMILLE BARCELONA", "email": "barcelona.et@obmontessori.edu.ph"}
    ],
    "girls-area": [
        {"name": "XYLEE GOYENECHEA", "email": "goyenechea.xa@obmontessori.edu.ph"},
        {"name": "Ioana Biel B. Haberia", "email": "haberia.ib@obmontessori.edu.ph"},
        {"name": "ALEXANDRA VARGAS", "email": "vargas.ame@obmontessori.edu.ph"},
        {"name": "ARABELLA LUBO", "email": "lubo.aes@obmontessori.edu.ph"},
        {"name": "AUDREY TAN", "email": "tan.ah@obmontessori.edu.ph"},
        {"name": "CYRENE BRION", "email": "brion.cm@obmontessori.edu.ph"},
        {"name": "LUISA MANUEL", "email": "manuel.ali@obmontessori.edu.ph"},
        {"name": "Gianna Entrada", "email": "entrada.gd@obmontessori.edu.ph"},
        {"name": "JANINE MARIPOSQUE", "email": "mariposque.jr@obmontessori.edu.ph"},
        {"name": "Karla Cassandra Del Prado", "email": "delprado.kc@obmontessori.edu.ph"},
        {"name": "LIAN CANDICE CASTRO", "email": "castro.lg@obmontessori.edu.ph"},
        {"name": "SOFIA GUEVARRA", "email": "guevarra.sr@obmontessori.edu.ph"}
    ]
}

# 2. Logic using String Methods and Multiline Strings
def build_html(student_list):
    all_cards = ""  # We will use Concatenation (+) here
    
    for s in student_list:
        # Using .title() to make names look nice (Capitalize Each Word)
        # Using .lower() on emails to ensure they are consistent
        clean_name = s['name'].title()
        clean_email = s['email'].lower()
        
        # Using Triple Quotes for a Multiline String
        card_template = f"""
        <div class="card">
            <div class="name">{clean_name}</div>
            <div class="email">{clean_email}</div>
            <div class="role">Member</div>
        </div>
        """
        # Concatenation
        all_cards = all_cards + card_template
        
    return all_cards

# 3. Execution using js.document to fix the "raw text" issue
for target_id, data in students.items():
    container = js.document.getElementById(target_id)
    if container:
        # Injects the string as actual HTML elements
        container.innerHTML = build_html(data)