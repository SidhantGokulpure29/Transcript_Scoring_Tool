# 🎤 Transcript Scoring Tool

A Streamlit application that evaluates your transcripts against a rubric.  
It provides an **overall score (0–100)** and a **per‑criterion breakdown** with transcript length.

---

## 🚀 Run Instructions

### Prerequisites
- Python 3.8+
- Git
- Streamlit

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/SidhantGokulpure29/Transcript_Scoring_Tool.git
   cd Transcript_Scoring_Tool

2. Install Dependecies
   ```bash
   pip install -r requirements.txt

3. Run the app on colab/CLI
   ```bash
   streamlit run app.py

---

## 📊 Scoring Formula

The transcript is evaluated across **eight criteria**, each contributing to the final score.  
Maximum total = **100 points**.

| Criterion       | Max Points | Description                                                                 |
|-----------------|------------|-----------------------------------------------------------------------------|
| **Salutation**  | 5          | Detects greetings like “Hello”, “Good morning”, or enthusiastic openings.   |
| **Keywords**    | 30         | Checks for required details (name, age, class, school, family, hobbies).    |
| **Flow**        | 5          | Ensures logical order: salutation → basic details → extras → closing.       |
| **Speech Rate** | 10         | Words per minute (WPM). Ideal range: 111–140 WPM.                           |
| **Grammar**     | 10         | Simple heuristics: capitalization, repetition, sentence length.             |
| **Vocabulary**  | 10         | Type‑token ratio (unique words ÷ total words).                              |
| **Clarity**     | 15         | Penalizes filler words (“um”, “uh”, “like”).                                |
| **Engagement**  | 12         | Sentiment/positivity or presence of enthusiastic words.                     |

---

### 📝 Output Format

When you evaluate a transcript, the app shows:

- **Overall Score (0–100)** with a progress bar  
- **Transcript Length (words)**  
- **Per‑criterion breakdown** as an array of objects:
  ```json
  [
    {"criterion": "Salutation", "score": 5, "words": 120},
    {"criterion": "Keywords", "score": 24, "words": 120},
    {"criterion": "Flow", "score": 5, "words": 120},
    {"criterion": "Speech Rate", "score": 10, "words": 120},
    {"criterion": "Grammar", "score": 9, "words": 120},
    {"criterion": "Vocabulary", "score": 8, "words": 120},
    {"criterion": "Clarity", "score": 12, "words": 120},
    {"criterion": "Engagement", "score": 11, "words": 120}
  ]

<img width="1477" height="756" alt="Screenshot 2025-11-24 122903" src="https://github.com/user-attachments/assets/64de3c93-f8cd-4af4-ba70-c2f3a3db94e8" />
<img width="1919" height="844" alt="image" src="https://github.com/user-attachments/assets/061e2723-d5a3-4474-b738-acd075c46ccf" />
<img width="1919" height="858" alt="image" src="https://github.com/user-attachments/assets/82a661d3-032e-4fb2-9063-0427e944522a" />
<img width="1919" height="788" alt="image" src="https://github.com/user-attachments/assets/ad36d76b-bf2d-4554-9b32-29dbe85c755e" />

