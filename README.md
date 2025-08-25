# 📊 Teen Phone Addiction Data Visualization

An **interactive data visualization dashboard** built with **Streamlit** to explore and analyze **teen smartphone usage and addiction patterns**. This project helps uncover behavioral insights through clean and dynamic visualizations.

---

## 🚀 Features

* 📂 **Dataset Preview** – View raw data and filter it by gender, age, or location.
* 🎛️ **Interactive Filters** – Instantly update charts with user selections.
* 📈 **Univariate Visualizations** – Histograms, bar charts, pie charts, and donut charts for distribution insights.
* 🔗 **Bivariate Visualizations** – Clustered bar charts and scatter plots to compare variables.
* ⚡ **Dynamic Updates** – All visuals refresh automatically with applied filters.
* 🖥️ **User-Friendly Dashboard** – Simple and intuitive interface built with Streamlit.

---

## 📂 Project Structure

```
├── teen_phone_addiction_dataset.csv   # Dataset file
├── app.py                             # Streamlit application
├── requirements.txt                   # Dependencies
└── README.md                          # Project documentation
```

---

## 🛠️ Installation & Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/teen-phone-addiction-viz.git
   cd teen-phone-addiction-viz
   ```

2. **(Optional) Create virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit app**

   ```bash
   streamlit run app.py
   ```

5. **Open in browser**
   The app will be available at 👉 [http://localhost:8501](http://localhost:8501)

---

## 📊 Visualizations Included

* 📉 **Histogram** – Distribution of daily phone usage hours
* 📊 **Bar Charts** – Counts of addiction levels, usage patterns, etc.
* 🟦 **Clustered Bar Charts** – Compare categories across groups
* 🔵 **Scatter Plots** – Relationship between usage and addiction levels
* 🍩 **Pie & Donut Charts** – Proportional breakdowns of categories

---

## 📦 Requirements

Dependencies are listed in **`requirements.txt`**:

* `streamlit`
* `pandas`
* `matplotlib`
* `seaborn`
* `plotly`

Install them with:

```bash
pip install -r requirements.txt
```

---

## 📖 Dataset

The dataset (**teen\_phone\_addiction\_dataset.csv**) contains information about teenagers’ smartphone usage, including:

* **Daily usage hours**
* **Addiction levels**
* **Location**
* **School grade**
* **Demographics**

---

## 🎯 Purpose

This project turns raw data into meaningful **visual insights** to better understand **teen smartphone addiction patterns**. It is useful for **researchers, educators, and policymakers** studying digital addiction among teenagers.



