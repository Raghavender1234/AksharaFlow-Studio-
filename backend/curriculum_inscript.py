# -*- coding: utf-8 -*-
"""
Complete 13 Indian Language InScript Curriculum, Keymaps & Native Setup Guides
Supports:
  1. Hindi (hi - हिन्दी)
  2. Marathi (mr - मराठी)
  3. Sanskrit (sa - संस्कृतम्)
  4. Bengali (bn - বাংলা)
  5. Punjabi (pa - ਪੰਜਾਬੀ)
  6. Gujarati (gu - ગુજરાતી)
  7. Odia (or - ଓଡ଼ିଆ)
  8. Tamil (ta - தமிழ்)
  9. Telugu (te - తెలుగు)
  10. Kannada (kn - ಕನ್ನಡ)
  11. Malayalam (ml - മലയാളം)
  12. Assamese (as - অসমীয়া)
  13. Urdu (ur - اردو)
"""

# Standard QWERTY physical key codes mapped to finger codes
CODE_TO_FINGER = {
    "Backquote": "L_PINKY", "Digit1": "L_PINKY", "Digit2": "L_RING", "Digit3": "L_MIDDLE",
    "Digit4": "L_INDEX", "Digit5": "L_INDEX", "Digit6": "R_INDEX", "Digit7": "R_INDEX",
    "Digit8": "R_MIDDLE", "Digit9": "R_RING", "Digit0": "R_PINKY", "Minus": "R_PINKY", "Equal": "R_PINKY",
    "KeyQ": "L_PINKY", "KeyW": "L_RING", "KeyE": "L_MIDDLE", "KeyR": "L_INDEX", "KeyT": "L_INDEX",
    "KeyY": "R_INDEX", "KeyU": "R_INDEX", "KeyI": "R_MIDDLE", "KeyO": "R_RING", "KeyP": "R_PINKY",
    "BracketLeft": "R_PINKY", "BracketRight": "R_PINKY", "Backslash": "R_PINKY",
    "KeyA": "L_PINKY", "KeyS": "L_RING", "KeyD": "L_MIDDLE", "KeyF": "L_INDEX", "KeyG": "L_INDEX",
    "KeyH": "R_INDEX", "KeyJ": "R_INDEX", "KeyK": "R_MIDDLE", "KeyL": "R_RING",
    "Semicolon": "R_PINKY", "Quote": "R_PINKY",
    "KeyZ": "L_PINKY", "KeyX": "L_RING", "KeyC": "L_MIDDLE", "KeyV": "L_INDEX", "KeyB": "L_INDEX",
    "KeyN": "R_INDEX", "KeyM": "R_INDEX", "Comma": "R_MIDDLE", "Period": "R_RING", "Slash": "R_PINKY",
    "Space": "THUMB"
}


def _build_brahmic_keymap(base_offset: int, digits: str, extra_overrides: dict = None):
    """
    Constructs the official Government of India InScript keymap for any Brahmic Unicode block
    (Devanagari=0x0900, Bengali=0x0980, Gurmukhi=0x0A00, Gujarati=0x0A80, Odia=0x0B00,
     Tamil=0x0B80, Telugu=0x0C00, Kannada=0x0C80, Malayalam=0x0D00).
    Left hand = Vowels (Shift) & Matras (Normal). Right hand = Consonants.
    """
    def c(offset):
        return chr(base_offset + offset)

    # Standard Brahmic Unicode offsets relative to block start (0x0900 for Devanagari)
    km = {
        # Number Row
        "Backquote": {"main": c(0x4A), "shift": c(0x12)},
        "Digit1": {"main": digits[1], "shift": "!"},
        "Digit2": {"main": digits[2], "shift": "@"},
        "Digit3": {"main": digits[3], "shift": "#"},
        "Digit4": {"main": digits[4], "shift": "$"},
        "Digit5": {"main": digits[5], "shift": "%"},
        "Digit6": {"main": digits[6], "shift": "^"},
        "Digit7": {"main": digits[7], "shift": "&"},
        "Digit8": {"main": digits[8], "shift": "*"},
        "Digit9": {"main": digits[9], "shift": "("},
        "Digit0": {"main": digits[0], "shift": ")"},
        "Minus": {"main": "-", "shift": c(0x03)},   # Visarga ः
        "Equal": {"main": c(0x43), "shift": c(0x0B)},  # ृ / ऋ

        # Top Row (Left = Matras/Vowels, Right = Consonants)
        "KeyQ": {"main": c(0x4C), "shift": c(0x14)},  # ौ / औ
        "KeyW": {"main": c(0x48), "shift": c(0x10)},  # ै / ऐ
        "KeyE": {"main": c(0x3E), "shift": c(0x06)},  # ा / आ
        "KeyR": {"main": c(0x40), "shift": c(0x08)},  # ी / ई
        "KeyT": {"main": c(0x42), "shift": c(0x0A)},  # ू / ऊ
        "KeyY": {"main": c(0x2C), "shift": c(0x2D)},  # ब / भ
        "KeyU": {"main": c(0x39), "shift": c(0x19)},  # ह / ङ
        "KeyI": {"main": c(0x17), "shift": c(0x18)},  # ग / घ
        "KeyO": {"main": c(0x26), "shift": c(0x27)},  # द / ध
        "KeyP": {"main": c(0x1C), "shift": c(0x1D)},  # ज / झ
        "BracketLeft": {"main": c(0x21), "shift": c(0x22)},  # ड / ढ
        "BracketRight": {"main": c(0x3C), "shift": c(0x1E)}, # ़ / ञ
        "Backslash": {"main": c(0x49), "shift": c(0x11)},

        # Home Row (Anchor Row!)
        "KeyA": {"main": c(0x4B), "shift": c(0x13)},  # ो / ओ
        "KeyS": {"main": c(0x47), "shift": c(0x0F)},  # े / ए
        "KeyD": {"main": c(0x4D), "shift": c(0x05)},  # ् (Halant) / अ
        "KeyF": {"main": c(0x3F), "shift": c(0x07)},  # ि / इ
        "KeyG": {"main": c(0x41), "shift": c(0x09)},  # ु / उ
        "KeyH": {"main": c(0x2A), "shift": c(0x2B)},  # प / फ
        "KeyJ": {"main": c(0x30), "shift": c(0x31)},  # र / ऱ
        "KeyK": {"main": c(0x15), "shift": c(0x16)},  # क / ख
        "KeyL": {"main": c(0x24), "shift": c(0x25)},  # त / थ
        "Semicolon": {"main": c(0x1A), "shift": c(0x1B)},  # च / छ
        "Quote": {"main": c(0x1F), "shift": c(0x20)},      # ट / ठ

        # Bottom Row
        "KeyZ": {"main": c(0x46), "shift": c(0x0E)},  # ॆ / ऎ
        "KeyX": {"main": c(0x02), "shift": c(0x01)},  # ं (Anusvara) / ँ
        "KeyC": {"main": c(0x2E), "shift": c(0x23)},  # म / ण
        "KeyV": {"main": c(0x28), "shift": c(0x29)},  # न / ऩ
        "KeyB": {"main": c(0x35), "shift": c(0x34)},  # व / ळ
        "KeyN": {"main": c(0x32), "shift": c(0x33)},  # ल / ळ
        "KeyM": {"main": c(0x38), "shift": c(0x36)},  # स / श
        "Comma": {"main": ",", "shift": c(0x37)},     # , / ष
        "Period": {"main": ".", "shift": "।"},        # . / । (Purna Viram)
        "Slash": {"main": c(0x2F), "shift": "?"},     # य / ?
        "Space": {"main": " ", "shift": " "}
    }
    if extra_overrides:
        for k, v in extra_overrides.items():
            km[k] = v
    return km


# Urdu InScript / Phonetic-Standard Keymap
URDU_KEYMAP = {
    "Backquote": {"main": "ً", "shift": "ّ"},
    "Digit1": {"main": "۱", "shift": "!"},
    "Digit2": {"main": "۲", "shift": "@"},
    "Digit3": {"main": "۳", "shift": "#"},
    "Digit4": {"main": "۴", "shift": "$"},
    "Digit5": {"main": "۵", "shift": "%"},
    "Digit6": {"main": "۶", "shift": "^"},
    "Digit7": {"main": "۷", "shift": "&"},
    "Digit8": {"main": "۸", "shift": "*"},
    "Digit9": {"main": "۹", "shift": "("},
    "Digit0": {"main": "۰", "shift": ")"},
    "Minus": {"main": "-", "shift": "_"},
    "Equal": {"main": "=", "shift": "+"},
    "KeyQ": {"main": "ق", "shift": "ْ"},
    "KeyW": {"main": "و", "shift": "ؤ"},
    "KeyE": {"main": "ع", "shift": "ئ"},
    "KeyR": {"main": "ر", "shift": "ڑ"},
    "KeyT": {"main": "ت", "shift": "ٹ"},
    "KeyY": {"main": "ے", "shift": "أ"},
    "KeyU": {"main": "ء", "shift": "إ"},
    "KeyI": {"main": "ی", "shift": "ٰ"},
    "KeyO": {"main": "ہ", "shift": "ۃ"},
    "KeyP": {"main": "پ", "shift": "ُ"},
    "BracketLeft": {"main": "[", "shift": "{"},
    "BracketRight": {"main": "]", "shift": "}"},
    "Backslash": {"main": "۔", "shift": "|"},
    "KeyA": {"main": "ا", "shift": "آ"},
    "KeyS": {"main": "س", "shift": "ص"},
    "KeyD": {"main": "د", "shift": "ڈ"},
    "KeyF": {"main": "ف", "shift": "ِ"},
    "KeyG": {"main": "گ", "shift": "غ"},
    "KeyH": {"main": "ح", "shift": "ھ"},
    "KeyJ": {"main": "ج", "shift": "ض"},
    "KeyK": {"main": "ک", "shift": "خ"},
    "KeyL": {"main": "ل", "shift": "ظ"},
    "Semicolon": {"main": "؛", "shift": ":"},
    "Quote": {"main": "ط", "shift": "\""},
    "KeyZ": {"main": "ز", "shift": "ذ"},
    "KeyX": {"main": "ش", "shift": "ژ"},
    "KeyC": {"main": "چ", "shift": "ث"},
    "KeyV": {"main": "ط", "shift": "ظ"},
    "KeyB": {"main": "ب", "shift": "أ"},
    "KeyN": {"main": "ن", "shift": "ں"},
    "KeyM": {"main": "م", "shift": "َ"},
    "Comma": {"main": "،", "shift": "<"},
    "Period": {"main": "۔", "shift": ">"},
    "Slash": {"main": "/", "shift": "؟"},
    "Space": {"main": " ", "shift": " "}
}


