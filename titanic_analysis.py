# Titanic_Analysis_Extended.py

import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from dash import Dash, dcc, html

# Load Titanic dataset
df = pd.read_excel("Titanic Dataset.xlsx", engine="openpyxl")

# Data Cleaning
df['Age'] = df['Age'].fillna(df['Age'].median())  # Fixes FutureWarning
df = df.drop(columns=['Cabin'])  # Ensures proper inplace handling
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
df['Embarked'] = df['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})

# Create Dash app
app = Dash(__name__)

app.layout = html.Div([
    html.H1("Titanic Data Analysis", style={'textAlign': 'center'}),

    # Existing Visualizations
    dcc.Graph(figure=px.histogram(df, x='Age', title='Age Distribution')),
    dcc.Graph(figure=px.bar(df, x='Pclass', y='Survived', color='Pclass', title='Survival Rate by Class')),
    dcc.Graph(figure=px.pie(df, names='Sex', values='Survived', title='Survival Rate by Gender')),
    dcc.Graph(figure=px.scatter(df, x='Fare', y='Age', color='Survived', title='Fare vs Age Survival Comparison')),

    # New Visualizations
    dcc.Graph(figure=px.box(df, x='Pclass', y='Age', title='Age Distribution by Class')),    
    dcc.Graph(figure=px.bar(df, x='Embarked', y='Survived', color='Embarked', title='Survival Rate by Embarkation Point')),
    dcc.Graph(figure=px.violin(df, x='Pclass', y='Fare', title='Fare Distribution by Class')),
    dcc.Graph(figure=px.histogram(df, x='Fare', title='Fare Distribution Among Passengers')),
    dcc.Graph(figure=px.bar(df, x='SibSp', y='Survived', title='Survival Rate Based on Siblings/Spouses')),
    dcc.Graph(figure=px.scatter(df, x='Age', y='Survived', color='Pclass', title='Age vs Survival Colored by Class')),
    dcc.Graph(figure=px.bar(df, x='Parch', y='Survived', title='Survival Rate Based on Parents/Children')),
    dcc.Graph(figure=px.scatter(df, x='Fare', y='Age', color='Pclass', title='Fare vs Age Relationship by Class')),
])
# Run the server
if __name__ == '__main__':
    app.run(debug=True)