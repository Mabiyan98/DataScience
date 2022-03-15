"""
Name:  Muhammad Abiyan
Email: Muhammad.abiyan31@myhunter.cuny.edu
Resources: NYC Department of City Planning (DCP) Housing Database
lecture 8 slides
"""

import pandas as pd

def make_housing_df(file_name):
    df = pd.read_csv(file_name)
    df = df.dropna(subset=['total'])
    df = df.rename(columns={"nta2010": "NTA Code"})

    return df

def make_pop_df(file_name):
    df = pd.read_csv(file_name)
    df = df[df['Year'] == 2010]
    return df

def combine_df(housing_df, pop_df, cols):
#Returns a DataFrame that merges the two inputted DataFrames
#on their common key, NTA Code. The returned DataFrame should
    df = pd.merge(housing_df, pop_df, on='NTA Code')
#include only the columns specified in cols.
    df = df[cols]
    
    return df

def compute_density(df, col = 'Density'):
    df = df.assign(col = df['Population']/df['Shape__Area'])
    return df

def most_corr(df, y = 'total', xes = ['Population','Shape__Area','Density','comp2010']):
#Returns the column name and Pearson's R correlation
#coefficient from xes that has the highest absolute correlation with y
    return 0

def convert_std_units(ser):

    return ser
        
    
    

