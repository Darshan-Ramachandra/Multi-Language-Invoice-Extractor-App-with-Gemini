
# Multi-Language Invoice Extractor App with Gemini 🧾🌍

## Overview 🔍  
A powerful image-based invoice parsing app that uses **Google Gemini** to intelligently extract and analyze key information from invoices — even those written in **multiple languages** like Hindi. Built using **Streamlit** for an intuitive web interface and **Gemini 1.5 Flash** for high-performance language and vision capabilities.

## Features ✨

- **Multi-Language Invoice Analysis**
  - Upload invoices in different languages (e.g., Hindi, English,spanish,etc.,).
  - Extract billing information, item details, prices, taxes, and more.

- **Vision + Language AI (Gemini)**
  - Uses Gemini 1.5 Flash model(or choose any new latest model) to analyze both text and visual content.

- **Streamlit Frontend**
  - Simple, interactive UI for uploading invoice images and querying details.

- **Prompt Engineering**
  - Predefined prompts to assist Gemini in understanding invoice structure.

## Technologies Used

| Technology             | Description                                                                   |
|------------------------|-------------------------------------------------------------------------------|
| **Streamlit**          | Interactive Python framework for web apps.                                   |
| **Google Gemini API**  | Vision-language model for image understanding and natural language response. |
| **Pillow (PIL)**       | For handling uploaded images.                                                 |
| **Python (dotenv)**    | Manages environment variables securely.                                       |

## Setup Instructions 🔧

### 1. Clone the Repository

```bash
git clone https://github.com/Darshan-Ramachandra/SQL-Query-Gemini.git
```

### 2. Navigate to the Project Directory

```bash
cd multi-lang-invoice-extractor
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 4. Install Dependencies

Ensure Python 3.8+ is installed.

```bash
pip install -r requirements.txt
```

### 5. Set Up Environment Variables

Create a `.env` file in the root directory with your Gemini API key:

```env
GOOGLE_API_KEY=<your-gemini-api-key>
```

### 6. Run the App

```bash
streamlit run app.py
```

> This will open a local Streamlit server where you can upload invoices and get AI-powered insights.

---

## How to Get Your Google Gemini API Key 🔑

1. Visit [Google AI Studio](https://makersuite.google.com/app).
2. Log in with your Google account.
3. Go to **Profile > API Keys**.
4. Generate and copy your key.
5. Paste it into the `.env` file as shown above.

> Make sure billing is enabled and the Gemini API is accessible in your Google Cloud project.

---

## Project Structure 📁

```
.
├── app.py              # Main Streamlit application
├── .env                # Environment variables (API key)
├── requirements.txt    # Project dependencies
```

---

## Contributing 🤝

### 1. Fork the Repository

Click the "Fork" button in GitHub to copy the repo to your account.

### 2. Clone Your Fork

```bash
git clone https://github.com/Darshan-Ramachandra/SQL-Query-Gemini.git
```

### 3. Create a Branch

```bash
git checkout -b feature-branch-name
```

### 4. Commit and Push

```bash
git add .
git commit -m "Added new feature or fix"
git push origin feature-branch-name
```

### 5. Submit a Pull Request

Open a PR to the original repository from your fork.

---

🌟 **If this project helped you, consider giving it a star on GitHub!**
