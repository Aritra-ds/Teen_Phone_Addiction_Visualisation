import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from pandas.plotting import scatter_matrix
import plotly.figure_factory as ff

# ================================================
# Load dataset
# ================================================
df = pd.read_csv("teen_phone_addiction_dataset.csv")

st.title("Teen Phone Addiction Dataset - Full Visualizations")

# ================================================
# Dataset Preview
# ================================================
st.subheader("Dataset Preview")
st.dataframe(df.head())

# ================================================
# Sidebar Filters
# ================================================
st.sidebar.header("Filters")
selected_gender = st.sidebar.multiselect("Select Gender", df["Gender"].unique())
selected_age = st.sidebar.multiselect("Select Age Group", df["Age"].unique())
selected_location = st.sidebar.multiselect("Select Location", df["Location"].unique())

filtered_df = df.copy()
if selected_gender:
    filtered_df = filtered_df[filtered_df["Gender"].isin(selected_gender)]
if selected_age:
    filtered_df = filtered_df[filtered_df["Age"].isin(selected_age)]
if selected_location:
    filtered_df = filtered_df[filtered_df["Location"].isin(selected_location)]

# ================================================
# Show Filtered Data
# ================================================
st.subheader("Filtered Data")
st.dataframe(filtered_df)

# ================================================
# Univariate Visualizations
# ================================================
st.header("Univariate Visualizations")

# Histogram - Daily Usage Hours
st.subheader("Histogram of Daily Usage Hours")
if not filtered_df.empty:
    fig, ax = plt.subplots()
    sns.histplot(filtered_df["Daily_Usage_Hours"], bins=20, kde=True, color="skyblue", ax=ax)
    ax.set_xlabel("Daily Usage Hours")
    ax.set_ylabel("Count")
    st.pyplot(fig)
else:
    st.info("No data available for histogram.")

# Pie chart - Gender distribution
st.subheader("Gender Distribution")
if not filtered_df.empty:
    gender_counts = filtered_df["Gender"].value_counts()
    fig, ax = plt.subplots()
    ax.pie(gender_counts, labels=gender_counts.index, autopct="%1.1f%%", startangle=90)
    st.pyplot(fig)
else:
    st.info("No data available for pie chart.")

# ================================================
# Bivariate Visualizations
# ================================================
st.header("Bivariate Visualizations")

# Scatterplot
st.subheader("Daily Usage Hours vs Addiction Level")
if not filtered_df.empty:
    fig = px.scatter(filtered_df, x="Daily_Usage_Hours", y="Addiction_Level",
                     color="Gender", size="Sleep_Hours", hover_data=["Age"])
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("No data available for scatterplot.")

# Boxplot
st.subheader("Addiction Level by Gender")
if not filtered_df.empty:
    fig = px.box(filtered_df, x="Gender", y="Addiction_Level", color="Gender")
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("No data available for boxplot.")

# ================================================
# Multivariate Visualizations
# ================================================
st.header(" Multivariate Visualizations")

# Pairplot (Seaborn)
st.subheader("Pairplot of Usage, Addiction, and Sleep Hours")
if not filtered_df.empty:
    try:
        fig = sns.pairplot(filtered_df[["Daily_Usage_Hours", "Addiction_Level", "Sleep_Hours", "Gender"]],
                           hue="Gender")
        st.pyplot(fig)
    except Exception as e:
        st.warning(f"Could not generate pairplot: {e}")
else:
    st.info("No data available for pairplot.")

# Heatmap
st.subheader("Correlation Heatmap")
if not filtered_df.empty:
    corr = filtered_df[["Daily_Usage_Hours", "Addiction_Level", "Sleep_Hours"]].corr()
    fig, ax = plt.subplots()
    sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)
else:
    st.info("No data available for heatmap.")

# Clustered Bar Chart
st.subheader("Clustered Bar Chart: Average Usage by Gender and Age")
if not filtered_df.empty:
    grouped = filtered_df.groupby(["Age", "Gender"])["Daily_Usage_Hours"].mean().reset_index()
    fig = px.bar(grouped, x="Age", y="Daily_Usage_Hours", color="Gender", barmode="group")
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("No data available for clustered bar chart.")

# Donut Chart - Addiction Level Distribution
st.subheader("Donut Chart of Addiction Level Distribution")
if not filtered_df.empty:
    level_counts = filtered_df["Addiction_Level"].value_counts()
    fig = go.Figure(data=[go.Pie(labels=level_counts.index, values=level_counts.values, hole=0.5)])
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("No data available for donut chart.")

# Scatter Bar Chart (variation: bar + scatter overlay)
st.subheader("Scatter Bar Chart: Usage Hours by Age")
if not filtered_df.empty:
    avg_usage = filtered_df.groupby("Age")["Daily_Usage_Hours"].mean().reset_index()
    fig = go.Figure()
    fig.add_trace(go.Bar(x=avg_usage["Age"], y=avg_usage["Daily_Usage_Hours"], name="Avg Usage"))
    fig.add_trace(go.Scatter(x=avg_usage["Age"], y=avg_usage["Daily_Usage_Hours"],
                             mode="markers+lines", name="Trend"))
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("No data available for scatter bar chart.")

# Density Plot
st.subheader("Density Plot of Daily Usage Hours")
if not filtered_df.empty:
    fig = ff.create_distplot([filtered_df["Daily_Usage_Hours"].dropna()],
                             ["Daily Usage"], show_hist=False, show_rug=False)
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("No data available for density plot.")
