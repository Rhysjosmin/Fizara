d = {}
AppointmentDB = {
    'James': {
    },
    'John': {
    },
    'Jennifer': {
    },
    'Richard': {
    },
    'William': {
    },
    'Robert': {
    },
    'Michael': {
    },
    'David': {
    },
    'Stephen': {
    },
    'Jeffrey': {
    },
    'Charles': {
    },
    'Daniel': {
    },
    'Steven': {
    },
    'Paul': {
    },
    'Elizabeth': {
    },
    'Susan': {
    },
    'Mary': {
    },
    'Elizabeth': {
    },
    'Joseph': {
    },
    'Mark': {
    },
    'Thomas': {
    },

}
TodoDB = {

    'Mary': [
        'Eat 5 Calories', 'Sleep 8 hours', '2 Sets of 10 pushups', 'Take Paracetamol At 8 AM', 'Take Insulin', 'Eat Food', 'Drink Water', 'Take Medicine'
    ],
    'Anya': [
        'Dont Eat 5 Calories', 'Sleep 8 hours', '2 Sets of 20 Pullups', 'Take Insulin'
    ],
    'Penelope': [
        'Eat 5 Calories', 'Sleep 8 hours', '2 Sets of 10 pushups', 'Take Paracetamol At 8 AM', 'Take Insulin'
    ],
    'Adriana': [
        'Eat 3 Calories', 'Sleep 5 hours', '2 Sets of 10 pushups', 'Take Paracetamol At  AM', 'Take Insulin'
    ],
    'Emily': [
        'Eat 5 Calories', 'Sleep 8 hours', '2 Sets of 10 pushups', 'Take Paracetamol At 8 AM', 'Take Insulin'
    ],
    'Jane': [
        'Eat 5 Calories', 'Sleep 8 hours', '2 Sets of 10 pushups', 'Take Paracetamol At 8 AM', 'Take Insulin'
    ],
    'Ava': [
        'Eat 5 Calories', 'Sleep 8 hours', '2 Sets of 10 pushups', 'Take Paracetamol At 8 AM', 'Take Insulin'
    ],
    'Megan': [
        'Eat 5 Calories', 'Sleep 8 hours', '2 Sets of 10 pushups', 'Take Paracetamol At 8 AM', 'Take Insulin'
    ],
    'Irene': [
        'Eat 5 Calories', 'Sleep 8 hours', '2 Sets of 10 pushups', 'Take Paracetamol At 8 AM', 'Take Insulin'
    ],



}
Ratings = {}
NewsDB = {
    'In Conversation: Is the ketogenic diet right for autoimmune conditions?': {
        'Body': 'The ketogenic diet is often labelled controversial due to its low carb, high fat nature. However, it is also touted as one of the best diets for weight loss, improving insulin sensitivity, and controlling seizures. But could this diet also have the potential to help inflammatory autoimmune conditions and reduce chronic pain?',
        'link': 'https://www.medicalnewstoday.com/articles/in-conversation-is-the-ketogenic-diet-right-for-autoimmune-conditions'
    },
    'Gout may be caused by deficiency of a protein found in joint fluid': {
        'Body': 'Gout, a common form of inflammatory arthritis, can cause intense pain, swelling, and stiffness in the joints.',
        'link': 'https://www.medicalnewstoday.com/articles/new-look-at-an-ancient-disease-study-finds-novel-treatment-targets-for-gout'
    },
    "New research reveals potential link between coffee consumption and reduced risk of heart disease": {
        "Body": "A new study suggests that drinking coffee may lower the risk of developing heart disease. The study found that people who drank two to three cups of coffee per day had a 20% lower risk of heart disease compared to those who did not drink coffee. The researchers believe that the antioxidants and other beneficial compounds in coffee may be responsible for this protective effect.",
        "link": "https://www.medicalnewstoday.com/articles/new-research-reveals-potential-link-between-coffee-consumption-and-reduced-risk-of-heart-disease"
    },
    "Scientists discover new species of deep-sea fish off the coast of Australia": {
        "Body": "A team of scientists has discovered a new species of deep-sea fish off the coast of Australia. The fish, which has been named the 'Black-Blotched Stingray', was found at a depth of over 2,000 meters and has unique features such as its black and white coloration and a spine that is used for defense. The discovery is an exciting development for marine biology and highlights the need to continue exploring the depths of the ocean.",
        "link": "https://www.sciencedaily.com/releases/2022/03/220328104006.htm"
    },
    "Researchers find potential new treatment for type 2 diabetes": {
        "Body": "Researchers have discovered a potential new treatment for type 2 diabetes. The treatment involves a drug that targets a specific protein in the liver, which has been found to play a key role in regulating blood sugar levels. In tests on mice, the drug was able to significantly lower blood sugar levels and improve insulin sensitivity. Further research is needed to determine whether the drug is safe and effective in humans, but the findings offer hope for those living with type 2 diabetes.",
        "link": "https://www.medicalnewstoday.com/articles/researchers-find-potential-new-treatment-for-type-2-diabetes"
    },
    "New study suggests link between screen time and increased risk of depression in teenagers": {
        "Body": "A new study has found a potential link between high levels of screen time and an increased risk of depression in teenagers. The study followed over 1,000 teenagers for two years and found that those who spent more than four hours per day on screens were significantly more likely to develop symptoms of depression compared to those who spent less time on screens. The researchers suggest that this link may be due to the social isolation and lack of physical activity that often accompanies excessive screen time.",
        "link": "https://www.theguardian.com/society/2022/mar/24/link-between-screen-time-and-depression-in-teenagers-study-suggests"
    }
}