# Comprehensive Language Pack Definitions for all 13 Indian Languages
INDIAN_LANGUAGE_PACKS = {
    "hi": {
        "code": "hi",
        "name": "Hindi (InScript)",
        "native_name": "हिन्दी",
        "script": "Devanagari",
        "keymap": _build_brahmic_keymap(0x0900, "०१२३४५६७८९"),
        "setup_guide": {
            "native_title": "हिन्दी (InScript) कीबोर्ड कैसे चालू करें",
            "native_steps": [
                "१. अपने कीबोर्ड पर 'Windows + Space' (या 'Alt + Shift') दबाएँ और 'हिन्दी (Hindi - InScript)' चुनें।",
                "२. चिंता न करें! यदि आपके कंप्यूटर में InScript कीबोर्ड चालू नहीं भी है, तो भी हमारा 'Auto-InScript स्मार्ट मोड' आपके अंग्रेजी बटनों को अपने आप हिन्दी (InScript) में बदल देगा!",
                "३. बायाँ हाथ मात्राओं और स्वरों (ा, ि, ी, ु, ू, े, ो) के लिए है, और दायाँ हाथ व्यंजनों (क, र, त, च, प, म, न, स) के लिए है।"
            ],
            "en_steps": [
                "1. Press 'Win + Space' on your PC to switch to Hindi InScript—OR simply start typing right away with our built-in Auto-InScript Mapper!",
                "2. InScript Rule: Left hand types Matras & Vowels; Right hand types Consonants."
            ]
        },
        "vocab": {
            "home_words": ["कर", "पर", "तप", "चर", "रति", "कवि", "पिर", "तुर", "कुप", "चिर", "पति", "रुचि"],
            "top_words": ["कागज", "बाहर", "दवा", "गीत", "पूजा", "राजा", "तारा", "सीता", "हीरा", "पानी", "दरबार"],
            "bottom_words": ["कमल", "नमन", "समय", "पवन", "सरल", "चमन", "मकान", "सफल", "वचन", "जीवन"],
            "shift_words": ["आज", "आम", "इनाम", "ईमान", "उजाला", "ऊर्जा", "एकता", "ओस", "औषधि", "भारत", "शिक्षा"],
            "conjunct_words": ["कर्म", "धर्म", "सत्य", "विद्या", "प्रगति", "शक्ति", "राष्ट्र", "स्वस्थ", "लक्ष्य", "अभ्यास"],
            "paragraphs": [
                "अभ्यास ही सफलता की सबसे बड़ी कुंजी है। जब आप प्रतिदिन शांत मन से टाइपिंग का अभ्यास करते हैं, तो आपकी उँगलियाँ बिना देखे सही अक्षरों को पहचानने लगती हैं; धैर्य रखें और शुद्धता पर ध्यान दें।",
                "भारत की भाषाई विविधता हमारी सबसे बड़ी सांस्कृतिक शक्ति है। सन् 2026 में डिजिटल तकनीक के माध्यम से करोड़ों लोग अपनी मातृभाषा में शिक्षा, विज्ञान और साहित्य का सृजन कर रहे हैं!"
            ]
        }
    },
    "mr": {
        "code": "mr",
        "name": "Marathi (InScript)",
        "native_name": "मराठी",
        "script": "Devanagari",
        "keymap": _build_brahmic_keymap(0x0900, "०१२३४५६७८९"),
        "setup_guide": {
            "native_title": "मराठी (InScript) कीबोर्ड कसा सुरू करावा",
            "native_steps": [
                "१. तुमच्या कीबोर्डवर 'Windows + Space' दाबा आणि 'मराठी (Marathi - InScript)' निवडा.",
                "२. तुमच्या संगणकावर InScript चालू नसले तरी काळजी करू नका! आमचे 'Auto-InScript स्मार्ट मोड' तुमची बटणे आपोआप मराठीत टाइप करेल.",
                "३. डावा हात काना, मात्रा, वेलांटीसाठी (ा, ि, ी, ु, ू, े, ो) आणि उजवा हात व्यंजनांसाठी (क, र, त, च, प, म, न, स, ळ) वापरा."
            ],
            "en_steps": [
                "1. Press 'Win + Space' for Marathi InScript, or type directly using our built-in Auto-InScript Mapper.",
                "2. Left hand controls Matras & Vowels; Right hand controls Consonants."
            ]
        },
        "vocab": {
            "home_words": ["कर", "पर", "तप", "रति", "कवि", "पति", "रुचि", "चिर", "तुर", "किर"],
            "top_words": ["कागद", "बाहेर", "पाणी", "गीत", "पूजा", "राजा", "तारा", "हिरा", "दार", "गाणे"],
            "bottom_words": ["कमळ", "नमन", "वेळ", "पवन", "सरळ", "सकाळ", "सफळ", "वचन", "जीवन", "माती"],
            "shift_words": ["आज", "आकाश", "इमान", "उजेड", "ऊर्जा", "एकता", "ओढ", "औषध", "महाराष्ट्र", "शिक्षण"],
            "conjunct_words": ["कर्म", "धर्म", "सत्य", "विद्या", "प्रगती", "शक्ती", "राष्ट्र", "स्वप्न", "लक्ष्य", "अभ्यास"],
            "paragraphs": [
                "नियमित सराव हाच यशाचा राजमार्ग आहे. जेव्हा तुम्ही एकाग्र चित्ताने टंकलेखनाचा सराव करता, तेव्हा तुमची बोटे न पाहता अचूक अक्षरे शोधतात; आधी अचूकतेवर लक्ष द्या, वेग आपोआप वाढेल.",
                "मराठी भाषा ही आपली सांस्कृतिक ओळख आणि अभिमान आहे. आधुनिक तंत्रज्ञानाच्या युगात मातृभाषेतून जलद आणि अचूक टंकलेखन करणे हे अत्यंत महत्त्वाचे कौशल्य बनले आहे!"
            ]
        }
    },
    "sa": {
        "code": "sa",
        "name": "Sanskrit (InScript)",
        "native_name": "संस्कृतम्",
        "script": "Devanagari",
        "keymap": _build_brahmic_keymap(0x0900, "०१२३४५६७८९"),
        "setup_guide": {
            "native_title": "संस्कृतम् (InScript) टङ्कनफलकं कथंप्रारभेत",
            "native_steps": [
                "१. संगणके 'Windows + Space' नुत्वा 'Sanskrit / Devanagari InScript' चिनुत।",
                "२. अस्माकं 'Auto-InScript' सुविधायाः सहाय्येन विना अतिरिक्त-सेटिंग् अपि साक्षात् संस्कृत-टङ्कनं कर्तुं शक्यते!",
                "३. वामहस्तेन स्वराः मात्राः च (ा, ि, ी, ु, ू, ृ, े, ो), दक्षिणहस्तेन व्यञ्जनानि (क, र, त, च, प, म, न, स) टङ्कनीयानि।"
            ],
            "en_steps": [
                "1. Press 'Win + Space' to select Devanagari InScript, or use the built-in Auto-InScript Mapper immediately.",
                "2. Left hand types Vowels & Matras; Right hand types Consonants."
            ]
        },
        "vocab": {
            "home_words": ["कर", "पर", "तप", "रति", "कवि", "हरि", "गिरि", "पति", "रुचि", "चिर"],
            "top_words": ["राजा", "तारा", "गीता", "पूजा", "सीता", "वाणी", "दाना", "नीर", "तीर", "धीर"],
            "bottom_words": ["कमलम्", "नमनम्", "वनम्", "जलम्", "फलम्", "सत्यम्", "वचनम्", "जीवनम्", "मनः", "सरलम्"],
            "shift_words": ["आत्मा", "ईश्वरः", "उद्यमः", "ऊर्जा", "एकता", "औषधम्", "शिक्षा", "धर्मः", "अहिंसा", "ऋषिः"],
            "conjunct_words": ["कर्म", "धर्मः", "सत्यम्", "विद्या", "प्रज्ञा", "शक्तिः", "राष्ट्रम्", "स्वाध्यायः", "लक्ष्यम्", "अभ्यासः"],
            "paragraphs": [
                "उद्यमेन हि सिध्यन्ति कार्याणि न मनोरथैः। निरन्तर-अभ्यासेन टङ्कन-कौशलं सरलम् अचूकं च भवति; एकाग्रचित्तेन अभ्यासं कुरुत।",
                "विद्या ददाति विनयं, विनयाद् याति पात्रताम्। संस्कृतभाषा विश्वस्य प्राचीनतमा समृद्धा वैज्ञानिक-भाषा च अस्ति; अस्याः टङ्कनं अतीव सरलम् आनन्ददायकं च वर्तते!"
            ]
        }
    },
    "bn": {
        "code": "bn",
        "name": "Bengali (InScript)",
        "native_name": "বাংলা",
        "script": "Bengali",
        "keymap": _build_brahmic_keymap(0x0980, "০১২৩৪৫৬৭৮৯"),
        "setup_guide": {
            "native_title": "বাংলা (InScript) কীবোর্ড কীভাবে চালু করবেন",
            "native_steps": [
                "১. আপনার কীবোর্ডে 'Windows + Space' চেপে 'বাংলা (Bengali - InScript)' নির্বাচন করুন।",
                "২. চিন্তা করবেন না! আমাদের অ্যাপে বিল্ট-ইন 'Auto-InScript' মোড চালু আছে, তাই আপনি সরাসরি টাইপ শুরু করতে পারেন!",
                "৩. বাম হাত দিয়ে কার-চিহ্ন ও স্বরবর্ণ (া, ি, ী, ু, ূ, ে, ো) এবং ডান হাত দিয়ে ব্যঞ্জনবর্ণ (ক, র, ত, চ, প, ম, ন, স) টাইপ করুন।"
            ],
            "en_steps": [
                "1. Press 'Win + Space' to select Bengali InScript, or type directly with our built-in Auto-InScript Mapper.",
                "2. Left hand types Vowel signs (Kar) & Vowels; Right hand types Consonants."
            ]
        },
        "vocab": {
            "home_words": ["কর", "পর", "তপ", "কবি", "রতি", "পতি", "রুচি", "চির", "তুমি", "কি"],
            "top_words": ["কাগজ", "বাহির", "গান", "পূজা", "রাজা", "তারা", "হীরা", "জল", "দাদা", "দিদি"],
            "bottom_words": ["কমল", "নমন", "সময়", "পবন", "সরল", "সকাল", "সফল", "বচন", "জীবন", "মন"],
            "shift_words": ["আজ", "আকাশ", "ইচ্ছা", "ঈগল", "উৎসব", "ঊষা", "একতা", "ওষুধ", "শিক্ষা", "ভারত"],
            "conjunct_words": ["কর্ম", "ধর্ম", "সত্য", "বিদ্যা", "প্রগতি", "শক্তি", "রাষ্ট্র", "স্বপ্ন", "লক্ষ্য", "অভ্যাস"],
            "paragraphs": [
                "নিয়মিত অনুশীলনই সাফল্যের মূল চাবিকাঠি। আপনি যখন শান্ত মনে প্রতিদিন টাইপিং অনুশীলন করবেন, তখন আপনার আঙুলগুলো না দেখেই সঠিক অক্ষর খুঁজে নেবে; প্রথমে নির্ভুলতার দিকে মনোযোগ দিন।",
                "বাংলা ভাষা আমাদের গর্ব ও সংস্কৃতির প্রতীক। আধুনিক প্রযুক্তির যুগে মাতৃভাষায় দ্রুত ও নির্ভুলভাবে টাইপ করতে পারা একটি অত্যন্ত মূল্যবান দক্ষতা!"
            ]
        }
    },
    "pa": {
        "code": "pa",
        "name": "Punjabi (InScript)",
        "native_name": "ਪੰਜਾਬੀ",
        "script": "Gurmukhi",
        "keymap": _build_brahmic_keymap(0x0A00, "੦੧੨੩੪੫੬੭੮੯"),
        "setup_guide": {
            "native_title": "ਪੰਜਾਬੀ (InScript) ਕੀਬੋਰਡ ਕਿਵੇਂ ਚਾਲੂ ਕਰੀਏ",
            "native_steps": [
                "੧. ਆਪਣੇ ਕੀਬੋਰਡ 'ਤੇ 'Windows + Space' ਦਬਾਓ ਅਤੇ 'ਪੰਜਾਬੀ (Punjabi - InScript)' ਚੁਣੋ।",
                "੨. ਫਿਕਰ ਨਾ ਕਰੋ! ਸਾਡਾ ਬਿਲਟ-ਇਨ 'Auto-InScript' ਮੋਡ ਤੁਹਾਡੇ ਅੰਗਰੇਜ਼ੀ ਬਟਨਾਂ ਨੂੰ ਆਪਣੇ ਆਪ ਗੁਰਮੁਖੀ ਵਿੱਚ ਬਦਲ ਦੇਵੇਗਾ!",
                "੩. ਖੱਬਾ ਹੱਥ ਲਗਾਂ-ਮਾਤਰਾਵਾਂ (ਾ, ਿ, ੀ, ੁ, ੂ, ੇ, ੋ) ਲਈ ਅਤੇ ਸੱਜਾ ਹੱਥ ਵਿਅੰਜਨਾਂ (ਕ, ਰ, ਤ, ਚ, ਪ, ਮ, ਨ, ਸ) ਲਈ ਵਰਤੋ।"
            ],
            "en_steps": [
                "1. Press 'Win + Space' for Punjabi Gurmukhi InScript, or type right away using our Auto-InScript Mapper.",
                "2. Left hand types Lagaan-Matra & Vowels; Right hand types Consonants."
            ]
        },
        "vocab": {
            "home_words": ["ਕਰ", "ਪਰ", "ਤਪ", "ਕਵਿ", "ਰੁਚਿ", "ਚਿਰ", "ਤੁਰ", "ਪਤਿ", "ਹਰਿ", "ਗੁਰ"],
            "top_words": ["ਕਾਗਜ", "ਬਾਹਰ", "ਪਾਣੀ", "ਗੀਤ", "ਪੂਜਾ", "ਰਾਜਾ", "ਤਾਰਾ", "ਹੀਰਾ", "ਦਾਤਾ", "ਕਾਰ"],
            "bottom_words": ["ਕਮਲ", "ਨਮਨ", "ਸਮਾਂ", "ਪਵਨ", "ਸਰਲ", "ਸਫਲ", "ਵਚਨ", "ਜੀਵਨ", "ਮਨ", "ਚਮਨ"],
            "shift_words": ["ਅੱਜ", "ਆਕਾਸ਼", "ਇਨਸਾਨ", "ਈਮਾਨ", "ਉਜਾਲਾ", "ਊਰਜਾ", "ਏਕਤਾ", "ਸਿੱਖਿਆ", "ਪੰਜਾਬ", "ਭਾਰਤ"],
            "conjunct_words": ["ਕਰਮ", "ਧਰਮ", "ਸੱਚ", "ਵਿੱਦਿਆ", "ਤਰੱਕੀ", "ਸ਼ਕਤੀ", "ਰਾਸ਼ਟਰ", "ਸੁਪਨਾ", "ਅਭਿਆਸ", "ਮਿਹਨਤ"],
            "paragraphs": [
                "ਲਗਾਤਾਰ ਅਭਿਆਸ ਹੀ ਸਫਲਤਾ ਦੀ ਕੁੰਜੀ ਹੈ। ਜਦੋਂ ਤੁਸੀਂ ਸ਼ਾਂਤ ਮਨ ਨਾਲ ਰੋਜ਼ਾਨਾ ਟਾਈਪਿੰਗ ਦਾ ਅਭਿਆਸ ਕਰਦੇ ਹੋ, ਤਾਂ ਤੁਹਾਡੀਆਂ ਉਂਗਲਾਂ ਬਿਨਾਂ ਦੇਖੇ ਸਹੀ ਅੱਖਰਾਂ ਨੂੰ ਪਛਾਣ ਲੈਂਦੀਆਂ ਹਨ; ਪਹਿਲਾਂ ਸ਼ੁੱਧਤਾ 'ਤੇ ਧਿਆਨ ਦਿਓ।",
                "ਪੰਜਾਬੀ ਭਾਸ਼ਾ ਸਾਡੀ ਸ਼ਾਨ ਅਤੇ ਸੱਭਿਆਚਾਰਕ ਪਛਾਣ ਹੈ। ਡਿਜੀਟਲ ਯੁੱਗ ਵਿੱਚ ਆਪਣੀ ਮਾਂ-ਬੋਲੀ ਗੁਰਮੁਖੀ ਵਿੱਚ ਤੇਜ਼ ਅਤੇ ਸ਼ੁੱਧ ਟਾਈਪਿੰਗ ਕਰਨਾ ਇੱਕ ਬਹੁਤ ਹੀ ਵਧੀਆ ਹੁਨਰ ਹੈ!"
            ]
        }
    },
    "gu": {
        "code": "gu",
        "name": "Gujarati (InScript)",
        "native_name": "ગુજરાતી",
        "script": "Gujarati",
        "keymap": _build_brahmic_keymap(0x0A80, "૦૧૨૩૪૫૬૭૮૯"),
        "setup_guide": {
            "native_title": "ગુજરાતી (InScript) કીબોર્ડ કેવી રીતે ચાલુ કરવું",
            "native_steps": [
                "૧. તમારા કીબોર્ડ પર 'Windows + Space' દબાવો અને 'ગુજરાતી (Gujarati - InScript)' પસંદ કરો.",
                "૨. ચિંતા કરશો નહીં! અમારું બિલ્ટ-ઇન 'Auto-InScript' મોડ ચાલુ છે, તેથી તમે સીધું જ ગુજરાતી ટાઇપિંગ શરૂ કરી શકો છો!",
                "૩. ડાબો હાથ કાના-માત્રા અને સ્વરો (ા, િ, ી, ુ, ૂ, ે, ો) માટે અને જમણો હાથ વ્યંજનો (ક, ર, ત, ચ, પ, મ, ન, સ) માટે વાપરો."
            ],
            "en_steps": [
                "1. Press 'Win + Space' for Gujarati InScript, or start typing directly with our Auto-InScript Mapper.",
                "2. Left hand types Matras & Vowels; Right hand types Consonants."
            ]
        },
        "vocab": {
            "home_words": ["કર", "પર", "તપ", "કવિ", "રતિ", "પતિ", "રુચિ", "ચિર", "તુર", "હરિ"],
            "top_words": ["કાગળ", "બહાર", "પાણી", "ગીત", "પૂજા", "રાજા", "તારા", "હીરા", "દાદા", "કાર"],
            "bottom_words": ["કમળ", "નમન", "સમય", "પવન", "સરળ", "સવાર", "સફળ", "વચન", "જીવન", "મન"],
            "shift_words": ["આજ", "આકાશ", "ઇનામ", "ઈમાન", "ઉજાસ", "ઊર્જા", "એકતા", "ઔષધ", "ગુજરાત", "શિક્ષણ"],
            "conjunct_words": ["કર્મ", "ધર્મ", "સત્ય", "વિદ્યા", "પ્રગતિ", "શક્તિ", "રાષ્ટ્ર", "સ્વપ્ન", "લક્ષ્ય", "અભ્યાસ"],
            "paragraphs": [
                "નિયમિત મહાવરો એ જ સફળતાની સાચી ચાવી છે. જ્યારે તમે શાંત મનથી દરરોજ ટાઇપિંગનો અભ્યાસ કરો છો, ત્યારે તમારી આંગળીઓ કીબોર્ડ જોયા વગર જ સાચા અક્ષરો શોધી લે છે; ચોકસાઈ પર ધ્યાન આપો.",
                "ગુજરાતી ભાષા આપણી સંસ્કૃતિ અને ગૌરવ છે. આધુનિક ડિજિટલ યુગમાં માતૃભાષામાં ઝડપી અને ભૂલરહિત ટાઇપિંગ કરવું એ દરેક માટે ખૂબ જ ઉપયોગી કૌશલ્ય છે!"
            ]
        }
    },
    "or": {
        "code": "or",
        "name": "Odia (InScript)",
        "native_name": "ଓଡ଼ିଆ",
        "script": "Odia",
        "keymap": _build_brahmic_keymap(0x0B00, "୦୧୨୩୪୫୬୭୮୯"),
        "setup_guide": {
            "native_title": "ଓଡ଼ିଆ (InScript) କିবୋର୍ଡ୍ କିପରି ଚାଲୁ କରିବେ",
            "native_steps": [
                "୧. ଆପଣଙ୍କ କିବୋର୍ଡରେ 'Windows + Space' ଦବାନ୍ତୁ ଏବଂ 'ଓଡ଼ିଆ (Odia - InScript)' ବାଛନ୍ତୁ।",
                "୨. ଚିନ୍ତା କରନ୍ତୁ ନାହିଁ! ଆମର 'Auto-InScript' ସ୍ମାର୍ଟ ମୋଡ୍ ସାହାଯ୍ୟରେ ଆପଣ ସିଧାସଳଖ ଓଡ଼ିଆ ଟାଇపిଂ ଆରମ୍ଭ କରିପାରିବେ!",
                "୩. ବାମ ହାତ ମାତ୍ରା ଓ ସ୍ୱରବର୍ଣ୍ଣ (ା, ି, ୀ, ୁ, ୂ, େ, ୋ) ପାଇଁ ଏବଂ ডାହାଣ ହାତ ବ୍ୟଞ୍ଜନବର୍ଣ୍ଣ (କ, ର, ତ, ଚ, ପ, ମ, ନ, ସ) ପାଇଁ ବ୍ୟବହାର କରନ୍ତୁ।"
            ],
            "en_steps": [
                "1. Press 'Win + Space' for Odia InScript, or type immediately with our built-in Auto-InScript Mapper.",
                "2. Left hand types Matras & Vowels; Right hand types Consonants."
            ]
        },
        "vocab": {
            "home_words": ["କର", "ପର", "ତପ", "କବି", "ରତି", "ପତି", "ରୁଚି", "ଚିର", "ହରି", "ഗିରି"].copy() if False else ["କର", "ପର", "ତପ", "କବି", "ରତି", "ପତି", "ରୁଚି", "ଚିର", "ହରି", "ଗିରି"],
            "top_words": ["କାଗଜ", "ବାହାର", "ପାଣି", "ଗୀତ", "ପୂଜା", "ରାଜା", "ତାରା", "ହୀରା", "ଦାନ", "କାର"],
            "bottom_words": ["କମଳ", "ନମନ", "ସମୟ", "ପବନ", "ସରଳ", "ସକାଳ", "ସଫଳ", "ବଚନ", "ଜୀବନ", "ମନ"],
            "shift_words": ["ଆଜି", "ଆକାଶ", "ଇচ্ছা", "ଈଶ୍ୱର", "ଉତ୍ସବ", "ଊର୍ଜା", "ଏକତା", "ଔଷଧ", "ଓଡ଼ିଶା", "ଶିକ୍ଷା"],
            "conjunct_words": ["କର୍ମ", "ଧର୍ମ", "ସତ୍ୟ", "ବିଦ୍ୟା", "ପ୍ରଗତି", "ଶକ୍ତି", "ରାଷ୍ଟ୍ର", "ସ୍ୱପ୍ନ", "ଲକ୍ଷ୍ୟ", "ଅଭ୍ୟାସ"],
            "paragraphs": [
                "ନିୟମିତ ଅଭ୍ୟାସ ହିଁ ସଫଳତାର ମୂଳମନ୍ତ୍ର ଅଟେ। ଯେତେବେଳେ ଆପଣ ଶାନ୍ତ ମନରେ ପ୍ରତିଦିନ ଟାଇପିଂ ଅଭ୍ୟାସ କରନ୍ତି, ଆପଣଙ୍କ ଆଙ୍ଗୁଠିଗୁଡ଼ିକ ନ ଦେଖି ସଠିକ୍ ଅକ୍ଷର ଚିହ୍ନିପାରେ; ପ୍ରଥମେ ସଠିକତା ଉପରେ ଧ୍ୟାନ ଦିଅନ୍ତୁ।",
                "ଓଡ଼ିଆ ଭାଷା ଆମର ଗୌରବ ଓ ଶାସ୍ତ୍ରୀୟ ପରିଚୟ ଅଟେ। ଆଧୁନିକ ପ୍ରଯୁକ୍ତିବିଦ୍ୟା ଯୁଗରେ ମାତୃଭାଷାରେ ଦ୍ରୁତ ଏବଂ ସଠିକ୍ ଟାଇପିଂ ଶିଖିବା ଅତ୍ୟନ୍ତ ଉପଯୋଗୀ!"
            ]
        }
    },
    "ta": {
        "code": "ta",
        "name": "Tamil (InScript)",
        "native_name": "தமிழ்",
        "script": "Tamil",
        "keymap": _build_brahmic_keymap(0x0B80, "௦௧௨௩௪௫௬௭௮௯"),
        "setup_guide": {
            "native_title": "தமிழ் (InScript) விசைப்பலகையை இயக்குவது எப்படி",
            "native_steps": [
                "1. உங்கள் கணினியில் 'Windows + Space' அழுத்தி 'தமிழ் (Tamil - InScript)' என்பதைத் தேர்ந்தெடுக்கவும்.",
                "2. கவலை வேண்டாம்! எமது 'Auto-InScript' வசதி மூலம் விசைப்பலகை மாற்றாமலேயே நேரடியாகத் தமிழில் தட்டச்சு செய்யலாம்!",
                "3. இடது கை உயிர் மற்றும் உயிர்மெய் குறிகளுக்கும் (ா, ி, ீ, ு, ூ, ெ, ே, ொ, ோ, ்), வலது கை மெய்யெழுத்துக்களுக்கும் (க, ச, ட, த, ப, ற, ம, ந, ல, வ) பயன்படுகிறது."
            ],
            "en_steps": [
                "1. Press 'Win + Space' for Tamil InScript, or type right away with our built-in Auto-InScript Mapper.",
                "2. Left hand types Vowel signs & Pulli (்); Right hand types Consonants."
            ]
        },
        "vocab": {
            "home_words": ["கர", "பர", "தப", "கவி", "பதி", "சிர", "புலி", "கிரி", "ரிசி", "பரி"],
            "top_words": ["காகம்", "பாதை", "பாடல்", "பூஜை", "ராஜா", "தாரா", "நீர்", "தீர", "கார்", "பார்"],
            "bottom_words": ["மலர்", "மனம்", "சமயம்", "பவனம்", "பழம்", "வனம்", "சफल", "வசனம்", "ஜீவன்", "நிலம்"].copy() if False else ["மலர்", "மனம்", "சமயம்", "பவனம்", "பழம்", "வனம்", "காலம்", "வசனம்", "வாழ்க்கை", "நிலம்"],
            "shift_words": ["அம்மா", "ஆकाश", "இனிமை", "ஈகை", "உலகம்", "ஊக்கம்", "ஒற்றுமை", "ஔடதம்", "தமிழ்நாடு", "கல்வி"].copy() if False else ["அம்மா", "ஆகாயம்", "இனிமை", "ஈகை", "உலகம்", "ஊக்கம்", "ஒற்றுமை", "ஔடதம்", "தமிழ்நாடு", "கல்வி"],
            "conjunct_words": ["தர்மம்", "சத்தியம்", "பயிற்சி", "முயற்சி", "வெற்றி", "சக்தி", "பண்பு", "இலக்கு", "கல்வி", "அறிவு"],
            "paragraphs": [
                "தொடர்ச்சியான பயிற்சியே வெற்றியின் திறவுகோல் ஆகும். தினமும் அமைதியான மனதுடன் தட்டச்சுப் பயிற்சி செய்யும்போது, உங்கள் விரல்கள் விசைப்பலகையைப் பார்க்காமலேயே சரியான எழுத்துக்களைத் தட்டச்சு செய்யும்.",
                "செம்மொழியாம் தமிழ் மொழி நமது பண்பாட்டின் அடையாளம் ஆகும். நவீன கணினி யுகத்தில் தாய்மொழியில் விரைவாகவும் துல்லியமாகவும் தட்டச்சு செய்வது மிகச் சிறந்த திறமையாகும்!"
            ]
        }
    },
    "te": {
        "code": "te",
        "name": "Telugu (InScript)",
        "native_name": "తెలుగు",
        "script": "Telugu",
        "keymap": _build_brahmic_keymap(0x0C00, "౦౧౨౩౪౫౬౭౮౯"),
        "setup_guide": {
            "native_title": "తెలుగు (InScript) కీబోర్డును ఎలా ప్రారంభించాలి",
            "native_steps": [
                "1. మీ కీబోర్డుపై 'Windows + Space' నొక్కి 'తెలుగు (Telugu - InScript)' ఎంచుకోండి.",
                "2. చింతించకండి! మా యాప్‌లోని 'Auto-InScript' సదుపాయంతో మీరు నేరుగా తెలుగులో టైపింగ్ ప్రారంభించవచ్చు!",
                "3. ఎడమ చేతితో గుణింతపు గుర్తులు మరియు అచ్చులు (ా, ి, ీ, ు, ూ, ె, ే, ొ, ో, ్), కుడి చేతితో హల్లులు (క, ర, త, చ, ప, మ, న, స) టైప్ చేయండి."
            ],
            "en_steps": [
                "1. Press 'Win + Space' for Telugu InScript, or start typing directly with our Auto-InScript Mapper.",
                "2. Left hand types Gunintalu & Vowels; Right hand types Consonants."
            ]
        },
        "vocab": {
            "home_words": ["కర", "పర", "తప", "కవి", "రతి", "పతి", "రుచి", "చిర", "హరి", "గిరి"],
            "top_words": ["కాగితం", "బాట", "పాట", "గీత", "పూజ", "రాజు", "తార", "హీర", "నీరు", "తీరం"],
            "bottom_words": ["కమలం", "నమనం", "సమయం", "పవనం", "సరళం", "సఫలం", "వచనం", "జీవనం", "మనసు", "వనం"],
            "shift_words": ["అమ్మ", "ఆకాశం", "ఇల్లు", "ఈగ", "ఉదయం", "ఊరు", "ఐక్యత", "ఔషధం", "తెలుగు", "విద్య"],
            "conjunct_words": ["కర్మ", "ధర్మం", "సత్యం", "విద్య", "ప్రగతి", "శక్తి", "రాష్ట్రం", "స్వప్నం", "లక్ష్యం", "అభ్యాసం"],
            "paragraphs": [
                "నిరంతర అభ్యాసమే విజయానికి మూల సూత్రం. మీరు ప్రతిరోజూ ప్రశాంతమైన మనస్సుతో టైపింగ్ సాధన చేసినప్పుడు, మీ వేళ్లు కీబోర్డు వైపు చూడకుండానే సరైన అక్షరాలను టైప్ చేస్తాయి; ముందుగా కచ్చితత్వంపై దృష్టి పెట్టండి.",
                "దేశ భాషలందు తెలుగు లెస్స అన్నారు పెద్దలు. ఆధునిక సాంకేతిక యుగంలో మాతృభాషలో వేగంగా మరియు తప్పులు లేకుండా టైప్ చేయడం ఎంతో విలువైన నైపుణ్యం!"
            ]
        }
    },
    "kn": {
        "code": "kn",
        "name": "Kannada (InScript)",
        "native_name": "ಕನ್ನಡ",
        "script": "Kannada",
        "keymap": _build_brahmic_keymap(0x0C80, "೦೧೨೩೪೫೬೭೮೯"),
        "setup_guide": {
            "native_title": "ಕನ್ನಡ (InScript) ಕೀಬೋರ್ಡ್ ಆನ್ ಮಾಡುವುದು ಹೇಗೆ",
            "native_steps": [
                "1. ನಿಮ್ಮ ಕೀಬೋರ್ಡ್‌ನಲ್ಲಿ 'Windows + Space' ಒತ್ತಿ ಮತ್ತು 'ಕನ್ನಡ (Kannada - InScript)' ಆಯ್ಕೆಮಾಡಿ.",
                "2. ಚಿಂತಿಸಬೇಡಿ! ನಮ್ಮ 'Auto-InScript' ಸ್ಮಾರ್ಟ್ ಮೋಡ್ ಮೂಲಕ ನೀವು ಯಾವುದೇ ಸೆಟ್ಟಿಂಗ್ ಬದಲಾಯಿಸದೆಯೂ ನೇರವಾಗಿ ಕನ್ನಡದಲ್ಲಿ ಟೈಪ್ ಮಾಡಬಹುದು!",
                "3. ಎಡಗೈಯಿಂದ ಗುಣಿತಾಕ್ಷರ ಚಿಹ್ನೆಗಳು ಮತ್ತು ಸ್ವರಗಳನ್ನು (ಾ, ಿ, ೀ, ು, ೂ, ೆ, ೇ, ೊ, ೋ, ್), ಬಲಗೈಯಿಂದ ವ್ಯಂಜನಗಳನ್ನು (ಕ, ರ, ತ, ಚ, ಪ, ಮ, ನ, ಸ) ಟೈಪ್ ಮಾಡಿ."
            ],
            "en_steps": [
                "1. Press 'Win + Space' for Kannada InScript, or type immediately with our built-in Auto-InScript Mapper.",
                "2. Left hand types Vowel signs & Vowels; Right hand types Consonants."
            ]
        },
        "vocab": {
            "home_words": ["ಕರ", "ಪರ", "ತಪ", "ಕವಿ", "ರತಿ", "ಪತಿ", "ರುಚಿ", "ಚಿರ", "ಹರಿ", "ಗಿರಿ"],
            "top_words": ["ಕಾಗದ", "ಬಾಗಿಲು", "ಹಾಡು", "ಗೀತೆ", "ಪೂಜೆ", "ರಾಜ", "ತಾರೆ", "ಹೀರ", "ನೀರು", "ತೀರ"],
            "bottom_words": ["ಕಮಲ", "ನಮನ", "ಸಮಯ", "ಪವನ", "ಸರಳ", "ಸಫಲ", "ವಚನ", "ಜೀವನ", "ಮನಸ್ಸು", "ವನ"],
            "shift_words": ["ಅಮ್ಮ", "ಆಕಾಶ", "ಇನಾಮು", "ಈಶ್ವರ", "ಉದಯ", "ಊರು", "ಏಕತೆ", "ಔಷಧ", "ಕರ್ನಾಟಕ", "ಶಿಕ್ಷಣ"],
            "conjunct_words": ["ಕರ್ಮ", "ಧರ್ಮ", "ಸತ್ಯ", "ವಿದ್ಯೆ", "ಪ್ರಗತಿ", "ಶಕ್ತಿ", "ರಾಷ್ಟ್ರ", "ಸ್ವಪ್ನ", "ಲಕ್ಷ್ಯ", "ಅಭ್ಯಾಸ"],
            "paragraphs": [
                "ನಿರಂತರ ಅಭ್ಯಾಸವೇ ಯಶಸ್ಸಿನ ಗುಟ್ಟು. ನೀವು ಪ್ರತಿದಿನ ಶಾಂತ ಮನಸ್ಸಿನಿಂದ ಟೈಪಿಂಗ್ ಅಭ್ಯಾಸ ಮಾಡಿದಾಗ, ನಿಮ್ಮ ಬೆರಳುಗಳು ಕೀಬೋರ್ಡ್ ನೋಡದೆಯೇ ಸರಿಯಾದ ಅಕ್ಷರಗಳನ್ನು ಗುರುತಿಸುತ್ತವೆ; ಮೊದಲು ನಿಖರತೆಗೆ ಗಮನ ಕೊಡಿ.",
                "ಕನ್ನಡ ಭಾಷೆಯು ನಮ್ಮ ಹೆಮ್ಮೆ ಮತ್ತು ಸಾಂಸ್ಕೃತಿಕ ಗುರುತಾಗಿದೆ. ಆಧುನಿಕ ತಂತ್ರಜ್ಞಾನ ಯುಗದಲ್ಲಿ ಮಾತೃಭಾಷೆಯಲ್ಲಿ ವೇಗವಾಗಿ ಮತ್ತು ನಿಖರವಾಗಿ ಟೈಪ್ ಮಾಡುವುದು ಅತ್ಯಂತ ಉಪಯುಕ್ತ ಕೌಶಲ್ಯವಾಗಿದೆ!"
            ]
        }
    },
    "ml": {
        "code": "ml",
        "name": "Malayalam (InScript)",
        "native_name": "മലയാളം",
        "script": "Malayalam",
        "keymap": _build_brahmic_keymap(0x0D00, "൦൧൨൩൪൫൬൭൮൯"),
        "setup_guide": {
            "native_title": "മലയാളം (InScript) കീബോർഡ് എങ്ങനെ ഓണാക്കാം",
            "native_steps": [
                "1. കീബോർഡിൽ 'Windows + Space' അമർത്തി 'മലയാളം (Malayalam - InScript)' തിരഞ്ഞെടുക്കുക.",
                "2. വിഷമിക്കേണ്ട! ഞങ്ങളുടെ 'Auto-InScript' മോഡ് ഉള്ളതിനാൽ സെറ്റിംഗ്സ് മാറ്റാതെ തന്നെ നിങ്ങൾക്ക് നേരിട്ട് മലയാളം ടൈപ്പ് ചെയ്യാം!",
                "3. ഇടതുകൈ സ്വരചിഹ്നങ്ങൾക്കും സ്വരങ്ങൾക്കും (ാ, ി, ീ, ു, ൂ, െ, േ, ൊ, ോ, ്), വലതുകൈ വ്യഞ്ജനങ്ങൾക്കും (ക, ര, ത, ച, പ, മ, ന, സ) ഉപയോഗിക്കുക."
            ],
            "en_steps": [
                "1. Press 'Win + Space' for Malayalam InScript, or start typing right away with our Auto-InScript Mapper.",
                "2. Left hand types Vowel signs & Chandrakkala (്); Right hand types Consonants."
            ]
        },
        "vocab": {
            "home_words": ["കര", "പര", "തപ", "കവി", "രതി", "പതി", "രുചി", "ചിര", "ഹരി", "ഗിരി"],
            "top_words": ["കാകൻ", "പാത", "ഗാനം", "ഗീതം", "പൂജ", "രാജാ", "താര", "തീരം", "നീര്", "കാറ്"],
            "bottom_words": ["കമലം", "നമനം", "സമയം", "പവനൻ", "സരളം", "സഫലം", "വചനം", "ജീവിതം", "മനസ്സ്", "വനം"],
            "shift_words": ["അമ്മ", "ആകാശം", "ഇല", "ഈശ്വരൻ", "ഉദയം", "ഊർജ്ജം", "ഐക്യം", "ഔഷധം", "കേരളം", "വിദ്യ"],
            "conjunct_words": ["കർമ്മം", "ധർമ്മം", "സത്യം", "വിദ്യ", "പ്രഗതി", "ശക്തി", "രാഷ്ട്രം", "സ്വപ്നം", "ലക്ഷ്യം", "അഭ്യാസം"],
            "paragraphs": [
                "നിരന്തരമായ പരിശീലനമാണ് വിജയത്തിന്റെ അടിസ്ഥാനം. ശാന്തമായ മനസ്സോടെ ദിവസവും ടൈപ്പിംഗ് പരിശീലിക്കുമ്പോൾ, കീബോർഡിൽ നോക്കാതെ തന്നെ ശരിയായ അക്ഷരങ്ങൾ ടൈപ്പ് ചെയ്യാൻ നിങ്ങളുടെ വിരലുകൾ പഠിക്കുന്നു.",
                "മലയാള ഭാഷ നമ്മുടെ സംസ്കാരവും അഭിമാനവുമാണ്. ആധുനിക ഡിജിറ്റൽ യുഗത്തിൽ മാതൃഭാഷയിൽ വേഗത്തിലും കൃത്യതയിലും ടൈപ്പ് ചെയ്യാൻ പഠിക്കുന്നത് വളരെ മികച്ചൊരു കഴിവാണ്!"
            ]
        }
    },
    "as": {
        "code": "as",
        "name": "Assamese (InScript)",
        "native_name": "অসমীয়া",
        "script": "Assamese",
        "keymap": _build_brahmic_keymap(0x0980, "০১২৩৪৫৬৭৮৯", extra_overrides={
            "KeyJ": {"main": "ৰ", "shift": "ড়"},
            "KeyB": {"main": "ৱ", "shift": "ঢ়"}
        }),
        "setup_guide": {
            "native_title": "অসমীয়া (InScript) কীবোৰ্ড কেনেকৈ অন কৰিব",
            "native_steps": [
                "১. আপোনাৰ কীবোৰ্ডত 'Windows + Space' টিপি 'অসমীয়া (Assamese - InScript)' বাছনি কৰক।",
                "২. চিন্তা নকৰিব! আমাৰ 'Auto-InScript' স্মাৰ্ট মোডৰ জৰিয়তে আপুনি পোনে পোনে অসমীয়া টাইপিং আৰম্ভ কৰিব পাৰে!",
                "৩. বাওঁ হাত স্বৰচিহ্ন আৰু স্বৰবৰ্ণৰ বাবে (া, ি, ী, ু, ূ, ে, ো) আৰু সোঁ হাত ব্যঞ্জনবৰ্ণৰ বাবে (ক, ৰ, ত, চ, প, ম, ন, স, ৱ) ব্যৱহাৰ কৰক।"
            ],
            "en_steps": [
                "1. Press 'Win + Space' for Assamese InScript, or type directly using our built-in Auto-InScript Mapper.",
                "2. Left hand types Vowel signs & Vowels; Right hand types Consonants (including ৰ and ৱ)."
            ]
        },
        "vocab": {
            "home_words": ["কৰ", "পৰ", "তপ", "কবি", "ৰতি", "পতি", "ৰুচি", "চিৰ", "হৰি", "গিৰি"],
            "top_words": ["কাগজ", "বাহিৰ", "গান", "পূজা", "ৰজা", "তৰা", "হীৰা", "পানী", "দাদা", "গাড়ী"],
            "bottom_words": ["কমল", "নমন", "সময়", "পৱন", "সৰল", "সকাল", "সফল", "বচন", "জীৱন", "মন"],
            "shift_words": ["আজি", "আকাশ", "ইচ্ছা", "ঈশ্বৰ", "উৎসৱ", "ঊষা", "একতা", "ঔষধ", "অসম", "শিক্ষা"],
            "conjunct_words": ["কৰ্ম", "ধৰ্ম", "সত্য", "বিদ্যা", "প্ৰগতি", "শক্তি", "ৰাষ্ট্ৰ", "স্বপ্ন", "লক্ষ্য", "অভ্যাস"],
            "paragraphs": [
                "নিয়মীয়া অনুশীলনেই সফলতাৰ মূল চাবিকাঠি। যেতিয়া আপুনি শান্ত মনেৰে প্ৰতিদিনে টাইপিং অনুশীলন কৰিব, তেতিয়া আপোনাৰ আঙুলিবোৰে নোচোৱাকৈয়ে সঠিক আখৰ বিচাৰি পাব; প্ৰথমে শুদ্ধতাৰ ওপৰত গুৰুত্ব দিয়ক।",
                "অসমীয়া ভাষা আমাৰ গৌৰৱ আৰু স্বাভিমান। আধুনিক প্ৰযুক্তিৰ যুগত মাতৃভাষাত দ্ৰুত আৰু শুদ্ধকৈ টাইপ কৰিব জনাটো এটা অত্যন্ত মূল্যৱান দক্ষতা!"
            ]
        }
    },
    "ur": {
        "code": "ur",
        "name": "Urdu (InScript / Standard)",
        "native_name": "اردو",
        "script": "Perso-Arabic",
        "keymap": URDU_KEYMAP,
        "setup_guide": {
            "native_title": "اردو کی بورڈ کیسے آن کریں",
            "native_steps": [
                "۱۔ اپنے کمپیوٹر پر 'Windows + Space' دبائیں اور 'اردو (Urdu)' کی بورڈ منتخب کریں۔",
                "۲۔ پریشان نہ ہوں! ہمارا بلٹ ان 'Auto-Mapper' موڈ آن ہے، اس لیے آپ بغیر کسی سیٹنگ کے براہِ راست اردو ٹائپنگ شروع کر سکتے ہیں!",
                "۳۔ اپنی انگلیاں ہوم رو (ا، س، د، ف اور ج، ک، ل، ؛) پر رکھیں اور اسکرین پر دیکھ کر مشق کریں۔"
            ],
            "en_steps": [
                "1. Press 'Win + Space' to select Urdu keyboard, or start typing immediately with our built-in Auto-Mapper!",
                "2. Keep your fingers anchored on the Home Row and follow the highlighted on-screen keycaps."
            ]
        },
        "vocab": {
            "home_words": ["دل", "سدا", "کل", "جس", "گل", "حل", "فصل", "لسان", "کال", "جال"],
            "top_words": ["قلم", "وقت", "علم", "رات", "تاج", "یار", "پر", "تارا", "دریا", "ہوا"],
            "bottom_words": ["زمیں", "شام", "چمن", "وطن", "بہار", "نور", "منزل", "سفر", "زندگی", "محبت"],
            "shift_words": ["آسمان", "اخلاق", "صبر", "ضیا", "طاقت", "ظفر", "غالب", "خوشی", "ذوق", "ثمر"],
            "conjunct_words": ["محنت", "کامیابی", "صداقت", "تعلیم", "ترقی", "مقصد", "مشق", "مہارت", "خوبصورت", "مستقبل"],
            "paragraphs": [
                "مسلسل مشق ہی کامیابی کی سب سے بڑی کنجی ہے۔ جب آپ روزانہ پرسکون ذہن کے ساتھ ٹائپنگ کی مشق کرتے ہیں تو آپ کی انگلیاں کی بورڈ دیکھے بغیر درست حروف کو پہچان لیتی ہیں؛ ہمیشہ درستگی پر توجہ دیں۔",
                "اردو ایک نہایت شیریں اور خوبصورت زبان ہے۔ جدید ڈیجیٹل دور میں اپنی مادری زبان میں تیز اور درست ٹائپنگ کرنا ایک انتہائی مفید ہنر ہے!"
            ]
        }
    }
}


