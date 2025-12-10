import os
import json

# Define the root directory
ROOT_DIR = "LDB_Dataset"
DATA_DIR = os.path.join(ROOT_DIR, "data")

# 1. 100 Languages List (Top spoken + Representative)
# Source: Ethnologue 2024 & Whitepaper representatives
LANGUAGES = [
    {"code": "san", "name": "Sanskrit", "family": "Indo-Aryan", "morphology": "Synthetic/Inflectional"},
    {"code": "eng", "name": "English", "family": "Germanic", "morphology": "Analytic"},
    {"code": "cmn", "name": "Mandarin Chinese", "family": "Sino-Tibetan", "morphology": "Analytic"},
    {"code": "hin", "name": "Hindi", "family": "Indo-Aryan", "morphology": "Inflectional"},
    {"code": "spa", "name": "Spanish", "family": "Romance", "morphology": "Fusional"},
    {"code": "fra", "name": "French", "family": "Romance", "morphology": "Fusional"},
    {"code": "ara", "name": "Arabic", "family": "Semitic", "morphology": "Introflexive"},
    {"code": "ben", "name": "Bengali", "family": "Indo-Aryan", "morphology": "Inflectional"},
    {"code": "por", "name": "Portuguese", "family": "Romance", "morphology": "Fusional"},
    {"code": "rus", "name": "Russian", "family": "Balto-Slavic", "morphology": "Fusional"},
    {"code": "urd", "name": "Urdu", "family": "Indo-Aryan", "morphology": "Inflectional"},
    {"code": "ind", "name": "Indonesian", "family": "Austronesian", "morphology": "Agglutinative"},
    {"code": "deu", "name": "German", "family": "Germanic", "morphology": "Fusional"},
    {"code": "jpn", "name": "Japanese", "family": "Japonic", "morphology": "Agglutinative"},
    {"code": "mar", "name": "Marathi", "family": "Indo-Aryan", "morphology": "Inflectional"},
    {"code": "tel", "name": "Telugu", "family": "Dravidian", "morphology": "Agglutinative"},
    {"code": "tur", "name": "Turkish", "family": "Turkic", "morphology": "Agglutinative"},
    {"code": "tam", "name": "Tamil", "family": "Dravidian", "morphology": "Agglutinative"},
    {"code": "yue", "name": "Yue Chinese (Cantonese)", "family": "Sino-Tibetan", "morphology": "Analytic"},
    {"code": "vie", "name": "Vietnamese", "family": "Austroasiatic", "morphology": "Analytic"},
    {"code": "kor", "name": "Korean", "family": "Koreanic", "morphology": "Agglutinative"},
    {"code": "ita", "name": "Italian", "family": "Romance", "morphology": "Fusional"},
    {"code": "tha", "name": "Thai", "family": "Kra-Dai", "morphology": "Analytic"},
    {"code": "guj", "name": "Gujarati", "family": "Indo-Aryan", "morphology": "Inflectional"},
    {"code": "jav", "name": "Javanese", "family": "Austronesian", "morphology": "Agglutinative"},
    {"code": "fas", "name": "Persian (Farsi)", "family": "Iranian", "morphology": "Analytic"},
    {"code": "pol", "name": "Polish", "family": "Balto-Slavic", "morphology": "Fusional"},
    {"code": "kan", "name": "Kannada", "family": "Dravidian", "morphology": "Agglutinative"},
    {"code": "mal", "name": "Malayalam", "family": "Dravidian", "morphology": "Agglutinative"},
    {"code": "sun", "name": "Sundanese", "family": "Austronesian", "morphology": "Agglutinative"},
    {"code": "hau", "name": "Hausa", "family": "Chadic", "morphology": "Analytic"},
    {"code": "pan", "name": "Punjabi (Eastern)", "family": "Indo-Aryan", "morphology": "Inflectional"},
    {"code": "pnb", "name": "Punjabi (Western)", "family": "Indo-Aryan", "morphology": "Inflectional"},
    {"code": "bho", "name": "Bhojpuri", "family": "Indo-Aryan", "morphology": "Inflectional"},
    {"code": "yor", "name": "Yoruba", "family": "Volta-Niger", "morphology": "Isolating"},
    {"code": "ukr", "name": "Ukrainian", "family": "Balto-Slavic", "morphology": "Fusional"},
    {"code": "ibo", "name": "Igbo", "family": "Volta-Niger", "morphology": "Agglutinative"},
    {"code": "uzb", "name": "Uzbek", "family": "Turkic", "morphology": "Agglutinative"},
    {"code": "sin", "name": "Sindhi", "family": "Indo-Aryan", "morphology": "Inflectional"},
    {"code": "amh", "name": "Amharic", "family": "Semitic", "morphology": "Introflexive"},
    {"code": "orm", "name": "Oromo", "family": "Cushitic", "morphology": "Inflectional"},
    {"code": "azj", "name": "Azerbaijani", "family": "Turkic", "morphology": "Agglutinative"},
    {"code": "mai", "name": "Maithili", "family": "Indo-Aryan", "morphology": "Inflectional"},
    {"code": "fil", "name": "Filipino", "family": "Austronesian", "morphology": "Agglutinative"},
    {"code": "bur", "name": "Burmese", "family": "Sino-Tibetan", "morphology": "Analytic"},
    {"code": "pus", "name": "Pashto", "family": "Iranian", "morphology": "Inflectional"},
    {"code": "swa", "name": "Swahili", "family": "Bantu", "morphology": "Agglutinative"},
    {"code": "mal", "name": "Malay", "family": "Austronesian", "morphology": "Agglutinative"},
    {"code": "nep", "name": "Nepali", "family": "Indo-Aryan", "morphology": "Inflectional"},
    {"code": "ori", "name": "Odia", "family": "Indo-Aryan", "morphology": "Inflectional"},
    {"code": "kur", "name": "Kurdish (Kurmanji)", "family": "Iranian", "morphology": "Inflectional"},
    {"code": "som", "name": "Somali", "family": "Cushitic", "morphology": "Agglutinative"},
    {"code": "ceb", "name": "Cebuano", "family": "Austronesian", "morphology": "Agglutinative"},
    {"code": "mag", "name": "Magahi", "family": "Indo-Aryan", "morphology": "Inflectional"},
    {"code": "hym", "name": "Haryanvi", "family": "Indo-Aryan", "morphology": "Inflectional"},
    {"code": "hun", "name": "Hungarian", "family": "Uralic", "morphology": "Agglutinative"},
    {"code": "ell", "name": "Greek", "family": "Hellenic", "morphology": "Fusional"},
    {"code": "cat", "name": "Catalan", "family": "Romance", "morphology": "Fusional"},
    {"code": "khm", "name": "Khmer", "family": "Austroasiatic", "morphology": "Analytic"},
    {"code": "zha", "name": "Zhuang", "family": "Kra-Dai", "morphology": "Analytic"},
    {"code": "zul", "name": "Zulu", "family": "Bantu", "morphology": "Agglutinative"},
    {"code": "ces", "name": "Czech", "family": "Balto-Slavic", "morphology": "Fusional"},
    {"code": "run", "name": "Rundi", "family": "Bantu", "morphology": "Agglutinative"},
    {"code": "kin", "name": "Kinyarwanda", "family": "Bantu", "morphology": "Agglutinative"},
    {"code": "uig", "name": "Uyghur", "family": "Turkic", "morphology": "Agglutinative"},
    {"code": "hmn", "name": "Hmong", "family": "Hmong-Mien", "morphology": "Analytic"},
    {"code": "sna", "name": "Shona", "family": "Bantu", "morphology": "Agglutinative"},
    {"code": "min", "name": "Minangkabau", "family": "Austronesian", "morphology": "Agglutinative"},
    {"code": "bul", "name": "Bulgarian", "family": "Balto-Slavic", "morphology": "Fusional"},
    {"code": "kaz", "name": "Kazakh", "family": "Turkic", "morphology": "Agglutinative"},
    {"code": "que", "name": "Quechua", "family": "Quechuan", "morphology": "Agglutinative"},
    {"code": "swe", "name": "Swedish", "family": "Germanic", "morphology": "Fusional"},
    {"code": "tat", "name": "Tatar", "family": "Turkic", "morphology": "Agglutinative"},
    {"code": "lav", "name": "Latvian", "family": "Balto-Slavic", "morphology": "Fusional"},
    {"code": "mad", "name": "Madurese", "family": "Austronesian", "morphology": "Agglutinative"},
    {"code": "hil", "name": "Hiligaynon", "family": "Austronesian", "morphology": "Agglutinative"},
    {"code": "lug", "name": "Ganda", "family": "Bantu", "morphology": "Agglutinative"},
    {"code": "mos", "name": "Mossi", "family": "Gur", "morphology": "Agglutinative"},
    {"code": "xho", "name": "Xhosa", "family": "Bantu", "morphology": "Agglutinative"},
    {"code": "bel", "name": "Belarusian", "family": "Balto-Slavic", "morphology": "Fusional"},
    {"code": "bal", "name": "Balochi", "family": "Iranian", "morphology": "Inflectional"},
    {"code": "kon", "name": "Kongo", "family": "Bantu", "morphology": "Agglutinative"},
    {"code": "nld", "name": "Dutch", "family": "Germanic", "morphology": "Fusional"},
    {"code": "wol", "name": "Wolof", "family": "Niger-Congo", "morphology": "Agglutinative"},
    {"code": "heb", "name": "Hebrew", "family": "Semitic", "morphology": "Introflexive"},
    {"code": "aka", "name": "Akan", "family": "Kwa", "morphology": "Analytic"},
    {"code": "mlg", "name": "Malagasy", "family": "Austronesian", "morphology": "Agglutinative"},
    {"code": "tuk", "name": "Turkmen", "family": "Turkic", "morphology": "Agglutinative"},
    {"code": "ron", "name": "Romanian", "family": "Romance", "morphology": "Fusional"},
    {"code": "ssw", "name": "Swati", "family": "Bantu", "morphology": "Agglutinative"},
    {"code": "tsn", "name": "Tswana", "family": "Bantu", "morphology": "Agglutinative"},
    {"code": "war", "name": "Waray", "family": "Austronesian", "morphology": "Agglutinative"},
    {"code": "srp", "name": "Serbian", "family": "Balto-Slavic", "morphology": "Fusional"},
    {"code": "hrv", "name": "Croatian", "family": "Balto-Slavic", "morphology": "Fusional"},
    {"code": "nso", "name": "Northern Sotho", "family": "Bantu", "morphology": "Agglutinative"},
    {"code": "grn", "name": "Guarani", "family": "Tupian", "morphology": "Agglutinative"},
    {"code": "kir", "name": "Kyrgyz", "family": "Turkic", "morphology": "Agglutinative"},
    {"code": "sot", "name": "Sotho", "family": "Bantu", "morphology": "Agglutinative"},
    {"code": "bod", "name": "Tibetan", "family": "Sino-Tibetan", "morphology": "Analytic"},
    {"code": "lao", "name": "Lao", "family": "Kra-Dai", "morphology": "Analytic"},
]

# Ensure we have exactly 100
LANGUAGES = LANGUAGES[:100]

# 2. Archetype Prompts (25 per category)
PROMPTS = {
    "linguistic_fidelity": [
        "The boy, who chased the dog that bit the cat, ran home.",
        "Give the book to the man with the telescope.",
        "Visiting relatives can be boring.",
        "I saw her duck.",
        "The chicken is ready to eat.",
        "Time flies like an arrow, fruit flies like a banana.",
        "The old man the boat.",
        "The complex houses married and single soldiers and their families.",
        "The horse raced past the barn fell.",
        "The cotton clothing is made of grows in Mississippi.",
        "Effectuate the termination of the employee.",
        "Synthesize the data into a coherent report.",
        "Analyze the impact of the policy on the economy.",
        "Describe the beauty of the sunset in 50 words.",
        "Explain quantum entanglement to a 5-year-old.",
        "Translate the following legal contract accurately.",
        "Summarize the main points of the article.",
        "Debate the pros and cons of artificial intelligence.",
        "Write a poem about a lonely robot.",
        "Create a dialogue between two philosophers.",
        "Critique the painting 'Starry Night'.",
        "Justify the use of nuclear energy.",
        "Predict the future of space exploration.",
        "Compare and contrast democracy and autocracy.",
        "Define the concept of 'justice' in 3 sentences."
    ],
    "generative_multimodal": [
        "A red ball on a blue table.",
        "A cat sitting on a windowsill looking at rain.",
        "A futuristic city with flying cars.",
        "A medieval knight fighting a dragon.",
        "A serene lake reflecting the mountains.",
        "A cyberpunk street market at night.",
        "A portrait of an old woman with wise eyes.",
        "An astronaut floating in space.",
        "A tiger leaping through a hoop of fire.",
        "A minimalist living room with a white sofa.",
        "A detailed map of a fantasy world.",
        "A blueprint of a perpetual motion machine.",
        "A logo for eco-friendly coffee shop.",
        "A comic book strip about a superhero dog.",
        "A visualization of a black hole.",
        "Video: A time-lapse of a flower blooming.",
        "Video: A drone shot flying over a canyon.",
        "Video: A slow-motion drop of water hitting a surface.",
        "Video: A chef chopping vegetables rapidly.",
        "Video: A dancer performing ballet on a stage.",
        "Video: A dog catching a frisbee in mid-air.",
        "Video: A car drifting around a corner.",
        "Video: Clouds moving quickly across the sky.",
        "Video: A fire crackling in a fireplace.",
        "Video: Rain falling on a window pane."
    ],
    "robotic_control": [
        "Pick up the red block and place it on the blue block.",
        "Move the arm to coordinate (10, 20, 30).",
        "Rotate the wrist 90 degrees clockwise.",
        "Grasp the object with 5N force.",
        "Navigate to the kitchen and avoid obstacles.",
        "Pour water from the pitcher into the glass.",
        "Fold the laundry neatly.",
        "Open the door and hold it for the person.",
        "Assemble the IKEA chair following instructions.",
        "Weld the two metal plates together.",
        "Solder the component onto the PCB.",
        "Harvest the ripe tomatoes from the vine.",
        "Sort the packages by size and color.",
        "Stack the boxes in a pyramid shape.",
        "Unscrew the bolt from the engine block.",
        "Paint the wall with vertical strokes.",
        "Vacuum the living room carpet.",
        "Mow the lawn in a striped pattern.",
        "Serve the food to the guests at the table.",
        "Clear the dishes and put them in the dishwasher.",
        "Retrieve the medical kit from the shelf.",
        "Assist the patient in walking to the bed.",
        "Perform CPR on the dummy.",
        "Disarm the mock explosive device.",
        "Inspect the pipeline for cracks."
    ],
    "context_density": [
        "Summarize the following 5000-word legal document.",
        "Extract all dates and names from the history book chapter.",
        "Identify the main themes in this 10-page essay.",
        "Find the contradiction in these two witness statements.",
        "List all the ingredients mentioned in this cookbook.",
        "Map the character relationships in this novel excerpt.",
        "Timeline the events of the war described here.",
        "Calculate the total revenue from this quarterly report.",
        "Explain the scientific method based on this paper.",
        "Compare the two political platforms detailed below.",
        "Draft a response to this long email thread.",
        "Create a quiz based on this textbook chapter.",
        "Write an abstract for this technical specification.",
        "Translate this short story while keeping cultural nuance.",
        "Paraphrase this complex philosophical argument.",
        "Condense this meeting transcript into action items.",
        "Highlight the key risks in this investment prospectus.",
        "Categorize the feedback in these 100 customer reviews.",
        "Detect the sentiment in this long diary entry.",
        "Anonymize the personal data in this medical record.",
        "Format this raw text into a structured table.",
        "Generate a tag cloud from this forum discussion.",
        "Identify the bias in this news article.",
        "Fact-check the claims in this political speech.",
        "Retrieve the answer to 'Who is the killer?' from this mystery story."
    ]
}

