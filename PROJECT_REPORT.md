# RULE-BASED COLLEGE ENQUIRY CHATBOT
## Mini Project Report

---

## 1. INTRODUCTION

### 1.1 Project Title
**Rule-Based College Enquiry Chatbot**

### 1.2 Project Type
Desktop Application (Console-based Python Application)

### 1.3 Problem Statement
Many students and parents face difficulty in getting accurate and quick information about college admissions, courses, fee structure, eligibility criteria, placement details, and campus facilities. They often need to visit the college website, call the administration office, or physically visit the campus to clarify their doubts. This process consumes time, creates delays, and increases the workload of administrative staff.

### 1.4 Solution Overview
This project implements a Rule-Based College Enquiry Chatbot that provides instant, automated responses to frequently asked questions using keyword matching techniques. The chatbot is available 24/7 and provides quick, accurate information through a simple chat interface.

---

## 2. SYSTEM ARCHITECTURE

### 2.1 High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                     USER INTERFACE LAYER                        │
│                   (Console/Command Line)                        │
└─────────────────────────┬───────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────────┐
│                    CHATBOT ENGINE LAYER                          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐         │
│  │   Input      │  │   Response   │  │   Session    │         │
│  │   Handler    │──▶│   Generator  │──▶│   Manager    │         │
│  └──────────────┘  └──────────────┘  └──────────────┘         │
└─────────────────────────┬───────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────────┐
│                    KNOWLEDGE BASE LAYER                         │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  Categories:                                             │   │
│  │  • Admissions          • Courses                         │   │
│  │  • Eligibility         • Fee Structure                   │   │
│  │  • Hostel Facilities   • Placements                     │   │
│  │  • Scholarships         • Contact Information            │   │
│  │  • About College        • Greetings                       │   │
│  └──────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

### 2.2 System Components

| Component | Description | Function |
|-----------|-------------|----------|
| **Input Handler** | Processes user messages | Receives input, handles empty/invalid cases |
| **Preprocessor** | Normalizes input text | Lowercase conversion, typo correction |
| **Keyword Matcher** | Matches input against rules | Regex-based pattern matching |
| **Response Selector** | Selects appropriate response | Priority-based category selection |
| **Knowledge Base** | Stores all Q&A data | Predefined responses for each category |
| **Session Manager** | Handles conversation flow | Tracks history, manages state |

### 2.3 Data Flow

```
User Input → Preprocessing → Keyword Matching → Category Selection → Response Output
    │              │                │                │                │
    ▼              ▼                ▼                ▼                ▼
"admission    "admission    [admission]       ADMISSION       Fee details
 query"        query"        keywords           category        displayed"
```

---

## 3. ALGORITHM STEPS

### 3.1 Main Algorithm

```
BEGIN
    Initialize Knowledge Base with all categories
    Display Welcome Message
    
    WHILE user wants to continue DO
        GET user_input
        IF user_input is empty THEN
            DISPLAY "Please enter valid query"
            CONTINUE
        END IF
        
        IF user_input is exit command THEN
            DISPLAY Goodbye Message
            EXIT LOOP
        END IF
        
        processed_input = preprocess(user_input)
        response = find_best_match(processed_input)
        DISPLAY response
        ADD to conversation history
    END WHILE
    
    DISPLAY session summary
END
```

### 3.2 Preprocessing Algorithm

```
FUNCTION preprocess(input_text)
    // Step 1: Convert to lowercase
    processed = lowercase(input_text)
    
    // Step 2: Remove extra whitespace
    processed = normalize_whitespace(processed)
    
    // Step 3: Fix common typos
    FOR each (typo, correction) in typo_dictionary
        processed = replace(typo, correction)
    END FOR
    
    RETURN processed
END FUNCTION
```

### 3.3 Keyword Matching Algorithm

```
FUNCTION find_best_match(processed_input)
    // Define priority order
    priority_order = [
        "MENU", "GREETING", "THANKS", "ADMISSION", "ELIGIBILITY",
        "COURSES", "FEE", "HOSTEL", "PLACEMENT", "CONTACT",
        "SCHOLARSHIP", "ABOUT"
    ]
    
    // Search in priority order
    FOR each category in priority_order
        keywords = get_keywords(category)
        
        FOR each keyword in keywords
            IF keyword_found_in_input(keyword, processed_input) THEN
                RETURN get_response(category)
            END IF
        END FOR
    END FOR
    
    // No match found
    RETURN fallback_response
END FUNCTION
```

### 3.4 Keyword Matching Detail

```
FUNCTION keyword_found_in_input(keyword, input_text)
    // Create regex pattern with word boundaries
    pattern = "\b" + escape_regex(keyword) + "\b"
    
    // Case-insensitive search
    IF regex_search(pattern, input_text, IGNORECASE) THEN
        RETURN TRUE
    ELSE
        RETURN FALSE
    END IF
END FUNCTION
```

