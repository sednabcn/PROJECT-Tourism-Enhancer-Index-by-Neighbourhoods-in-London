# Tourism-Enhancer-Index-by-Neighbourhoods-in-London
Geo-spatial Data Project to Build a Recommendation Engine for the Tourism Industry in London

# Project Overview
This project develops a Tourism Enhancer Index to help tourists and businesses identify the best neighborhoods in London based on geo-spatial data, clustering analysis, and classification models. It provides personalized recommendations using machine learning and data visualization techniques.

# Project Goal
✅ Provide data-driven insights for tourists to choose the best areas to visit based on venues, attractions, and accessibility.
✅ Use clustering techniques to categorize London boroughs based on tourism attractiveness.
✅ Implement classification models to predict the best areas based on tourist activity trends.
✅ Visualize heatmaps of tourism demand for businesses and travel agencies to optimize their services.

# Technologies Used
Programming & Machine Learning
Python (Pandas, NumPy, Scikit-Learn, Matplotlib, Seaborn)
K-Means Clustering, Decision Trees, Random Forests, Confusion Matrix Analysis
Geo-Spatial Data Analysis
GeoJSON mapping for borough visualization
Folium for heatmap-based visualization of tourism hotspots
OpenStreetMap & London Boroughs Data for geo-location insights
Visualization & Data Processing
Matplotlib, Seaborn, and Plotly for statistical data visualization
Jupyter Notebooks for step-by-step data analysis
Data Cleaning & Feature Engineering for clustering and classification
# Implementation Details
1. Data Collection & Preprocessing
📌 Datasets Used:

London Boroughs & Tourism Data (Boroughs_london.csv, Borough_Cluster_05.csv)
Geo-spatial Mapping Data (geojson maps.ipynb)
Venue Distribution Data from OpenStreetMap & Google Places
📌 Data Cleaning & Feature Engineering:

Extracting venue data from raw datasets using drop_boroughs.py, isfloat.py
Transforming location data into machine learning-friendly formats
2. Clustering Analysis – Identifying Tourist Hotspots
📌 Goal: Use K-Means clustering to group London boroughs based on their tourism potential.

📌 Clustering Process:

Optimal K-Means Selection: kmeans_R_optimal.ipynb
Cluster Assignments & Venue Distribution:
london_boroughs_CLUSTERING.ipynb
Neighbourhood Venues Distribution in London.png
📌 Results:

Boroughs were classified into high, medium, and low tourism potential zones.
Identified neighborhoods with high tourist attraction density for better recommendations.
3. Classification Models – Predicting Ideal Tourist Spots
📌 Goal: Train classification models to predict the best boroughs based on tourism data trends.

📌 Models Used:

Decision Trees & Random Forests (london-classification-engine.ipynb)
Model Performance Analysis (Confusion matrix of Classifier Models.png)
📌 Results:

Developed a predictive model to recommend boroughs based on real-time data.
Improved accuracy by incorporating multiple features such as venues, historical tourism trends, and user preferences.
4. Heatmap & Interactive Visualization
📌 Goal: Create geo-spatial visualizations to help tourists and businesses analyze London’s tourism landscape.

📌 Implementation:

Folium-based Heatmaps (TEST-FOLIUM-HEATMAP.ipynb)
Tourism Index Mapping (London-International-Tourist-Series.ipynb)
📌 Results:

Interactive heatmaps show tourism density in different boroughs.
Visual insights help businesses optimize marketing strategies based on demand.
Impact & Results
✅ For Tourists: Personalized borough recommendations based on real-time and historical data.
✅ For Businesses: Marketing insights on tourism demand by location.
✅ For City Planners: Optimized tourism infrastructure based on geospatial analysis.

# How Tourists Can Use the System
🔹 Example 1: Finding the Best Neighborhood for Sightseeing
1️⃣ A tourist wants to explore London’s best sightseeing locations.
2️⃣ The system processes their preferences (historical sites, museums, entertainment).
3️⃣ The Tourism Enhancer Index suggests boroughs like Westminster, South Bank, and Kensington.
4️⃣ The tourist gets a map-based recommendation with highlighted hotspots.

🔹 Example 2: Personalized Recommendations for Nightlife
1️⃣ A traveler wants the best nightlife spots in London.
2️⃣ The classification model analyzes venue data (bars, nightclubs, entertainment venues).
3️⃣ The system recommends Camden, Soho, and Shoreditch as top nightlife neighborhoods.
4️⃣ A heatmap visualization shows live tourist density in those areas.

# Repository Files Navigation
📂 Data Collection & Preprocessing
Boroughs_london.csv – London boroughs dataset
drop_boroughs.py, isfloat.py – Data preprocessing scripts
📂 Clustering & Venue Analysis
BC05-CLUSTER-1.ipynb – K-Means clustering
Neighbourhood Venues Distribution in London.png – Venue analysis
📂 Classification & Model Performance
london-classification-engine.ipynb – Classification models
Confusion matrix of Classifier Models.png – Model accuracy visualization
📂 Heatmap & Visualization
TEST-FOLIUM-HEATMAP.ipynb – Interactive heatmap visualization
PROJECT-RESULTS.ipynb, PROJECT-RESULTS03.ipynb, PROJECT-RESULTS05.ipynb – Final project results
Would You Like to Add?
📌 Installation Guide for running the project?
📌 API Integration for real-time data updates?
📌 User Interface (UI) for tourists to input their preferences? 🚀












