AI NEWS SUMMARIZER

An ML-powered news article summarizer application in Python which is available in GUI version. It lets the user paste or enter raw links or text of a news article. The app generates a summary of what is being read using a transformer model, and has the ability to read the summary or save it to a file.

FEATURES
- Summarization of News Articles from URL
  
- Condense user-pasted news summaries
  
- Save the summary as a. txt file
  
- Read Listen to summaryciThe summary cited.EventTypeCOVID-19COVID-19 in immune neglected diseasesCOVID-19 in immune neglected diseasesSummaryThe COVID-19 pandemic has taken an immense and tragic human toll.
  
- Graphical interface with Tkinter easy to use.

REQUIREMENTS
Python 3.7 or higher
Install the dependencies with pip install -r requirements.txt.
pip install torch torchvision torchaudio --index url https://download.pytorch.org/whl/cpu
pip install transformers newspaper3k pyttsx3

USAGE
-----
1. Run the script:
   python news_summarizer.py
2. You have two input options:
   - Enter a **news article URL** in the top entry box, OR
   - Paste **text content** into the large text box below.
3. Click **"Summarize"** to generate the summary.
4. Use:
   - **"Save Summary"** to store the summary as a `.txt` file.
   - **"Read Aloud"** to hear the summary using your system's speaker.

FILES
-----
- `news_summarizer.py` — Main application script  
- `summary_YYYYMMDD_HHMMSS.txt` — Saved summaries with timestamps

NOTES
-----
- Internet connection is required to fetch articles from URLs.
- Make sure the article URL is publicly accessible.
- The summarizer uses the `facebook/bart-large-cnn` model from Hugging Face.


LICENSE
-------
This project is free to use for educational and non-commercial purposes.
