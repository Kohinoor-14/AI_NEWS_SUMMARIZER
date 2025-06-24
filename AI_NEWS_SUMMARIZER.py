import tkinter as tk
from tkinter import messagebox, filedialog
from transformers import pipeline
from newspaper import Article
import pyttsx3
import datetime

summarizer = pipeline("summarization",model="facebook/bart-large-cnn")

engine = pyttsx3.init()

def summarize_text(text, min_len=30,max_len=130):
    summary = summarizer(text, max_length=max_len, min_length=min_len, do_sample=False)
    return summary[0]['summary_text']

def fetch_article(url):
    article = Article(url)
    article.download()
    article.parse()
    return article.text

def save_summary_to_file(summary):
    filename = f"summary_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename,'w', encoding='utf-8') as f:
        f.write(summary)
    messagebox.showinfo("Saved", f"Summary saves as {filename}")

def read_summary(summary):
    engine.say(summary)
    engine.runAndWait()

def handle_summarize():
    input_text = input_box.get("1.0", tk.END).strip()
    url_text = url_entry.get().strip() 

    if url_text:
        try:
            input_text = fetch_article(url_text)
        except Exception as e:
            messagebox.showerror("Error",f"could not fetch article: {e}")
            return
    
    if not input_text:
        messagebox.showwarning("Warning","please enter news text or a valid URL.")
        return 
    
    try :
        summary = summarize_text(input_text)
        summary_box.delete("1.0", tk.END)
        summary_box.insert(tk.END, summary)
    except Exception as e:
        messagebox.showerror("Error", f"summarization failed: {e}")

def handle_save():
        summary = summary_box.get("1.0",tk.END).strip()
        if summary:
            save_summary_to_file(summary)
        else:
            messagebox.showwarning("warning","No summary to save.")

def handle_speak():
        summary = summary_box.get("1.0", tk.END).strip()
        if summary:
            read_summary(summary)
        else:
            messagebox.showwarning("warning","No summary to read aloud.")

root = tk.Tk()
root.title("AI News Summarizer")

tk.Label(root, text="Enter News URL (optional):").pack(pady=5)
url_entry = tk.Entry(root, width=80)
url_entry.pack()

tk.Label(root, text="Or Paste News Text Below:").pack(pady=5)
input_box = tk.Text(root, height=10, width=100)
input_box.pack()

tk.Button(root, text="Summarize", command=handle_summarize).pack(pady=10)

tk.Label(root, text="Summary:").pack()
summary_box = tk.Text(root, height=10, width=100)
summary_box.pack()

button_frame = tk.Frame(root)
button_frame.pack(pady=5)

tk.Button(button_frame, text="Save Summary", command=handle_save).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Read Aloud", command= handle_speak).grid(row=0, column=1, padx=5)

root.mainloop()
