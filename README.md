<<<<<<< HEAD
KAIM Week 0 - Solar Data Analysis
This project is part of the 10 Academy Week 0 Challenge. The goal is to analyze, clean, and draw insights from solar radiation data to support MoonLight Energy Solutions in making data-driven decisions about solar farm installations.

📋 Project Objective
Analyze environmental data to identify high-potential regions for solar energy investment by cleaning and exploring key features such as solar radiation, temperature, humidity, and wind speed.

⚙️ Tools & Technologies
Python (Pandas, NumPy, Matplotlib, Seaborn, SciPy)
Git & GitHub for version control
Jupyter Notebook / VS Code for coding and analysis
📂 Project Structure
bash
Copy code
kaim_week_0/
├── notebooks/
│   └── benin.ipynb  # Notebook with data cleaning and EDA
├── README.md        # Project overview and instructions

📈 Work Done So Far
Environment Setup: Created a virtual environment and set up Git.
Git Version Control: Created a new branch, staged, committed, and pushed changes to GitHub.
Data Exploration:
Plotted solar radiation (GHI, DNI, DHI) over time.
Calculated summary statistics (mean, median, standard deviation) for key columns.
Visualized correlations between key features like GHI, temperature, and humidity.
Data Cleaning:
Handled missing values by checking and tracking missing entries.
Detected negative values in columns where they shouldn't exist (like GHI, DNI, and DHI) and corrected them.
Analyzed the impact of cleaning sensor data (ModA, ModB).
🚀 How to Run
Clone the repository:

bash
Copy code
git clone https://github.com/kaleabb266/kaim_week_0.git
Create and activate a virtual environment:

bash
Copy code
python -m venv .venv
.venv\Scripts\activate  # For Windows
Install required libraries:

