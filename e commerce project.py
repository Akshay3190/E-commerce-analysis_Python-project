#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import plotly.express as px               # for data visualisation 
import plotly.graph_objects as go         # for advanced & customisable graphs 
import plotly.io as pio                   # for customisable graph templates 
import plotly.colors as colors
pio.templates.defaults = "plotly_white"   # for default white them


# # Import the dataset

# In[2]:


data = pd.read_csv("C:\\DATA ANALYSIS\\PYTHON\\E commerce sales analysis\\Sample - Superstore.csv", encoding='latin-1')


# In[3]:


data.head()


# In[4]:


data.tail()


# In[5]:


data.info()


# # Let’s start by looking at the descriptive statistics of the dataset

# In[6]:


data.describe()


# # Converting Date column

# In[7]:


data['Order Date'] = pd.to_datetime(data['Order Date'])
data['Ship Date'] = pd.to_datetime(data['Ship Date'])


# In[8]:


data.info()


# # Adding New Date-based Columns

# In[10]:


data['Order Month'] = data['Order Date'].dt.month
data['Order Year'] = data['Order Date'].dt.year
data['Order Day of Week'] = data['Order Date'].dt.dayofweek


# In[11]:


data.head()


# # Monthly Sales Analysis

# In[12]:


sales_by_month = data.groupby('Order Month')['Sales'].sum().reset_index()
fig = px.line(sales_by_month, 
              x='Order Month', 
              y='Sales', 
              title='Monthly Sales Analysis')
fig.show()


# # Sales Analysis by Category

# In[15]:


sales_by_category = data.groupby('Category')['Sales'].sum().reset_index()


# In[16]:


sales_by_category


# In[27]:


fig = px.pie(sales_by_category,
             values='Sales',
             names='Category',
             hole=0.5,
             color_discrete_sequence=px.colors.qualitative.Pastel)

fig.update_traces(textposition='inside', textinfo='percent+label')
fig.update_layout(title_text='Sales Analysis by Category', title_font=dict(size=24))

fig.show()


# # Sales Analysis by Sub-category

# In[29]:


sales_by_subcategory = data.groupby('Sub-Category')['Sales'].sum().reset_index()
fig = px.bar(sales_by_subcategory, 
              x='Sub-Category', 
              y='Sales', 
              title='Sales Analysis by Sub-Category')
fig.show()


# # Monthly Profit Analysis

# In[58]:


profit_by_month = data.groupby('Order Month')['Profit'].sum().reset_index()
fig = px.line(profit_by_month, 
              x='Order Month', 
              y='Profit', 
              title='Monthly profit Analysis')

fig.update_traces(line_color='darkred')

fig.update_layout(
    plot_bgcolor='white',  # Background color of the plotting area
    paper_bgcolor='white'   # Background color of the entire figure
)

fig.show()


# # Profit Analysis by Category

# In[46]:


profit_by_category = data.groupby('Category')['Profit'].sum().reset_index()

fig = px.pie(profit_by_category,
             values='Profit',
             names='Category',
             hole=0.5,
             color_discrete_sequence=px.colors.qualitative.Set2)

fig.update_traces(textposition='inside', textinfo='percent+label')
fig.update_layout(title_text='Profit Analysis by Category', title_font=dict(size=24))

fig.show()


# # Proft Analysis by Sub-category

# In[60]:


profit_by_subcategory = data.groupby('Sub-Category')['Profit'].sum().reset_index()
fig = px.bar(profit_by_subcategory, 
              x='Sub-Category', 
              y='Profit', 
              title='Profit Analysis by Sub-Category')

fig.update_traces(marker_color='#4dd500')

fig.update_layout(
    plot_bgcolor='white',  # Background color of the plotting area
    paper_bgcolor='white'   # Background color of the entire figure
)

fig.show()


# # Sales and Profit Analysis by Customer Segment

# In[65]:


unique_segments=data['Segment'].unique()
print(unique_segments)


# In[69]:


sales_profit_by_segment = data.groupby('Segment').agg({'Sales': 'sum', 'Profit': 'sum'}).reset_index()

color_palette = colors.qualitative.Set2

fig = go.Figure()
fig.add_trace(go.Bar(x=sales_profit_by_segment['Segment'], 
                     y=sales_profit_by_segment['Sales'], 
                     name='Sales',
                     marker_color=color_palette[0]))

fig.add_trace(go.Bar(x=sales_profit_by_segment['Segment'], 
                     y=sales_profit_by_segment['Profit'], 
                     name='Profit',
                     marker_color=color_palette[1]))

fig.update_layout(title='Sales and Profit Analysis by Customer Segment',
                  xaxis_title='Customer Segment', yaxis_title='Amount')

fig.show()


# # Analysis of Sales to Profit Ratio

# In[73]:


sales_profit_by_segment = data.groupby('Segment').agg({'Sales': 'sum', 'Profit': 'sum'}).reset_index()
sales_profit_by_segment['Sales_to_Profit_Ratio'] = sales_profit_by_segment['Sales']/sales_profit_by_segment['Profit']

print(sales_profit_by_segment[['Segment','Sales_to_Profit_Ratio']])


# In[ ]:




