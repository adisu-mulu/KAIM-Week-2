import pandas as pd

# class UserOverview:
#     def __init__(self):
#         pass

#     def read_data(self, path):
#         return pd.read_csv(self.path)

def read_data(path):
    return pd.read_csv(path)

def user_aggregated_data(data):
    aggregate= data.groupby('MSISDN/Number').agg(
     # Step 2: Count the number of xDR sessions per user
     Number_of_xDR_Sessions=('Bearer Id', 'count'),
    
     # Step 3: Calculate the total session duration per user
     Total_Session_Duration=('Dur. (ms)', 'sum'),
    
     # Step 4: Sum the total downloaded data per user
     Total_DL_Data=('Total DL (Bytes)', 'sum'),
    
     # Step 5: Sum the total uploaded data per user
     Total_UL_Data=('Total UL (Bytes)', 'sum')
        )

    # Step 6: Add a new column for total data volume (DL + UL)
    aggregate['Total_Data_Volume'] = aggregate['Total_DL_Data'] + aggregate['Total_UL_Data']

    # # Step 7: Reset the index to turn the grouped data back into a DataFrame
    aggregate = aggregate.reset_index()
    return aggregate