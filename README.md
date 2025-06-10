# 🚢 Titanic Dataset Analysis  

### **Unveiling Survival Patterns with Python & Dash**  

This repository presents an **interactive, visualization-rich analysis** of the Titanic dataset using Python libraries **pandas, Plotly, and Dash**. We explore survival trends and hidden correlations through **data-driven storytelling**.  

## 🔍 **What's Inside?**  

### **🛠 Data Cleaning & Preparation**  

- Filled missing **Age** values using median imputation.  
- Dropped **Cabin** column due to excessive missing values.  
- Encoded categorical variables:  
  ```python
  df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})  
  df['Embarked'] = df['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})  
  ```  

### **📊 Key Survival Insights**  

✔ **First-class survival rate:** 62.2% vs. **Third-class:** 24.2%—privilege mattered.  

✔ **Women’s survival rate:** 74.2% vs. **Men:** 18.9%—lifeboat priority confirmed. 
 
✔ **Highest fare paid:** $512.3, while third-class paid under $10—did money secure safety?  

✔ **Cherbourg passengers survived at 55.4%**, while **Southampton at 33.7%**—regional factors in play?  

✔ **Passengers traveling with family had a 46.5% survival rate**, but **large families saw lower survival odds due to chaotic evacuation dynamics**.  

## 📊 **Visualizations: Interactive Dash Graphs**  

### **1️⃣ Age Distribution**  
Shows the overall age spread among passengers.  

```python
dcc.Graph(figure=px.histogram(df, x='Age', title='Age Distribution'))
```  

### **2️⃣ Survival Rate by Class**  

Visualizes survival likelihood based on passenger class.  

```python
dcc.Graph(figure=px.bar(df, x='Pclass', y='Survived', color='Pclass', title='Survival Rate by Class'))
```  

### **3️⃣ Survival Rate by Gender**  

Illustrates the stark contrast in survival rates between male and female passengers.  

```python
dcc.Graph(figure=px.pie(df, names='Sex', values='Survived', title='Survival Rate by Gender'))
```  

### **4️⃣ Fare vs. Age Survival Comparison**  

Displays how fares varied with age, colored by survival.  

```python
dcc.Graph(figure=px.scatter(df, x='Fare', y='Age', color='Survived', title='Fare vs Age Survival Comparison'))
```  

### **5️⃣ Age Distribution by Class**  

Shows how age trends differed across passenger classes.  

```python
dcc.Graph(figure=px.box(df, x='Pclass', y='Age', title='Age Distribution by Class'))
```  

### **6️⃣ Survival Rate by Embarkation Point**  

Examines the impact of embarkation location on survival odds.  

```python
dcc.Graph(figure=px.bar(df, x='Embarked', y='Survived', color='Embarked', title='Survival Rate by Embarkation Point'))
```  

### **7️⃣ Fare Distribution by Class**  

Visualizes the range of ticket fares across different classes.  

```python
dcc.Graph(figure=px.violin(df, x='Pclass', y='Fare', title='Fare Distribution by Class'))
```  

### **8️⃣ Fare Distribution Among Passengers**  

Displays overall fare spread within the dataset.  
```python
dcc.Graph(figure=px.histogram(df, x='Fare', title='Fare Distribution Among Passengers'))
```  

### **9️⃣ Survival Rate Based on Siblings/Spouses**  

Illustrates how traveling with siblings/spouses influenced survival odds.  

```python
dcc.Graph(figure=px.bar(df, x='SibSp', y='Survived', title='Survival Rate Based on Siblings/Spouses'))
```  

### **🔟 Age vs. Survival Colored by Class**  

Shows survival trends across different age groups, separated by class.  

```python
dcc.Graph(figure=px.scatter(df, x='Age', y='Survived', color='Pclass', title='Age vs Survival Colored by Class'))
```  

### **1️⃣1️⃣ Survival Rate Based on Parents/Children**  

Examines whether traveling with parents or children impacted survival.  

```python
dcc.Graph(figure=px.bar(df, x='Parch', y='Survived', title='Survival Rate Based on Parents/Children'))
```  

### **1️⃣2️⃣ Fare vs. Age Relationship by Class**  

Analyzes how fare prices differed across age groups within different classes.  

```python
dcc.Graph(figure=px.scatter(df, x='Fare', y='Age', color='Pclass', title='Fare vs Age Relationship by Class'))
```  

## 🛠 **Getting Started**  

Clone the repository and install required dependencies:
  
```bash
git clone https://GitHub.com/Gyanankur23/TitanicAnalysis.git  
cd TitanicAnalysis  
pip install -r requirements.txt  
python app.py  
```
This will launch the **interactive Dash dashboard**, allowing you to explore survival trends dynamically!  

## 🚀 **Final Deliverables** 
 
📊 **PowerPoint Summary**—all insights consolidated into a compelling presentation.  

🔗 **GitHub Repository with Python scripts and interactive outputs.**  

📑 **Future Work Recommendations:**  

   - Using **machine learning models** for survival prediction. 

   - Comparative studies on **modern evacuation protocols vs. Titanic survival rates**.  

## 🌍 **Join the Discussion!**
  
Connect on LinkedIn:
 [@GyanankurBaruah](https://linkedin.com/in/gyanankurbaruah)  


🚢 **Explore, analyze, and uncover Titanic’s survival mysteries!**  
