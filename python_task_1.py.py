#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


# In[3]:


dataset_path=pd.read_csv(r"C:\Users\karan\Downloads\dataset-1.csv")
dataset_path


# In[4]:


import pandas as pd

def generate_car_matrix(dataset_path):
    # Read the dataset into a DataFrame
    df = pd.read_csv(r"C:\Users\karan\Downloads\dataset-1.csv")

    # Create a pivot table using id_1, id_2, and car columns
    car_matrix = df.pivot(index='id_1', columns='id_2', values='car')

    # Fill NaN values with 0
    car_matrix = car_matrix.fillna(0)

    # Set diagonal values to 0
    for i in car_matrix.index:
        if i in car_matrix.columns:
            car_matrix.at[i, i] = 0

    return car_matrix

# Example usage
dataset_path = 'dataset-1.csv'
result_matrix = generate_car_matrix(dataset_path)
print(result_matrix)


# In[5]:




def get_type_count(dataset_path):
    # Read the dataset into a DataFrame
    df = pd.read_csv(r"C:\Users\karan\Downloads\dataset-1.csv")

    # Add a new categorical column 'car_type' based on the values of the 'car' column
    conditions = [
        (df['car'] <= 15),
        (df['car'] > 15) & (df['car'] <= 25),
        (df['car'] > 25)
    ]
    choices = ['low', 'medium', 'high']
    df['car_type'] = pd.cut(df['car'], bins=[-float('inf'), 15, 25, float('inf')], labels=choices)

    # Calculate the count of occurrences for each car_type category
    type_count = df['car_type'].value_counts().to_dict()

    # Sort the dictionary alphabetically based on keys
    type_count = dict(sorted(type_count.items()))

    return type_count

# Example usage
dataset_path = 'dataset-1.csv'
result_count = get_type_count(dataset_path)
print(result_count)


# In[6]:


import pandas as pd

def get_bus_indexes(dataset_path):
    # Read the dataset into a DataFrame
    df = pd.read_csv(r"C:\Users\karan\Downloads\dataset-1.csv")

    # Calculate the mean value of the 'bus' column
    mean_bus = df['bus'].mean()

    # Identify indices where the 'bus' values are greater than twice the mean
    bus_indexes = df[df['bus'] > 2 * mean_bus].index.tolist()

    # Sort the indices in ascending order
    bus_indexes.sort()

    return bus_indexes

# Example usage
dataset_path = 'dataset-1.csv'
result_indexes = get_bus_indexes(dataset_path)
print(result_indexes)


# In[7]:


import pandas as pd

def filter_routes(dataset_path):
    # Read the dataset into a DataFrame
    df = pd.read_csv(r"C:\Users\karan\Downloads\dataset-1.csv")

    # Group by 'route' and calculate the average of the 'truck' column
    route_avg_truck = df.groupby('route')['truck'].mean()

    # Filter routes where the average of 'truck' column is greater than 7
    selected_routes = route_avg_truck[route_avg_truck > 7].index.tolist()

    # Sort the list of selected routes
    selected_routes.sort()

    return selected_routes

# Example usage
dataset_path = 'dataset-1.csv'
result_routes = filter_routes(dataset_path)
print(result_routes)


# In[8]:


def multiply_matrix(result_matrix):
    # Create a copy of the DataFrame to avoid modifying the original
    modified_matrix = result_matrix.copy()

    # Apply the specified logic to modify values
    modified_matrix = modified_matrix.applymap(lambda x: x * 0.75 if x > 20 else x * 1.25)

    # Round values to 1 decimal place
    modified_matrix = modified_matrix.round(1)

    return modified_matrix

# Example usage
# Assuming result_matrix is the DataFrame obtained from Question 1
result_matrix = generate_car_matrix('dataset-1.csv')
modified_result = multiply_matrix(result_matrix)
print(modified_result)


# In[24]:


import pandas as pd

def check_time_completeness(df):
    # Replace 'timestamp_column_name' with the actual column name in your dataset
    timestamp_column_name = 'startTime'
    
    # Convert the timestamp column to datetime format
    df[timestamp_column_name] = pd.to_datetime(df[timestamp_column_name])
    
    # Create a column for the day of the week (Monday=0, Sunday=6)
    df['day_of_week'] = df[timestamp_column_name].dt.dayofweek
    
    # Check if the timestamps cover a full 24-hour period and span all 7 days for each (id, id_2) pair
    completeness_check = df.groupby(['id', 'id_2']).apply(lambda group: (
        group[timestamp_column_name].min().time() == pd.Timestamp('00:00:00').time() and
        group[timestamp_column_name].max().time() == pd.Timestamp('23:59:59').time() and
        set(group['day_of_week']) == set(range(7))
    ))
    
    return completeness_check

# Example usage
# Assuming df is the DataFrame loaded from dataset-2.csv
df = pd.read_csv(r"C:\Users\karan\Downloads\dataset-2.csv")
completeness_series = check_time_completeness(df)
print(completeness_series)


# In[ ]:




