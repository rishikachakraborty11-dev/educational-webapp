import random
import streamlit as st

# ----------------------------------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------------------------------
st.set_page_config(
    page_title="Abhishek Coaching — Learn Online",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

BOARDS = ["CBSE", "ICSE", "IGCSE", "IB", "Cambridge"]
GRADES = [3, 4, 5, 6, 7, 8]
SUBJECTS = ["English", "Maths", "Science"]
WHATSAPP_NUMBER = "919836014935"  # change to your own number

# ----------------------------------------------------------------------------
# CONTENT — chapters + notes (board-general core curriculum topics)
# ----------------------------------------------------------------------------
MATHS_CONTENT = {
    3: {
        "Numbers up to 1000": "- Reading, writing and comparing numbers up to 1000.\n- Place value: hundreds, tens, ones.\n- Ordering numbers (ascending/descending) and number patterns.",
        "Addition & Subtraction": "- Adding and subtracting 2 and 3 digit numbers with regrouping.\n- Word problems using addition and subtraction.\n- Estimating sums and differences.",
        "Multiplication": "- Multiplication as repeated addition.\n- Tables up to 10.\n- Multiplying 2-digit numbers by a 1-digit number.",
        "Division": "- Division as equal sharing/grouping.\n- Relationship between multiplication and division.\n- Simple word problems on division.",
        "Fractions (Basics)": "- Understanding a fraction as part of a whole.\n- Halves, thirds and quarters.\n- Comparing simple fractions with the same denominator.",
        "Shapes & Patterns": "- 2D shapes: circle, square, triangle, rectangle.\n- 3D shapes: cube, cone, sphere, cylinder.\n- Identifying and extending simple patterns.",
    },
    4: {
        "Large Numbers": "- Numbers up to 1,00,000 (lakh) or 6-digit numbers.\n- Place value, expanded and standard form.\n- Rounding off numbers.",
        "Four Operations": "- Addition, subtraction, multiplication and division of large numbers.\n- Order of operations (BODMAS basics).\n- Word problems combining operations.",
        "Fractions & Decimals": "- Equivalent fractions and simplifying fractions.\n- Introduction to decimals and place value of decimals.\n- Converting simple fractions to decimals.",
        "Geometry Basics": "- Points, lines, line segments and rays.\n- Types of angles: acute, right, obtuse.\n- Symmetry in shapes.",
        "Perimeter & Area": "- Perimeter of squares and rectangles.\n- Area of squares and rectangles using unit squares.\n- Real-life word problems.",
        "Data Handling": "- Collecting and organising data.\n- Reading bar graphs and pictographs.\n- Drawing simple bar graphs.",
    },
    5: {
        "Number System": "- Numbers up to crores/millions, place value.\n- Factors, multiples, prime and composite numbers.\n- HCF and LCM (introduction).",
        "Fractions & Decimals": "- Addition/subtraction of fractions with different denominators.\n- Multiplying and dividing decimals.\n- Converting between fractions and decimals.",
        "Percentage": "- Meaning of percentage as 'per hundred'.\n- Converting fractions/decimals to percentages and back.\n- Simple percentage word problems.",
        "Geometry": "- Types of triangles and quadrilaterals.\n- Measuring and constructing angles with a protractor.\n- Properties of circles: radius, diameter, circumference.",
        "Perimeter, Area & Volume": "- Perimeter and area of composite shapes.\n- Introduction to volume using cubes.\n- Units of measurement conversions.",
        "Data Handling": "- Mean (average) of a data set.\n- Reading and interpreting line graphs.\n- Probability — likely, unlikely, certain (introduction).",
    },
    6: {
        "Integers": "- Positive and negative numbers on a number line.\n- Addition and subtraction of integers.\n- Comparing and ordering integers.",
        "Fractions & Decimals": "- Operations on fractions and decimals together.\n- Converting between fractions, decimals and percentages.\n- Word problems involving all three.",
        "Introduction to Algebra": "- Using letters/variables to represent numbers.\n- Forming simple algebraic expressions.\n- Evaluating expressions by substitution.",
        "Ratio & Proportion": "- Meaning of ratio and simplifying ratios.\n- Direct proportion and unitary method.\n- Real-life applications of ratio.",
        "Basic Geometry": "- Angles, triangles and their properties.\n- Types of quadrilaterals and their properties.\n- Introduction to 3D shapes (nets and faces).",
        "Mensuration": "- Perimeter and area of rectangles, squares and triangles.\n- Area of a parallelogram (introduction).\n- Practical measurement problems.",
    },
    7: {
        "Integers": "- Properties of integers (commutative, associative).\n- Multiplication and division of integers.\n- Word problems with integers.",
        "Rational Numbers": "- Definition and representation on a number line.\n- Comparing and ordering rational numbers.\n- Operations on rational numbers.",
        "Algebraic Expressions": "- Terms, factors and coefficients.\n- Like and unlike terms; addition/subtraction of expressions.\n- Simplifying algebraic expressions.",
        "Simple Equations": "- Forming a linear equation from a statement.\n- Solving simple equations in one variable.\n- Applications of simple equations.",
        "Lines & Angles": "- Complementary and supplementary angles.\n- Angles made by a transversal with parallel lines.\n- Vertically opposite angles.",
        "Percentage, Profit & Loss": "- Calculating percentage increase/decrease.\n- Profit, loss and discount calculations.\n- Simple interest (introduction).",
    },
    8: {
        "Rational Numbers": "- Properties of rational numbers (closure, commutative, associative).\n- Representing rational numbers on a number line.\n- Operations involving rational numbers.",
        "Linear Equations in One Variable": "- Solving equations with variables on both sides.\n- Word problems leading to linear equations.\n- Applications in age, number and money problems.",
        "Squares & Square Roots": "- Perfect squares and properties of square numbers.\n- Finding square roots by prime factorisation/division method.\n- Estimating square roots.",
        "Mensuration": "- Area of a trapezium and general quadrilaterals.\n- Surface area and volume of cubes and cuboids.\n- Volume and surface area of a cylinder (introduction).",
        "Algebraic Expressions & Identities": "- Multiplying algebraic expressions.\n- Standard identities: (a+b)^2, (a-b)^2, (a+b)(a-b).\n- Using identities to simplify calculations.",
        "Data Handling": "- Organising data using frequency distribution tables.\n- Drawing and reading pie charts.\n- Basic probability of simple events.",
    },
}

SCIENCE_CONTENT = {
    3: {
        "Living & Non-Living Things": "- Characteristics of living things: growth, movement, reproduction.\n- Differences between living and non-living things.\n- Examples from our surroundings.",
        "Plants Around Us": "- Parts of a plant: root, stem, leaf, flower, fruit.\n- Functions of each part.\n- Types of plants: herbs, shrubs, trees.",
        "Animals Around Us": "- Classification: wild, domestic, aquatic, aerial animals.\n- Animal habitats and adaptations.\n- Movement and coverings of animals.",
        "Our Body": "- Major external body parts and sense organs.\n- Importance of the five senses.\n- Basic hygiene and care of the body.",
        "Food & Nutrition": "- Sources of food: plants and animals.\n- Balanced diet and food groups.\n- Importance of clean and healthy food.",
        "Water": "- Sources of water and states of water.\n- Uses of water and the need to conserve it.\n- Simple water cycle (introduction).",
    },
    4: {
        "Plant Life": "- Photosynthesis (introduction) — how plants make food.\n- Reproduction in plants: seeds and germination.\n- Plant adaptations to different habitats.",
        "Animal Adaptations": "- How animals adapt to hot, cold and water habitats.\n- Life cycles of common animals (butterfly, frog).\n- Food chains (introduction).",
        "Human Body Systems": "- Digestive system — journey of food.\n- Skeletal system — bones and their function.\n- Importance of exercise and rest.",
        "Force & Motion": "- Types of force: push and pull.\n- Effects of force on objects.\n- Simple machines (introduction).",
        "Matter & Materials": "- States of matter: solid, liquid, gas.\n- Change of state (melting, freezing, evaporation).\n- Properties of common materials.",
        "Natural Resources": "- Renewable and non-renewable resources.\n- Importance of air, water and soil.\n- Conserving natural resources.",
    },
    5: {
        "The Living World": "- Classification of living things into groups.\n- Microorganisms — useful and harmful.\n- Interdependence of living organisms.",
        "Human Body Systems": "- Respiratory and circulatory systems.\n- Nervous system (introduction).\n- Keeping the body healthy.",
        "Force & Energy": "- Forms of energy: heat, light, sound.\n- Sources of energy — renewable vs non-renewable.\n- Simple concept of work and energy.",
        "Matter": "- Physical and chemical properties of matter.\n- Mixtures and simple separation methods.\n- Solubility (introduction).",
        "Earth & Space": "- The solar system — sun, planets, moon.\n- Day and night, seasons (introduction).\n- Earth's rotation and revolution (basic idea).",
        "Air & Water": "- Composition of air.\n- Air and water pollution — causes and effects.\n- Simple conservation practices.",
    },
    6: {
        "Food & Nutrition": "- Nutrients: carbohydrates, proteins, fats, vitamins, minerals.\n- Balanced diet and deficiency diseases.\n- Preservation of food.",
        "Living Organisms & Surroundings": "- Habitats and adaptations of organisms.\n- Characteristics of living organisms.\n- Interaction between organisms and environment.",
        "Motion & Measurement": "- Types of motion: rectilinear, circular, periodic.\n- Standard units of measurement (SI units).\n- Measuring length, mass and time accurately.",
        "Light, Shadows & Reflections": "- Formation of shadows.\n- Reflection of light from a mirror.\n- Transparent, translucent and opaque objects.",
        "Electricity & Circuits": "- Simple electric circuit and its components.\n- Conductors and insulators.\n- Safety precautions with electricity.",
        "Natural Resources": "- Air, water and land as resources.\n- Garbage management and recycling.\n- Sustainable use of resources.",
    },
    7: {
        "Nutrition in Plants & Animals": "- Photosynthesis — process and requirements.\n- Modes of nutrition: autotrophic and heterotrophic.\n- Digestion in humans (detailed).",
        "Heat & Temperature": "- Difference between heat and temperature.\n- Measuring temperature using a thermometer.\n- Transfer of heat: conduction, convection, radiation.",
        "Acids, Bases & Salts": "- Properties of acids and bases.\n- Indicators: litmus, turmeric.\n- Neutralisation reaction (introduction).",
        "Physical & Chemical Changes": "- Differences between physical and chemical changes.\n- Rusting and its prevention.\n- Examples from daily life.",
        "Weather, Climate & Adaptations": "- Difference between weather and climate.\n- Adaptations of animals to their climate.\n- Factors affecting climate.",
        "Motion & Time": "- Speed = distance/time.\n- Measuring time using different devices.\n- Distance-time graphs (introduction).",
    },
    8: {
        "Crop Production & Management": "- Agricultural practices: ploughing, sowing, irrigation.\n- Manures and fertilisers.\n- Harvesting and storage of crops.",
        "Cell — Structure & Functions": "- Cell as the basic unit of life.\n- Plant cell vs animal cell.\n- Functions of major cell organelles.",
        "Reproduction in Animals": "- Sexual and asexual reproduction.\n- Fertilisation — internal and external.\n- Development of embryo (introduction).",
        "Force & Pressure": "- Effects of force: change in shape, speed, direction.\n- Pressure exerted by solids, liquids and gases.\n- Atmospheric pressure (introduction).",
        "Chemical Effects of Electric Current": "- Conduction of electricity through liquids.\n- Electroplating and its uses.\n- Chemical effects observed during electrolysis.",
        "Pollution & Conservation": "- Causes and effects of air and water pollution.\n- Greenhouse effect and global warming (introduction).\n- Conservation practices and biodiversity.",
    },
}

ENGLISH_CONTENT = {
    3: {
        "Nouns": "- Naming words: people, places, things, animals.\n- Common nouns vs proper nouns.\n- Singular and plural nouns.",
        "Pronouns": "- Words used in place of nouns (he, she, it, they).\n- Using pronouns correctly in sentences.\n- Avoiding repetition of nouns.",
        "Verbs": "- Action/doing words in a sentence.\n- Identifying the verb in a sentence.\n- Simple present tense verbs.",
        "Adjectives": "- Describing words for nouns.\n- Adjectives of quality, quantity and number.\n- Using adjectives to make sentences more descriptive.",
        "Simple Sentences": "- Subject and predicate.\n- Types of sentences: statement, question, exclamation.\n- Correct punctuation at the end of sentences.",
        "Reading Comprehension": "- Reading a short passage carefully.\n- Answering 'who, what, where, when' questions.\n- Picking out key details from the text.",
    },
    4: {
        "Tenses": "- Simple present, past and future tense.\n- Identifying the correct tense in a sentence.\n- Changing sentences from one tense to another.",
        "Punctuation": "- Capital letters, full stops, commas.\n- Question marks and exclamation marks.\n- Correct use of apostrophes.",
        "Adverbs": "- Words that describe verbs (how, when, where).\n- Adverbs of manner, time and place.\n- Forming adverbs from adjectives.",
        "Prepositions": "- Words showing position/relationship (in, on, under, between).\n- Using prepositions correctly in sentences.\n- Common preposition errors.",
        "Story Writing": "- Structure of a story: beginning, middle, end.\n- Using descriptive words and dialogue.\n- Writing a simple story from picture prompts.",
        "Comprehension Skills": "- Understanding the main idea of a passage.\n- Making simple inferences.\n- Answering in complete sentences.",
    },
    5: {
        "Tenses in Detail": "- Continuous and perfect tenses (introduction).\n- Using appropriate tense for different situations.\n- Common tense errors.",
        "Active & Passive Voice": "- Difference between active and passive voice.\n- Changing sentences from active to passive.\n- When to use passive voice.",
        "Direct & Indirect Speech": "- Reporting someone's exact words vs reported speech.\n- Changing pronouns and tenses in reported speech.\n- Punctuation in direct speech.",
        "Grammar Essentials": "- Subject-verb agreement.\n- Conjunctions (and, but, because, so).\n- Articles: a, an, the.",
        "Comprehension": "- Reading longer passages for detail.\n- Identifying the writer's purpose and tone.\n- Vocabulary in context.",
        "Letter Writing": "- Format of informal and formal letters.\n- Writing a letter to a friend or an authority.\n- Appropriate salutations and closings.",
    },
    6: {
        "Parts of Speech": "- Review of all 8 parts of speech.\n- Identifying parts of speech in a sentence.\n- Using each correctly in writing.",
        "Clauses & Phrases": "- Difference between a phrase and a clause.\n- Main (independent) and subordinate (dependent) clauses.\n- Joining clauses with conjunctions.",
        "Tenses Revision": "- All tenses revised with examples.\n- Choosing the correct tense for context.\n- Common mistakes to avoid.",
        "Comprehension": "- Unseen passage comprehension practice.\n- Answering inferential and factual questions.\n- Summarising a passage in your own words.",
        "Essay Writing": "- Structuring an essay: introduction, body, conclusion.\n- Writing on descriptive and narrative topics.\n- Using linking words for coherence.",
        "Vocabulary Building": "- Synonyms and antonyms.\n- Using a dictionary and thesaurus effectively.\n- Word formation (prefixes and suffixes).",
    },
    7: {
        "Voice — Active & Passive": "- Rules for converting all tenses to passive voice.\n- When passive voice is preferred.\n- Practice with varied sentence types.",
        "Reported Speech": "- Reporting questions, commands and requests.\n- Changes in time and place expressions.\n- Practice converting direct to indirect speech.",
        "Clauses": "- Noun, adjective and adverb clauses.\n- Identifying clause type and function.\n- Combining sentences using clauses.",
        "Comprehension": "- Analytical reading of prose and poetry extracts.\n- Answering 'reference to context' questions.\n- Identifying literary devices (introduction).",
        "Letter & Essay Writing": "- Formal letters: complaint, application, enquiry.\n- Essay writing on argumentative topics.\n- Organising ideas with clear paragraphs.",
        "Vocabulary & Synonyms": "- Building academic vocabulary.\n- Idioms and phrases in everyday use.\n- Synonym/antonym practice for precision writing.",
    },
    8: {
        "Advanced Grammar": "- Modal verbs and their uses.\n- Conditional sentences (if-clauses).\n- Gerunds and infinitives.",
        "Comprehension Skills": "- Critical reading of unseen passages.\n- Distinguishing fact from opinion.\n- Summary writing in a fixed word limit.",
        "Essay Writing": "- Persuasive and argumentative essay writing.\n- Using evidence and examples to support ideas.\n- Editing and proofreading your own writing.",
        "Report Writing": "- Format and features of a newspaper report.\n- Writing objectively using the 5 Ws and 1 H.\n- Using an appropriate headline.",
        "Vocabulary Enrichment": "- Advanced synonyms, antonyms and homophones.\n- One-word substitutions.\n- Using new vocabulary accurately in writing.",
        "Introduction to Literature": "- Identifying theme, character and setting.\n- Basic literary devices: simile, metaphor, personification.\n- Responding to a short story or poem extract.",
    },
}

CHAPTERS = {"Maths": MATHS_CONTENT, "Science": SCIENCE_CONTENT, "English": ENGLISH_CONTENT}

# ----------------------------------------------------------------------------
# STATIC MCQs — English & Science (5 per grade)
# ----------------------------------------------------------------------------
ENGLISH_MCQS = {
    3: [
        {"q": "Which word is a noun?", "options": ["Run", "Happy", "Table", "Quickly"], "answer": "Table"},
        {"q": "Choose the correct pronoun: '___ is my friend.'", "options": ["Him", "She", "Her", "Them"], "answer": "She"},
        {"q": "Which is the verb in 'The dog barks loudly'?", "options": ["Dog", "Barks", "Loudly", "The"], "answer": "Barks"},
        {"q": "Pick the adjective: 'It is a beautiful flower.'", "options": ["Flower", "Is", "A", "Beautiful"], "answer": "Beautiful"},
        {"q": "What punctuation ends a question?", "options": [".", "!", "?", ","], "answer": "?"},
    ],
    4: [
        {"q": "'She ___ to school every day.' (simple present)", "options": ["go", "goes", "gone", "going"], "answer": "goes"},
        {"q": "Which is an adverb of manner?", "options": ["Quickly", "Yesterday", "Here", "Tomorrow"], "answer": "Quickly"},
        {"q": "Choose the correct preposition: 'The cat is ___ the table.'", "options": ["under", "run", "happy", "blue"], "answer": "under"},
        {"q": "Which sentence uses correct punctuation?", "options": ["hello how are you", "Hello, how are you?", "hello, How are you", "Hello how are you."], "answer": "Hello, how are you?"},
        {"q": "A story usually has a beginning, middle and ___.", "options": ["title", "end", "picture", "author"], "answer": "end"},
    ],
    5: [
        {"q": "Change to passive voice: 'The cat chased the mouse.'", "options": ["The mouse chased the cat.", "The mouse was chased by the cat.", "The cat is chasing the mouse.", "The mouse chases the cat."], "answer": "The mouse was chased by the cat."},
        {"q": "Choose the article: '___ apple a day keeps the doctor away.'", "options": ["A", "An", "The", "No article"], "answer": "An"},
        {"q": "Direct speech: He said, 'I am tired.' Indirect speech:", "options": ["He said he is tired.", "He said that he was tired.", "He says he was tired.", "He said I am tired."], "answer": "He said that he was tired."},
        {"q": "Which conjunction shows a reason?", "options": ["But", "Because", "And", "Or"], "answer": "Because"},
        {"q": "Formal letters usually end with:", "options": ["Bye bye", "Yours faithfully", "See you", "Love"], "answer": "Yours faithfully"},
    ],
    6: [
        {"q": "Which word is a conjunction?", "options": ["Although", "Green", "Jump", "Slowly"], "answer": "Although"},
        {"q": "A group of words with a subject and verb is a:", "options": ["Phrase", "Clause", "Adjective", "Noun"], "answer": "Clause"},
        {"q": "Which sentence is in the past tense?", "options": ["She plays football.", "She played football.", "She will play football.", "She is playing football."], "answer": "She played football."},
        {"q": "The opposite (antonym) of 'ancient' is:", "options": ["Old", "Modern", "Historic", "Aged"], "answer": "Modern"},
        {"q": "An essay's first paragraph is called the:", "options": ["Conclusion", "Introduction", "Body", "Summary"], "answer": "Introduction"},
    ],
    7: [
        {"q": "Passive of 'They are building a house':", "options": ["A house is built by them.", "A house is being built by them.", "A house was built by them.", "A house builds by them."], "answer": "A house is being built by them."},
        {"q": "Reported speech of: She said, 'I will come tomorrow.'", "options": ["She said she will come tomorrow.", "She said she would come the next day.", "She says she will come tomorrow.", "She said I will come tomorrow."], "answer": "She said she would come the next day."},
        {"q": "'Because he was late' is an example of a/an:", "options": ["Noun clause", "Adverb clause", "Main clause", "Adjective"], "answer": "Adverb clause"},
        {"q": "A letter of complaint should be written in a ___ tone.", "options": ["Casual", "Polite and formal", "Rude", "Funny"], "answer": "Polite and formal"},
        {"q": "'As busy as a bee' is an example of a/an:", "options": ["Metaphor", "Idiom", "Synonym", "Preposition"], "answer": "Idiom"},
    ],
    8: [
        {"q": "Which is a modal verb?", "options": ["Run", "Could", "Happy", "Table"], "answer": "Could"},
        {"q": "'If it rains, we ___ stay indoors.' (conditional)", "options": ["will", "would", "was", "were"], "answer": "will"},
        {"q": "A newspaper report should answer the 5 Ws and:", "options": ["1 H", "2 Hs", "No H", "3 Hs"], "answer": "1 H"},
        {"q": "'Bright as the sun' comparing two things using 'as' is a:", "options": ["Metaphor", "Simile", "Personification", "Idiom"], "answer": "Simile"},
        {"q": "A word that means the opposite is called a/an:", "options": ["Synonym", "Antonym", "Homophone", "Pronoun"], "answer": "Antonym"},
    ],
}

SCIENCE_MCQS = {
    3: [
        {"q": "Which of these is a living thing?", "options": ["Stone", "Plant", "Chair", "Book"], "answer": "Plant"},
        {"q": "Which part of the plant makes food?", "options": ["Root", "Stem", "Leaf", "Flower"], "answer": "Leaf"},
        {"q": "Which sense organ is used to see?", "options": ["Ear", "Nose", "Eye", "Tongue"], "answer": "Eye"},
        {"q": "Water exists in how many states?", "options": ["1", "2", "3", "4"], "answer": "3"},
        {"q": "A balanced diet includes:", "options": ["Only sweets", "Only fruits", "A variety of foods", "Only water"], "answer": "A variety of foods"},
    ],
    4: [
        {"q": "Plants make their own food through:", "options": ["Digestion", "Photosynthesis", "Respiration", "Excretion"], "answer": "Photosynthesis"},
        {"q": "A push or a pull is called a:", "options": ["Force", "Energy", "Motion", "Speed"], "answer": "Force"},
        {"q": "Ice changing to water is called:", "options": ["Freezing", "Melting", "Evaporation", "Condensation"], "answer": "Melting"},
        {"q": "Which is a renewable resource?", "options": ["Coal", "Sunlight", "Petroleum", "Natural gas"], "answer": "Sunlight"},
        {"q": "The hard structures that support our body are called:", "options": ["Muscles", "Bones", "Skin", "Nerves"], "answer": "Bones"},
    ],
    5: [
        {"q": "Microorganisms are:", "options": ["Always harmful", "Always useful", "Both useful and harmful", "Not living"], "answer": "Both useful and harmful"},
        {"q": "The organ that pumps blood in our body is the:", "options": ["Lungs", "Heart", "Kidney", "Liver"], "answer": "Heart"},
        {"q": "Which is a non-renewable source of energy?", "options": ["Wind", "Solar", "Coal", "Water"], "answer": "Coal"},
        {"q": "Which planet is known as the Red Planet?", "options": ["Earth", "Mars", "Venus", "Jupiter"], "answer": "Mars"},
        {"q": "The gas most abundant in air is:", "options": ["Oxygen", "Nitrogen", "Carbon dioxide", "Hydrogen"], "answer": "Nitrogen"},
    ],
    6: [
        {"q": "Which nutrient mainly gives us energy?", "options": ["Vitamins", "Carbohydrates", "Minerals", "Water"], "answer": "Carbohydrates"},
        {"q": "The SI unit of length is:", "options": ["Kilogram", "Metre", "Second", "Litre"], "answer": "Metre"},
        {"q": "A material that allows electricity to pass through is a:", "options": ["Insulator", "Conductor", "Resistor", "Magnet"], "answer": "Conductor"},
        {"q": "A shadow is formed when light is:", "options": ["Reflected", "Blocked", "Absorbed completely", "Refracted"], "answer": "Blocked"},
        {"q": "Which is an example of recycling?", "options": ["Throwing waste in a river", "Burning plastic", "Reusing paper to make new paper", "Burying garbage"], "answer": "Reusing paper to make new paper"},
    ],
    7: [
        {"q": "Photosynthesis requires sunlight, water and:", "options": ["Oxygen", "Carbon dioxide", "Nitrogen", "Methane"], "answer": "Carbon dioxide"},
        {"q": "A substance that turns blue litmus red is a/an:", "options": ["Base", "Acid", "Salt", "Neutral substance"], "answer": "Acid"},
        {"q": "Rusting of iron is an example of a:", "options": ["Physical change", "Chemical change", "No change", "Temporary change"], "answer": "Chemical change"},
        {"q": "Speed is calculated as:", "options": ["Time / Distance", "Distance / Time", "Distance x Time", "Distance + Time"], "answer": "Distance / Time"},
        {"q": "Heat transfer through a solid rod is mainly by:", "options": ["Convection", "Radiation", "Conduction", "Evaporation"], "answer": "Conduction"},
    ],
    8: [
        {"q": "The basic unit of life is the:", "options": ["Tissue", "Cell", "Organ", "Organism"], "answer": "Cell"},
        {"q": "Manures and fertilisers are added to soil to provide:", "options": ["Water", "Nutrients", "Sunlight", "Air"], "answer": "Nutrients"},
        {"q": "Pressure is defined as force per unit:", "options": ["Volume", "Area", "Length", "Mass"], "answer": "Area"},
        {"q": "Electroplating uses the ___ effect of electric current.", "options": ["Heating", "Magnetic", "Chemical", "Light"], "answer": "Chemical"},
        {"q": "Global warming is mainly caused by an increase in:", "options": ["Oxygen", "Greenhouse gases", "Nitrogen", "Water vapour only"], "answer": "Greenhouse gases"},
    ],
}

STATIC_MCQS = {"English": ENGLISH_MCQS, "Science": SCIENCE_MCQS}

# ----------------------------------------------------------------------------
# DYNAMIC MATHS MCQ GENERATOR (always correct, varies each time)
# ----------------------------------------------------------------------------
def _make_options(correct):
    options = {correct}
    tries = 0
    while len(options) < 4 and tries < 30:
        delta = random.choice([-12, -10, -5, -3, -2, -1, 1, 2, 3, 5, 10, 12])
        val = correct + delta
        if val != correct and val not in options and (isinstance(correct, float) or val >= 0 or correct < 0):
            options.add(val)
        tries += 1
    options = list(options)
    random.shuffle(options)
    return options


def generate_math_mcqs(grade, n=5):
    questions = []
    for _ in range(n):
        if grade == 3:
            a, b = random.randint(1, 50), random.randint(1, 50)
            op = random.choice(["+", "-", "x"])
        elif grade == 4:
            a, b = random.randint(10, 200), random.randint(1, 20)
            op = random.choice(["+", "-", "x"])
        elif grade == 5:
            a, b = random.randint(10, 500), random.randint(2, 20)
            op = random.choice(["+", "-", "x", "/"])
        elif grade == 6:
            a, b = random.randint(-50, 50), random.randint(-20, 20)
            op = random.choice(["+", "-", "x"])
        elif grade == 7:
            a, b = random.randint(-100, 100), random.randint(2, 15)
            op = random.choice(["+", "-", "x", "/"])
        else:  # grade 8
            a, b = random.randint(2, 15), random.randint(2, 15)
            op = random.choice(["square", "x", "+", "-"])

        if op == "+":
            ans, qtext = a + b, f"What is {a} + {b}?"
        elif op == "-":
            ans, qtext = a - b, f"What is {a} - {b}?"
        elif op == "x":
            ans, qtext = a * b, f"What is {a} x {b}?"
        elif op == "/":
            a = b * random.randint(2, 12)  # ensure divisible
            ans, qtext = a // b, f"What is {a} / {b}?"
        else:  # square
            ans, qtext = a * a, f"What is {a} squared (a x a)?"

        options = _make_options(ans)
        questions.append({"q": qtext, "options": [str(o) for o in options], "answer": str(ans)})
    return questions


# ----------------------------------------------------------------------------
# CSS — matches the reference site's look (dark navbar, red/yellow accents,
# blue hero banner, colourful rounded subject cards, WhatsApp float button)
# ----------------------------------------------------------------------------
st.markdown(
    """
    <style>
    #MainMenu, footer {visibility: hidden;}
    .block-container {padding-top: 1rem; padding-bottom: 4rem;}

    .top-navbar {
        background-color: #0d0d0d;
        padding: 12px 24px;
        display: flex;
        align-items: center;
        border-radius: 6px;
        margin-bottom: 0;
    }
    .brand-box {
        background-color: #8b0000;
        border: 2px solid #ffd700;
        border-radius: 6px;
        padding: 8px 20px;
        display: inline-block;
    }
    .brand-box span {
        color: #ffd700;
        font-weight: 800;
        font-size: 22px;
        letter-spacing: 1px;
    }

    .hero-banner {
        background: linear-gradient(135deg, #0b1d4d 0%, #16327a 60%, #1e3a8a 100%);
        border-radius: 6px;
        padding: 40px 36px;
        margin-top: 8px;
        margin-bottom: 22px;
        color: white;
    }
    .hero-banner h1 {
        color: #ffd700;
        font-size: 34px;
        font-weight: 800;
        margin-bottom: 6px;
    }
    .hero-banner h2 {
        color: white;
        font-size: 22px;
        font-weight: 600;
        margin-top: 0;
    }
    .hero-banner p {
        color: #e5e7eb;
        font-size: 16px;
    }

    .subject-card {
        border-radius: 12px;
        padding: 22px 14px;
        text-align: center;
        font-weight: 800;
        font-size: 19px;
        color: #111;
        border: 2px solid #cc0000;
        margin-bottom: 12px;
    }
    .card-english { background-color: #ffb3b3; }
    .card-maths { background-color: #fff3a3; }
    .card-science { background-color: #c9f7c5; }

    .whatsapp-float {
        position: fixed;
        bottom: 26px;
        right: 24px;
        background-color: #25D366;
        color: white !important;
        border-radius: 50px;
        padding: 12px 20px;
        font-weight: 700;
        text-decoration: none !important;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.35);
        z-index: 9999;
        font-size: 15px;
    }
    .whatsapp-float:hover { background-color: #1ebe5b; }

    .footer-box {
        background-color: #0b1d4d;
        color: white;
        padding: 24px 30px;
        border-radius: 6px;
        margin-top: 30px;
    }
    .footer-box a { color: #93c5fd; }

    .stButton>button {
        background-color: #8b0000;
        color: white;
        font-weight: 700;
        border-radius: 20px;
        border: 2px solid #ffd700;
    }
    .stButton>button:hover { background-color: #a30000; color: #ffd700; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ----------------------------------------------------------------------------
# TOP NAVBAR + HERO
# ----------------------------------------------------------------------------
st.markdown(
    """
    <div class="top-navbar">
        <div class="brand-box"><span>ABHISHEK COACHING</span></div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="hero-banner">
        <h1>AI-powered classes that actually click</h1>
        <h2>Free Notes &amp; MCQ Practice — Grades 3 to 8</h2>
        <p>English, Maths &amp; Science mapped to CBSE, ICSE, IGCSE, IB and Cambridge. 100% free and open to all students.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ----------------------------------------------------------------------------
# SIDEBAR — vertical dropdown menu
# ----------------------------------------------------------------------------
st.sidebar.markdown("## 📚 Choose Your Class")
board = st.sidebar.selectbox("🏫 Select Board", BOARDS, index=0)
grade = st.sidebar.selectbox("🎒 Select Grade", GRADES, index=0, format_func=lambda g: f"Grade {g}")
subject = st.sidebar.selectbox("📖 Select Subject", SUBJECTS, index=0)

st.sidebar.markdown("---")
st.sidebar.markdown(
    f"**Currently viewing:**\n\n"
    f"- Board: `{board}`\n"
    f"- Grade: `{grade}`\n"
    f"- Subject: `{subject}`"
)
st.sidebar.markdown("---")
st.sidebar.markdown("📞 **Call / WhatsApp / Telegram:**\n+91 98360 14935")
st.sidebar.markdown("🌐 www.abhishekcoaching.com")

# ----------------------------------------------------------------------------
# SUBJECT QUICK-LINK CARDS (like the reference screenshot)
# ----------------------------------------------------------------------------
st.markdown("#### Quick Jump")
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown('<div class="subject-card card-english">📘 English</div>', unsafe_allow_html=True)
    if st.button("Open English", use_container_width=True, key="btn_eng"):
        subject = "English"
with c2:
    st.markdown('<div class="subject-card card-maths">➗ Maths</div>', unsafe_allow_html=True)
    if st.button("Open Maths", use_container_width=True, key="btn_math"):
        subject = "Maths"
with c3:
    st.markdown('<div class="subject-card card-science">🔬 Science</div>', unsafe_allow_html=True)
    if st.button("Open Science", use_container_width=True, key="btn_sci"):
        subject = "Science"

st.markdown("---")
st.markdown(f"### {subject} — Grade {grade} ({board} aligned)")
st.caption(
    "Core topics are common across major boards at this grade level; depth and terminology "
    "may vary slightly by board — use these notes as a strong general foundation."
)

tab_notes, tab_quiz = st.tabs(["📘 Notes", "📝 MCQ Quiz"])

# ----------------------------------------------------------------------------
# NOTES TAB
# ----------------------------------------------------------------------------
with tab_notes:
    chapters = CHAPTERS[subject][grade]
    for chapter_name, notes in chapters.items():
        with st.expander(f"📖 {chapter_name}"):
            st.markdown(notes)

# ----------------------------------------------------------------------------
# QUIZ TAB
# ----------------------------------------------------------------------------
with tab_quiz:
    quiz_key = f"quiz_{subject}_{grade}"
    submitted_key = f"submitted_{quiz_key}"

    colq1, colq2 = st.columns([3, 1])
    with colq1:
        st.write(f"**{subject} MCQ Quiz — Grade {grade}** (5 questions)")
    with colq2:
        if st.button("🔄 New Questions", use_container_width=True):
            st.session_state.pop(quiz_key, None)
            st.session_state[submitted_key] = False

    if quiz_key not in st.session_state:
        if subject == "Maths":
            st.session_state[quiz_key] = generate_math_mcqs(grade)
        else:
            st.session_state[quiz_key] = STATIC_MCQS[subject][grade]
        st.session_state[submitted_key] = False

    questions = st.session_state[quiz_key]

    with st.form(key=f"form_{quiz_key}"):
        user_answers = []
        for i, q in enumerate(questions):
            st.markdown(f"**Q{i + 1}. {q['q']}**")
            ans = st.radio("Choose one:", q["options"], key=f"{quiz_key}_q{i}", index=None, label_visibility="collapsed")
            user_answers.append(ans)
            st.write("")
        submit = st.form_submit_button("✅ Submit Quiz")

    if submit:
        st.session_state[submitted_key] = True

    if st.session_state.get(submitted_key):
        score = 0
        for i, q in enumerate(questions):
            correct = str(q["answer"])
            given = user_answers[i] if i < len(user_answers) else None
            if given == correct:
                score += 1
                st.success(f"Q{i + 1}: Correct! ✅ ({correct})")
            else:
                st.error(f"Q{i + 1}: Your answer: {given or 'No answer'} — Correct answer: {correct}")
        st.markdown(f"### 🏆 Your Score: {score} / {len(questions)}")
        if score == len(questions):
            st.balloons()

# ----------------------------------------------------------------------------
# FOOTER
# ----------------------------------------------------------------------------
st.markdown(
    """
    <div class="footer-box">
        <b>Contact Us</b><br>
        Near Airport Gate No. 1, Dum Dum Cantt., Kolkata – 28, India<br>
        Phone / WhatsApp: +91 98360 14935 &nbsp;|&nbsp; Email: info@abhishekcoaching.com<br><br>
        <b>© Abhishek Coaching.</b> Free learning resource for students, Grades 3–8, across CBSE, ICSE, IGCSE, IB and Cambridge boards.
    </div>
    """,
    unsafe_allow_html=True,
)

# Floating WhatsApp button
st.markdown(
    f"""
    <a class="whatsapp-float" href="https://wa.me/{WHATSAPP_NUMBER}" target="_blank">
        💬 WhatsApp
    </a>
    """,
    unsafe_allow_html=True,
)
