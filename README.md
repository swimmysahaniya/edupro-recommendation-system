# 🎓 EduPro Personalized Course Recommendation System

<p align="center">
  <img src="assets/demo.png" width="850"/>
</p>

<p align="center">
  🚀 AI-powered student segmentation & personalized course recommendations
</p>

---

## 🌐 Live Demo
👉 https://swimmysahaniya-edupro-recommendation-system-uiapp-aqupyc.streamlit.app/

---

## 📌 Project Overview

EduPro is an **end-to-end Machine Learning project** that analyzes student behavior and segments users using clustering techniques to deliver **personalized course recommendations**.

It simulates a real-world EdTech platform where learners receive **smart, data-driven suggestions** instead of generic recommendations.

---

## 🎯 Key Features

✅ User Segmentation using **KMeans Clustering**  
✅ Advanced Feature Engineering  
- Diversity Score  
- Learning Depth  
- Enrollment Frequency  

✅ Personalized Recommendation Engine  
✅ Interactive Dashboard using **Streamlit**  
✅ Real-time User Insights & Visualization  

---

## 🧠 Machine Learning Workflow

1. **Data Preprocessing**
   - Handling missing values
   - Encoding categorical features
   - Feature scaling

2. **Feature Engineering**
   - Behavioral metrics creation
   - Aggregation at user level

3. **Clustering (KMeans)**
   - Elbow Method for optimal K
   - Silhouette Score for validation

4. **Recommendation Logic**
   - Cluster-based filtering
   - Popularity & rating-based ranking

---

## 📊 Tech Stack

| Category        | Tools Used |
|----------------|-----------|
| Programming     | Python |
| Data Processing | Pandas, NumPy |
| Machine Learning| Scikit-learn |
| Visualization   | Matplotlib |
| UI Framework    | Streamlit |

---

## 📸 Demo

<p align="center">
  <img src="assets/demo.png" width="850"/>
</p>

---

## 🖥️ Run Locally

```bash
# Clone repository
git clone https://github.com/swimmysahaniya/edupro-recommendation-system.git

# Move into project
cd edupro-recommendation-system

# Install dependencies
pip install -r requirements.txt

# Run app
streamlit run ui/app.py