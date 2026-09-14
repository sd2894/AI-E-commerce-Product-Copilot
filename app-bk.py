import streamlit as st
import base64
from google import genai


# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="AI E-commerce Product Copilot",
    page_icon="🛍️",
    layout="wide"
)


# --------------------------------------------------
# CUSTOM UI
# --------------------------------------------------

st.markdown(
    """
    <style>
    .main-title {
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 18px;
        color: #666;
        margin-bottom: 25px;
    }

    .feature-box {
        padding: 18px;
        border-radius: 12px;
        background-color: #f5f7fa;
        margin-bottom: 20px;
    }

    .section-title {
        font-size: 24px;
        font-weight: 600;
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown(
    '<div class="main-title">🛍️ AI E-commerce Product Copilot</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Turn a product image into ready-to-use e-commerce content with AI.'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="feature-box">
    💡 <b>How it works:</b>
    Upload a product image → AI analyzes the product →
    Get product listing, marketing and SEO content instantly.
    </div>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# API KEY
# --------------------------------------------------

api_key = st.text_input(
    "🔑 Gemini API Key",
    type="password"
)


# --------------------------------------------------
# PRODUCT IMAGE
# --------------------------------------------------

st.subheader("📸 Product Image")

uploaded_image = st.file_uploader(
    "Upload your product image",
    type=["jpg", "jpeg", "png", "webp"]
)

if uploaded_image:

    st.image(
        uploaded_image,
        caption="Uploaded Product",
        use_container_width=True
    )


# --------------------------------------------------
# OPTIONAL PRODUCT DETAILS
# --------------------------------------------------

st.subheader("📝 Product Information")

col1, col2 = st.columns(2)

with col1:

    product_name = st.text_input(
        "Product Name (optional)",
        placeholder="Example: Korean Silver Chain"
    )


with col2:

    price = st.text_input(
        "Price (optional)",
        placeholder="Example: ₹299"
    )


features = st.text_area(
    "Additional Features (optional)",
    placeholder="Example: Lightweight, waterproof, daily wear"
)


# --------------------------------------------------
# GENERATE BUTTON
# --------------------------------------------------

generate = st.button(
    "🚀 Generate Product Content",
    use_container_width=True
)


# --------------------------------------------------
# GENERATE CONTENT
# --------------------------------------------------

if generate:

    # --------------------------------------------------
    # VALIDATION
    # --------------------------------------------------

    if not api_key:

        st.error(
            "Please enter your Gemini API key."
        )

    elif not uploaded_image:

        st.error(
            "Please upload a product image."
        )

    else:

        try:

            # --------------------------------------------------
            # CREATE GEMINI CLIENT
            # --------------------------------------------------

            client = genai.Client(
                api_key=api_key
            )


            # --------------------------------------------------
            # READ IMAGE
            # --------------------------------------------------

            image_bytes = uploaded_image.getvalue()


            # Convert image bytes to Base64
            image_base64 = base64.b64encode(
                image_bytes
            ).decode("utf-8")


            # --------------------------------------------------
            # AI PROMPT
            # --------------------------------------------------

            prompt = f"""
You are an expert e-commerce marketing assistant.

Analyze the uploaded product image carefully.

Product name provided by user:
{product_name}

Price:
{price}

Additional features:
{features}

Create a complete e-commerce product content package.

Return the result EXACTLY using these headings:

## PRODUCT TITLE

Write an attractive product title.

## SHORT DESCRIPTION

Write a short e-commerce description.

## DETAILED DESCRIPTION

Write a detailed product description suitable for an online store.

## KEY SELLING POINTS

Give exactly 5 selling points.

## INSTAGRAM CAPTION

Create an attractive Instagram caption with suitable emojis
and hashtags.

## SEO KEYWORDS

Give relevant SEO keywords separated by commas.

## PRODUCT CATEGORY

Suggest the most suitable product category.

Important rules:

- Analyze the product image carefully.
- Do not invent technical specifications.
- Do not claim a material unless it is provided or clearly visible.
- If something is uncertain, use safe wording.
- Keep the language professional and easy to understand.
- Make the content suitable for e-commerce websites.
- Make the Instagram caption suitable for social media marketing.
"""


            # --------------------------------------------------
            # CALL GEMINI
            # --------------------------------------------------

            with st.spinner(
                "🤖 AI is analyzing your product..."
            ):

                interaction = client.interactions.create(

                    model="gemini-3.6-flash",

                    input=[
                        {
                            "type": "image",
                            "data": image_base64,
                            "mime_type": uploaded_image.type
                        },
                        {
                            "type": "text",
                            "text": prompt
                        }
                    ]
                )


                # --------------------------------------------------
                # GET AI RESPONSE
                # --------------------------------------------------

                generated_content = interaction.output_text


            # --------------------------------------------------
            # SUCCESS
            # --------------------------------------------------

            st.success(
                "✅ Product content generated!"
            )


            # --------------------------------------------------
            # DISPLAY RESULT
            # --------------------------------------------------

            st.subheader(
                "🛒 E-commerce Ready Content"
            )

            st.caption(
                "Each section can be copied individually "
                "using the copy button."
            )


            # --------------------------------------------------
            # PARSE SECTIONS
            # --------------------------------------------------

            sections = {}

            current_section = None

            for line in generated_content.splitlines():

                line_clean = line.strip()

                if line_clean.startswith("## "):

                    current_section = line_clean.replace(
                        "## ",
                        ""
                    ).strip()

                    sections[current_section] = ""

                elif current_section:

                    sections[current_section] += (
                        line + "\n"
                    )


            # --------------------------------------------------
            # DISPLAY ORDER
            # --------------------------------------------------

            display_order = [

                "PRODUCT TITLE",

                "SHORT DESCRIPTION",

                "DETAILED DESCRIPTION",

                "KEY SELLING POINTS",

                "INSTAGRAM CAPTION",

                "SEO KEYWORDS",

                "PRODUCT CATEGORY"

            ]


            # --------------------------------------------------
            # DISPLAY EACH SECTION
            # --------------------------------------------------

            for section in display_order:

                if section in sections:

                    st.markdown(
                        f"### {section.title()}"
                    )

                    content = sections[
                        section
                    ].strip()

                    st.code(
                        content,
                        language="text"
                    )


            # --------------------------------------------------
            # DOWNLOAD
            # --------------------------------------------------

            st.divider()

            st.subheader(
                "📥 Export"
            )

            st.download_button(

                label="📥 Download Complete Product Content",

                data=generated_content,

                file_name="product_content.txt",

                mime="text/plain",

                use_container_width=True
            )


            # --------------------------------------------------
            # RAW RESPONSE
            # --------------------------------------------------

            with st.expander(
                "🔍 View Complete AI Response"
            ):

                st.markdown(
                    generated_content
                )


        # --------------------------------------------------
        # ERROR HANDLING
        # --------------------------------------------------

        except Exception as e:

            st.error(
                "⚠️ Unable to generate product content."
            )

            st.caption(
                f"Technical details: {e}"
            )
