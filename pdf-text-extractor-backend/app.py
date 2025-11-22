import streamlit as st
from pdf_utils import extract_text_from_pdf
from llm_infer import summarize_text

# from pdf_utils import extract_text_from_pdf
# from summarizer import summarize_text

# Page settings
st.set_page_config(
    page_title="AI Research Paper Summarizer", layout="centered")
st.title("📄 AI Research Paper Summarizer (Gemini-powered)")

# Upload PDF
uploaded_file = st.file_uploader("📎 Upload a research paper (PDF)", type="pdf")

if uploaded_file:
    # Save file temporarily
    with open("temp_uploaded.pdf", "wb") as f:
        f.write(uploaded_file.read())

    # Extract text
    extracted_text = extract_text_from_pdf("temp_uploaded.pdf")

    if not extracted_text.strip():
        st.error("⚠️ No extractable text found in the PDF. Try another file.")
    else:
        st.success("✅ PDF text extracted successfully!")

        st.subheader("📃 Extracted Preview (first 1000 characters):")
        st.text(extracted_text[:1000])

        if st.button("🧠 Generate Summary"):
            with st.spinner("Generating summary using Gemini..."):
                summary = summarize_text(extracted_text[:8000])

                if summary:
                    st.subheader("📝 AI-Generated Summary")
                    st.write(summary)

                    # Optional: Download button
                    st.download_button(
                        label="📥 Download Summary as TXT",
                        data=summary,
                        file_name="summary.txt",
                        mime="text/plain"
                    )
                else:
                    st.error("❌ Failed to generate summary. Try again.")

else:
    st.info("👆 Upload a PDF file above to get started.")


# Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit & Gemini API")
