
# Healthcare Data Analysis & Interactive Dashboard

A data analytics project that explores healthcare data to uncover insights into patient demographics, medical conditions, billing patterns, admission trends, and insurance providers.

This project combines **Python-based Exploratory Data Analysis (EDA)** with an **interactive web dashboard** built using HTML, CSS, and JavaScript.

## Project Overview

The objective of this project is to analyze healthcare records, identify meaningful patterns, and present key findings through an interactive dashboard.

The analysis focuses on:
- Patient demographics and age distribution.
- Medical condition frequency.
- Monthly average treatment costs.
- Insurance provider distribution.
- Emergency admission trends.
- High-value billing records.
- Emergency admissions with abnormal test results.

## Technologies Used

- **Python** – Data analysis and preprocessing.
- **Pandas** – Data manipulation and cleaning.
- **NumPy** – Numerical operations.
- **Matplotlib** – Data visualization.
- **HTML5** – Dashboard structure.
- **CSS3** – Dashboard styling and responsive layout.
- **JavaScript** – Interactive dashboard functionality.

## Project Structure

```text
Healthcare-Analytics-Dashboard/
│
├── healthcare_analysis.py
├── healthcare_dashboard.html
├── healthcare_dataset.csv
└── README.md
```

*Note: Add the dataset file to your project folder before running the Python script. Only publish the dataset if its license and privacy conditions allow it.*

## Data Cleaning & Preprocessing

The following preprocessing steps were performed:

- Inspected dataset structure, data types, and statistical summaries.
- Checked for missing values and duplicate records.
- Removed duplicate records.
- Cleaned patient names by trimming unnecessary spaces and standardizing capitalization.
- Replaced negative billing amounts with the mean billing amount.
- Converted admission and discharge dates into datetime format.
- Created a new feature, `Length_of_stay`, by calculating the difference between discharge and admission dates.

## Exploratory Data Analysis (EDA)

The project explores several important healthcare metrics:

| Analysis | Objective |
|---|---|
| Patient Count by Medical Condition | Identify the most common medical conditions. |
| Age Distribution | Understand the distribution of patient ages. |
| Average Treatment Cost by Month | Analyze monthly billing trends. |
| Age vs. Billing Amount | Explore the relationship between patient age and billing. |
| Insurance Provider Distribution | Compare patient distribution across insurance providers. |
| Emergency Admissions by Month | Identify monthly emergency admission patterns. |
| High Billing Records | Analyze billing amounts above the 90th percentile. |
| Emergency Admissions with Abnormal Results | Identify emergency cases with abnormal test results. |

## Interactive Dashboard Features

The project includes a standalone interactive dashboard with the following features:

- **KPI Cards:** Displays important healthcare metrics.
- **Chart Search:** Quickly search for specific charts.
- **Section Filters:** Filter core analysis and business analysis sections.
- **Dark/Light Mode:** Switch between themes with preferences saved in local storage.
- **Chart Sorting:** Sort chart categories for easier comparison.
- **Interactive Categories:** Select and highlight related chart categories.
- **Scatter Plot Filters:** Filter age and billing ranges.
- **Insurance Provider Filters:** Include or exclude providers in the donut chart.
- **Monthly Billing Trend:** Explore monthly billing with a crosshair and three-month moving average.
- **CSV Export:** Export dashboard summary values.
- **Expandable Cards:** Expand dashboard cards for a closer look.
- **Reset Controls:** Restore dashboard filters and settings.

## Key Project Insights

The dashboard presents the following results after data cleaning:

| Metric | Value |
|---|---:|
| Total Patient Records | 54,966 |
| Duplicate Records Removed | 534 |
| Average Patient Age | 51.5 years |
| Average Billing Amount | $25,595 |
| Average Length of Stay | 15.5 days |
| Total Billing Amount | $1.41 Billion |
| Admission Date Range | May 8, 2019 – May 7, 2024 |

## How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Healthcare-Analytics-Dashboard.git
```

### 2. Navigate to the Project Folder

```bash
cd Healthcare-Analytics-Dashboard
```

### 3. Install Required Libraries

```bash
pip install pandas numpy matplotlib
```

### 4. Add the Dataset

Place `healthcare_dataset.csv` in the project directory.

### 5. Run the Python Analysis

```bash
python healthcare_analysis.py
```

### 6. Open the Interactive Dashboard

Open `healthcare_dashboard.html` in your web browser.

No additional server setup is required for the standalone dashboard.

## Project Limitations

- The dashboard uses pre-rendered data and is not connected to a live backend.
- The CSV export provides dashboard summary values, not the complete patient-level dataset.
- The analysis depends on the dataset supplied locally.

## Future Improvements

- Integrate a live database for dynamic data updates.
- Build predictive models for patient admission trends.
- Develop hospital resource and inventory forecasting.
- Add advanced statistical analysis.
- Implement real-time dashboard updates.
- Explore machine learning for healthcare trend prediction.

## Author

**Tanusree Ghosh**

BCA Undergraduate | Aspiring Data Analyst

---

If you found this project interesting, feel free to explore the repository and share your feedback!