def build_reverse_char_to_finger_map(keymap: dict):
    """Maps every character in an InScript keymap to its finger code (L_PINKY..R_PINKY) and physical key."""
    fmap = {" ": "THUMB"}
    for code, pair in keymap.items():
        finger = CODE_TO_FINGER.get(code, "R_INDEX")
        if pair.get("main"):
            fmap[pair["main"]] = finger
        if pair.get("shift"):
            fmap[pair["shift"]] = finger
    return fmap


GUNINTALU_LABELS = {
    "hi": "बारहखड़ी (Barakhadi — 12 Vowel Combinations)",
    "mr": "बाराखडी (Barakhadi — 12 Vowel Combinations)",
    "sa": "मात्रा-संयोगः (Barakhadi — 12 Vowel Combinations)",
    "bn": "কার-চিহ্ন ও ব্যঞ্জন (Barakhadi — 12 Vowel Combinations)",
    "as": "কাৰ-চিহ্ন আৰু ব্যঞ্জন (Barakhadi — 12 Vowel Combinations)",
    "pa": "ਮੁਹਾਰਨੀ (Muharni — 12 Vowel Combinations)",
    "gu": "બારાખડી (Barakhadi — 12 Vowel Combinations)",
    "or": "ମାତ୍ରା ଓ ଫଳା (Barakhadi — 12 Vowel Combinations)",
    "ta": "உயிர்மெய் எழுத்துக்கள் (Uyirmei — 12 Vowel Combinations)",
    "te": "గుణింతాలు (Gunintalu — 14 Vowel Combinations)",
    "kn": "ಕಾಗುಣಿತ (Kagunita — 14 Vowel Combinations)",
    "ml": "സ്വരചിഹ്ന സംയോജനം (Gunintalu — 14 Vowel Combinations)",
}


