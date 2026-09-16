# 🤖 AI Product Content Generator

A multimodal AI-powered e-commerce assistant that analyzes a
product image and automatically generates marketing and SEO content.

## 📸 Demo
1. <img width="1366" height="607" alt="image" src="https://github.com/user-attachments/assets/d512f7a7-3872-4ddd-bd26-265be55bb1a4" />

2. <img width="1366" height="607" alt="image" src="https://github.com/user-attachments/assets/30547095-a34d-4b21-888b-416e4356e7db" />

3. <img width="1366" height="607" alt="image" src="https://github.com/user-attachments/assets/6ea960be-4fd5-4655-8d0c-4ea9b0c4d57c" />

4. <img width="1366" height="607" alt="image" src="https://github.com/user-attachments/assets/b84abafc-33e3-4890-ac90-7144c6ffc153" />







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
