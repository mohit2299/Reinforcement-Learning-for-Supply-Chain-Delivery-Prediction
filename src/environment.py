import numpy as np

class SupplyChainEnv:
    def __init__(self, data):
        self.data = data
        self.current_step = 0
        # Set max_steps to the total number of rows minus one.
        self.max_steps = len(data) - 1

    def reset(self):
        self.current_step = 0
        return self._get_state()

    def step(self, action):
        # Calculate reward for the current state.
        reward = self._calculate_reward(action)
        # Advance the step.
        self.current_step += 1
        done = self.current_step >= self.max_steps
        next_state = self._get_state() if not done else np.zeros(self.state_size())
        return next_state, reward, done

    def _get_state(self):
        # Return state features (all columns except 'Delivery Status').
        row = self.data.iloc[self.current_step]
        return row.drop('Delivery Status').values

    def _calculate_reward(self, action):
        actual_status = self.data.iloc[self.current_step]['Delivery Status']
        return 1 if action == actual_status else -1

    def state_size(self):
        # Return the number of state features.
        return self.data.drop('Delivery Status', axis=1).shape[1]