---

## 4. FLOWCHART

```
┌─────────────────────────────────────────────────────────────────┐
│                          START                                   │
│                            │                                     │
│                            ▼                                     │
│    ┌─────────────────────────────────────────────────┐           │
│    │         Display Welcome Message                 │           │
│    └─────────────────────────────────────────────────┘           │
│                            │                                     │
│                            ▼                                     │
│    ┌─────────────────────────────────────────────────┐           │
│    │          Initialize Knowledge Base               │           │
│    └─────────────────────────────────────────────────┘           │
│                            │                                     │
│                            ▼                                     │
│                     ┌────────────┐                              │
│                     │  Get User  │                              │
│                     │   Input    │                              │
│                     └─────┬──────┘                              │
│                           │                                      │
│                           ▼                                      │
│               ┌───────────────────────┐                         │
│               │  Input Empty?         │                         │
│               └───────────┬───────────┘                         │
│                    Yes     │     No                             │
│                    ┌───────┴───────┐                            │
│                    ▼               ▼                            │
│           ┌────────────┐    ┌──────────────────┐               │
│           │ Display    │    │ Preprocess Input  │               │
│           │ Error Msg  │    │ (Lowercase, Fix   │               │
│           └─────┬──────┘    │  Typos, Trim)    │               │
│                 │           └────────┬─────────┘               │
│                 │                    │                          │
│                 └──────────┬─────────┘                          │
│                            │                                    │
│                            ▼                                    │
│               ┌───────────────────────┐                         │
│               │  Is Exit Command?     │                         │
│               │  (bye, quit, exit)     │                         │
│               └───────────┬───────────┘                         │
│                    Yes     │     No                             │
│                    ┌───────┴───────┐                            │
│                    ▼               ▼                            │
│           ┌────────────┐    ┌──────────────────┐               │
│           │  Display   │    │ Search Knowledge  │               │
│           │  Goodbye   │    │ Base (Priority    │               │
│           │  Message   │    │ Order Match)      │               │
│           └─────┬──────┘    └────────┬─────────┘               │
│                 │                   │                          │
│                 │            ┌──────┴──────┐                   │
│                 │            │  Match      │                   │
│                 │            │  Found?     │                   │
│                 │            └──────┬──────┘                   │
│                 │             Yes   │    No                   │
│                 │             ┌─────┴─────┐                  │
│                 │             ▼           ▼                   │
│                 │      ┌───────────┐ ┌──────────────┐          │
│                 │      │ Get Match │ │ Get Fallback │          │
│                 │      │ Response  │ │  Response    │          │
│                 │      └─────┬─────┘ └──────┬───────┘          │
│                 │            │              │                  │
│                 │            └──────┬───────┘                  │
│                 │                   │                          │
│                 │                   ▼                          │
│                 │         ┌──────────────────┐                │
│                 │         │  Display Response │                │
│                 │         └──────────────────┘                │
│                 │                   │                          │
│                 │                   ▼                          │
│                 │         ┌──────────────────┐                │
│                 │         │  Add to History   │                │
│                 │         └──────────────────┘                │
│                 │                   │                          │
│                 │                   ▼                          │
│                 │            ┌────────────┐                    │
│                 └───────────▶│    END     │                    │
│                                └────────────┘                    │
└─────────────────────────────────────────────────────────────────┘
```

---

## 5. FEATURES & FUNCTIONALITY

### 5.1 Supported Query Categories

| Category | Sample Queries | Response Content |
|----------|----------------|------------------|
| **Admissions** | "How to apply?", "Admission process" | Application steps, documents required, important dates |
| **Eligibility** | "Am I eligible?", "Minimum criteria" | Qualification requirements, percentage criteria |
| **Courses** | "What courses?", "B.Tech programs" | List of all programs, specializations |
| **Fees** | "Fee structure?", "How much to pay?" | Detailed fee breakdown, payment options |
| **Hostel** | "Hostel facility?", "Room available?" | Accommodation types, amenities, mess details |
| **Placements** | "Placement statistics?", "Companies visiting" | Package details, recruiting companies, process |
| **Scholarships** | "Scholarship?", "Financial aid" | Merit-based, government schemes, education loans |
| **Contact** | "Phone number?", "Email address" | Full contact details, office hours, map |
| **About** | "About college?", "History" | College background, vision, mission, rankings |
| **Menu** | "What can you do?", "Help" | List of all available commands |

### 5.2 Input Processing Features

- **Case Insensitivity**: "ADMISSION" = "admission" = "Admission"
- **Whitespace Normalization**: Multiple spaces/tabs converted to single space
- **Typo Correction**: Common spelling mistakes automatically corrected
- **Partial Matching**: Keywords like "adm" match "admission"
- **Word Boundary Matching**: Prevents false matches within words

