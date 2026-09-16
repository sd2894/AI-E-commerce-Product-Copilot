# 🤖 AI Product Content Generator

A multimodal AI-powered e-commerce assistant that analyzes a
product image and automatically generates marketing and SEO content.

## 📸 Demo
<img width="1366" height="607" alt="image" src="https://github.com/user-attachments/assets/eb82bf05-06de-42bb-a3f7-4bf440e01dd7" />

<img width="1366" height="607" alt="image" src="https://github.com/user-attachments/assets/434b853b-7031-4d8d-9052-48f487df5fb7" />

<img width="1366" height="607" alt="image" src="https://github.com/user-attachments/assets/0f148ec2-00e3-4673-93c7-ea07165c0fd4" />

<img width="1366" height="607" alt="image" src="https://github.com/user-attachments/assets/082d9997-73a4-4ce7-a319-7915ae6e8abb" />
















## ✨ Features

- Upload a product image
- AI analyzes the product
- Generate product title
- Generate short description
- Generate detailed description
- Generate key selling points
- Generate Instagram caption
- Generate SEO keywords
- Identify product category
- Download generated content

## 🛠️ Tech Stack

- Python
- Streamlit
- Google Gemini API
- Google GenAI Python SDK
- Multimodal AI
- Base64 image processing

## 🧠 How It Works

Product Image
      ↓
Streamlit Upload
      ↓
Image → Base64
      ↓
Google Gemini API
      ↓
AI Product Analysis
      ↓
Structured E-commerce Content
      ↓
Download / Copy

## 🔐 API Configuration

This application requires a Gemini API key.

Create your API key through Google AI Studio and enter it
when running the application.

Never commit your API key to GitHub.

## ▶️ Run Locally

```bash
git clone YOUR_REPOSITORY_URL
cd ai-product-generator

python -m venv venv

# Windows
venv\Scripts\activate

pip install -r requirements.txt

streamlit run app.py