def _build_gunintalu_unit(lang_code: str, native: str, km: dict):
    """
    Constructs a dedicated 5-lesson Gunintalu / Barakhadi / Kagunita / Uyirmei unit
    teaching all 12-14 vowel matra combinations for every consonant varga!
    """
    if lang_code == "ur":
        return None

    # Build authentic matra sequence for each script family
    if lang_code in ("te", "kn", "ml"):
        # Short & Long e/o + Anusvara + Visarga (14 forms)
        matras = [
            "", km["KeyE"]["main"], km["KeyF"]["main"], km["KeyR"]["main"],
            km["KeyG"]["main"], km["KeyT"]["main"], km["KeyZ"]["main"], km["KeyS"]["main"],
            km["KeyW"]["main"], km["Backquote"]["main"], km["KeyA"]["main"], km["KeyQ"]["main"],
            km["KeyX"]["main"], km["Minus"]["shift"],
        ]
    elif lang_code == "ta":
        # Pure 12 Tamil Uyirmei vowel forms
        matras = [
            "", km["KeyE"]["main"], km["KeyF"]["main"], km["KeyR"]["main"],
            km["KeyG"]["main"], km["KeyT"]["main"], km["KeyZ"]["main"], km["KeyS"]["main"],
            km["KeyW"]["main"], km["Backquote"]["main"], km["KeyA"]["main"], km["KeyQ"]["main"],
        ]
    else:
        # Standard 12 Barakhadi forms (Devanagari, Bengali, Assamese, Gurmukhi, Gujarati, Odia)
        matras = [
            "", km["KeyE"]["main"], km["KeyF"]["main"], km["KeyR"]["main"],
            km["KeyG"]["main"], km["KeyT"]["main"], km["KeyS"]["main"], km["KeyW"]["main"],
            km["KeyA"]["main"], km["KeyQ"]["main"], km["KeyX"]["main"], km["Minus"]["shift"],
        ]

    def series(cons_list):
        out = []
        for c in cons_list:
            for m in matras:
                out.append(f"{c}{m}")
        return " ".join(out)

    # Consonant groups (Tamil uses its valid consonant set without unvoiced/voiced aspirates)
    home_cons = [km["KeyK"]["main"], km["KeyL"]["main"], km["Semicolon"]["main"], km["KeyH"]["main"], km["KeyJ"]["main"]]
    if lang_code == "ta":
        varga_1 = [km["KeyK"]["main"], km["Semicolon"]["main"], km["Quote"]["main"], km["KeyL"]["main"]]
        varga_2 = [km["KeyH"]["main"], km["KeyC"]["main"], km["Slash"]["main"], km["KeyJ"]["main"]]
        varga_3 = [km["KeyN"]["main"], km["KeyB"]["main"], km["KeyV"]["main"], km["KeyM"]["main"]]
    else:
        varga_1 = [km["KeyK"]["main"], km["KeyK"]["shift"], km["KeyI"]["main"], km["KeyI"]["shift"], km["Semicolon"]["main"], km["KeyP"]["main"]]
        varga_2 = [km["Quote"]["main"], km["BracketLeft"]["main"], km["KeyL"]["main"], km["KeyO"]["main"], km["KeyV"]["main"]]
        varga_3 = [km["KeyH"]["main"], km["KeyY"]["main"], km["KeyC"]["main"], km["Slash"]["main"], km["KeyN"]["main"], km["KeyB"]["main"], km["KeyM"]["main"], km["KeyU"]["main"]]

    # Mixed rapid-fire alternating consonant + matra sprint
    mixed_cons = [km["KeyK"]["main"], km["KeyH"]["main"], km["KeyL"]["main"], km["KeyC"]["main"], km["KeyV"]["main"], km["KeyJ"]["main"], km["KeyN"]["main"], km["KeyM"]["main"]]
    mixed_tokens = []
    for idx in range(36):
        c = mixed_cons[idx % len(mixed_cons)]
        m = matras[(idx * 5 + 1) % len(matras)]
        mixed_tokens.append(f"{c}{m}")

    label = GUNINTALU_LABELS.get(lang_code, "Gunintalu / Barakhadi (12 Vowel Combinations)")
    sample_row = " ".join(f"{home_cons[0]}{m}" for m in matras[:6])

    return {
        "unit_id": f"{lang_code}_u4_gunintalu",
        "unit_number": 4,
        "title": f"Unit 4: {native} {label}",
        "subtitle": f"Master all {len(matras)} vowel matra combinations for every consonant ({sample_row} ...). Right hand strikes the consonant; Left hand sweeps the matras!",
        "focus_keys": [m for m in matras if m][:8],
        "lessons": [
            {
                "id": f"{lang_code}_u4_g1",
                "title": f"4.1 Home-Row Consonants {label.split('(')[0].strip()} ({' '.join(home_cons)})",
                "type": "key_drill",
                "new_keys": [m for m in matras if m][:6],
                "target_wpm": 16,
                "min_accuracy": 90,
                "tip": f"Type each Home-Row consonant with your Right Hand, then immediately sweep through all {len(matras)} vowel matras with your Left Hand!",
                "text": series(home_cons[:4])
            },
            {
                "id": f"{lang_code}_u4_g2",
                "title": f"4.2 Ka & Cha Varga Combinations ({' '.join(varga_1[:4])})",
                "type": "key_drill",
                "new_keys": varga_1[:4],
                "target_wpm": 17,
                "min_accuracy": 90,
                "tip": f"Build complete {len(matras)}-vowel rhythm for {' '.join(varga_1[:4])}. Notice how your Left Hand repeats the exact same matra pattern!",
                "text": series(varga_1[:4])
            },
            {
                "id": f"{lang_code}_u4_g3",
                "title": f"4.3 Ta & Tha Varga Combinations ({' '.join(varga_2[:4])})",
                "type": "key_drill",
                "new_keys": varga_2[:4],
                "target_wpm": 18,
                "min_accuracy": 90,
                "tip": f"Practice full vowel combinations for {' '.join(varga_2[:4])} without looking down at the keyboard.",
                "text": series(varga_2[:4])
            },
            {
                "id": f"{lang_code}_u4_g4",
                "title": f"4.4 Pa Varga & Ya-Ra-La-Va-Sa Combinations ({' '.join(varga_3[:5])})",
                "type": "key_drill",
                "new_keys": varga_3[:5],
                "target_wpm": 18,
                "min_accuracy": 90,
                "tip": f"Master the remaining frequent consonants ({' '.join(varga_3[:5])}) across all {len(matras)} vowel sounds.",
                "text": series(varga_3[:4])
            },
            {
                "id": f"{lang_code}_u4_g5",
                "title": f"4.5 Rapid-Fire Mixed {label.split('(')[0].strip()} Sprint",
                "type": "word_drill",
                "new_keys": [],
                "target_wpm": 20,
                "min_accuracy": 91,
                "tip": "Randomly alternating consonants and matras! This locks in real-world touch-typing speed for every syllable.",
                "text": " ".join(mixed_tokens)
            }
        ]
    }


