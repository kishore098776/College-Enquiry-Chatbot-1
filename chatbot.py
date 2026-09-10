"""
=============================================================================
RULE-BASED COLLEGE ENQUIRY CHATBOT
=============================================================================

A simple rule-based chatbot that responds to student queries about college
information using keyword matching techniques.

Project Type: Mini Project (College Level)
Language: Python 3.x
Approach: Rule-Based (Keyword Matching)

=============================================================================
"""

import re
import sys
import time

# =============================================================================
# KNOWLEDGE BASE - Predefined responses for different categories
# =============================================================================


class KnowledgeBase:
    """Contains all predefined responses categorized by topic."""

    # Category: Admissions
    ADMISSION = {
        "keywords": [
            "admission",
            "admissions",
            "apply",
            "apply online",
            "register",
            "registration",
            "enrollment",
            "enrolment",
        ],
        "response": """
╔══════════════════════════════════════════════════════════════════╗
║                    🎓 ADMISSION INFORMATION                        ║
╚══════════════════════════════════════════════════════════════════╝

📌 ADMISSION PROCESS:
   1. Visit the official college website
   2. Fill out the online application form
   3. Upload required documents
   4. Pay the application fee (₹1000)
   5. Appear for entrance examination (if applicable)
   6. Attend counseling session
   7. Report to college for document verification
   8. Pay first semester fees

📋 DOCUMENTS REQUIRED:
   • 10th & 12th mark sheets (original + copies)
   • Transfer Certificate (TC)
   • Character Certificate
   • Recent passport-size photographs (8 copies)
   • Aadhaar Card copy
   • Caste Certificate (if applicable)

📅 IMPORTANT DATES:
   • Application Start: March 1, 2026
   • Last Date to Apply: June 30, 2026
   • Entrance Exam: July 15, 2026
   • Counseling: July 25-30, 2026
   • Classes Start: August 1, 2026

For more details, visit: www.college.edu.in/admissions
""",
    }

    # Category: Eligibility Criteria
    ELIGIBILITY = {
        "keywords": [
            "eligibility",
            "eligible",
            "criteria",
            "qualification",
            "qualify",
            "minimum",
            "percentage",
            "marks",
            "cutoff",
        ],
        "response": """
╔══════════════════════════════════════════════════════════════════╗
║               ✅ ELIGIBILITY CRITERIA                             ║
╚══════════════════════════════════════════════════════════════════╝

📗 UNDERGRADUATE COURSES (B.Tech, BBA, BCA, etc.):
   • Must have passed 10+2 from a recognized board
   • Minimum 60% aggregate marks (50% for SC/ST)
   • Physics, Chemistry, Mathematics mandatory for B.Tech
   • Valid JEE Main score for B.Tech admission

📘 POSTGRADUATE COURSES (M.Tech, MBA, M.Sc, etc.):
   • Bachelor's degree in relevant discipline
   • Minimum 55% aggregate marks (50% for SC/ST)
   • Valid GATE/CAT score for respective courses

📙 DIPLOMA COURSES:
   • 10th pass with minimum 50% marks
   • ITI certificate (for lateral entry)

⚠️ NOTE: Eligibility criteria may vary for different courses.
   Please check the specific course page for details.
""",
    }

    # Category: Courses Offered
    COURSES = {
        "keywords": [
            "course",
            "courses",
            "program",
            "programs",
            "branches",
            "engineering",
            "btech",
            "mtech",
            "bca",
            "mca",
            "bba",
            "mba",
            "degree",
            "subjects",
            "curriculum",
            "specialization",
        ],
        "response": """
╔══════════════════════════════════════════════════════════════════╗
║                 📚 COURSES OFFERED                                ║
╚══════════════════════════════════════════════════════════════════╝

🎓 UNDERGRADUATE PROGRAMS (4 Years):

   ENGINEERING (B.Tech):
   ├── Computer Science & Engineering (CSE)
   ├── Electronics & Communication (ECE)
   ├── Mechanical Engineering (ME)
   ├── Civil Engineering (CE)
   ├── Electrical Engineering (EE)
   └── Information Technology (IT)

   MANAGEMENT:
   ├── Bachelor of Business Administration (BBA)
   └── Bachelor of Computer Applications (BCA)

   SCIENCE:
   ├── B.Sc (Physics, Chemistry, Mathematics)
   └── B.Sc (Computer Science)

   COMMERCE:
   └── B.Com (Hons.)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎓 POSTGRADUATE PROGRAMS (2 Years):

   ENGINEERING:
   ├── M.Tech (CSE, ECE, ME, CE)
   └── M.Tech (Data Science, AI/ML)

   MANAGEMENT:
   ├── MBA (Finance, Marketing, HR, Operations)
   └── MBA (Business Analytics)

   SCIENCE:
   ├── M.Sc (Physics, Chemistry, Mathematics)
   └── MCA (Master of Computer Applications)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎓 DOCTORAL PROGRAMMES:
   └── Ph.D. in all major disciplines
""",
    }

    # Category: Fee Structure
    FEE = {
        "keywords": [
            "fee",
            "fees",
            "payment",
            "pay",
            "cost",
            "charge",
            "charges",
            "tuition",
            "price",
            "amount",
            "expense",
            "semester",
            "annual",
        ],
        "response": """
╔══════════════════════════════════════════════════════════════════╗
║                 💰 FEE STRUCTURE                                  ║
╚══════════════════════════════════════════════════════════════════╝

📊 TUITION FEES (Per Year):

   ┌─────────────────────────┬──────────────────┐
   │ Course                  │ Annual Fee       │
   ├─────────────────────────┼──────────────────┤
   │ B.Tech (All Branches)   │ ₹1,25,000        │
   │ BBA                     │ ₹65,000          │
   │ BCA                     │ ₹60,000          │
   │ B.Sc                    │ ₹45,000          │
   │ B.Com                   │ ₹40,000          │
   │ M.Tech                  │ ₹95,000          │
   │ MBA                     │ ₹1,50,000        │
   │ MCA                     │ ₹80,000          │
   │ M.Sc                    │ ₹50,000          │
   └─────────────────────────┴──────────────────┘

📋 OTHER FEES (One-time):
   • Admission Fee: ₹5,000
   • Registration Fee: ₹2,000
   • Security Deposit (Refundable): ₹10,000

📋 RECURRING FEES (Per Year):
   • Laboratory Fee: ₹15,000
   • Library Fee: ₹8,000
   • Examination Fee: ₹10,000
   • Student Activity Fee: ₹5,000
   • Sports Fee: ₹3,000

💳 PAYMENT OPTIONS:
   • Annual Payment (5% discount on tuition)
   • Semester-wise Payment
   • Monthly Installment (via EMI)

📌 For detailed fee breakup, visit:
   www.college.edu.in/fees
""",
    }

    # Category: Hostel Facilities
    HOSTEL = {
        "keywords": [
            "hostel",
            "hostel facility",
            "room",
            "rooms",
            "accommodation",
            "accomodation",
            "dormitory",
            "living",
            "residence",
            "mess",
            "food",
            "vegetarian",
            "non-veg",
        ],
        "response": """
╔══════════════════════════════════════════════════════════════════╗
║                 🏠 HOSTEL FACILITIES                              ║
╚══════════════════════════════════════════════════════════════════╝

🏢 HOSTEL ACCOMMODATION:

   ┌─────────────────────────┬──────────────────┐
   │ Room Type               │ Annual Fee       │
   ├─────────────────────────┼──────────────────┤
   │ Single Occupancy (AC)    │ ₹1,20,000        │
   │ Single Occupancy (Non-AC)│ ₹80,000         │
   │ Double Sharing (AC)      │ ₹90,000         │
   │ Double Sharing (Non-AC)  │ ₹60,000         │
   │ Triple Sharing (Non-AC)  │ ₹45,000         │
   └─────────────────────────┴──────────────────┘

🏡 AMENITIES PROVIDED:
   ✓ Wi-Fi enabled rooms
   ✓ 24/7 Security surveillance
   ✓ Air conditioning (in AC rooms)
   ✓ Geysers in all bathrooms
   ✓ Regular housekeeping
   ✓ Common room with TV
   ✓ Study room with computer access
   ✓ Reading room

🍽️ MESS FACILITIES:
   • Hygienic multi-cuisine food
   • North Indian & South Indian cuisine
   • Veg and Non-Veg options
   • Special diet food on medical grounds
   • Festival special meals

⚽ RECREATION:
   • Indoor games (Table Tennis, Carrom, Chess)
   • Outdoor sports facilities
   • Gymnasium access
   • Television lounge

⚠️ IMPORTANT NOTES:
   • Hostel allocation is on first-come, first-served basis
   • Apply for hostel along with admission
   • Mess fees are included in hostel fees
   • Refundable security deposit: ₹5,000
""",
    }

    # Category: Placement Details
    PLACEMENT = {
        "keywords": [
            "placement",
            "placements",
            "job",
            "jobs",
            "recruit",
            "recruitment",
            "package",
            "packages",
            "salary",
            "career",
            "interview",
            "company",
            "companies",
            "hired",
            "campus",
            "recruiting",
            "offer",
            "CTC",
        ],
        "response": """
╔══════════════════════════════════════════════════════════════════╗
║                 💼 PLACEMENT DETAILS                              ║
╚══════════════════════════════════════════════════════════════════╝

📈 PLACEMENT STATISTICS (2024-25 Batch):

   • Total Students Eligible: 850
   • Students Placed: 808 (95.1%)
   • Total Companies Visited: 350+
   • Highest Package: ₹45 LPA (Amazon)
   • Average Package: ₹8.5 LPA
   • Median Package: ₹7.2 LPA

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🏢 TOP RECRUITING COMPANIES:

   TECHNOLOGY:
   • Google, Microsoft, Amazon, Meta, Apple
   • TCS, Infosys, Wipro, HCL, Tech Mahindra
   • Adobe, Oracle, SAP, IBM

   FINANCE & BANKING:
   • HDFC Bank, ICICI Bank, Axis Bank
   • Deloitte, KPMG, PwC, EY
   • Bajaj Finance, Muthoot Finance

   CONSULTING:
   • McKinsey, BCG, Bain
   • Accenture, Capgemini

   MANUFACTURING:
   • Tata Motors, Mahindra, Maruti
   • L&T, Reliance, ONGC

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📋 PLACEMENT PROCESS:

   Step 1: Pre-Placement Talk (Company Presentation)
   Step 2: Written/Online Test
   Step 3: Technical Interview (Round 1)
   Step 4: Technical Interview (Round 2)
   Step 5: HR Interview
   Step 6: Final Selection & Offer Letter

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯 TRAINING & DEVELOPMENT:

   • Aptitude Training (6 months)
   • Technical Skill Development
   • Soft Skills & Communication
   • Mock Interviews
   • Group Discussion Practice
   • Resume Building Workshop

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📞 PLACEMENT CELL CONTACT:
   Email: placement@college.edu.in
   Phone: +91 11-XXXX YYYY
""",
    }

    # Category: Contact Information
    CONTACT = {
        "keywords": [
            "contact",
            "phone",
            "email",
            "address",
            "location",
            "office",
            "help",
            "support",
            "reach",
            "call",
            "mail",
            "enquire",
            "query",
            "helpline",
            "toll free",
        ],
        "response": """
╔══════════════════════════════════════════════════════════════════╗
║                 📞 CONTACT INFORMATION                           ║
╚══════════════════════════════════════════════════════════════════╝

🏛️ COLLEGE ADDRESS:

   Tech Valley Institute of Technology
   Academic Road, Knowledge Park
   Sector - 62, Greater Noida
   Uttar Pradesh - 201309
   India

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📱 CONTACT NUMBERS:

   Main Office:      +91 120-XXXXXXX
   Admission Desk:   +91 120-YYYYYYY
   Helpline:         1800-XXX-XXXX (Toll Free)
   WhatsApp:         +91-XXXXXXXXXX

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📧 EMAIL ADDRESSES:

   General Enquiries:    info@techvalley.edu.in
   Admissions:           admissions@techvalley.edu.in
   Academics:            academic@techvalley.edu.in
   Placements:           placement@techvalley.edu.in
   Scholarships:          scholarship@techvalley.edu.in
   Hostel:               hostel@techvalley.edu.in
   Accounts:             accounts@techvalley.edu.in

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🕐 OFFICE HOURS:

   Monday - Friday:   9:00 AM - 5:00 PM
   Saturday:          9:00 AM - 1:00 PM
   Sunday:            Closed

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🌐 WEBSITE & SOCIAL MEDIA:

   Website:     www.techvalley.edu.in
   Facebook:    facebook.com/techvalley.edu
   Twitter:     @techvalley_ed
   Instagram:   @techvalley_institute
   LinkedIn:    Tech Valley Institute
   YouTube:     Tech Valley TV

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📍 HOW TO REACH:

   🚇 Metro: Blue Line to Sector 62 Metro Station (2 km)
   🚌 Bus:    UPSRTC buses available from ISBT
   🚗 Taxi:   Available via Uber/Ola apps
   ✈️ Airport: Indira Gandhi International Airport (45 km)
""",
    }

    # Category: Scholarships
    SCHOLARSHIP = {
        "keywords": [
            "scholarship",
            "scholarships",
            "financial",
            "aid",
            "merit",
            "education loan",
            "loan",
            "bank",
            "free",
            "waiver",
            "concession",
            "government",
            "minority",
            "sc",
            "st",
            "obc",
        ],
        "response": """
╔══════════════════════════════════════════════════════════════════╗
║              🎓 SCHOLARSHIPS & FINANCIAL AID                       ║
╚══════════════════════════════════════════════════════════════════╝

🏆 INSTITUTIVE SCHOLARSHIPS (Merit-based):

   Based on Qualifying Examination Marks:
   
   ┌───────────────────────┬─────────────────────────────┐
   │ Marks Obtained         │ Tuition Fee Waiver          │
   ├───────────────────────┼─────────────────────────────┤
   │ 95% & Above            │ 75% Waiver                  │
   │ 90-94.9%               │ 50% Waiver                  │
   │ 85-89.9%               │ 25% Waiver                  │
   │ 80-84.9%               │ 10% Waiver                  │
   └───────────────────────┴─────────────────────────────┘

   *Applicable only for first year; renewal based on academic performance

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🏛️ GOVERNMENT SCHOLARSHIPS:

   • SC/ST Scholarship: As per government norms
     - Maintenance allowance: ₹1000/month (day scholar)
     - ₹2000/month (hosteller)
   
   • OBC Scholarship: 10-25% fee concession
   
   • Minority Scholarship: Up to 50% fee waiver
   
   • Physically Challenged: 25% concession

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🏦 EDUCATION LOANS:

   Banks offering education loans:
   • State Bank of India (SBI)
   • Punjab National Bank (PNB)
   • HDFC Credila
   • Axis Bank
   • ICICI Bank

   Features:
   • Loan amount: Up to ₹20 Lakhs
   • Interest rate: 8.5% - 12%
   • Moratorium period: Course duration + 1 year
   • No collateral required up to ₹7.5 Lakhs

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📝 HOW TO APPLY FOR SCHOLARSHIPS:

   1. Visit National Scholarship Portal (NSP)
   2. Register with valid credentials
   3. Fill application form
   4. Upload required documents
   5. Submit and track application status

   Portal: www.scholarships.gov.in

📞 Scholarship Cell: scholarship@college.edu.in
""",
    }

    # Category: About College
    ABOUT = {
        "keywords": [
            "about",
            "college",
            "university",
            "history",
            "established",
            "vision",
            "mission",
            "visionary",
            "founder",
            "principal",
            "director",
            "dean",
            "ranking",
            "naac",
            "nba",
            "accredited",
        ],
        "response": """
╔══════════════════════════════════════════════════════════════════╗
║                 🏛️ ABOUT THE INSTITUTION                           ║
╚══════════════════════════════════════════════════════════════════╝

📜 HISTORY & BACKGROUND:

   Tech Valley Institute of Technology was established in 1995
   with a vision to become a center of excellence in technical
   education. Starting with 4 B.Tech programs and 100 students,
   we have grown to become one of the premier engineering colleges
   in North India.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯 VISION:

   "To be a globally recognized institution that nurtures 
   innovation, creativity, and excellence in technical education,
   producing industry-ready professionals who contribute to 
   societal development."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📌 MISSION:

   • Provide quality education aligned with global standards
   • Foster research and innovation culture
   • Bridge the gap between academia and industry
   • Develop holistic professionals with ethical values
   • Promote inclusive education and diversity

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🏆 ACHIEVEMENTS & RANKINGS:

   • NAAC Accreditation: 'A' Grade (3.28/4)
   • NBA Accredited: All B.Tech Programs
   • NIRF Ranking: 87th (Engineering Category)
   • QS India Ranking: Top 150
   • ARIIA Ranking: Band 'Performer'

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

👨‍🏫 LEADERSHIP:

   Chief Patron:     Dr. R.K. Sharma (Chairman)
   Director:         Prof. A.K. Mishra, Ph.D.
   Principal:        Dr. S. Verma, Ph.D.
   Dean (Academic):  Prof. P. Kumar, Ph.D.
   Dean (Placements): Prof. R. Agarwal, Ph.D.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 AT A GLANCE:

   • Campus Area:        25+ Acres (Green Campus)
   • Total Students:     5000+
   • Faculty:           200+ (85% Ph.D. holders)
   • Departments:       12
   • Programs:          35+
   • Research Labs:     45+
   • Alumni Network:    25000+
""",
    }

    # Category: General Greetings
    GREETING = {
        "keywords": [
            "hi",
            "hello",
            "hey",
            "good morning",
            "good afternoon",
            "good evening",
            "greetings",
            "namaste",
            "howdy",
        ],
        "response": """
╭──────────────────────────────────────────────────────────────────╮
│                                                                  │
│    🙏 NAMASTE! Welcome to Tech Valley Institute!                │
│                                                                  │
│    I'm your Virtual Assistant, here to help you with all         │
│    college-related queries 24/7!                                 │
│                                                                  │
│    You can ask me about:                                         │
│                                                                  │
│    📝 Admissions      - How to apply, process, documents         │
│    ✅ Eligibility    - Qualification criteria, cutoffs            │
│    📚 Courses        - Programs offered, specializations        │
│    💰 Fees           - Fee structure, payment options            │
│    🏠 Hostel         - Accommodation, facilities, mess           │
│    💼 Placements     - Statistics, companies, packages           │
│    🎓 Scholarships   - Merit-based, government schemes           │
│    📞 Contact        - Phone, email, address, location           │
│    🏛️ About          - College history, vision, rankings         │
│                                                                  │
│    Type your question below and I'll be happy to assist! 😊     │
│                                                                  │
╰──────────────────────────────────────────────────────────────────╯
""",
    }

    # Category: Thanks
    THANKS = {
        "keywords": [
            "thank",
            "thanks",
            "thankyou",
            "thank you",
            "appreciate",
            "grateful",
        ],
        "response": """
╭──────────────────────────────────────────────────────────────────╮
│                                                                  │
│    😊 THANK YOU for connecting with us!                         │
│                                                                  │
│    It was my pleasure to assist you. If you have any more       │
│    questions, feel free to ask anytime.                          │
│                                                                  │
│    Have a great day! Best wishes for your future endeavors! 🌟 │
│                                                                  │
╰──────────────────────────────────────────────────────────────────╯
""",
    }

    # Fallback response for unrecognized queries
    FALLBACK = {
        "keywords": [],
        "response": """
╭──────────────────────────────────────────────────────────────────╮
│                                                                  │
│    🤔 Oops! I didn't quite understand that query.                │
│                                                                  │
│    Please try asking in a different way, or select from         │
│    these common topics:                                          │
│                                                                  │
│    • Admission process and how to apply                          │
│    • Eligibility criteria for various courses                   │
│    • List of courses and programs offered                        │
│    • Fee structure and payment options                           │
│    • Hostel facilities and accommodation                         │
│    • Placement statistics and recruiting companies               │
│    • Scholarship schemes and financial aid                       │
│    • Contact information and office hours                       │
│    • About the college, vision, and mission                      │
│                                                                  │
│    You can also type "menu" to see all available topics! 📋     │
│                                                                  │
╰──────────────────────────────────────────────────────────────────╯
""",
    }

    # Menu response
    MENU = {
        "keywords": [
            "menu",
            "help",
            "options",
            "list",
            "topics",
            "categories",
            "what can you do",
            "show",
        ],
        "response": """
╭──────────────────────────────────────────────────────────────────╮
│              📋 AVAILABLE TOPICS (Type or Click)                  │
╰──────────────────────────────────────────────────────────────────╯

   ┌──────────┬────────────────────────────────────────────────┐
   │ COMMAND  │ TOPIC DESCRIPTION                              │
   ├──────────┼────────────────────────────────────────────────┤
   │ admission│ Admission process, how to apply, documents      │
   │ eligibility│ Qualification criteria, minimum requirements  │
   │ courses  │ All programs and specializations offered        │
   │ fees     │ Fee structure, payment options, breakup         │
   │ hostel   │ Accommodation, rooms, mess facilities          │
   │ placement│ Placement statistics, companies, packages        │
   │ scholarship│ Scholarships, financial aid, loans             │
   │ contact  │ Phone, email, address, office hours             │
   │ about    │ College history, vision, mission, rankings      │
   │ bye      │ End conversation                                │
   └──────────┴────────────────────────────────────────────────┘

   💡 TIP: Type any of the above commands or ask naturally!
""",
    }


