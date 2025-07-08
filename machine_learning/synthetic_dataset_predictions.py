import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import torch
from torch.utils.data import TensorDataset, DataLoader
import matplotlib.pyplot as plt
import seaborn as sns
import torch.nn as nn
import torch.optim as optim

num_samples = 30000
num_features = 10
X = np.random.rand(num_samples, num_features)
weights = np.random.rand(num_features)
y = X.dot(weights) + 0.5 * np.sin(X[:, 0]) + np.random.normal(0, 0.1, num_samples)
# Convert to DataFrame for easier handling
feature_columns = [f'feature_{i+1}' for i in range(num_features)]
dataset = pd.DataFrame(X, columns=feature_columns)
dataset['target'] = y

# Preview the dataset
print(dataset.shape)
dataset.to_csv('master_dataset.csv', index=False)

train_data, temp_data = train_test_split(dataset, test_size=0.3, random_state=42)
validate_data, test_data = train_test_split(temp_data, test_size=0.5, random_state=42)

# Check the sizes of each split
train_size = train_data.shape[0]
validate_size = validate_data.shape[0]
test_size = test_data.shape[0]

train_size, validate_size, test_size
train_data.to_csv("train_data.csv", index=False)
test_data.to_csv("test_data.csv", index=False)
validate_data.to_csv("validate_data.csv", index=False)
temp_data.to_csv("temp_data.csv", index=False)
# Convert dataframes to tensors
X_train = torch.tensor(train_data[feature_columns].values, dtype=torch.float32)
y_train = torch.tensor(train_data['target'].values, dtype=torch.float32).view(-1, 1)

X_validate = torch.tensor(validate_data[feature_columns].values, dtype=torch.float32)
y_validate = torch.tensor(validate_data['target'].values, dtype=torch.float32).view(-1, 1)

X_test = torch.tensor(test_data[feature_columns].values, dtype=torch.float32)
y_test = torch.tensor(test_data['target'].values, dtype=torch.float32).view(-1, 1)

# Create TensorDatasets
train_dataset = TensorDataset(X_train, y_train)
validate_dataset = TensorDataset(X_validate, y_validate)
test_dataset = TensorDataset(X_test, y_test)

# Create DataLoaders
batch_size = 256
train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
validate_loader = DataLoader(validate_dataset, batch_size=batch_size, shuffle=False)
test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)

train_loader, validate_loader, test_loader
# 1. Define a PyTorch Model
class SimpleRegressionModel(nn.Module):
    def __init__(self, input_features):
        super(SimpleRegressionModel, self).__init__()
        self.fc1 = nn.Linear(input_features, 64)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(64, 32)
        self.fc3 = nn.Linear(32, 1) # Output a single regression value

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        x = self.relu(x)
        x = self.fc3(x)
        return x

model = SimpleRegressionModel(num_features)

# 2. Define Loss Function and Optimizer
criterion = nn.MSELoss() # Mean Squared Error for regression
optimizer = optim.Adam(model.parameters(), lr=0.001)

# 3. Implement Training Loop and 4. Evaluation Loop
num_epochs = 50 # Reduced for quicker visualization
train_losses = []
validate_losses = []

for epoch in range(num_epochs):
    # Training
    model.train() # Set model to training mode
    running_train_loss = 0.0
    for inputs, targets in train_loader:
        optimizer.zero_grad() # Clear gradients
        outputs = model(inputs)
        loss = criterion(outputs, targets)
        loss.backward() # Backpropagation
        optimizer.step() # Update weights
        running_train_loss += loss.item() * inputs.size(0)
    epoch_train_loss = running_train_loss / len(train_loader.dataset)
    train_losses.append(epoch_train_loss)

    # Validation
    model.eval() # Set model to evaluation mode
    running_validate_loss = 0.0
    with torch.no_grad(): # Disable gradient calculation during validation
        for inputs, targets in validate_loader:
            outputs = model(inputs)
            loss = criterion(outputs, targets)
            running_validate_loss += loss.item() * inputs.size(0)
    epoch_validate_loss = running_validate_loss / len(validate_loader.dataset)
    validate_losses.append(epoch_validate_loss)

    if (epoch + 1) % 10 == 0:
        print(f'Epoch [{epoch+1}/{num_epochs}], '
              f'Train Loss: {epoch_train_loss:.4f}, '
              f'Validate Loss: {epoch_validate_loss:.4f}')

# 5. Make Predictions on a Small Sample for Visualization
model.eval()
with torch.no_grad():
    # Take a small sample from the test set for visualization
    sample_size = 50
    sample_indices = np.random.choice(len(X_test), sample_size, replace=False)
    X_test_sample = X_test[sample_indices]
    y_test_sample = y_test[sample_indices]

    predictions_sample = model(X_test_sample)

    # Convert to numpy for plotting
    y_test_sample_np = y_test_sample.cpu().numpy().flatten()
    predictions_sample_np = predictions_sample.cpu().numpy().flatten()

# --- Visualization ---

# 1. Training and Validation Loss Plot
plt.figure(figsize=(10, 6))
plt.plot(train_losses, label='Training Loss')
plt.plot(validate_losses, label='Validation Loss')
plt.title('Training and Validation Loss Over Epochs')
plt.xlabel('Epoch')
plt.ylabel('Loss (MSE)')
plt.legend()
plt.grid(True)
plt.show()

# 2. Actual vs. Predicted Values (on a small test sample)
plt.figure(figsize=(10, 6))
sns.scatterplot(x=y_test_sample_np, y=predictions_sample_np, alpha=0.7)
plt.plot([min(y_test_sample_np), max(y_test_sample_np)], [min(y_test_sample_np), max(y_test_sample_np)], color='red', linestyle='--', label='Perfect Prediction Line')
plt.title('Actual vs. Predicted Values (Test Sample)')
plt.xlabel('Actual Target Value')
plt.ylabel('Predicted Target Value')
plt.legend()
plt.grid(True)
plt.show()

# 3. Residuals Plot (on a small test sample)
residuals = y_test_sample_np - predictions_sample_np
plt.figure(figsize=(10, 6))
sns.scatterplot(x=predictions_sample_np, y=residuals, alpha=0.7)
plt.axhline(y=0, color='red', linestyle='--', label='Zero Residuals Line')
plt.title('Residuals Plot (Test Sample)')
plt.xlabel('Predicted Value')
plt.ylabel('Residual (Actual - Predicted)')
plt.legend()
plt.grid(True)
plt.show()

# If you want to see the distribution of actual vs. predicted values for the whole test set:
# (This might be too dense for very large test sets, but good for understanding distribution)
model.eval()
with torch.no_grad():
    all_test_predictions = []
    for inputs, _ in test_loader:
        outputs = model(inputs)
        all_test_predictions.append(outputs.cpu().numpy())
    all_test_predictions_np = np.concatenate(all_test_predictions).flatten()
    y_test_np = y_test.cpu().numpy().flatten()

plt.figure(figsize=(12, 6))
sns.histplot(y_test_np, color='blue', label='Actual Values', kde=True, stat='density', alpha=0.6)
sns.histplot(all_test_predictions_np, color='green', label='Predicted Values', kde=True, stat='density', alpha=0.6)
plt.title('Distribution of Actual vs. Predicted Values (Full Test Set)')
plt.xlabel('Value')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()
