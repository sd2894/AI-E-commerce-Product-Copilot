import streamlit as st
from google import genai
from google.genai import types

st.set_page_config(
    page_title="AI Product Content Generator",
    page_icon="✨"
)

st.title("🛍️ AI E-commerce Product Copilot")

st.write(
    "Upload a product image and let AI create "
    "ready-to-use e-commerce marketing content."
)

st.info(
    "💡 Designed for small businesses and online sellers — "
    "turn one product image into a complete product listing."
)

api_key = st.text_input(
    "Gemini API Key",
    type="password"
)

st.subheader("📸 Upload Product Image")

uploaded_image = st.file_uploader(
    "Upload your product image",
    type=["jpg", "jpeg", "png", "webp"]
)

if uploaded_image:
    st.image(
        uploaded_image,
        caption="Product Image",
        use_container_width=True
    )

st.subheader("Product Information")

product_name = st.text_input(
    "Product Name (optional)",
    placeholder="Example: Korean Silver Chain"
)

price = st.text_input(
    "Price (optional)",
    placeholder="Example: ₹299"
)

features = st.text_area(
    "Additional Features (optional)",
    placeholder="Example: Lightweight, waterproof, daily wear"
)

if st.button("🚀 Generate Product Content"):

    if not api_key:
        st.error("Please enter your Gemini API key.")

    elif not uploaded_image:
        st.error("Please upload a product image.")

    else:

        client = genai.Client(api_key=api_key)

        image_bytes = uploaded_image.getvalue()

        image_part = types.Part.from_bytes(
            data=image_bytes,
            mime_type=uploaded_image.type
        )

        prompt = f"""
You are an expert e-commerce marketing assistant.

Analyze the uploaded product image carefully.

Product name provided by user:
{product_name}

Price:
{price}

Additional features:
{features}

Based on the image and the information provided, create:

1. Product Title
2. Short Product Description
3. Detailed Product Description
4. 5 Key Selling Points
5. Instagram Caption
6. SEO Keywords
7. Suggested Product Category

Important:
- Do not invent technical specifications that cannot be determined.
- If material is uncertain, use safe wording such as
  "appears to be".
- Make the content suitable for an online jewellery store.
- Keep the language attractive and easy to understand.
"""

        with st.spinner("🤖 Gemini is analyzing your product..."):

            response = client.models.generate_content(
                model="gemini-3.5-flash-lite",
                contents=[
                    image_part,
                    prompt
                ]
            )

        st.success("✅ Product content generated!")

        st.markdown(response.text)