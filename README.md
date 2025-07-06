# Rental Market Analysis in European Capitals Using Airbnb Data

## Project Overview

This project, developed for the course "Presentation and Information Visualization" (1st semester of the Master’s in Information Systems Engineering and Management), aims to build interactive dashboards to analyze the short-term rental market in major European capitals using Airbnb data.

### Objectives

* Explore pricing trends, demand patterns, and guest satisfaction metrics.
* Provide actionable insights for two user personas: property managers and real estate investors.
* Apply advanced information visualization techniques to support strategic decision-making.

## Dataset

* **Source**: Kaggle – *Airbnb Prices in European Cities* ([https://www.kaggle.com/datasets/thedevastator/airbnb-prices-in-european-cities](https://www.kaggle.com/datasets/thedevastator/airbnb-prices-in-european-cities))
* **Key variables**:

  * Location (city names, latitude/longitude, distances to city center)
  * Price (`realSum`)
  * Capacity (`person_capacity`)
  * Guest satisfaction (`guest_satisfaction_overall`, `cleanliness_rating`)
  * Proximity indices (attractions, restaurants)
  * Superhost status
  * Accommodation type

## Personas

1. **Teresa Silva** (Property Manager) – Limited technical background, focuses on simple metrics to optimize guest satisfaction and occupancy.
2. **Warren Buffett** (Investor) – Data-savvy user seeking strategic comparisons and scenario analysis to maximize returns.

## Solution Architecture

Two customized dashboards were developed:

### Teresa's Dashboard

* **Bar and column charts**: Compare average prices and review counts across cities.
* **Pyramid chart**: Compare cleanliness ratings between weekdays and weekends.
* **Correlation heatmap**: Show relationships between price, guest satisfaction, and cleanliness.
* **Donut chart**: Distribution of accommodation types.
* **Geospatial heatmaps**: Visualize satisfaction scores by location.
* **Line charts**: Track temporal trends in price and capacity.
* **Scatter plot**: Analyze the relationship between distance to city center, price, and proximity to attractions.

### Warren's Dashboard

* **Parallel coordinates plot** (Dash/Plotly): Compare multiple listing attributes simultaneously.
* **Geographic IRP heatmap**: Visualize the Potential Profitability Index (IRP) alongside prices.
* **Sunburst chart**: Hierarchical breakdown (city → distance band → number of bedrooms).
* **Column charts**: Average IRP and satisfaction by city and defined intervals.
* **Pyramid chart**: IRP comparison for weekdays vs. weekends by city.
* **Line chart**: Relationship between number of bedrooms and average IRP/price.

### Potential Profitability Index (IRP)

Calculated based on:

1. Average nightly price
2. Estimated occupancy rate (base 30% with 10% increments for favorable factors)
3. Listing capacity

Projected annual revenue = `average_price × capacity × occupancy_rate × 365`

## Technologies and Tools

* **Power BI**: Main dashboard development.
* **Python (Dash + Plotly)**: Interactive visualizations (parallel coordinates).
* **Python libraries**: Pandas, Plotly, Dash.
* **Generative AI**: Integrated chatbot for interactive data exploration and support.


## Installation & Execution

1. **Clone the repository:**

   ```bash
   ```

git clone [https://github.com/your-username/airbnb-europe-dashboard.git](https://github.com/your-username/airbnb-europe-dashboard.git)
cd airbnb-europe-dashboard

````
2. **Install dependencies:**
   ```bash
pip install -r requirements.txt
````

3. **Run the Dash application:**

   ```bash
   ```

cd app
python main.py

```
4. **Open Power BI dashboards:**
   - Open the files in `dashboards/` using Power BI Desktop.

## License & Acknowledgments
- Data sourced from Kaggle under the appropriate license.
- Developed by:
  - Pedro Pires (PG57851)
  - Liandro Cruz (A100436)
  - José Novais (PG57847)

---
*This project leverages cutting-edge visualization techniques to empower decision-makers in a competitive rental market.*

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request. Refer to `CONTRIBUTING.md` for guidelines on code style and branch management.

## Contact

For questions, feedback, or support, please reach out to the project team:

- **Pedro Pires**: pedro.pires@example.com
- **Liandro Cruz**: liandro.cruz@example.com
- **José Novais**: jose.novais@example.com

Thank you for your interest in this project!
```
