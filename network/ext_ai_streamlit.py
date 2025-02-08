import streamlit as st
import pandas as pd

# Load data
experts = pd.read_csv("experts.csv")
resources = pd.read_csv("resources.csv")

# App title and navigation
st.title("AI SME Network")
st.sidebar.title("Navigation")
options = st.sidebar.radio("Select a service:", ["Consult an AI Expert", "Expert Roundtables", "AI Info Centre"])

# 1. Consult an AI Expert Section
if options == "Consult an AI Expert":
    st.header("Consult an AI Expert")
    st.write("Find AI experts available for consultation:")
    selected_expert = st.selectbox("Choose an expert:", experts["Name"])

    expert_details = experts[experts["Name"] == selected_expert].iloc[0]
    st.subheader(f"Expert: {expert_details['Name']}")
    st.write(f"**Specialization:** {expert_details['Specialization']}")
    st.write(f"**Availability:** {expert_details['Availability']}")
    st.write(f"**Contact:** {expert_details['Contact']}")

    st.info("📧 Contact them via email to schedule a consultation.")

# 2. Expert Roundtables Section
elif options == "Expert Roundtables":
    st.header("Expert Roundtables")
    st.write("""
    Our roundtables provide an opportunity for staff to engage in discussions with AI experts.  
    **Next Event:** Quarterly discussions focused on key AI topics.
    """)
    st.write("- **When:** March, June, September, December")
    st.write("- **Format:** Interactive discussions and Q&A sessions.")
    st.write("📧 Contact the organizer at `roundtables@example.com` for more info.")

# 3. AI Info Centre Section
elif options == "AI Info Centre":
    st.header("AI Info Centre")
    st.write("Explore external AI resources to stay updated:")
    
    for index, row in resources.iterrows():
        st.subheader(row["Title"])
        st.write(row["Description"])
        st.markdown(f"[Learn more]({row['URL']})")

# Footer
st.sidebar.write("🔍 **Want to suggest a resource or ask a question?** Contact us at [ai-network@example.com](mailto:ai-network@example.com).")
