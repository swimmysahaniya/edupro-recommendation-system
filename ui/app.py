import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

import os

BASE_DIR = os.path.dirname(__file__)


@st.cache_data
def load_data():
    user_features = pd.read_csv(os.path.join(BASE_DIR, "user_features.csv"))
    top_courses = pd.read_csv(os.path.join(BASE_DIR, "top_courses.csv"))
    courses = pd.read_csv(os.path.join(BASE_DIR, "courses.csv"))
    user_courses = pd.read_csv(os.path.join(BASE_DIR, "user_courses.csv"))
    return user_features, top_courses, courses, user_courses


user_features, top_courses, courses, user_courses = load_data()

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="EduPro Recommendation System",
    page_icon="🎓",
    layout="wide"
)

st.markdown("""
<style>
.big-title {
    font-size: 40px;
    font-weight: bold;
}
.card {
    padding: 20px;
    border-radius: 15px;
    background-color: #111827;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.4);
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# LOAD DATA
# -----------------------------
#user_features = pd.read_csv("user_features.csv")
#top_courses = pd.read_csv("top_courses.csv")
#courses = pd.read_csv("courses.csv")

# -----------------------------
# TITLE
# -----------------------------
st.title("🎓 EduPro Personalized Course Recommendation System")
st.markdown("### AI-powered student segmentation & smart course suggestions")

st.success("✅ Model successfully loaded & ready!")

# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.header("🔍 Select User")

user_id = st.sidebar.selectbox(
    "Select a User",
    user_features['UserID']
)

# -----------------------------
# GET USER DATA
# -----------------------------
with st.spinner("🤖 AI is analyzing your learning behavior..."):
    user_data = user_features[user_features['UserID'] == user_id]

if user_data.empty:
    st.error("User not found!")
    st.stop()

cluster = user_data['Cluster'].values[0]

if cluster == 0:
    st.success("🟢 Beginner Explorers - Trying different domains")
elif cluster == 1:
    st.info("🔵 Focused Learners - Prefer specific category")
elif cluster == 2:
    st.warning("🟡 High Spenders - Invest heavily in learning")
else:
    st.error("🔴 Advanced Users - Deep learners")

# -----------------------------
# TOP SECTION (USER INFO)
# -----------------------------
user = user_data.iloc[0]

st.markdown("## 👤 User Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Cluster", user['Cluster'])
col2.metric("Courses", user['CourseID'])
col3.metric("Spending ($)", f"{user['Amount']:.2f}")
col4.metric("Rating ⭐", f"{user['CourseRating']:.2f}")

st.info(f"""
🎯 **User belongs to Cluster {user['Cluster']}**

This user prefers **{user['CourseCategory']}** courses and mostly learns at **{user['CourseLevel']} level**
""")

# -----------------------------
# EXTRA FEATURES
# -----------------------------
st.markdown("## 📊 Learning Behavior")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Diversity Score", int(user['DiversityScore']))

with col2:
    st.metric("Enrollment Frequency", int(user['EnrollmentFrequency']))

with col3:
    st.metric("Learning Depth", round(float(user['LearningDepth']), 2))


# -----------------------------
# enrolled courses
# -----------------------------
user_course_ids = user_courses[user_courses['UserID'] == user_id]['CourseID']

# -----------------------------
# RECOMMENDATION
# -----------------------------
st.markdown("## 🎯 Recommended Courses")

# Filter cluster courses
#recs = top_courses[top_courses['Cluster'] == cluster].head(5)
recs = top_courses[
    (top_courses['Cluster'] == cluster) &
    (~top_courses['CourseID'].isin(user_course_ids))
].head(5)

# Merge with course details
recs = recs.merge(courses, on='CourseID')

recs = recs.sort_values(by="CourseRating", ascending=False)

for _, row in recs.iterrows():
    st.markdown(f"""
    ### 📘 {row['CourseName']}
    - Category: **{row['CourseCategory']}**
    - Level: **{row['CourseLevel']}**
    - ⭐ Rating: **{row['CourseRating']}**

    💡 Recommended because it matches your **cluster behavior & interests**
    """)
    st.markdown("---")

if recs.empty:
    st.warning("No recommendations available for this user.")

# -----------------------------
# Download Button
# -----------------------------
st.download_button(
    "📥 Download Recommendations",
    recs.to_csv(index=False),
    file_name="recommendations.csv"
)
st.markdown("---")

# -----------------------------
# CHART
# -----------------------------
st.markdown("## 📈 Course Category Distribution")

category_counts = recs['CourseCategory'].value_counts()

fig, ax = plt.subplots()

fig.patch.set_facecolor('none')      # remove white background
ax.set_facecolor('none')

category_counts.plot(kind='bar', ax=ax)
ax.grid(True, linestyle='--', alpha=0.3)

ax.tick_params(colors='white')       # text color
ax.set_title("Course Category Distribution", color='white')
ax.set_xlabel("Category", color='white')
ax.set_ylabel("Count", color='white')

st.pyplot(fig)

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("---")
st.markdown("🚀 Built by Swimmy Sahaniya | EduPro ML System")