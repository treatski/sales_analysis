import pandas as pd
def load_data():
    df_contracts = pd.read_csv('../data/contracts.csv')
    df_customers = pd.read_csv('../data/customers.csv')
    return df_contracts, df_customers
    
def combined_data(df_contracts, df_customers):
    df_customers.rename(columns={'id':'customer_id'}, inplace = True)
    df_customers.set_index('customer_id', inplace = True)
    df_contracts.set_index('customer_id', inplace = True)
    df = df_contracts.join(df_customers, how='left')
    return df


#def clean_data(df): 