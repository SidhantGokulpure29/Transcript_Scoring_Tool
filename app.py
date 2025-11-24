
import re
import streamlit as st

FILLER_WORDS = {"um","uh","like","you know","so","actually","basically","right",
                "i mean","well","kinda","sort of","okay","hmm","ah"}

def preprocess_transcript(text: str):
    cleaned = text.lower().strip()
    cleaned = re.sub(r"\s+", " ", cleaned)
    words = cleaned.split()
    word_count = len(words)
    filler_hits = [w for w in words if w in FILLER_WORDS]
    filler_count = len(filler_hits)
    filler_rate = round((filler_count / word_count) * 100, 2) if word_count > 0 else 0
    return {"word_count": word_count, "filler_count": filler_count, "filler_rate": filler_rate}

def score_salutation(text: str):
    return (5 if "hello" in text.lower() else 0), "Salutation"

def score_keywords(text: str):
    return (10 if "name" in text.lower() else 0), "Keywords"

def score_flow(text: str):
    return 5, "Flow"

def score_speech_rate(word_count: int, duration_sec: int):
    if duration_sec <= 0: return 0,"Invalid"
    wpm = (word_count/duration_sec)*60
    return (10 if 111 <= wpm <= 140 else 6), f"{round(wpm,2)} WPM"

def score_grammar_simple(text: str):
    return 10, "Grammar"

def score_vocabulary(text: str):
    words = text.lower().split()
    if not words: return 0,"No words"
    ttr = len(set(words))/len(words)
    return (10 if ttr>0.5 else 6), f"TTR={round(ttr,2)}"

def score_clarity(prep: dict):
    return (15 if prep["filler_rate"]<=3 else 9), f"{prep['filler_rate']}% fillers"

def score_engagement(text: str):
    return 12, "Engagement"

# --- Aggregator ---
def evaluate_transcript(text: str, duration_sec: int):
    prep = preprocess_transcript(text)
    scores = {
        "Salutation": score_salutation(text)[0],
        "Keywords": score_keywords(text)[0],
        "Flow": score_flow(text)[0],
        "Speech Rate": score_speech_rate(prep["word_count"], duration_sec)[0],
        "Grammar": score_grammar_simple(text)[0],
        "Vocabulary": score_vocabulary(text)[0],
        "Clarity": score_clarity(prep)[0],
        "Engagement": score_engagement(text)[0],
    }
    total = sum(scores.values())
    overall = round((total/100)*100,2)  
    return scores, overall, prep["word_count"]

# --- Streamlit UI ---
def run_app():
    st.title("Communication Scoring Tool")
    user_text = st.text_area("Type your transcript here:", height=200)
    duration_sec = st.number_input("Enter speech duration (in seconds):", min_value=1, value=60)

    if st.button("Evaluate Transcript"):
        if user_text.strip():
            scores, overall, word_count = evaluate_transcript(user_text, duration_sec)

            st.subheader("📊 Overall Score")
            st.progress(overall/100)
            st.write(f"**Overall Score:** {overall}/100")
            st.write(f"**Transcript Length:** {word_count} words")

            st.subheader("📋 Per-Criterion Breakdown")
            breakdown = []
            for crit, val in scores.items():
                breakdown.append({"criterion": crit, "score": val, "words": word_count})
            st.json(breakdown)

        else:
            st.warning("Please enter a transcript before evaluating.")

if __name__ == "__main__":
    run_app()