def generate_units_for_indian_language(lang_code: str):
    """
    Generates a full 8-Unit, 24-Lesson structured InScript course for the specified Indian language!
    Starts from Home Row Matras & Consonants -> Top Row -> Bottom Row -> Shift Vowels/Aspirates ->
    Conjuncts (Halant) -> Native Numbers -> High-Frequency Words -> Full Paragraphs with Punctuation.
    """
    pack = INDIAN_LANGUAGE_PACKS.get(lang_code)
    if not pack:
        return []

    km = pack["keymap"]
    v = pack["vocab"]
    native = pack["native_name"]

    # Extract Home, Top, Bottom, Shift, and Digit characters from keymap
    hr_left = [km["KeyA"]["main"], km["KeyS"]["main"], km["KeyD"]["main"], km["KeyF"]["main"], km["KeyG"]["main"]]
    hr_right = [km["KeyH"]["main"], km["KeyJ"]["main"], km["KeyK"]["main"], km["KeyL"]["main"], km["Semicolon"]["main"], km["Quote"]["main"]]
    tr_left = [km["KeyQ"]["main"], km["KeyW"]["main"], km["KeyE"]["main"], km["KeyR"]["main"], km["KeyT"]["main"]]
    tr_right = [km["KeyY"]["main"], km["KeyU"]["main"], km["KeyI"]["main"], km["KeyO"]["main"], km["KeyP"]["main"]]
    br_keys = [km["KeyX"]["main"], km["KeyC"]["main"], km["KeyV"]["main"], km["KeyB"]["main"], km["KeyN"]["main"], km["KeyM"]["main"]]
    sh_vowels = [km["KeyD"]["shift"], km["KeyE"]["shift"], km["KeyF"]["shift"], km["KeyR"]["shift"], km["KeyG"]["shift"], km["KeyT"]["shift"], km["KeyS"]["shift"], km["KeyA"]["shift"]]
    sh_cons = [km["KeyK"]["shift"], km["KeyI"]["shift"], km["Semicolon"]["shift"], km["KeyL"]["shift"], km["KeyO"]["shift"], km["KeyH"]["shift"], km["KeyY"]["shift"], km["KeyM"]["shift"]]
    digits = [km[f"Digit{i}"]["main"] for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]]

    hw = v["home_words"]
    tw = v["top_words"]
    bw = v["bottom_words"]
    sw = v["shift_words"]
    cw = v["conjunct_words"]
    paras = v["paragraphs"]

    units = [
        {
            "unit_id": f"{lang_code}_u1",
            "unit_number": 1,
            "title": f"Unit 1: {native} Home Row — Matras & Core Consonants",
            "subtitle": f"Master the InScript Home Row: Left hand types Matras ({' '.join(hr_left[:4])}) and Right hand types Consonants ({' '.join(hr_right[:5])}).",
            "focus_keys": hr_left + hr_right,
            "lessons": [
                {
                    "id": f"{lang_code}_u1_l1",
                    "title": f"1.1 Right-Hand Home Consonants ({' '.join(hr_right[:4])})",
                    "type": "key_drill",
                    "new_keys": hr_right[:4],
                    "target_wpm": 14,
                    "min_accuracy": 88,
                    "tip": f"Anchor your Right Hand on J ({hr_right[1]}), K ({hr_right[2]}), L ({hr_right[3]}), and ; ({hr_right[4]}).",
                    "text": " ".join([
                        f"{hr_right[1]}{hr_right[2]}", f"{hr_right[2]}{hr_right[1]}",
                        f"{hr_right[3]}{hr_right[4]}", f"{hr_right[0]}{hr_right[1]}",
                        f"{hr_right[2]}{hr_right[1]}", f"{hr_right[3]}{hr_right[0]}",
                        hw[0], hw[1], hw[2], hw[0], hw[1], hw[2], hw[0], hw[1]
                    ])
                },
                {
                    "id": f"{lang_code}_u1_l2",
                    "title": f"1.2 Left-Hand Home Matras ({' '.join(hr_left)})",
                    "type": "key_drill",
                    "new_keys": hr_left,
                    "target_wpm": 15,
                    "min_accuracy": 88,
                    "tip": f"In InScript, always type the Consonant first (Right Hand) followed by the Matra (Left Hand: {' '.join(hr_left)})!",
                    "text": " ".join(hw + hw[:6])
                },
                {
                    "id": f"{lang_code}_u1_l3",
                    "title": f"1.3 {native} Home Row Words & Rhythm",
                    "type": "word_drill",
                    "new_keys": hr_right[4:],
                    "target_wpm": 16,
                    "min_accuracy": 90,
                    "tip": "Keep a smooth alternating rhythm between your Right Hand (consonant) and Left Hand (matra).",
                    "text": " ".join(hw + list(reversed(hw)))
                },
                {
                    "id": f"{lang_code}_u1_l4",
                    "title": f"1.4 Right-Left Hand Alternation (Consonant + Home Matra)",
                    "type": "key_drill",
                    "new_keys": hr_left[:4],
                    "target_wpm": 16,
                    "min_accuracy": 90,
                    "tip": "Build instant Right-Hand Consonant -> Left-Hand Matra alternation speed without pausing!",
                    "text": " ".join([
                        f"{c}{m}"
                        for c in hr_right[:5]
                        for m in [hr_left[3], hr_left[4], hr_left[1], hr_left[0]]
                    ])
                },
                {
                    "id": f"{lang_code}_u1_l5",
                    "title": f"1.5 Home Row Full Phrases & Flow",
                    "type": "sentence_drill",
                    "new_keys": [],
                    "target_wpm": 18,
                    "min_accuracy": 91,
                    "tip": "Type complete Home Row word groups smoothly with crisp spacebar taps.",
                    "text": f"{hw[0]} {hw[1]} {hw[2]} {hw[3]}. {hw[4]} {hw[5]} {hw[6]} {hw[7]}. {hw[8]} {hw[9]} {hw[0]} {hw[4]}."
                }
            ]
        },
        {
            "unit_id": f"{lang_code}_u2",
            "unit_number": 2,
            "title": f"Unit 2: {native} Top Row — Long Matras & Consonants",
            "subtitle": f"Reach upward for long vowel matras ({' '.join(tr_left)}) and top-row consonants ({' '.join(tr_right)}).",
            "focus_keys": tr_left + tr_right,
            "lessons": [
                {
                    "id": f"{lang_code}_u2_l1",
                    "title": f"2.1 Top Row Consonants ({' '.join(tr_right)})",
                    "type": "key_drill",
                    "new_keys": tr_right,
                    "target_wpm": 15,
                    "min_accuracy": 88,
                    "tip": f"Reach up with your Right Hand fingers for {' '.join(tr_right)}, then return to the Home Row.",
                    "text": " ".join(tw[:6] + tw[:6])
                },
                {
                    "id": f"{lang_code}_u2_l2",
                    "title": f"2.2 Top Row Vowel Signs ({' '.join(tr_left)})",
                    "type": "word_drill",
                    "new_keys": tr_left,
                    "target_wpm": 16,
                    "min_accuracy": 90,
                    "tip": f"Left Middle ('E' key) types '{tr_left[2]}' — the most frequent vowel sign in {native}!",
                    "text": " ".join(tw + hw[:4])
                },
                {
                    "id": f"{lang_code}_u2_l3",
                    "title": f"2.3 Short vs. Long Vowel Matras Contrast",
                    "type": "key_drill",
                    "new_keys": [hr_left[3], tr_left[3], hr_left[4], tr_left[4]],
                    "target_wpm": 17,
                    "min_accuracy": 90,
                    "tip": "Notice how every Long Matra sits directly ABOVE its Short Matra on the Left Hand (F->R, G->T, S->W, A->Q)!",
                    "text": " ".join([
                        f"{c}{hr_left[3]} {c}{tr_left[3]} {c}{hr_left[4]} {c}{tr_left[4]} {c}{hr_left[1]} {c}{tr_left[1]} {c}{hr_left[0]} {c}{tr_left[0]}"
                        for c in [hr_right[2], hr_right[3], hr_right[0], tr_right[0]]
                    ])
                },
                {
                    "id": f"{lang_code}_u2_l4",
                    "title": f"2.4 Combined Top & Home Row Fluency",
                    "type": "sentence_drill",
                    "new_keys": [],
                    "target_wpm": 18,
                    "min_accuracy": 90,
                    "tip": "Combine Home and Top row characters into natural native words.",
                    "text": " ".join(tw + hw[:5] + tw[:5])
                }
            ]
        },
        {
            "unit_id": f"{lang_code}_u3",
            "unit_number": 3,
            "title": f"Unit 3: {native} Bottom Row & Basic Punctuation",
            "subtitle": f"Master nasal/liquid consonants ({' '.join(br_keys)}) plus commas, semicolons, and full stops.",
            "focus_keys": br_keys + [",", "."],
            "lessons": [
                {
                    "id": f"{lang_code}_u3_l1",
                    "title": f"3.1 Bottom Row Consonants ({' '.join(br_keys)})",
                    "type": "key_drill",
                    "new_keys": br_keys,
                    "target_wpm": 16,
                    "min_accuracy": 88,
                    "tip": f"Practice curling your fingers down for {' '.join(br_keys)} and snapping back to home.",
                    "text": " ".join(bw[:6] + bw[:6])
                },
                {
                    "id": f"{lang_code}_u3_l2",
                    "title": f"3.2 {native} Anusvara & Liquid Consonants Drill",
                    "type": "word_drill",
                    "new_keys": [br_keys[0], br_keys[1], br_keys[2], br_keys[4]],
                    "target_wpm": 17,
                    "min_accuracy": 90,
                    "tip": f"Left Ring curls down to 'X' for Anusvara ({br_keys[0]}). Practice smooth nasal endings!",
                    "text": " ".join([f"{c}{br_keys[0]}" for c in [hr_right[2], hr_right[0], br_keys[1], br_keys[2], br_keys[4], br_keys[5]]] + bw[:8])
                },
                {
                    "id": f"{lang_code}_u3_l3",
                    "title": f"3.3 {native} Everyday Words with Commas, Question Marks & Stops",
                    "type": "sentence_drill",
                    "new_keys": [",", ".", "?"],
                    "target_wpm": 18,
                    "min_accuracy": 90,
                    "tip": "Practice clean spacing, commas (,), question marks (?), and stops (.) between words.",
                    "text": f"{bw[0]}, {bw[1]}, {bw[2]}. {bw[3]}, {bw[4]}? {bw[5]}, {bw[6]}! {bw[7]} {bw[8]} {bw[9]}."
                }
            ]
        },
        {
            "unit_id": f"{lang_code}_u4",
            "unit_number": 4,
            "title": f"Unit 4: Shift Layer — Full Vowels & Aspirated Consonants",
            "subtitle": f"Use Shift + Left Hand for full independent vowels ({' '.join(sh_vowels[:5])}) and Shift + Right Hand for aspirated consonants ({' '.join(sh_cons[:5])}).",
            "focus_keys": sh_vowels[:5] + sh_cons[:5],
            "lessons": [
                {
                    "id": f"{lang_code}_u4_l1",
                    "title": f"4.1 Complete Independent Vowels ({' '.join(sh_vowels)})",
                    "type": "key_drill",
                    "new_keys": sh_vowels[:6],
                    "target_wpm": 16,
                    "min_accuracy": 88,
                    "tip": "In InScript, every Left-Hand Matra key produces its full Independent Vowel when you hold Right Shift!",
                    "text": " ".join(sh_vowels + sh_vowels + sw[:6])
                },
                {
                    "id": f"{lang_code}_u4_l2",
                    "title": f"4.2 Unaspirated vs. Aspirated Contrast (Normal vs. Shift Key)",
                    "type": "key_drill",
                    "new_keys": sh_cons[:6],
                    "target_wpm": 16,
                    "min_accuracy": 89,
                    "tip": "In InScript, holding Left Shift on a consonant key types its Aspirated partner (e.g., क->ख, ग->घ, च->छ, त->थ, द->ध, प->फ, ब->भ)!",
                    "text": " ".join([
                        f"{km['KeyK']['main']} {km['KeyK']['shift']}",
                        f"{km['KeyI']['main']} {km['KeyI']['shift']}",
                        f"{km['Semicolon']['main']} {km['Semicolon']['shift']}",
                        f"{km['KeyP']['main']} {km['KeyP']['shift']}",
                        f"{km['Quote']['main']} {km['Quote']['shift']}",
                        f"{km['BracketLeft']['main']} {km['BracketLeft']['shift']}",
                        f"{km['KeyL']['main']} {km['KeyL']['shift']}",
                        f"{km['KeyO']['main']} {km['KeyO']['shift']}",
                        f"{km['KeyH']['main']} {km['KeyH']['shift']}",
                        f"{km['KeyY']['main']} {km['KeyY']['shift']}",
                    ] * 2)
                },
                {
                    "id": f"{lang_code}_u4_l3",
                    "title": f"4.3 Shift-Layer {native} Words & Fluency",
                    "type": "word_drill",
                    "new_keys": sh_cons[:6],
                    "target_wpm": 18,
                    "min_accuracy": 90,
                    "tip": "Combine independent vowels and aspirated consonants in real native words.",
                    "text": " ".join(sw + list(reversed(sw[:6])) + bw[:4])
                }
            ]
        },
        {
            "unit_id": f"{lang_code}_u5",
            "unit_number": 5,
            "title": f"Unit 5: Halant / Conjunct Letters (संयुक्त अक्षर)",
            "subtitle": f"Join consonants smoothly using the Left Middle finger ('D' key = '{km['KeyD']['main']}').",
            "focus_keys": [km["KeyD"]["main"]],
            "lessons": [
                {
                    "id": f"{lang_code}_u5_l1",
                    "title": f"5.1 Geminate / Double Consonants (Consonant + d + Consonant)",
                    "type": "key_drill",
                    "new_keys": [km["KeyD"]["main"]],
                    "target_wpm": 17,
                    "min_accuracy": 90,
                    "tip": f"Type Consonant + '{km['KeyD']['main']}' (D key) + Same Consonant to build crisp double-letter ottulu/conjuncts!",
                    "text": " ".join([
                        f"{c}{km['KeyD']['main']}{c} {c}{km['KeyD']['main']}{c}{tr_left[2]}"
                        for c in [hr_right[2], hr_right[3], hr_right[4], hr_right[0], br_keys[1], br_keys[2], br_keys[4]]
                    ])
                },
                {
                    "id": f"{lang_code}_u5_l2",
                    "title": f"5.2 Conjunct Consonants & Real-World Clusters",
                    "type": "word_drill",
                    "new_keys": [km["KeyD"]["main"]],
                    "target_wpm": 18,
                    "min_accuracy": 90,
                    "tip": f"To form any conjunct, type Consonant 1 + '{km['KeyD']['main']}' (D key) + Consonant 2!",
                    "text": " ".join(cw + cw[:5])
                },
                {
                    "id": f"{lang_code}_u5_l3",
                    "title": f"5.3 Advanced {native} Vocabulary Drill",
                    "type": "sentence_drill",
                    "new_keys": [],
                    "target_wpm": 20,
                    "min_accuracy": 91,
                    "tip": "Maintain a relaxed rhythm on words with conjuncts and vowel signs.",
                    "text": " ".join(cw + sw[:5] + tw[:4])
                },
                {
                    "id": f"{lang_code}_u5_l4",
                    "title": f"5.4 English Loanwords & Explicit Halant Break (d + d = ZWNJ)",
                    "type": "word_drill",
                    "new_keys": [km["KeyD"]["main"]],
                    "target_wpm": 18,
                    "min_accuracy": 90,
                    "tip": "Pro Translator Trick: On Windows InScript, double-tap 'D' (d + d) after a consonant to insert Halant + ZWNJ so the next consonant won't merge into an awkward conjunct!",
                    "text": {
                        "te": "ఇన్\u200cస్టిట్యూషన్ ఆన్\u200cలైన్ ఇన్\u200cపుట్ మెయిన్\u200cరోడ్ ఫోన్\u200cపే కంప్యూటర్ ఇంటర్నెట్ యూనివర్సిటీ ఇన్\u200cస్టిట్యూషన్ ఆన్\u200cలైన్ ఇన్\u200cపుట్",
                        "kn": "ಇನ್\u200cಸ್ಟಿಟ್ಯೂಷನ್ ಆನ್\u200cಲೈನ್ ಇನ್\u200cಪುಟ್ ಮೇನ್\u200cರೋಡ್ ಕಂಪ್ಯೂಟರ್ ಇಂಟರ್ನೆಟ್ ಯೂನಿವರ್ಸಿಟಿ ಇನ್\u200cಸ್ಟಿಟ್ಯೂಷನ್ ಆನ್\u200cಲೈನ್",
                        "ml": "ഇൻ\u200cസ്റ്റിറ്റ്യൂഷൻ ഓൺ\u200cലൈൻ ഇൻ\u200cപുട്ട് കമ്പ്യൂട്ടർ ഇന്റർനെറ്റ് യൂണിവേഴ്സിറ്റി ഇൻ\u200cസ്റ്റിറ്റ്യൂഷൻ ഓൺ\u200cലൈൻ",
                        "hi": "इन\u200cस्टीट्यूशन ऑन\u200cलाइन इन\u200cपुट कंप्यूटर इंटरनेट यूनिवर्सिटी डॉक्टर प्रोजेक्ट इन\u200cस्टीट्यूशन ऑन\u200cलाइन",
                        "mr": "इन\u200cस्टिट्यूशन ऑन\u200cलाईन इन\u200cपुट संगणक इंटरनेट युनिव्हर्सिटी डॉक्टर प्रोजेक्ट इन\u200cस्टिट्यूशन ऑन\u200cलाईन",
                        "sa": "विद्\u200cया सद्\u200cभावः उत्\u200cसवः सत्\u200cकर्म वाक्\u200cशक्तिः तत्\u200cत्वम् जगत्\u200cगुरुः सद्\u200cभावः उत्\u200cसवः",
                        "bn": "ইন\u200cস্টিটিউশন অন\u200cলাইন ইন\u200cপুট কম্পিউটার ইন্টারনেট ইউনিভার্সিটি ইন\u200cস্টিটিউশন অন\u200cলাইন",
                        "as": "ইন\u200cষ্টিটিউচন অন\u200cলাইন ইন\u200cপুট কম্পিউটাৰ ইন্টাৰনেট বিশ্ববিদ্যালয় ইন\u200cষ্টিটিউচন অন\u200cলাইন",
                        "gu": "ઇન\u200cસ્ટિટ્યૂશન ઓન\u200cલાઇન ઇન\u200cપુટ કમ્પ્યુટર ઇન્ટરનેટ યુનિવર્સિટી ઇન\u200cસ્ટિટ્યૂશન ઓન\u200cલાઇન",
                        "pa": "ਇਨ\u200cਸਟੀਚਿਊਸ਼ਨ ਆਨ\u200cਲਾਈਨ ਇਨ\u200cਪੁੱਟ ਕੰਪਿਊਟਰ ਇੰਟਰਨੈੱਟ ਯੂਨੀਵਰਸਿਟੀ ਇਨ\u200cਸਟੀਚਿਊਸ਼ਨ ਆਨ\u200cਲਾਈਨ",
                        "or": "ଇନ୍\u200cଷ୍ଟିଚ୍ୟୁସନ୍ ଅନ୍\u200cଲାଇନ୍ ଇନ୍\u200cପୁଟ୍ କମ୍ପ୍ୟୁଟର ଇଣ୍ଟରନେଟ୍ ବିଶ୍ୱବିଦ୍ୟାଳୟ ଇନ୍\u200cଷ୍ଟିଚ୍ୟୁସନ୍ ଅନ୍\u200cଲାଇନ୍",
                        "ta": "இன்ஸ்டிடியூஷன் ஆன்லைன் இன்புட் கம்ப்யூட்டர் இன்டர்நெட் யூனிவர்சிட்டி இன்ஸ்டிடியூஷன் ஆன்லைன்",
                    }.get(lang_code, " ".join(cw[:8]))
                }
            ]
        },
        {
            "unit_id": f"{lang_code}_u6",
            "unit_number": 6,
            "title": f"Unit 6: {native} Numbers, Dates & Measurements",
            "subtitle": f"Practice the number row ({' '.join(digits[:5])} {' '.join(digits[5:])}) mixed with dates, percentages, and native words.",
            "focus_keys": digits,
            "lessons": [
                {
                    "id": f"{lang_code}_u6_l1",
                    "title": f"6.1 Native Number Row ({' '.join(digits)})",
                    "type": "key_drill",
                    "new_keys": digits,
                    "target_wpm": 18,
                    "min_accuracy": 90,
                    "tip": "Reach up from the Home Row to strike native digits cleanly without looking down.",
                    "text": f"{digits[0]}{digits[1]} {digits[2]}{digits[3]} {digits[4]}{digits[5]} {digits[6]}{digits[7]} {digits[8]}{digits[9]} {digits[1]}{digits[0]}{digits[0]} {digits[2]}{digits[0]}{digits[2]}{digits[6]} {bw[0]} {tw[0]}"
                },
                {
                    "id": f"{lang_code}_u6_l2",
                    "title": f"6.2 Real-World Dates, Times & Statistics",
                    "type": "sentence_drill",
                    "new_keys": [],
                    "target_wpm": 20,
                    "min_accuracy": 91,
                    "tip": "Combine standard figures, colons, percentages, and native vocabulary.",
                    "text": f"2026: {bw[0]} 100%, {tw[0]} 450, {sw[0]} 12:30, {cw[0]} 98.5, {hw[0]} 15-08-1947, {bw[2]} 24/7."
                }
            ]
        },
        {
            "unit_id": f"{lang_code}_u7",
            "unit_number": 7,
            "title": f"Unit 7: {native} Speed Building & Exam Fluency",
            "subtitle": "Build effortless WPM across high-frequency native words, phrases, and exam vocabulary.",
            "focus_keys": [],
            "lessons": [
                {
                    "id": f"{lang_code}_u7_l1",
                    "title": f"7.1 High-Frequency {native} Word Sprint",
                    "type": "word_drill",
                    "new_keys": [],
                    "target_wpm": 22,
                    "min_accuracy": 92,
                    "tip": "Read one word ahead while your fingers complete the current word.",
                    "text": " ".join(hw[:4] + tw[:4] + bw[:4] + sw[:4] + cw[:4])
                },
                {
                    "id": f"{lang_code}_u7_l2",
                    "title": f"7.2 {native} Office, News & Academic Fluency",
                    "type": "sentence_drill",
                    "new_keys": [],
                    "target_wpm": 24,
                    "min_accuracy": 92,
                    "tip": "Maintain steady breathing and consistent keystroke intervals across longer words.",
                    "text": " ".join(cw + sw + tw[:6] + bw[:6])
                }
            ]
        },
        {
            "unit_id": f"{lang_code}_u8",
            "unit_number": 8,
            "title": f"Unit 8: {native} Full Paragraphs & Mastery Exam",
            "subtitle": "Complete native literary and modern passages with full punctuation (; , . । !).",
            "focus_keys": [],
            "lessons": [
                {
                    "id": f"{lang_code}_u8_l1",
                    "title": f"8.1 {native} Literature & Wisdom Paragraph",
                    "type": "paragraph_drill",
                    "new_keys": [],
                    "target_wpm": 24,
                    "min_accuracy": 92,
                    "tip": "Focus on smooth breathing and steady accuracy across full sentences.",
                    "text": paras[0]
                },
                {
                    "id": f"{lang_code}_u8_l2",
                    "title": f"8.2 {native} Modern Digital Era Paragraph",
                    "type": "paragraph_drill",
                    "new_keys": [],
                    "target_wpm": 25,
                    "min_accuracy": 93,
                    "tip": "Type modern sentences smoothly with punctuation marks and exclamation points.",
                    "text": paras[1]
                },
                {
                    "id": f"{lang_code}_u8_l3",
                    "title": f"8.3 {native} Grand Mastery Certification Passage",
                    "type": "paragraph_drill",
                    "new_keys": [],
                    "target_wpm": 26,
                    "min_accuracy": 93,
                    "tip": f"Final {native} Mastery Exam! Aim for 93%+ accuracy.",
                    "text": f"{paras[0]} {paras[1]}"
                }
            ]
        }
    ]
    gunintalu_unit = _build_gunintalu_unit(lang_code, native, km)
    if gunintalu_unit:
        units.insert(3, gunintalu_unit)
        # Renumber units cleanly from 1..9
        for idx, u in enumerate(units, start=1):
            u["unit_number"] = idx
            if u["title"].startswith("Unit "):
                colon_pos = u["title"].find(":")
                if colon_pos != -1:
                    u["title"] = f"Unit {idx}{u['title'][colon_pos:]}"
    return units


def get_speed_passages_for_indian_language(lang_code: str):
    pack = INDIAN_LANGUAGE_PACKS.get(lang_code)
    if not pack:
        return []
    paras = pack["vocab"]["paragraphs"]
    native = pack["native_name"]
    return [
        {
            "id": f"st_{lang_code}_1",
            "title": f"{native} — Practice & Focus Passage",
            "difficulty": "Standard",
            "text": f"{paras[0]} {paras[1]}"
        },
        {
            "id": f"st_{lang_code}_2",
            "title": f"{native} — Extended Mastery Passage",
            "difficulty": "Advanced",
            "text": f"{paras[1]} {paras[0]}"
        }
    ]
