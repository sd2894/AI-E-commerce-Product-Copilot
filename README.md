# 🤖 AI Product Content Generator

A multimodal AI-powered e-commerce assistant that analyzes a
product image and automatically generates marketing and SEO content.

## 📸 Demo



<img width="1366" height="5439" alt="image" src="https://github.com/user-attachments/assets/26fc067b-cd38-443a-b756-54a187c17afb" />




## Screen recorder

https://www.awesomescreenshot.com/video/56560537?key=f582165721aaaf8c001fc5f772f3ee44










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
