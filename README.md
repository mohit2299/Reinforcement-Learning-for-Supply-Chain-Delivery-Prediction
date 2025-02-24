# Supply Chain Optimization Project

This repository demonstrates two approaches for improving supply chain operations:

1. **Reinforcement Learning for Delivery Prediction:**  
   The project preprocesses a supply chain dataset and builds an RL environment with a Deep Q-Network (DQN) agent that learns to predict delivery status. The agent is trained and tested on this dataset.

2. **Route Optimization and Visualization:**  
   This part takes a user-provided list of cities, geocodes them, computes an (approximate) optimized route using a greedy nearest-neighbour algorithm, estimates travel time between cities (based on an assumption of 600 miles per day), and visualizes the route on an interactive map.

## Data Source

The dataset used in this project is obtained from [Kaggle](https://www.kaggle.com/).  
*Please note: you must download the dataset (e.g., `DataCoSupplyChainDataset.csv.zip`) from Kaggle and place it in the appropriate directory (or update the file path in the code).*



