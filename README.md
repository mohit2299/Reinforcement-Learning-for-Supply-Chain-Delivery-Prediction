# Supply Chain Optimization Project

This repository demonstrates two approaches for improving supply chain operations:

1. **Reinforcement Learning for Delivery Prediction:**  
   The project preprocesses a supply chain dataset and builds an RL environment with a Deep Q-network (DQN) agent that learns to predict delivery status. The agent is trained and tested on this dataset.

2. **Route Optimization and Visualization:**  
   This part takes a user-provided list of cities, geocodes them, computes an (approximate) optimized route using a greedy nearest-neighbour algorithm, estimates travel time between cities (based on an assumption of 600 miles per day), and visualizes the route on an interactive map.

## Data Source

The dataset used in this project is obtained from [Kaggle](https://www.kaggle.com/).  
*Please note: you must download the dataset (e.g., `DataCoSupplyChainDataset.csv.zip`) from Kaggle and place it in the appropriate directory (or update the file path in the code).*

Algorithm Overview
This project combines two complementary approaches to supply chain optimization:

1. Reinforcement Learning for Delivery Prediction
Approach:
A Deep Q-Network (DQN) agent is trained to predict delivery status using a custom RL environment. Each data row (from a Kaggle-sourced supply chain dataset) is treated as a state, with features scaled and processed (including time-based features). The agent learns via experience replay and an epsilon-greedy strategy, receiving +1 for correct predictions and -1 for incorrect ones.
Data Structures:
Utilizes Pandas DataFrames for data storage, NumPy arrays for states, and a Python list for replay memory.
Limitations & Improvements:
The DQN can be sensitive to hyperparameters and may require extensive data and tuning. Enhancements could include advanced DQN variants (Double/Dueling DQN, Prioritized Experience Replay), richer feature integration, and systematic hyperparameter optimization.
2. Route Optimization for Visualizing Supply Chain Routes
Approach:
A greedy nearest-neighbour (heuristic TSP) algorithm determines an approximate optimized route between user-specified cities. The algorithm starts from the first city and then iteratively chooses the closest unvisited city (using the Haversine formula to compute distances). Estimated travel times are calculated assuming a truck travels 600 miles daily, and the route is visualized with Folium.
Data Structures:


It uses a dictionary to map city names to coordinates, a list to store the computed route order, and a set to manage unvisited cities.
Limitations & Improvements:
As a heuristic, the greedy approach does not guarantee a globally optimal route and is sensitive to the starting city. Future improvements include 2-opt/3-opt local search, metaheuristics (like simulated annealing or genetic algorithms), and incorporation of real-world constraints (e.g., traffic, delivery windows).

Our solution goes beyond basic navigation. It: 
1. Integrates supply chain data (delivery performance, costs, etc.) into the routing decision.
2. Uses custom constraints and objectives tailored to business needs.
3. Leverages reinforcement learning to learn from historical data and provide proactive, context-specific insights.
4. In short, it’s a domain-specific, customizable tool focused on business metrics rather than just distance or time.