UserDatabase = {

    "Emanuel": {"email": "Emanuel@doc.com",
                "password": "1234",
                "DocID": "12345",
                "ActiveChats": {
                    "Emily": {
                        'Email': "Emily@email.com",
                        "Chat": [
                         "##Good morning, doctor. I've been experiencing some pain in my abdomen lately and I was wondering if you could help me figure out what's going on.",
                         "$$Of course 😆, I'll do my best. Can you describe the pain you're experiencing?",
                         "##It's a dull ache that seems to come and go. It's mostly in my lower abdomen, but sometimes it spreads to my sides as well.",
                         "$$I see. Have you noticed any other symptoms?",
                         "$$Not really, just some bloating and occasional constipation.",
                         "##Based on what you've told me, it's possible that you have Irritable Bowel Syndrome. However, we'll need to do some tests to confirm the diagnosis. I'll write you a referral for some tests and we can go from there.",
                         "$$Okay, thank you doctor."
                        ]
                    },
                    "Jasmine": {
                        'Email': "Jasmine@email.com",
                        "Chat": [
                            "##Good morning, doctor. I'm having trouble sleeping lately and I was hoping you could help me.",
                            "$$Of course, I'll do my best. Can you describe what's been keeping you awake?",
                            "##I just can't seem to relax. My mind races with all sorts of thoughts and worries and I can't seem to turn it off.",
                            "$$I understand. Have you tried any relaxation techniques or meditation?",
                            "##I've tried a few things, but nothing seems to work.",
                            "$$Okay. Well, there are some medications that can help with sleep, but I prefer to try non-medication approaches first. Let's try some relaxation techniques and see if that helps. I'll give you some resources to check out.",
                            "##Okay, thanks doctor.",
                            "$$You're welcome. Let me know if you need anything else."
                        ]
                    },
                    "Rose": {
                        'Email': "Rose@email.com",
                        "Chat": [
        
                        ]
                    },
                    "Isacc": {
                        'Email': "Isacc@email.com",
                        "Chat": [
                            "##Hey, how are you doing?",
                            "$$I'm good, thanks. How about you?",
                            "##I'm doing well, thanks for asking. Have you heard about the new restaurant that just opened up?",
                            "$$😆😆😆",
                            "$$No, I haven't. What's it called?",
                            "##It's called The Bistro, and I heard their food is amazing. Do you want to check it out sometime?",
                            "$$Sure, that sounds like a great idea.",
                        ]
                    },
                }
                },

    "James": {'email': 'james@icloud.com', 'password': '425932', 'DocID': '428809',
    "ActiveChats": {}
                },

    "John": {'email': 'john@icloud.com', 'password': '591493', 'DocID': '415132',
    "ActiveChats": {}
                },

    "Jennifer": {'email': 'jennifer@gmail.com', 'password': '972472', 'DocID': '975999',
    "ActiveChats": {}
                },

    "Richard": {'email': 'richard@icloud.com', 'password': '249470', 'DocID': '547443',
    "ActiveChats": {}
                },

    "William": {'email': 'william@icloud.com', 'password': '653334', 'DocID': '636128',
    "ActiveChats": {}
                },

    "Robert": {'email': 'robert@gmail.com', 'password': '307968', 'DocID': '283225',
    "ActiveChats": {}
                },

    "Michael": {'email': 'michael@gmail.com', 'password': '678136', 'DocID': '664056',
    "ActiveChats": {}
                },

    "David": {'email': 'david@icloud.com', 'password': '230031', 'DocID': '265466',
    "ActiveChats": {}
                },

    "Stephen": {'email': 'stephen@icloud.com', 'password': '660196', 'DocID': '917119',
    "ActiveChats": {}
                },

    "Jeffrey": {'email': 'jeffrey@icloud.com', 'password': '227062', 'DocID': '880658',
    "ActiveChats": {}
                },

    "Charles": {'email': 'charles@icloud.com', 'password': '256935', 'DocID': '136025',
    "ActiveChats": {}
                },

    "Daniel": {'email': 'daniel@icloud.com', 'password': '582863', 'DocID': '560825',
    "ActiveChats": {}
                },

    "Steven": {'email': 'steven@gmail.com', 'password': '720492', 'DocID': '774657',
    "ActiveChats": {}
                },

    "Paul": {'email': 'paul@icloud.com', 'password': '839491', 'DocID': '464418',
    "ActiveChats": {}
                },

    "Elizabeth": {'email': 'elizabeth@gmail.com', 'password': '459807', 'DocID': '509446',
    "ActiveChats": {}
                },

    "Susan": {'email': 'susan@gmail.com', 'password': '331193', 'DocID': '551320',
    "ActiveChats": {}
                },

    "Mary": {'email': 'mary@gmail.com', 'password': '323856', 'DocID': '972752',
    "ActiveChats": {}
                },

    "Joseph": {'email': 'joseph@icloud.com', 'password': '717302', 'DocID': '165582',
    "ActiveChats": {}
                },

    "Mark": {'email': 'mark@gmail.com', 'password': '938772', 'DocID': '195681',
    "ActiveChats": {}
                },

    "Thomas": {'email': 'thomas@icloud.com', 'password': '318568', 'DocID': '583772',
    "ActiveChats": {}
                },


    "User": {
        'email': 'user@email.com',
        'password': '1234',
        'Calorie': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 102, 13, 14, 15, 16, 17, 18, 19, 20],
        'Todo': [
            'Eat 5 Calories', 'Sleep 8 hours', '2 Sets of 10 pushups', 'Take Paracetamol At 8 AM', 'Take Insulin'
        ],
            "ActiveChats": {}
            },

    "Emily": {
        'email': 'Emily@email.com',
        'password': '1234',
        'Calorie': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 102, 13, 14, 15, 16, 17, 18, 19, 20],
        'Todo': [
            'Eat 5 Calories', 'Sleep 8 hours', '2 Sets of 10 pushups', 'Take Paracetamol At 8 AM', 'Take Insulin'
        ],
            "ActiveChats": {}
            },
    
}
Reason = [
    'Checkup',
    'X-Ray',
    'Blood Test',
    'Ultrasound'
]


UseDB = {}