def generate_dataset():
    # Create directories
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
        print(f"Created directory: {DATA_DIR}")

    # 1. Save Languages Metadata
    with open(os.path.join(ROOT_DIR, "languages.json"), "w") as f:
        json.dump(LANGUAGES, f, indent=4)
    print("Saved languages.json")

    # 2. Save Archetype Prompts
    with open(os.path.join(ROOT_DIR, "prompts_archetypes.json"), "w") as f:
        json.dump(PROMPTS, f, indent=4)
    print("Saved prompts_archetypes.json")

    # 3. Generate Language Directories and Files
    for lang in LANGUAGES:
        lang_dir_name = f"{lang['code']}_{lang['name'].replace(' ', '_').replace('/', '-')}"
        lang_path = os.path.join(DATA_DIR, lang_dir_name)
        
        if not os.path.exists(lang_path):
            os.makedirs(lang_path)
        
        # Create category files with English prompts (placeholder for translation)
        # We assume the user will eventually replace these with translations
        for category, prompts in PROMPTS.items():
            category_file = os.path.join(lang_path, f"{category}.json")
            
            data = {
                "language_code": lang['code'],
                "category": category,
                "prompts": []
            }
            
            for i, p in enumerate(prompts):
                data["prompts"].append({
                    "id": i + 1,
                    "english_archetype": p,
                    "target_translation": "" # To be filled
                })
            
            with open(category_file, "w") as f:
                json.dump(data, f, indent=4)
        
    print(f"Generated dataset structure for {len(LANGUAGES)} languages.")

if __name__ == "__main__":
    generate_dataset()
