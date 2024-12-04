### README for EV Analysis Project

#### Overview
This repository provides a suite of tools and scripts for analyzing and visualizing electric vehicle (EV) charging station data, infrastructure optimization, and vehicle fuel type trends. It includes Python scripts and Jupyter notebooks, offering flexibility in running and customizing analyses.

---

#### Repository Contents

1. **Config and Setup Files**
   - `config.json`: API settings for fetching EV station data.
   - `requirements.txt`: Lists Python dependencies needed for the project.

2. **Jupyter Notebooks** (Also runnable as Python scripts)
   - `EV_Station_Data_Processing.ipynb`: Processes EV station data using the NREL API.
   - `EV_Charging_Stations_Analysis_and_Mapping.ipynb`: Maps and analyzes charging station locations.
   - `Shortest_Path_Visualization.ipynb`: Visualizes shortest paths for EV routes.
   - `VFT_Analysis_Visualization_2018_2023.ipynb`: Analyzes fuel type trends over time.
   - `EV_Analysis_Poisson_Monte_Carlo_Dashboard.ipynb`: Uses Monte Carlo methods for statistical dashboards.

3. **Python Files**
   - `EV_Station_Data_Processing.py`: Automates running the corresponding notebook.
   - `EV_Charging_Stations_Analysis_and_Mapping.py`: Automates running the mapping and analysis notebook.
   - `Shortest_Path_Visualization.py`: Automates running the shortest path visualization notebook.
   - `VFT_Analysis_Visualization_2018_2023.py`: Automates running the fuel type trends analysis notebook.
   - `EV_Analysis_Poisson_Monte_Carlo_Dashboard.py`: Automates running the dashboard notebook.

---

#### Getting Started

1. **Clone the Repository**
   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```

2. **Install Requirements**
   Use a Python virtual environment and install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up the Config File**
   Update `config.json` with your API key and desired settings:
   ```json
   {
     "api_key": "<your_api_key>",
     "base_url": "https://developer.nrel.gov/api/alt-fuel-stations/v1",
     "state": "CA",
     "fuel_type": "ELEC"
   }
   ```

---

#### Running the Project

**Order of Execution**  
Run the files in the following sequence for a complete analysis:

1. **EV Station Data Processing**
   ```bash
   python EV_Station_Data_Processing.py
   ```
   - Retrieves and cleans data from the NREL API.

2. **EV Charging Stations Analysis and Mapping**
   ```bash
   python EV_Charging_Stations_Analysis_and_Mapping.py
   ```
   - Generates geospatial visualizations and summaries of EV station data.

3. **Shortest Path Visualization**
   ```bash
   python Shortest_Path_Visualization.py
   ```
   - Visualizes optimized EV travel routes.

4. **Vehicle Fuel Type Trends Analysis**
   ```bash
   python VFT_Analysis_Visualization_2018_2023.py
   ```
   - Analyzes trends in vehicle fuel types over time.

5. **EV Analysis Poisson Monte Carlo Dashboard**
   ```bash
   python EV_Analysis_Poisson_Monte_Carlo_Dashboard.py
   ```
   - Creates statistical dashboards for EV station data.

---

#### Features
- **Dynamic Visualizations**: Interactive maps for EV stations and routes.
- **Geospatial Analysis**: Uses tools like `folium` and `geopandas`.
- **Trend Analysis**: Time-series insights on vehicle fuel types.

---

#### Additional Notes
- **Python Version**: Use Python 3.7 or higher.
- **Interactive Outputs**: HTML maps are saved in the `Interactive_output` directory for exploration.
- **Customizability**: Modify parameters in the notebooks or scripts for tailored analyses.

---

#### Contributing
Contributions are welcome! Fork the repository and submit a pull request for improvements or new features.

---

#### License
This project is licensed under the MIT License. See `LICENSE` for details.

Let me know if further customization or clarification is needed!
