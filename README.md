# MakeMyList

**MakeMyList** is a modern, AI-powered event logistics and budget planner that transforms natural language event prompts (e.g., *"Arranging a house party for 6 people, keep budget under ₹2000"*) into complete, categorized event checklists with precise quantities and local Indian market price estimates (INR) in seconds.

Built with a focus on polished user experience, it features a sleek LLM-style prompt bar, an interactive Google-like loading state, and structural JSON response parsing powered by the latest **Gemini 2.5 Flash** model.

---

## Key Features

*   **Natural Language Planner:** Describe any event, attendee count, budget constraints, or theme, and the AI does the heavy lifting.
*   **Structured Output Engine:** Enforces strict Pydantic schemas using the modern `google-genai` SDK to guarantee robust, valid JSON response validation every single time.
*   **Premium LLM-Inspired UI:** A clean, horizontal search layout with a floating send action button mirroring ChatGPT and Gemini interfaces.
*   **Dynamic Interactive Loader:** Features a smooth cross-fading status message sequence (e.g., *Analyzing details...*, *Calculating quantities...*) and a Google-style animated progress bar to keep users engaged during generation.
*   **At-a-Glance Summaries:** Highlights overall item counts and total budget estimates dynamically calculated in Indian Rupees (₹).
*   **Responsive Glassmorphic Design:** Fully mobile-responsive layout utilizing modern CSS variables, harmonious HSL colors, micro-interactions, and hover-triggered grid card overlays.

---

## Tech Stack

*   **Backend:** Python 3.10+ / Flask (WSGI)
*   **AI Engine:** Gemini 2.5 Flash (`google-genai` SDK)
*   **Data Validation:** Pydantic v2
*   **Frontend:** HTML5 / CSS3 (Custom grid, Flexbox layouts, micro-animations)
*   **Deployment:** Vercel Serverless Functions

---

## Local Installation & Setup

Follow these steps to run the application locally on your machine.

### 1. Clone the Repository
```bash
git clone https://github.com/vihansr/MakeMyList.git
cd MakeMyList
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
# On Windows (PowerShell):
.\venv\Scripts\Activate.ps1
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a file named `.env` in the root directory:
```env
GEMINI_API_KEY=your_gemini_api_key_here
```

### 5. Run the Local Server
```bash
python app.py
```
Open your browser and navigate to `http://127.0.0.1:5000`.

---

## Deployment on Vercel

This repository is pre-configured for instant serverless deployment on Vercel using `vercel.json`.

1. Import your GitHub repository into [Vercel](https://vercel.com).
2. Under **Project Settings > Environment Variables**, add your `GEMINI_API_KEY`.
3. Click **Deploy**. Vercel will install the requirements and deploy the project to a serverless Python runtime.

---

## Project Architecture

```plaintext
├── app.py                  # Main Flask web application & router
├── main.py                 # Gemini Client, System Prompt, and Pydantic schemas
├── requirements.txt        # Python dependency manifest
├── vercel.json             # Vercel serverless routing configuration
├── .gitignore              # Ignored cache, keys, and temporary files
├── static/
│   └── style.css           # Premium responsive styles, variables, & animations
└── templates/
    └── index.html          # Clean structure with dynamic status script
```
