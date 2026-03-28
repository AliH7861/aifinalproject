from pathlib import Path

import streamlit as st

from manual_naive_bayes import ManualNaiveBayes, load_training_data


st.set_page_config(page_title="Spam Checker", page_icon="mail", layout="centered")


@st.cache_resource
def load_model():
    dataset_path = Path(__file__).parent / "data" / "spam_dataset.csv"
    texts, labels = load_training_data(dataset_path)

    model = ManualNaiveBayes()
    model.fit(texts, labels)
    return model


model = load_model()

st.markdown(
    """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    #MainMenu, footer, header { visibility: hidden; }

    .block-container {
        max-width: 680px;
        padding-top: 3rem;
        padding-bottom: 3rem;
    }

    .header-wrap { text-align: center; margin-bottom: 2.5rem; }
    .header-wrap h1 {
        font-size: 1.9rem;
        font-weight: 700;
        color: #111;
        margin: 0 0 0.3rem;
    }
    .header-wrap p {
        font-size: 0.95rem;
        color: #6b7280;
        margin: 0;
    }

    .input-label {
        font-size: 0.85rem;
        font-weight: 600;
        color: #374151;
        letter-spacing: 0.04em;
        text-transform: uppercase;
        margin-bottom: 0.4rem;
    }

    textarea {
        border-radius: 10px !important;
        border: 1.5px solid #e5e7eb !important;
        font-size: 0.92rem !important;
        color: #111 !important;
    }
    textarea:focus {
        border-color: #6366f1 !important;
        box-shadow: 0 0 0 3px rgba(99,102,241,0.12) !important;
    }

    [data-testid="stTextArea"] label { display: none; }

    div.stButton > button {
        width: 100%;
        background: #111;
        color: #fff;
        border: none;
        border-radius: 10px;
        padding: 0.65rem 1.2rem;
        font-size: 0.92rem;
        font-weight: 600;
        letter-spacing: 0.02em;
        cursor: pointer;
        margin-top: 0.5rem;
    }
    div.stButton > button:hover { background: #333; }

    .result-pill {
        display: flex;
        align-items: center;
        gap: 0.6rem;
        border-radius: 12px;
        padding: 1rem 1.3rem;
        margin: 1.4rem 0 0.5rem;
        font-size: 1rem;
        font-weight: 600;
        background: #fff;
        border: 1.5px solid #e5e7eb;
        color: #111;
    }

    .result-pill .badge {
        margin-left: auto;
        font-size: 0.78rem;
        font-weight: 700;
        letter-spacing: 0.06em;
        text-transform: uppercase;
        padding: 0.2rem 0.55rem;
        border-radius: 6px;
        background: #111;
        color: #fff;
    }

    .divider { height: 1px; background: #f3f4f6; margin: 1.4rem 0; }

    .conf-label {
        font-size: 0.78rem;
        font-weight: 700;
        letter-spacing: 0.07em;
        text-transform: uppercase;
        color: #9ca3af;
        margin-bottom: 0.9rem;
    }

    .bar-row { margin-bottom: 0.85rem; }
    .bar-meta {
        display: flex;
        justify-content: space-between;
        font-size: 0.83rem;
        font-weight: 500;
        color: #374151;
        margin-bottom: 0.25rem;
    }
    .bar-track {
        height: 7px;
        border-radius: 99px;
        background: #f3f4f6;
        overflow: hidden;
    }
    .bar-fill { height: 100%; border-radius: 99px; }
    .bar-fill.spam-bar { background: #6b7280; }
    .bar-fill.ham-bar  { background: #d1d5db; }
</style>
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="header-wrap">
    <h1>Spam Checker</h1>
    <p>Paste any email below and we'll tell you if it looks suspicious.</p>
</div>
""",
    unsafe_allow_html=True,
)

st.markdown('<p class="input-label">Email content</p>', unsafe_allow_html=True)
email_input = st.text_area(
    label="Email content",
    label_visibility="hidden",
    height=190,
    placeholder="e.g. Congratulations! You've been selected for a special offer...",
)

if st.button("Analyze Email"):
    if not email_input.strip():
        st.warning("Paste some email text first.")
    else:
        prediction = model.predict([email_input])[0]
        probabilities = model.predict_proba([email_input])[0]
        labels = list(model.classes_)

        spam_p = probabilities[labels.index("spam")]
        ham_p = probabilities[labels.index("not spam")]
        is_spam = prediction == "spam"
        confidence = max(spam_p, ham_p)

        if is_spam:
            st.markdown(
                f"""
            <div class="result-pill">
                Likely Spam
                <span class="badge">{confidence:.0%} confidence</span>
            </div>""",
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                f"""
            <div class="result-pill">
                Looks Clean
                <span class="badge">{confidence:.0%} confidence</span>
            </div>""",
                unsafe_allow_html=True,
            )

        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
        st.markdown('<p class="conf-label">Confidence breakdown</p>', unsafe_allow_html=True)

        st.markdown(
            f"""
        <div class="bar-row">
            <div class="bar-meta"><span>Spam</span><span>{spam_p:.0%}</span></div>
            <div class="bar-track">
                <div class="bar-fill spam-bar" style="width:{spam_p * 100:.1f}%"></div>
            </div>
        </div>
        <div class="bar-row">
            <div class="bar-meta"><span>Not Spam</span><span>{ham_p:.0%}</span></div>
            <div class="bar-track">
                <div class="bar-fill ham-bar" style="width:{ham_p * 100:.1f}%"></div>
            </div>
        </div>
        """,
            unsafe_allow_html=True,
        )

st.caption(
    "This version trains a manual Multinomial Naive Bayes classifier from the bundled dataset each time the app starts."
)
