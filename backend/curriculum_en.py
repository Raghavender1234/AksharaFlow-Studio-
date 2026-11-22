# -*- coding: utf-8 -*-
"""
Comprehensive English Touch-Typing Curriculum & Multi-Script Dispatcher
"""

from curriculum_inscript import (
    INDIAN_LANGUAGE_PACKS,
    CODE_TO_FINGER,
    build_reverse_char_to_finger_map,
    generate_units_for_indian_language,
    get_speed_passages_for_indian_language,
)

FINGER_MAP_EN = {
    "`": "L_PINKY", "~": "L_PINKY",
    "1": "L_PINKY", "!": "L_PINKY",
    "2": "L_RING", "@": "L_RING",
    "3": "L_MIDDLE", "#": "L_MIDDLE",
    "4": "L_INDEX", "$": "L_INDEX",
    "5": "L_INDEX", "%": "L_INDEX",
    "6": "R_INDEX", "^": "R_INDEX",
    "7": "R_INDEX", "&": "R_INDEX",
    "8": "R_MIDDLE", "*": "R_MIDDLE",
    "9": "R_RING", "(": "R_RING",
    "0": "R_PINKY", ")": "R_PINKY",
    "-": "R_PINKY", "_": "R_PINKY",
    "=": "R_PINKY", "+": "R_PINKY",

    "q": "L_PINKY", "Q": "L_PINKY",
    "w": "L_RING", "W": "L_RING",
    "e": "L_MIDDLE", "E": "L_MIDDLE",
    "r": "L_INDEX", "R": "L_INDEX",
    "t": "L_INDEX", "T": "L_INDEX",
    "y": "R_INDEX", "Y": "R_INDEX",
    "u": "R_INDEX", "U": "R_INDEX",
    "i": "R_MIDDLE", "I": "R_MIDDLE",
    "o": "R_RING", "O": "R_RING",
    "p": "R_PINKY", "P": "R_PINKY",
    "[": "R_PINKY", "{": "R_PINKY",
    "]": "R_PINKY", "}": "R_PINKY",
    "\\": "R_PINKY", "|": "R_PINKY",

    "a": "L_PINKY", "A": "L_PINKY",
    "s": "L_RING", "S": "L_RING",
    "d": "L_MIDDLE", "D": "L_MIDDLE",
    "f": "L_INDEX", "F": "L_INDEX",
    "g": "L_INDEX", "G": "L_INDEX",
    "h": "R_INDEX", "H": "R_INDEX",
    "j": "R_INDEX", "J": "R_INDEX",
    "k": "R_MIDDLE", "K": "R_MIDDLE",
    "l": "R_RING", "L": "R_RING",
    ";": "R_PINKY", ":": "R_PINKY",
    "'": "R_PINKY", "\"": "R_PINKY",

    "z": "L_PINKY", "Z": "L_PINKY",
    "x": "L_RING", "X": "L_RING",
    "c": "L_MIDDLE", "C": "L_MIDDLE",
    "v": "L_INDEX", "V": "L_INDEX",
    "b": "L_INDEX", "B": "L_INDEX",
    "n": "R_INDEX", "N": "R_INDEX",
    "m": "R_INDEX", "M": "R_INDEX",
    ",": "R_MIDDLE", "<": "R_MIDDLE",
    ".": "R_RING", ">": "R_RING",
    "/": "R_PINKY", "?": "R_PINKY",

    " ": "THUMB"
}

FINGER_LABELS = {
    "L_PINKY": "Left Pinky Finger",
    "L_RING": "Left Ring Finger",
    "L_MIDDLE": "Left Middle Finger",
    "L_INDEX": "Left Index Finger",
    "THUMB": "Thumbs (Spacebar)",
    "R_INDEX": "Right Index Finger",
    "R_MIDDLE": "Right Middle Finger",
    "R_RING": "Right Ring Finger",
    "R_PINKY": "Right Pinky Finger"
}


ENGLISH_UNITS = [
    {
        "unit_id": "en_u1",
        "unit_number": 1,
        "title": "Unit 1: The Home Row Foundation",
        "subtitle": "Master the anchor keys (A S D F G H J K L ;) without looking at the keyboard.",
        "focus_keys": ["a", "s", "d", "f", "g", "h", "j", "k", "l", ";"],
        "lessons": [
            {
                "id": "en_u1_l1",
                "title": "1.1 Index & Middle Anchor Keys (F J D K)",
                "type": "key_drill",
                "new_keys": ["f", "j", "d", "k"],
                "target_wpm": 15,
                "min_accuracy": 90,
                "tip": "Place your Left Index on F and Right Index on J (feel the tactile bumps). Use your Middle fingers for D and K.",
                "text": (
                    "ff jj ff jj fj jf fj jf dd kk dd kk dk kd dk kd "
                    "fd jk df kj fd jk df kj fjd jkf dfk kjd fjdk jfkd "
                    "ff dd jj kk fdjk kjdf fjdk dkfj jfkd dfkj fjdk"
                )
            },
            {
                "id": "en_u1_l2",
                "title": "1.2 Ring & Pinky Home Keys (S L A ;)",
                "type": "key_drill",
                "new_keys": ["s", "l", "a", ";"],
                "target_wpm": 16,
                "min_accuracy": 90,
                "tip": "Use your Ring fingers for S and L, and your Pinky fingers for A and Semicolon (;). Keep wrists floating.",
                "text": (
                    "ss ll ss ll sl ls aa ;; aa ;; a; ;a sla ;la asdf jkl; "
                    "fdsa ;lkj asdf jkl; fdsa ;lkj as;l dfjk sad; lad; "
                    "ask; fall; lass; dad; fad; salad; flask; falls; asks;"
                )
            },
            {
                "id": "en_u1_l3",
                "title": "1.3 Center Reach Keys (G & H)",
                "type": "key_drill",
                "new_keys": ["g", "h"],
                "target_wpm": 18,
                "min_accuracy": 90,
                "tip": "Stretch your Left Index sideways from F to G, and Right Index from J to H, then immediately return to F and J.",
                "text": (
                    "fg gf jh hj fg jh gf hj fgh jhg ghf hgj "
                    "gag hah gal hal had hag jag lag shag glad half "
                    "hall hash sash gash flash glass flags halls"
                )
            },
            {
                "id": "en_u1_l4",
                "title": "1.4 Home Row Word Building",
                "type": "word_drill",
                "new_keys": [],
                "target_wpm": 20,
                "min_accuracy": 92,
                "tip": "Type smooth, rhythmic words using only the Home Row. Do not pause between letters inside short words.",
                "text": (
                    "sad lad dad fad had glad half hall fall gall shall "
                    "ash dash lash gash flash slash sash hash flask glass "
                    "jag lag sag flag shag salad; a glad lad had a flask"
                )
            },
            {
                "id": "en_u1_l5",
                "title": "1.5 Home Row Clauses with Semicolons",
                "type": "sentence_drill",
                "new_keys": [";"],
                "target_wpm": 22,
                "min_accuracy": 92,
                "tip": "Practice hitting the semicolon (;) cleanly with your Right Pinky at the end of clauses.",
                "text": (
                    "all lads fall; dad has a glass; ask a glad lass; "
                    "a sad lad had half a salad; a flash falls; "
                    "shall a lass ask dad; add a dash; half a glass falls; "
                    "a glad dad has a small flask; all flags shall fall;"
                )
            }
        ]
    },
    {
        "unit_id": "en_u2",
        "unit_number": 2,
        "title": "Unit 2: The Top Row (Q W E R T Y U I O P)",
        "subtitle": "Extend upward from the Home Row to master all vowels and top-row consonants.",
        "focus_keys": ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"],
        "lessons": [
            {
                "id": "en_u2_l1",
                "title": "2.1 Index Upward Reach (R U T Y)",
                "type": "key_drill",
                "new_keys": ["r", "u", "t", "y"],
                "target_wpm": 20,
                "min_accuracy": 90,
                "tip": "Reach up with Left Index for R and T; reach up with Right Index for U and Y. Always snap back to F and J.",
                "text": (
                    "frf juj ftf jyj frft jujy rtfg yuhj furufuty "
                    "rug turf jury fury hurt truth duty study "
                    "truly fruit rusty; try a furry rug; trust a jury;"
                )
            },
            {
                "id": "en_u2_l2",
                "title": "2.2 Middle & Ring Vowels (E I W O)",
                "type": "key_drill",
                "new_keys": ["e", "i", "w", "o"],
                "target_wpm": 22,
                "min_accuracy": 91,
                "tip": "E and I use your Middle fingers; W and O use your Ring fingers. These 4 keys unlock thousands of English words!",
                "text": (
                    "ded kik sws lol deki swlo weio oiew fire wire "
                    "tire site write white polite word work world "
                    "flower power tower lower slower follow hollow; "
                    "write a good word; follow the wide road; feel the fire;"
                )
            },
            {
                "id": "en_u2_l3",
                "title": "2.3 Pinky Top Reach (Q & P)",
                "type": "key_drill",
                "new_keys": ["q", "p"],
                "target_wpm": 22,
                "min_accuracy": 91,
                "tip": "Reach up with your Left Pinky from A to Q, and Right Pinky from ; to P.",
                "text": (
                    "aqa ;p; aqa ;p; qp pq quip quit quite quiet quote "
                    "equal squad square opaque; pop top drop stop "
                    "shop paper pepper proper people; keep quiet please; "
                    "quote a proper paper; quite a proud people;"
                )
            },
            {
                "id": "en_u2_l4",
                "title": "2.4 Top & Home Row Fluency Drill",
                "type": "word_drill",
                "new_keys": [],
                "target_wpm": 25,
                "min_accuracy": 92,
                "tip": "Combine Home and Top rows into fluid phrases and semicolon-separated clauses.",
                "text": (
                    "the quick polite writer spoke quietly; our group will prepare "
                    "the report today; water powers the tall turbine; require equal "
                    "support for all people; history shows how thought shapes power; "
                    "keep your posture upright while typing every word;"
                )
            }
        ]
    },
    {
        "unit_id": "en_u3",
        "unit_number": 3,
        "title": "Unit 3: The Bottom Row & Basic Punctuation",
        "subtitle": "Complete the alphabet (Z X C V B N M) plus Commas (,), Full Stops (.), and Slashes (/).",
        "focus_keys": ["z", "x", "c", "v", "b", "n", "m", ",", ".", "/"],
        "lessons": [
            {
                "id": "en_u3_l1",
                "title": "3.1 Index Downward Reach (V M B N)",
                "type": "key_drill",
                "new_keys": ["v", "m", "b", "n"],
                "target_wpm": 22,
                "min_accuracy": 90,
                "tip": "Curl your Left Index down for V and B; curl your Right Index down for M and N.",
                "text": (
                    "fvf jmj fbf jnj fvfb jmjn verb move brave never "
                    "number member november seven eleven river silver "
                    "combine amber banner manner summer; never blame a brave man; "
                    "seven members move near the river;"
                )
            },
            {
                "id": "en_u3_l2",
                "title": "3.2 Middle & Ring Reach + Comma & Full Stop (C , X .)",
                "type": "key_drill",
                "new_keys": ["c", ",", "x", "."],
                "target_wpm": 24,
                "min_accuracy": 92,
                "tip": "Left Middle hits C, Right Middle hits Comma (,). Left Ring hits X, Right Ring hits Full Stop (.).",
                "text": (
                    "dcd k,k sxs l.l c, x. dc, sx. clear, exact, next, "
                    "voice, choice, space, place. fix the box, check the text, "
                    "expect success. practice makes perfect, so focus on accuracy first. "
                    "each small step builds confidence, speed, and control."
                )
            },
            {
                "id": "en_u3_l3",
                "title": "3.3 Pinky Downward Reach (Z & /)",
                "type": "key_drill",
                "new_keys": ["z", "/"],
                "target_wpm": 24,
                "min_accuracy": 92,
                "tip": "Left Pinky curls down to Z; Right Pinky curls down to Forward Slash (/). You now know all 26 letters!",
                "text": (
                    "aza ;/; aza ;/; zero zone zoom prize size freeze "
                    "breeze puzzle dazzle organize realize. yes/no, true/false, "
                    "input/output, either/or, speed/accuracy. realize your full "
                    "potential; organize the puzzle pieces, and zoom toward the prize."
                )
            },
            {
                "id": "en_u3_l4",
                "title": "3.4 Full Alphabet Pangrams & Punctuated Sentences",
                "type": "sentence_drill",
                "new_keys": [],
                "target_wpm": 26,
                "min_accuracy": 93,
                "tip": "Type famous pangrams that exercise every single letter of the English alphabet alongside commas, full stops, and semicolons.",
                "text": (
                    "the quick brown fox jumps over the lazy dog. "
                    "pack my box with five dozen liquor jugs; "
                    "how vexingly quick daft zebras jump. "
                    "sphinx of black quartz, judge my vow; "
                    "the five boxing wizards jump quickly, poised and exact."
                )
            }
        ]
    },
    {
        "unit_id": "en_u4",
        "unit_number": 4,
        "title": "Unit 4: Shift Keys, Capitals & Full Punctuation",
        "subtitle": "Master opposite-hand Shift coordination, Capital letters, Colons, Quotes, Question & Exclamation marks.",
        "focus_keys": ["A", "S", "D", "F", "J", "K", "L", ":", "\"", "'", "?", "!", "-"],
        "lessons": [
            {
                "id": "en_u4_l1",
                "title": "4.1 Opposite-Hand Shift & Capital Letters",
                "type": "key_drill",
                "new_keys": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"],
                "target_wpm": 25,
                "min_accuracy": 92,
                "tip": "Hold Right Shift with your Right Pinky when typing Left-Hand capitals, and Left Shift with your Left Pinky for Right-Hand capitals.",
                "text": (
                    "Alice Bob Clara David Elena Frank Grace Henry "
                    "India Japan Kenya London Madrid Norway Osaka Paris "
                    "Queen Robert Sophia Thomas Uma Victor William Xenia Yasmine Zachary. "
                    "Every great journey begins with a single disciplined step."
                )
            },
            {
                "id": "en_u4_l2",
                "title": "4.2 Colons, Semicolons, Apostrophes & Quotation Marks",
                "type": "sentence_drill",
                "new_keys": [":", "'", "\""],
                "target_wpm": 25,
                "min_accuracy": 92,
                "tip": "Your Right Pinky controls ; : ' and \". Use Left Shift + ; for Colon (:), and Left Shift + ' for Double Quotes (\").",
                "text": (
                    "Note the rule: don't rush; accuracy comes first. "
                    "She said, \"Consistent practice transforms hesitation into instinct.\" "
                    "Here is the schedule: Monday, rhythm; Tuesday, speed; Wednesday, mastery. "
                    "It's clear that today's effort shapes tomorrow's skill."
                )
            },
            {
                "id": "en_u4_l3",
                "title": "4.3 Question Marks, Exclamations & Hyphens (? ! -)",
                "type": "sentence_drill",
                "new_keys": ["?", "!", "-"],
                "target_wpm": 26,
                "min_accuracy": 92,
                "tip": "Question mark (?) is Left Shift + /. Exclamation (!) is Right Shift + 1. Hyphen (-) is Right Pinky on the number row.",
                "text": (
                    "Are you ready to test your touch-typing reflexes? Yes, right now! "
                    "Why look down at the keys when your fingers know the way? "
                    "Stay calm, keep a steady beat, and watch your self-confidence soar! "
                    "What is the secret to error-free writing? Well-trained muscle memory!"
                )
            },
            {
                "id": "en_u4_l4",
                "title": "4.4 Complete Literary Dialogue & Complex Punctuation",
                "type": "paragraph_drill",
                "new_keys": [],
                "target_wpm": 28,
                "min_accuracy": 93,
                "tip": "Combine capitals, commas, full stops, semicolons, colons, hyphens, and quotation marks in a realistic passage.",
                "text": (
                    "\"How fast should I type?\" asked the student. The instructor smiled: "
                    "\"Never chase raw speed at the expense of precision; instead, let speed "
                    "emerge naturally from smooth, relaxed accuracy!\" When each finger returns "
                    "home automatically, your mind is free to focus on ideas - not on hunting for keys."
                )
            }
        ]
    },
    {
        "unit_id": "en_u5",
        "unit_number": 5,
        "title": "Unit 5: The Number Row (1 2 3 4 5 6 7 8 9 0)",
        "subtitle": "Touch-type numbers accurately without looking down by anchoring to the Home Row.",
        "focus_keys": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"],
        "lessons": [
            {
                "id": "en_u5_l1",
                "title": "5.1 Left-Hand Numbers (1 2 3 4 5)",
                "type": "key_drill",
                "new_keys": ["1", "2", "3", "4", "5"],
                "target_wpm": 20,
                "min_accuracy": 90,
                "tip": "Anchor on A S D F: Left Pinky reaches 1, Ring reaches 2, Middle reaches 3, Index reaches 4 and 5.",
                "text": (
                    "a1a s2s d3d f4f f5f a1 s2 d3 f4 f5 123 234 345 451 "
                    "11 22 33 44 55 15 24 35 41 52; Page 12, Chapter 3, "
                    "Section 45; 145 items in 23 boxes; Order 54,321 confirmed."
                )
            },
            {
                "id": "en_u5_l2",
                "title": "5.2 Right-Hand Numbers (6 7 8 9 0)",
                "type": "key_drill",
                "new_keys": ["6", "7", "8", "9", "0"],
                "target_wpm": 20,
                "min_accuracy": 90,
                "tip": "Anchor on J K L ;: Right Index reaches 6 and 7, Middle reaches 8, Ring reaches 9, Pinky reaches 0.",
                "text": (
                    "j6j j7j k8k l9l ;0; j6 j7 k8 l9 ;0 678 789 890 607 "
                    "66 77 88 99 00 60 78 89 90 76; Flight 789 departs at 06:00; "
                    "Score 98 out of 100; 670 kilometers in 8.9 hours."
                )
            },
            {
                "id": "en_u5_l3",
                "title": "5.3 Dates, Statistics & Alphanumeric Mastery",
                "type": "sentence_drill",
                "new_keys": [],
                "target_wpm": 24,
                "min_accuracy": 92,
                "tip": "Mix words, numbers, colons, commas, and full stops seamlessly.",
                "text": (
                    "On July 20, 1969, Apollo 11 landed on the Moon at 20:17 UTC. "
                    "The library cataloged 14,580 books, 2,390 journals, and 675 digital archives. "
                    "Between 2020 and 2026, average processing throughput rose from 450 to 1,920 units per hour; "
                    "accuracy remained above 99.4% across all 128 stations."
                )
            }
        ]
    },
    {
        "unit_id": "en_u6",
        "unit_number": 6,
        "title": "Unit 6: Symbols & Special Characters",
        "subtitle": "Master commercial, mathematical, and technical symbols (@ # $ % & * ( ) + = [ ]).",
        "focus_keys": ["@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "=", "[", "]"],
        "lessons": [
            {
                "id": "en_u6_l1",
                "title": "6.1 Parentheses, Brackets & Math Operators (( ) [ ] + = * /)",
                "type": "key_drill",
                "new_keys": ["(", ")", "[", "]", "+", "=", "*"],
                "target_wpm": 20,
                "min_accuracy": 90,
                "tip": "Use Left Shift with Right Ring (9) for '(' and Right Pinky (0) for ')'. Brackets [ ] sit to the right of P.",
                "text": (
                    "(a + b) = (c * d); [x + y] = [100 / 4]; (12 + 38) * 2 = 100; "
                    "Please review items (1), (2), and (3) in reference [A-14]. "
                    "Formula: velocity = distance / time (measured in m/s); "
                    "check that (25 * 4) + (15 * 2) = 130."
                )
            },
            {
                "id": "en_u6_l2",
                "title": "6.2 Commercial & Web Symbols (@ # $ % & _)",
                "type": "sentence_drill",
                "new_keys": ["@", "#", "$", "%", "&", "_"],
                "target_wpm": 22,
                "min_accuracy": 90,
                "tip": "Shift + 2 is @, Shift + 3 is #, Shift + 4 is $, Shift + 5 is %, and Shift + 7 is &.",
                "text": (
                    "Send the report to support@example.org or admin_desk@company.com by 5:00 PM. "
                    "Invoice #4829 includes a 15% discount ($45.00 off the $300.00 subtotal) for R&D supplies. "
                    "File name: project_summary_2026.txt; tag #productivity & #accuracy for 100% completion!"
                )
            }
        ]
    },
    {
        "unit_id": "en_u7",
        "unit_number": 7,
        "title": "Unit 7: Speed Building & Word Rhythm",
        "subtitle": "Accelerate your WPM with high-frequency English words, common suffixes, and alternating-hand sprints.",
        "focus_keys": [],
        "lessons": [
            {
                "id": "en_u7_l1",
                "title": "7.1 Top 100 High-Frequency English Words Sprint",
                "type": "word_drill",
                "new_keys": [],
                "target_wpm": 32,
                "min_accuracy": 94,
                "tip": "These 100 words make up over 50% of all written English. Read one word ahead while your fingers finish the current word!",
                "text": (
                    "the be to of and a in that have I it for not on with he as you do at "
                    "this but his by from they we say her she or an will my one all would "
                    "there their what so up out if about who get which go me when make can "
                    "like time no just him know take people into year your good some could "
                    "them see other than then now look only come its over think also back"
                )
            },
            {
                "id": "en_u7_l2",
                "title": "7.2 Power N-Grams (-tion, -ment, -ight, -ough, -ould)",
                "type": "word_drill",
                "new_keys": [],
                "target_wpm": 34,
                "min_accuracy": 94,
                "tip": "Train your fingers to fire common 4-letter clusters as a single effortless motion.",
                "text": (
                    "action nation station education information; "
                    "moment highlight movement development agreement; "
                    "light night right bright sight flight thought brought through enough; "
                    "would could should; Understanding these patterns multiplies your typing speed."
                )
            },
            {
                "id": "en_u7_l3",
                "title": "7.3 Tricky Double Letters & Precision Words",
                "type": "sentence_drill",
                "new_keys": [],
                "target_wpm": 35,
                "min_accuracy": 95,
                "tip": "Keep double keystrokes crisp and evenly spaced without mashing the key.",
                "text": (
                    "The committee succeeded in arranging parallel sessions for the millennium conference. "
                    "A careful bookkeeper records every occurrence, address, and necessary assessment. "
                    "Excellence requires attention to detail, steady rhythm, and effortless composure."
                )
            }
        ]
    },
    {
        "unit_id": "en_u8",
        "unit_number": 8,
        "title": "Unit 8: Full Paragraphs & Mastery Certification",
        "subtitle": "Complete real-world paragraphs featuring full stops, semicolons, colons, quotes, numbers, and symbols.",
        "focus_keys": [],
        "lessons": [
            {
                "id": "en_u8_l1",
                "title": "8.1 Science & Discovery Paragraph",
                "type": "paragraph_drill",
                "new_keys": [],
                "target_wpm": 35,
                "min_accuracy": 95,
                "tip": "Maintain a steady, breathing pace across multiple long sentences.",
                "text": (
                    "Astronomy compels the soul to look upward and leads us from this world to another. "
                    "Light travels through the vacuum of space at approximately 299,792 kilometers per second; "
                    "consequently, when we observe the Andromeda Galaxy (located 2.5 million light-years away), "
                    "we are looking directly into the deep history of the cosmos. Every star, planet, and nebula "
                    "obeys precise physical laws: gravity pulls matter together, while nuclear fusion ignites the core."
                )
            },
            {
                "id": "en_u8_l2",
                "title": "8.2 Literature, Philosophy & Semicolon Mastery",
                "type": "paragraph_drill",
                "new_keys": [],
                "target_wpm": 38,
                "min_accuracy": 95,
                "tip": "Notice how semicolons, colons, dashes, and quotation marks structure complex thoughts.",
                "text": (
                    "\"We are what we repeatedly do,\" wrote Will Durant in his classic summary of Aristotle's ethics; "
                    "\"excellence, then, is not an act, but a habit.\" Consider how any craft is mastered: first, "
                    "the student learns the basic rules consciously; second, deliberate practice refines away errors; "
                    "finally, the skill becomes second nature. Whether you are composing an essay, writing software, "
                    "or drafting a legal brief, fluent typing removes the barrier between thought and expression."
                )
            },
            {
                "id": "en_u8_l3",
                "title": "8.3 Executive Business & Financial Report",
                "type": "paragraph_drill",
                "new_keys": [],
                "target_wpm": 38,
                "min_accuracy": 95,
                "tip": "Real-world executive passage mixing prose, numbers, percentages, and punctuation.",
                "text": (
                    "During Q4 2026, regional operations achieved a 18.5% increase in net productivity, surpassing "
                    "our initial target of $4.2 million by $310,000 (Report #2026-Q4). Three factors drove this "
                    "outcome: (1) streamlined supply-chain logistics; (2) a 24% reduction in equipment downtime; "
                    "and (3) comprehensive staff training across all 14 branches. Please send any questions or "
                    "revisions to board_review@enterprise.org before Friday at 17:30!"
                )
            },
            {
                "id": "en_u8_l4",
                "title": "8.4 Grand Mastery Certification Exam",
                "type": "paragraph_drill",
                "new_keys": [],
                "target_wpm": 42,
                "min_accuracy": 96,
                "tip": "Final English Mastery Exam! Aim for 96%+ accuracy and smooth, uninterrupted flow.",
                "text": (
                    "Mastery of the keyboard is one of the most practical lifelong skills you can acquire. "
                    "From the humble mechanical typewriters of the 1870s to modern high-speed mechanical switches, "
                    "the core principle of touch typing has never changed: keep your fingers anchored on the Home Row "
                    "(A, S, D, F and J, K, L, ;), keep your eyes focused on the screen, and trust your muscle memory! "
                    "When you can type words, numbers (0-9), and punctuation marks - such as commas, full stops, "
                    "semicolons, colons, and quotation marks - at 45+ WPM with 97% accuracy, you save hundreds of hours "
                    "every single year. Congratulations on completing the full English Touch-Typing Course!"
                )
            }
        ]
    }
]


SPEED_TEST_PASSAGES_EN = [
    {
        "id": "st_en_1",
        "title": "The Art of Deep Focus",
        "difficulty": "Medium",
        "text": (
            "In an age of constant digital distraction, the ability to concentrate without interruption "
            "has become both rare and extraordinarily valuable. When you sit down to work on a meaningful "
            "problem, your brain requires roughly fifteen minutes to reach its deepest state of flow; "
            "however, a single glance at a notification can shatter that focus instantly. By setting aside "
            "dedicated blocks of quiet time, organizing your workspace, and trusting your touch-typing rhythm, "
            "you can produce twice as much high-quality work in half the time. Clarity of mind always leads "
            "to clarity of execution."
        )
    },
    {
        "id": "st_en_2",
        "title": "History of the Printing Press & Typewriter",
        "difficulty": "Hard (Numbers & Punctuation)",
        "text": (
            "Around 1440, Johannes Gutenberg introduced the movable-type printing press in Mainz, Germany; "
            "within five decades, over 20 million volumes had been printed across Europe! Centuries later, "
            "in 1868, Christopher Latham Sholes patented the first practical typewriter, introducing the "
            "QWERTY layout that billions of people still use today. Why were the keys arranged this way? "
            "Early mechanical typebars jammed when adjacent keys were struck in rapid succession; therefore, "
            "common letter pairs were separated across the keyboard. Today, whether you type at 40 WPM or "
            "100+ WPM, you are participating in a 580-year tradition of mechanized human communication."
        )
    },
    {
        "id": "st_en_3",
        "title": "The Architecture of Nature",
        "difficulty": "Standard",
        "text": (
            "Walk through an ancient forest after a morning rain, and you will notice how every organism "
            "contributes to a balanced ecosystem. Tall canopy trees capture sunlight and convert carbon "
            "dioxide into oxygen; beneath the soil, vast networks of fungal threads connect roots from "
            "tree to tree, sharing water and vital minerals. Nothing in nature is wasted: fallen leaves "
            "nourish the earth, streams carve fertile valleys, and seasonal cycles renew the landscape year "
            "after year. Observing these quiet patterns reminds us that patience and cooperation are the "
            "true engines of resilience."
        )
    },
    {
        "id": "st_en_4",
        "title": "Modern Computing & Algorithms",
        "difficulty": "Technical (Symbols & Numbers)",
        "text": (
            "Every software application relies on fundamental data structures: arrays, hash tables, trees, "
            "and graphs. When an algorithm searches through 1,000,000 sorted records using binary search, "
            "it requires at most 20 comparisons (because 2^20 = 1,048,576), whereas a linear scan could "
            "take all 1,000,000 steps! Clean code is not merely written for computers to execute; as Donald "
            "Knuth famously observed, \"Programs are meant to be read by humans, and only incidentally for "
            "computers to execute.\" Always write clear documentation, test edge cases (0, -1, and null), "
            "and measure performance before optimizing."
        )
    }
]


# All 14 Supported Scripts (English + 13 Indian Languages via InScript — All Active!)
LANGUAGE_REGISTRY = [
    {"code": "en", "name": "English", "native_name": "English", "layout": "QWERTY Standard", "status": "active", "script": "Latin", "greeting": "Welcome! Ready to flow?"},
    {"code": "hi", "name": "Hindi", "native_name": "हिन्दी", "layout": "InScript Standard", "status": "active", "script": "Devanagari", "greeting": "नमस्ते! अभ्यास शुरू करें?"},
    {"code": "mr", "name": "Marathi", "native_name": "मराठी", "layout": "InScript Standard", "status": "active", "script": "Devanagari", "greeting": "नमस्कार! सराव सुरू करूया?"},
    {"code": "sa", "name": "Sanskrit", "native_name": "संस्कृतम्", "layout": "InScript Standard", "status": "active", "script": "Devanagari", "greeting": "सुस्वागतम्! अभ्यासं कुर्मः?"},
    {"code": "bn", "name": "Bengali", "native_name": "বাংলা", "layout": "InScript Standard", "status": "active", "script": "Bengali", "greeting": "নমস্কার! অনুশীলন শুরু করি?"},
    {"code": "pa", "name": "Punjabi", "native_name": "ਪੰਜਾਬੀ", "layout": "InScript Standard", "status": "active", "script": "Gurmukhi", "greeting": "ਸਤ ਸ੍ਰੀ ਅਕਾਲ! ਅਭਿਆਸ ਸ਼ੁਰੂ ਕਰੀਏ?"},
    {"code": "gu", "name": "Gujarati", "native_name": "ગુજરાતી", "layout": "InScript Standard", "status": "active", "script": "Gujarati", "greeting": "નમસ્તે! મહાવરો શરૂ કરીએ?"},
    {"code": "or", "name": "Odia", "native_name": "ଓଡ଼ିଆ", "layout": "InScript Standard", "status": "active", "script": "Odia", "greeting": "ନମସ୍କାର! ଅଭ୍ୟାସ ଆରମ୍ଭ କରିବା?"},
    {"code": "ta", "name": "Tamil", "native_name": "தமிழ்", "layout": "InScript Standard", "status": "active", "script": "Tamil", "greeting": "வணக்கம்! பயிற்சியைத் தொடங்கலாமா?"},
    {"code": "te", "name": "Telugu", "native_name": "తెలుగు", "layout": "InScript Standard", "status": "active", "script": "Telugu", "greeting": "నమస్కారం! సాధన ప్రారంభిద్దామా?"},
    {"code": "kn", "name": "Kannada", "native_name": "ಕನ್ನಡ", "layout": "InScript Standard", "status": "active", "script": "Kannada", "greeting": "ನಮಸ್ಕಾರ! ಅಭ್ಯಾಸ ಪ್ರಾರಂಭಿಸೋಣವೇ?"},
    {"code": "ml", "name": "Malayalam", "native_name": "മലയാളം", "layout": "InScript Standard", "status": "active", "script": "Malayalam", "greeting": "നമസ്കാരം! പരിശീലനം തുടങ്ങാം?"},
    {"code": "as", "name": "Assamese", "native_name": "অসমীয়া", "layout": "InScript Standard", "status": "active", "script": "Assamese", "greeting": "নমস্কাৰ! অনুশীলন আৰম্ভ কৰোঁনে?"},
    {"code": "ur", "name": "Urdu", "native_name": "اردو", "layout": "InScript / Standard", "status": "active", "script": "Perso-Arabic", "greeting": "خوش آمدید! مشق شروع کریں؟"},
]


def get_units_for_language(language: str = "en"):
    if language == "en" or language not in INDIAN_LANGUAGE_PACKS:
        return ENGLISH_UNITS
    return generate_units_for_indian_language(language)


def get_speed_passages_for_language(language: str = "en"):
    if language == "en" or language not in INDIAN_LANGUAGE_PACKS:
        return SPEED_TEST_PASSAGES_EN
    return get_speed_passages_for_indian_language(language)


def get_finger_map_for_language(language: str = "en"):
    if language == "en" or language not in INDIAN_LANGUAGE_PACKS:
        return FINGER_MAP_EN
    pack = INDIAN_LANGUAGE_PACKS[language]
    fmap = dict(FINGER_MAP_EN)
    fmap.update(build_reverse_char_to_finger_map(pack["keymap"]))
    return fmap


def get_keymap_and_guide_for_language(language: str = "en"):
    if language == "en" or language not in INDIAN_LANGUAGE_PACKS:
        return {"keymap": None, "setup_guide": None, "vocab": None}
    pack = INDIAN_LANGUAGE_PACKS[language]
    return {
        "keymap": pack["keymap"],
        "setup_guide": pack["setup_guide"],
        "vocab": pack["vocab"]
    }


def get_all_lessons_flat(language: str = "en"):
    units = get_units_for_language(language)
    flat = []
    for unit in units:
        for lesson in unit["lessons"]:
            item = dict(lesson)
            item["unit_id"] = unit["unit_id"]
            item["unit_number"] = unit["unit_number"]
            item["unit_title"] = unit["title"]
            flat.append(item)
    return flat


def get_lesson_by_id(lesson_id: str, language: str = "en"):
    flat = get_all_lessons_flat(language)
    for idx, l in enumerate(flat):
        if l["id"] == lesson_id:
            next_id = flat[idx + 1]["id"] if idx + 1 < len(flat) else None
            l["next_lesson_id"] = next_id
            return l
    if flat:
        first = dict(flat[0])
        first["next_lesson_id"] = flat[1]["id"] if len(flat) > 1 else None
        return first
    return None
