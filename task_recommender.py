import pandas as pd
import os
import sys
import logging
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Setup logging
logging.basicConfig(filename='recommender.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load mood log CSV
def load_mood_log(file_path="mood_log.csv"):
    if not os.path.exists(file_path):
        print(Fore.RED + "[❌] Mood log not found! Please run mood detection first.")
        logging.error("mood_log.csv not found.")
        sys.exit(1)

    try:
        df = pd.read_csv(file_path)
        if df.empty:
            print(Fore.RED + "[⚠️] Mood log is empty. No data to analyze.")
            logging.warning("mood_log.csv is empty.")
            sys.exit(1)

        latest_entry = df.iloc[-1]
        return latest_entry['emotion'], float(latest_entry['confidence'])

    except Exception as e:
        print(Fore.RED + f"[❌] Failed to read mood log: {e}")
        logging.exception("Error reading mood log")
        sys.exit(1)

# Mapping of moods to recommended tasks
mood_task_map = {
    "happy": "🎉 Work on a creative project or revise old topics.",
    "sad": "🧘 Take a short break or revise light material.",
    "angry": "😤 Do some breathing exercises, then review notes.",
    "surprise": "🎲 Explore a new topic or tool for fun!",
    "neutral": "📚 Continue with planned study sessions.",
    "fear": "💡 Watch a short explanatory video to reduce confusion.",
    "disgust": "😐 Clean up your workspace, then resume."
}

# Recommend task based on mood
def recommend_task(mood: str, confidence: float) -> str:
    task = mood_task_map.get(mood.lower(), "📝 Default: Revise previous material or take a break.")
    
    print(Fore.CYAN + f"\n[📊] Latest Mood Detected: {mood.capitalize()} ({confidence:.2f} confidence)")
    
    if confidence < 0.5:
        print(Fore.YELLOW + "[⚠️] Warning: Low confidence in prediction. You may want to rerun detection.")
    
    print(Fore.GREEN + f"\n[🎯 Recommended Task] → {task}")
    logging.info(f"Mood: {mood}, Confidence: {confidence:.2f}, Task: {task}")
    return task

# Main driver
if __name__ == "__main__":
    mood, confidence = load_mood_log()
    recommend_task(mood, confidence)
