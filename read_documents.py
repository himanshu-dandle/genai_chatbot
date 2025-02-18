import os
import fitz  # PyMuPDF for PDF processing
import re

# File Paths
txt_file = "hr_documents/leave_policy.txt"
pdf_file = "hr_documents/payroll_policy.pdf"

# ✅ Read Text File
def read_text_file(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    return "⚠️ No leave policy found."

# ✅ Read PDF File
def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        with fitz.open(pdf_path) as doc:
            for page in doc:
                text += page.get_text() + "\n"
    except Exception as e:
        return f"Error reading PDF: {e}"
    return text

# ✅ Clean Text: Remove unnecessary blank lines & headers
def clean_text(text):
    lines = text.split("\n")
    filtered_lines = [line.strip() for line in lines if len(line.strip()) > 3]  # Keep non-empty lines
    cleaned_text = " ".join(filtered_lines)  # Convert to a single string

    # Remove headers like "Company Leave Policy" and "Payroll Policy"
    cleaned_text = re.sub(r"\b(Company Leave Policy|Payroll Policy)\b", "", cleaned_text, flags=re.IGNORECASE)

    return cleaned_text

# ✅ Search for the most relevant policy sentence
def search_policy_documents(key_phrases):
    raw_leave_text = read_text_file(txt_file)
    raw_payroll_text = extract_text_from_pdf(pdf_file)

    leave_policy_text = clean_text(raw_leave_text)
    payroll_policy_text = clean_text(raw_payroll_text)
    combined_text = leave_policy_text + " " + payroll_policy_text

    # 🔍 Debugging: Print extracted full text
    print("\n📄 DEBUG: Extracted HR Policy Text →", combined_text, "\n")

    # Split text into proper sentences
    sentences = re.split(r'(?<=[.!?])\s+', combined_text)

    best_match = None
    highest_match_count = 0  # Track highest number of matching words

    # Step 1: **Find the sentence with the most exact word matches**
    for sentence in sentences:
        match_count = sum(1 for phrase in key_phrases if phrase.lower() in sentence.lower())

        if match_count > highest_match_count:
            best_match = sentence.strip()
            highest_match_count = match_count  # Update best match

    print("\n🔍 Best Matching Sentence Found:", best_match)

    if best_match:
        return f"📄 Found in policy: {best_match}"
    else:
        return "⚠️ No relevant policy found."

# ✅ Test the search function
if __name__ == "__main__":
    test_phrases = ["sick leave", "paid leave", "policy"]  # Replace with extracted key phrases
    result = search_policy_documents(test_phrases)
    print("\n🔍 Final Output:", result)