# =============================================================================
# RULE-BASED CHATBOT ENGINE
# =============================================================================


class CollegeEnquiryChatbot:
    """
    Rule-based chatbot that matches user input against predefined keywords
    and returns appropriate responses.
    """

    def __init__(self):
        """Initialize the chatbot with the knowledge base."""
        self.knowledge_base = KnowledgeBase()
        self.categories = [
            "ADMISSION",
            "ELIGIBILITY",
            "COURSES",
            "FEE",
            "HOSTEL",
            "PLACEMENT",
            "CONTACT",
            "SCHOLARSHIP",
            "ABOUT",
            "GREETING",
            "THANKS",
            "MENU",
        ]
        self.running = True
        self.conversation_history = []

    def preprocess_input(self, user_input):
        """
        Preprocess user input for better matching.
        - Convert to lowercase
        - Remove extra spaces
        - Handle common typos
        """
        # Convert to lowercase
        processed = user_input.lower().strip()

        # Remove extra whitespace
        processed = " ".join(processed.split())

        # Common typo corrections
        typo_fixes = {
            "admission ": "admissions ",
            "course ": "courses ",
            "placements ": "placement ",
            "scholarships ": "scholarship ",
            "contact ": "contact ",
            "admission.": "admissions.",
            "info": "information",
            "detail": "details",
            "quali": "eligibility",
            "qualif": "eligibility",
            "facilities": "facility",
            "eligibilty": "eligibility",
            "eligibiliti": "eligibility",
            "admission": "admissions",
            "fees": "fee",
            "hostel ": "hostel ",
            "contacct": "contact",
            "conatct": "contact",
        }

        for wrong, correct in typo_fixes.items():
            processed = processed.replace(wrong, correct)

        return processed

    def match_keywords(self, processed_input, category_keywords):
        """
        Match processed input against category keywords.
        Returns True if any keyword is found.
        """
        for keyword in category_keywords:
            # Use word boundary matching for better accuracy
            pattern = r"\b" + re.escape(keyword) + r"\b"
            if re.search(pattern, processed_input, re.IGNORECASE):
                return True
        return False

    def find_best_response(self, user_input):
        """
        Find the best matching response for user input.
        Uses priority-based keyword matching.
        """
        processed_input = self.preprocess_input(user_input)

        # Priority order for matching (more specific categories first)
        priority_order = [
            "MENU",
            "GREETING",
            "THANKS",
            "ADMISSION",
            "ELIGIBILITY",
            "COURSES",
            "FEE",
            "HOSTEL",
            "PLACEMENT",
            "CONTACT",
            "SCHOLARSHIP",
            "ABOUT",
        ]

        # Check each category in priority order
        for category_name in priority_order:
            category = getattr(self.knowledge_base, category_name)
            keywords = category["keywords"]

            if self.match_keywords(processed_input, keywords):
                return category["response"]

        # Return fallback if no match found
        return self.knowledge_base.FALLBACK["response"]

    def display_response(self, response):
        """Display the bot's response with formatting."""
        print(response)

    def add_to_history(self, user_input, bot_response):
        """Add conversation to history."""
        self.conversation_history.append({"user": user_input, "bot": bot_response})

    def show_welcome(self):
        """Display welcome message."""
        welcome = """
╭━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╮
║                                                                  ║
║        🎓 WELCOME TO TECH VALLEY INSTITUTE OF TECHNOLOGY         ║
║                                                                  ║
║               🤖 COLLEGE ENQUIRY CHATBOT 🤖                       ║
║                                                                  ║
║   Your 24/7 Virtual Assistant for All College-Related Queries    ║
║                                                                  ║
╰━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╯
"""
        print(welcome)
        time.sleep(0.5)
        self.display_response(self.knowledge_base.GREETING["response"])

    def run(self):
        """
        Main chatbot execution loop.
        Handles user interaction and response generation.
        """
        self.show_welcome()

        while self.running:
            try:
                # Get user input
                print("\n" + "─" * 60)
                user_input = input("👤 YOU: ").strip()

                # Handle empty input
                if not user_input:
                    print(
                        "\n🤖 BOT: Please enter a valid query. Type 'menu' for options."
                    )
                    continue

                # Check for exit commands
                if user_input.lower() in [
                    "bye",
                    "exit",
                    "quit",
                    "end",
                    "goodbye",
                    "see you",
                    "stop",
                ]:
                    goodbye = """
╭──────────────────────────────────────────────────────────────────╮
│                                                                  │
│    🙏 THANK YOU for using College Enquiry Chatbot!               │
│                                                                  │
│    We hope we could address your queries. Have a great day!     │
│    Feel free to visit us again anytime. Best wishes! 🌟         │
│                                                                  │
╰──────────────────────────────────────────────────────────────────╯
"""
                    print(goodbye)
                    self.running = False
                    break

                # Get and display response
                response = self.find_best_response(user_input)
                self.display_response("\n🤖 BOT: " + response)

                # Add to history
                self.add_to_history(user_input, response)

            except KeyboardInterrupt:
                print("\n\n⚠️ Chat session interrupted. Thank you!")
                self.running = False
                break
            except EOFError:
                print("\n\n👋 Goodbye!")
                self.running = False
                break

        # Show conversation summary
        if self.conversation_history:
            print(f"\n📊 This session had {len(self.conversation_history)} exchanges.")


# =============================================================================
# MAIN EXECUTION
# =============================================================================


def main():
    """Main function to start the chatbot."""
    print("\n" + "=" * 60)
    print("  Initializing College Enquiry Chatbot...")
    print("=" * 60 + "\n")
    time.sleep(1)

    chatbot = CollegeEnquiryChatbot()
    chatbot.run()


if __name__ == "__main__":
    main()
