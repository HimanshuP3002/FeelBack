import streamlit as st
from sentiment import analyze_sentiment

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="FeelBack – Student Feedback Analyzer",
    page_icon="💬",
    layout="centered"
)

# --------------------------------------------------
# Custom CSS (Modern, Premium Look)
# --------------------------------------------------
st.markdown("""
<style>

/* Background */
.main {
    background: linear-gradient(135deg, #e8f1ff, #f5fbff, #eefcf6);
}

/* Center container */
.container {
    max-width: 750px;
    margin: auto;
}

/* Glass card */
.card {
    background: rgba(255, 255, 255, 0.88);
    backdrop-filter: blur(14px);
    border-radius: 22px;
    padding: 30px;
    box-shadow: 0 22px 45px rgba(0,0,0,0.08);
    margin-top: 25px;
}

/* Header */
.title {
    font-size: 44px;
    font-weight: 800;
    color: #2563eb;
    text-align: center;
}

.subtitle {
    text-align: center;
    font-size: 17px;
    color: #555;
    margin-top: 6px;
}

/* Button */
div.stButton > button {
    width: 100%;
    height: 54px;
    border-radius: 16px;
    background: linear-gradient(135deg, #2563eb, #06b6d4);
    color: white;
    font-size: 16px;
    font-weight: 700;
    border: none;
    transition: all 0.25s ease;
}

div.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 14px 30px rgba(37,99,235,0.35);
}

/* Sentiment colors */
.positive { color: #16a34a; font-weight: 800; }
.neutral  { color: #ca8a04; font-weight: 800; }
.negative { color: #dc2626; font-weight: 800; }

/* Badge */
.badge {
    background: #eef2ff;
    padding: 6px 14px;
    border-radius: 14px;
    font-weight: 700;
}

/* Footer */
.footer {
    text-align: center;
    color: #777;
    font-size: 14px;
    margin: 40px 0 20px;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Layout Start
# --------------------------------------------------
st.markdown("<div class='container'>", unsafe_allow_html=True)

# Header
st.markdown("<div class='title'>FeelBack</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='subtitle'>AI-powered student feedback sentiment analyzer</div>",
    unsafe_allow_html=True
)

# --------------------------------------------------
# Input Card
# --------------------------------------------------
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("### 📝 Enter Student Feedback")

feedback = st.text_area(
    label="Student Feedback",
    placeholder="Example: The teacher explains concepts clearly and makes the class engaging...",
    height=160,
    label_visibility="collapsed"
)

analyze = st.button("Analyze Sentiment")
st.markdown("</div>", unsafe_allow_html=True)

# --------------------------------------------------
# Result Card
# --------------------------------------------------
if analyze:
    if feedback.strip() == "":
        st.warning("⚠️ Please enter some feedback before analyzing.")
    elif len(feedback.split()) < 5:
        st.warning("⚠️ Please enter at least 5 words for accurate analysis.")
    else:
        try:
            sentiment, emoji, polarity = analyze_sentiment(feedback)

            if sentiment == "Positive":
                cls = "positive"
                msg = "This feedback shows satisfaction and positive feelings."
            elif sentiment == "Negative":
                cls = "negative"
                msg = "This feedback highlights dissatisfaction or concern."
            else:
                cls = "neutral"
                msg = "This feedback is neutral with no strong emotion."

            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.markdown("### 📊 Analysis Result")

            st.markdown(
                f"""
                <p style="font-size:22px;">
                    <strong>Sentiment:</strong>
                    <span class="{cls}">{emoji} {sentiment}</span>
                </p>

                <p style="font-size:16px;">
                    <strong>Polarity Score:</strong>
                    <span class="badge">{polarity}</span>
                </p>
                """,
                unsafe_allow_html=True
            )

            if sentiment == "Positive":
                st.success(msg)
            elif sentiment == "Negative":
                st.error(msg)
            else:
                st.info(msg)

            st.markdown("</div>", unsafe_allow_html=True)

        except Exception:
            st.error("Something went wrong while analyzing the feedback. Please try again.")

# Footer
st.markdown("<div class='footer'>Built with ❤️ for students • FeelBack</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
