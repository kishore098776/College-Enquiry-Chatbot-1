# Rule-Based College Enquiry Chatbot - Specification

## 1. Project Overview

**Project Name:** Jansons Institute of Technology - Smart Enquiry Chatbot  
**Type:** Rule-Based Chatbot (Web Application)  
**Core Functionality:** An intelligent chatbot with advanced fee structure system, location map, and faculty directory. Uses keyword matching to respond to student queries about college admissions, courses, fees, placements, hostel, scholarships, and contact information.  
**Target Users:** Prospective students, parents, and visitors seeking information about Jansons Institute of Technology.

---

## 2. UI/UX Specification

### Layout Structure

**Page Sections:**
- Header: College name with subtitle
- Chat Container: Message display with conversation history
- Quick Action Buttons: 8 predefined query categories
- Input Area: Text input field with send button

**Responsive Breakpoints:**
- Mobile: < 640px (full-width, 2-column quick buttons)
- Desktop: > 640px (4-column quick buttons, max-width 900px)

### Visual Design

**Color Palette:**
- Primary: `#1E3A5F` (Deep Navy Blue)
- Secondary: `#2D5A87` (Medium Blue)
- Accent: `#E8B931` (Gold)
- Accent Light: `#f5d77a` (Light Gold)
- Success: `#10B981` (Green)
- Background: `#F0F4F8` (Light Gray)
- White: `#FFFFFF`
- Text Primary: `#1A1A2E`
- Text Secondary: `#64748B`

**Typography:**
- Font Family: `'Inter', sans-serif`
- Headings: 700-800 weight
- Body: 400-500 weight
- Chat messages: 0.95rem

**Spacing:**
- Container padding: 24px
- Message gap: 16px
- Border radius: 16px (bubbles), 12px (buttons), 20px (container)

**Effects:**
- Box shadow: `0 10px 40px rgba(30, 58, 95, 0.15)`
- Hover transitions: 0.3s ease
- Message slide-in animation: 0.4s cubic-bezier
- Typing indicator: 3 bouncing dots

### Components

**Chat Header:**
- Gradient background (primary to secondary)
- Avatar with border
- Online status indicator with pulse animation

**Message Bubbles:**
- Bot: White background, rounded corners, shadow
- User: Gradient background (primary to secondary), white text
- Avatar: Circular with initials/icons

**Quick Action Buttons:**
- 4-column grid (desktop), 2-column (mobile)
- Icon + text format
- Hover: border highlight, lift effect, shadow

**Fee Structure Cards:**
- Course fee table with gradient header
- Total sections with contrasting backgrounds
- Highlighted totals

**Map Container:**
- Embedded Google Maps iframe
- "View on Map" button with accent color

**Faculty Cards:**
- Grid layout (2 columns)
- Circular avatar with initials
- Name and designation

---

## 3. Functionality Specification

### 3.1 Knowledge Categories

| Category | Keywords | Response |
|----------|----------|----------|
| **Admissions** | admission, apply, eligibility, register | Process steps, eligibility criteria |
| **Courses** | course, program, branches, btech, engineering | List of courses offered |
| **Fee Structure** | fee, fees, payment, cost, structure | Interactive fee calculator |
| **Placements** | placement, job, package, salary, company | Statistics and recruiters |
| **Hostel** | hostel, room, accommodation, mess | Facilities and fees |
| **Scholarships** | scholarship, financial, aid, merit | Scholarship schemes |
| **Location** | location, map, address, directions | Embedded map + button |
| **Faculty** | faculty, staff, professor, hod | Staff directory |
| **General** | hi, hello, help, about | Welcome message |

### 3.2 Fee Structure System

**Interactive Flow:**
1. User asks about fees → Bot shows Hosteller/Day Scholar selection
2. **Hosteller Path:**
   - Shows table with College Fees + Hostel Fees
   - Displays 4-year summary with totals highlighted
   - Fixed hostel fee: ₹85,000/year
3. **Day Scholar Path:**
   - Prompts for distance input (km)
   - Calculates transport: ₹5,000 base + ₹15/km
   - Shows table with College Fees + Transport Fees
   - Displays 4-year summary separately

**Course-specific College Fees:**
| Course | Annual Fee |
|--------|-----------|
| CSE | ₹1,25,000 |
| IT | ₹1,15,000 |
| ECE | ₹1,10,000 |
| EEE | ₹1,05,000 |
| Mechanical | ₹1,00,000 |
| Civil | ₹95,000 |

### 3.3 Location Feature

- **College:** Jansons Institute of Technology (Autonomous)
- **Coordinates:** 11.1152089, 77.1880571
- **Embedded Map:** Google Maps iframe
- **View Button:** Opens in new tab

### 3.4 Faculty Directory

**Department Heads:**
- Dr. R. Kumar - HOD Computer Science
- Dr. P. Senthil - HOD Electronics & Comm
- Dr. M. Venkatesh - HOD Mechanical Eng.
- Dr. A. Jayakumar - HOD Civil Engineering

**Administrative Staff:**
- Ms. Priya R. - Admission Officer
- Mr. Suresh K. - Chief Warden (Boys)
- Ms. Lakshmi M. - Chief Warden (Girls)
- Mr. R. Gandhi - Placement Officer

### 3.5 Response Logic

- Keyword matching with priority order
- Case-insensitive matching
- Partial word matching
- Graceful fallback for unrecognized queries

---

## 4. Acceptance Criteria

- [x] Modern, professional chat interface loads correctly
- [x] User can type messages and receive responses
- [x] Keyword matching identifies query categories
- [x] Quick action buttons work correctly
- [x] Bot shows typing indicator before responding
- [x] Fee structure shows Hosteller/Day Scholar options
- [x] Day Scholar prompts for distance input
- [x] Transport fee calculated based on distance
- [x] 4-year fee table displays correctly
- [x] Total sections highlighted prominently
- [x] Google Maps embedded with View button
- [x] Faculty directory displays with avatars
- [x] Smooth animations on interactions
- [x] Responsive design works on all devices
- [x] All labels use bold formatting
- [x] Professional, student-friendly appearance

---

## 5. Technical Implementation

**Technology Stack:**
- HTML5, CSS3, JavaScript (Vanilla)
- Google Fonts (Inter)
- Google Maps Embed API

**Key Features:**
- No external dependencies (framework-free)
- Smooth CSS animations
- Interactive fee calculator
- Responsive grid layouts
- Message history scroll
- Real-time typing indicator