### 5.3 Response Features

- **Formatted Output**: ASCII art boxes for professional appearance
- **Comprehensive Information**: Detailed responses with all relevant data
- **Error Handling**: Graceful fallback for unrecognized queries
- **Session Tracking**: Conversation history maintained

---

## 6. SAMPLE CONVERSATION

### 6.1 Example Session 1: Admission Query

```
╭━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╮
║        🎓 WELCOME TO TECH VALLEY INSTITUTE OF TECHNOLOGY         ║
║               🤖 COLLEGE ENQUIRY CHATBOT 🤖                       ║
╰━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╯

👋 NAMASTE! Welcome to Tech Valley Institute!
I'm your Virtual Assistant, here to help you with all
college-related queries 24/7!

──────────────────────────────────────────────────────────────

👤 YOU: Hi, I want to know about admissions

🤖 BOT: 
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

──────────────────────────────────────────────────────────────

👤 YOU: What is the eligibility for B.Tech?

🤖 BOT:
╔══════════════════════════════════════════════════════════════════╗
║               ✅ ELIGIBILITY CRITERIA                             ║
╚══════════════════════════════════════════════════════════════════╝

📗 UNDERGRADUATE COURSES (B.Tech, BBA, BCA, etc.):
   • Must have passed 10+2 from a recognized board
   • Minimum 60% aggregate marks (50% for SC/ST)
   • Physics, Chemistry, Mathematics mandatory for B.Tech
   • Valid JEE Main score for B.Tech admission

──────────────────────────────────────────────────────────────

👤 YOU: Thank you!

🤖 BOT:
╭──────────────────────────────────────────────────────────────────╮
│    😊 THANK YOU for connecting with us!                         │
│    It was my pleasure to assist you. Best wishes! 🌟            │
╰──────────────────────────────────────────────────────────────────╯
```

### 6.2 Example Session 2: Fee and Placement Query

```
──────────────────────────────────────────────────────────────

👤 YOU: What are the fees for MBA?

🤖 BOT:
╔══════════════════════════════════════════════════════════════════╗
║                 💰 FEE STRUCTURE                                  ║
╚══════════════════════════════════════════════════════════════════╝

📊 TUITION FEES (Per Year):
   ┌─────────────────────────┬──────────────────┐
   │ Course                  │ Annual Fee       │
   ├─────────────────────────┼──────────────────┤
   │ B.Tech (All Branches)   │ ₹1,25,000        │
   │ MBA                     │ ₹1,50,000        │
   │ MCA                     │ ₹80,000          │
   └─────────────────────────┴──────────────────┘

💳 PAYMENT OPTIONS:
   • Annual Payment (5% discount on tuition)
   • Semester-wise Payment
   • Monthly Installment (via EMI)

──────────────────────────────────────────────────────────────

👤 YOU: Tell me about placements

🤖 BOT:
╔══════════════════════════════════════════════════════════════════╗
║                 💼 PLACEMENT DETAILS                              ║
╚══════════════════════════════════════════════════════════════════╝

📈 PLACEMENT STATISTICS (2024-25 Batch):
   • Total Students Placed: 808 (95.1%)
   • Highest Package: ₹45 LPA (Amazon)
   • Average Package: ₹8.5 LPA

🏢 TOP RECRUITING COMPANIES:
   Google, Microsoft, Amazon, TCS, Infosys, Wipro

──────────────────────────────────────────────────────────────

👤 YOU: bye

🤖 BOT:
╭──────────────────────────────────────────────────────────────────╮
│    🙏 THANK YOU for using College Enquiry Chatbot!               │
│    Feel free to visit us again anytime. Best wishes! 🌟         │
╰──────────────────────────────────────────────────────────────────╯

📊 This session had 5 exchanges.
```

---

## 7. ADVANTAGES & LIMITATIONS

### 7.1 Advantages

| Advantage | Description |
|-----------|-------------|
| **24/7 Availability** | Chatbot can serve users at any time, day or night |
| **Instant Responses** | Eliminates waiting time for manual responses |
| **Consistency** | Provides uniform information to all users |
| **Cost-Effective** | Reduces workload on administrative staff |
| **Scalability** | Can handle unlimited simultaneous queries |
| **No Human Error** | Responses are accurate and error-free |
| **Easy to Use** | Simple conversational interface |
| **Multilingual Support** | Can be extended to support multiple languages |
| **Data Collection** | Can log queries for analysis and improvement |
| **Beginner-Friendly** | Simple rule-based logic, easy to understand |

### 7.2 Limitations

| Limitation | Description | Mitigation |
|------------|-------------|------------|
| **Fixed Responses** | Can only respond to predefined queries | Expand knowledge base regularly |
| **No Understanding** | Cannot understand context or nuance | Implement context awareness |
| **Keyword Dependency** | May fail with synonyms or variations | Use NLP techniques |
| **No Learning** | Cannot learn from interactions | Implement ML-based improvements |
| **Single-turn Focus** | Limited multi-turn conversation | Add conversation state management |
| **No Personalization** | Cannot customize for individual users | Implement user profile tracking |
| **Spelling Sensitivity** | May fail with typos (though typos are handled) | Implement fuzzy matching |

---

## 8. FUTURE ENHANCEMENTS

### 8.1 Short-term Enhancements

1. **GUI Interface**: Develop a web-based or desktop GUI for better user experience
2. **Voice Support**: Add speech-to-text and text-to-speech capabilities
3. **Expanded Knowledge Base**: Add more colleges, courses, and detailed information
4. **Conversation History**: Allow users to save and review past conversations
5. **Feedback System**: Add satisfaction rating for responses

### 8.2 Medium-term Enhancements

1. **Natural Language Processing (NLP)**: Implement intent recognition and entity extraction
2. **Machine Learning Integration**: Train models to improve response accuracy
3. **Multi-language Support**: Add Hindi and regional language support
4. **Integration with College Portal**: Connect with official website for real-time data
5. **WhatsApp/Social Media Bot**: Deploy on messaging platforms

### 8.3 Long-term Enhancements

1. **Conversational AI**: Implement context-aware multi-turn conversations
2. **Personalized Recommendations**: Suggest courses based on student profile
3. **Sentiment Analysis**: Detect user frustration and escalate to humans
4. **Analytics Dashboard**: Admin panel for query analysis and insights
5. **Chatbot-as-a-Service**: Make it a platform for multiple institutions

---

## 9. TECHNICAL SPECIFICATIONS

### 9.1 Technology Stack

| Component | Technology |
|-----------|------------|
| **Language** | Python 3.x |
| **Approach** | Rule-Based (Keyword Matching) |
| **Pattern Matching** | Regular Expressions (re module) |
| **Interface** | Console/Command Line |

### 9.2 System Requirements

- **Python Version**: 3.6 or higher
- **RAM**: 256 MB minimum
- **Storage**: 10 MB
- **OS**: Windows, Linux, macOS

### 9.3 Code Structure

```
chatbot.py
├── KnowledgeBase Class
│   ├── ADMISSION (keywords + response)
│   ├── ELIGIBILITY (keywords + response)
│   ├── COURSES (keywords + response)
│   ├── FEE (keywords + response)
│   ├── HOSTEL (keywords + response)
│   ├── PLACEMENT (keywords + response)
│   ├── CONTACT (keywords + response)
│   ├── SCHOLARSHIP (keywords + response)
│   ├── ABOUT (keywords + response)
│   ├── GREETING (keywords + response)
│   ├── THANKS (keywords + response)
│   ├── MENU (keywords + response)
│   └── FALLBACK (response)
│
└── CollegeEnquiryChatbot Class
    ├── __init__() - Initialize chatbot
    ├── preprocess_input() - Clean user input
    ├── match_keywords() - Check keyword presence
    ├── find_best_response() - Select response
    ├── display_response() - Format output
    ├── add_to_history() - Track conversation
    ├── show_welcome() - Welcome message
    └── run() - Main execution loop
```

---

## 10. CONCLUSION

The Rule-Based College Enquiry Chatbot successfully demonstrates how simple keyword matching techniques can be used to create a functional and useful chatbot application. The project fulfills its objective of providing instant, accurate information about college-related queries.

### Key Takeaways:

1. **Simplicity**: Rule-based approaches are easy to implement and understand
2. **Effectiveness**: Can handle majority of common queries effectively
3. **Maintainability**: Easy to add/modify responses without changing code structure
4. **Foundation**: Provides a solid base for more advanced AI chatbot implementations

### Project Learning Outcomes:

- Understanding of chatbot architecture and components
- Implementation of keyword matching algorithms
- Knowledge base design and organization
- String processing and pattern matching
- User interface design for conversational systems

---

## APPENDIX: RUNNING THE CHATBOT

### How to Run

1. **Install Python** (if not already installed)
   ```
   Download from: https://www.python.org/downloads/
   ```

2. **Save the chatbot file** as `chatbot.py`

3. **Run the chatbot**:
   ```
   python chatbot.py
   ```

4. **Interact** by typing queries or using commands:
   - Type natural questions: "What is admission process?"
   - Use keywords: "admission", "fees", "placements"
   - Use command: "menu" to see all options
   - Type "bye" to exit

---

**Project Submitted By:** [Your Name]  
**Date:** [Submission Date]  
**Guide:** [Professor Name]

---
