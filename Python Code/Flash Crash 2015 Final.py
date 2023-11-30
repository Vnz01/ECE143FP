#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import datetime

import plotly.express as px


# In[2]:


#Reading the data(csv file)
exchange_rates_df = pd.read_csv('../Downloaded Database/euro-daily-hist_1999_2022.csv')
exchange_rates_df.info()


# In[3]:


#The reason why the dtype of some of the columns is 'object' is because there's '-' at some places, which is a string

exchange_rates_df.loc[exchange_rates_df['[Swiss franc ]'] == '-']


# In[4]:


# setting Period\Unit as the index

exchange_rates_df.rename(columns = {'[Swiss franc ]': 'CHF', 'Period\\Unit:' : 'Time'}, inplace = True)
exchange_rates_df['Time'] = pd.to_datetime(exchange_rates_df['Time'])
exchange_rates_df.sort_values('Time', inplace = True)
exchange_rates_df.reset_index(drop = True, inplace = True)

exchange_rates_df.set_index(['Time'], inplace=True)
exchange_rates_df.head()


# In[5]:


#Replace '-'s and interpret the numbers as floats

exchange_rates_df = exchange_rates_df.replace('-', np.nan).astype(float)
exchange_rates_df.head()


# In[6]:


px.line(exchange_rates_df)


# ## Slide 1 plot - EUR-CHF Exchange Rate

# In[7]:


import plotly.graph_objects as go


# In[8]:


#Setting the colors and thresholds for the graph
segment_colors = {
    1: '#219C90',
    2: '#E9B824',
    3: '#D83F31',
    4: '#EE9322'
}

date_threshold_zero = '1990-10-01'
date_threshold_one = '2007-10-01'
date_threshold_two = '2011-08-10'
date_threshold_three = '2015-01-23'
date_threshold_four = '2027-10-01'

segment_names = {
    1: 'The Beginning',
    2: 'Financial Crisis',
    3: 'SNB Peg',
    4: 'Recent Times'
}

line_width=2

plot_title = "EUR/CHF exchange rates"
xaxis_title = "Date"
yaxis_title = "Exchange Rate"


# In[9]:


# Initialization
slide_one_plot = go.Figure()


# Segment one - The Beginning
mask = (exchange_rates_df.index >= date_threshold_zero) & (exchange_rates_df.index < date_threshold_one)
slide_one_plot.add_trace(
    go.Scatter(
        x=exchange_rates_df[mask].index,
        y=exchange_rates_df.loc[mask, 'CHF'],
        name=segment_names[1],
        line=dict(color=segment_colors[1], width=line_width)
    )
)


#Segment two - Global Financial Crisis
mask = (exchange_rates_df.index >= date_threshold_one) & (exchange_rates_df.index < date_threshold_two)
slide_one_plot.add_trace(
    go.Scatter(
        x=exchange_rates_df[mask].index,
        y=exchange_rates_df.loc[mask, 'CHF'],
        name=segment_names[2],
        line=dict(color=segment_colors[2], width=line_width)
    )
)

#Segment three - SNB Peg
mask = (exchange_rates_df.index >= date_threshold_two) & (exchange_rates_df.index < date_threshold_three)
slide_one_plot.add_trace(
    go.Scatter(
        x=exchange_rates_df[mask].index,
        y=exchange_rates_df.loc[mask, 'CHF'],
        name=segment_names[3],
        line=dict(color=segment_colors[3], width=line_width)
    )
)

#Segment four - Recent times
mask = (exchange_rates_df.index >= date_threshold_three) & (exchange_rates_df.index < date_threshold_four)
slide_one_plot.add_trace(
    go.Scatter(
        x=exchange_rates_df[mask].index,
        y=exchange_rates_df.loc[mask, 'CHF'],
        name=segment_names[4],
        line=dict(color=segment_colors[4], width=line_width)
    )
)

#Adding titles and annotations
slide_one_plot.update_layout(
    title=plot_title,
    xaxis_title=xaxis_title,
    yaxis_title=yaxis_title,
    legend_title="EUR-CHF exchange rates",
    font=dict(
        # family="Courier New, monospace",
        size=14,
        color="#000000"
    )
)

slide_one_plot.add_annotation(
    x='2002-08-01',
    y=1.59,
    text="The Beginning",
    showarrow=False,
    yshift=10,
    textangle=0,
)

slide_one_plot.add_annotation(
    x='2008-10-30',
    y=1.6803,
    text="The Peak(EUR-CHF peaks in 2007)",
    showarrow=False,
    yshift=10,
    textangle=0,
)

slide_one_plot.add_annotation(
    x='2009-03-01',
    y=1.31,
    text="Global",
    showarrow=False,
    yshift=10,
    textangle=0,
)

slide_one_plot.add_annotation(
    x='2009-03-01',
    y=1.27,
    text="Financial",
    showarrow=False,
    yshift=10,
    textangle=0,
)

slide_one_plot.add_annotation(
    x='2009-03-01',
    y=1.23,
    text="Crisis",
    showarrow=False,
    yshift=10,
    textangle=0,
)

slide_one_plot.add_annotation(
    x='2013-05-01',
    y=1.24,
    text="SNB Peg",
    showarrow=False,
    yshift=10,
    textangle=0,
)

slide_one_plot.add_annotation(
    x='2018-07-01',
    y=1,
    text="Recent Times",
    showarrow=False,
    yshift=10,
    textangle=0,
)

slide_one_plot.add_vline(x='2007-09-28', line_width=1, line_dash="dash", line_color="grey")
slide_one_plot.add_vline(x='2011-08-11', line_width=1, line_dash="dash", line_color="grey")
slide_one_plot.add_vline(x='2015-01-23', line_width=1, line_dash="dash", line_color="grey")


slide_one_plot.show()


# ## Slide 2 - plot 1

# In[10]:


#Setting the colors and threshold for the graph for Segment One - The Beginning
plot_one_segment_colors = {
    1: '#435334',
    2: segment_colors[1],
    3: '#004225',
    4: segment_colors[1]
}

plot_one_date_threshold_zero = date_threshold_zero
plot_one_date_threshold_one = '2000-03-20'
plot_one_date_threshold_two = '2003-03-05'
plot_one_date_threshold_three = '2004-03-08'
plot_one_date_threshold_four = date_threshold_one

plot_one_segment_names = {
    1: 'Pegged at 1.6',
    2: '2002-2003',
    3: 'Euro Strengthening',
    4: '2003-2007'
}

line_width=1.5
line_width_bold = 2

plot_one_title = "The beginning"
xaxis_title = "Date"
yaxis_title = "Exchange Rate"


# In[11]:


#Initialization
slide_two_plot = go.Figure()


# Subsegment one - Pegged at 1.6
mask = (exchange_rates_df.index >= plot_one_date_threshold_zero) & (exchange_rates_df.index < plot_one_date_threshold_one)
slide_two_plot.add_trace(
    go.Scatter(
        x=exchange_rates_df[mask].index,
        y=exchange_rates_df.loc[mask, 'CHF'],
        name=plot_one_segment_names[1],
        line=dict(color=plot_one_segment_colors[1], width=line_width_bold)
    )
)

# Subsegment two - 2002-2003
mask = (exchange_rates_df.index >= plot_one_date_threshold_one) & (exchange_rates_df.index < plot_one_date_threshold_two)
slide_two_plot.add_trace(
    go.Scatter(
        x=exchange_rates_df[mask].index,
        y=exchange_rates_df.loc[mask, 'CHF'],
        name=plot_one_segment_names[2],
        line=dict(color=plot_one_segment_colors[2], width=line_width)
    )
)

# Subsegment three - Euro Strengthening
mask = (exchange_rates_df.index >= plot_one_date_threshold_two) & (exchange_rates_df.index < plot_one_date_threshold_three)
slide_two_plot.add_trace(
    go.Scatter(
        x=exchange_rates_df[mask].index,
        y=exchange_rates_df.loc[mask, 'CHF'],
        name=plot_one_segment_names[3],
        line=dict(color=plot_one_segment_colors[3], width=line_width_bold)
    )
)

# Subsegment four - 2003-2007
mask = (exchange_rates_df.index >= plot_one_date_threshold_three) & (exchange_rates_df.index < plot_one_date_threshold_four)
slide_two_plot.add_trace(
    go.Scatter(
        x=exchange_rates_df[mask].index,
        y=exchange_rates_df.loc[mask, 'CHF'],
        name=plot_one_segment_names[4],
        line=dict(color=plot_one_segment_colors[4], width=line_width)
    )
)

#Adding annotations 
slide_two_plot.add_annotation(
    x='1999-09-01',
    y=1.64,
    text="Pegged at 1.6",
    showarrow=False,
    yshift=10,
    textangle=0,
    font=dict(size=12)
)

slide_two_plot.add_annotation(
    x='1999-09-01',
    y=1.62,
    text="1Euro = 1.6CHF",
    showarrow=False,
    yshift=10,
    textangle=0,
    font=dict(size=12)
)

slide_two_plot.add_annotation(
    x='2003-10-01',
    y=1.6,
    text="Euro",
    showarrow=False,
    yshift=10,
    textangle=0,
    font=dict(size=12)
)

slide_two_plot.add_annotation(
    x='2003-10-01',
    y=1.59,
    text="Strengthening",
    showarrow=False,
    yshift=10,
    textangle=0,
    font=dict(size=12)
)

slide_two_plot.update_layout(
    title=plot_one_title,
    xaxis_title=xaxis_title,
    yaxis_title=yaxis_title,
    legend_title="The Beginning",
    font=dict(
        # family="Courier New, monospace",
        size=14,
        color="#000000"
    )
)

slide_two_plot.add_vline(x='2000-03-20', line_width=1, line_dash="dash", line_color="grey")
slide_two_plot.add_vline(x='2003-03-05', line_width=1, line_dash="dash", line_color="grey")
slide_two_plot.add_vline(x='2004-03-08', line_width=1, line_dash="dash", line_color="grey")

slide_two_plot.show()


# ## Slide 2 - Part 3

# In[12]:


#Setting colors and threshold for the graph Segment Two - Gloabal Financial Crisis
plot_two_segment_colors = {
    1: segment_colors[2],
    2: '#CC3636',
    3: segment_colors[2],
    4: '#9C254D',
}

plot_two_date_threshold_zero = date_threshold_one
plot_two_date_threshold_one = '2008-09-22'
plot_two_date_threshold_two = '2008-10-27'
plot_two_date_threshold_three = '2011-03-11'
plot_two_date_threshold_four = date_threshold_two

plot_two_segment_names = {
    1: '2007-2008',
    2: 'Global Financial Crisis',
    3: '2008-2011',
    4: 'Eurozone debt crisis'
}

line_width=2
line_width_bold=3

plot_two_title = "Financial Crisis"
xaxis_title = "Date"
yaxis_title = "Exchange Rate"


# In[13]:


# Initialization
slide_two_plot = go.Figure()


# Subsegment one - 2007-2008
mask = (exchange_rates_df.index >= plot_two_date_threshold_zero) & (exchange_rates_df.index < plot_two_date_threshold_one)
slide_two_plot.add_trace(
    go.Scatter(
        x=exchange_rates_df[mask].index,
        y=exchange_rates_df.loc[mask, 'CHF'],
        name=plot_two_segment_names[1],
        line=dict(color=plot_two_segment_colors[1], width=line_width)
    )
)

# Subsegment two - Global Financial Crisis
mask = (exchange_rates_df.index >= plot_two_date_threshold_one) & (exchange_rates_df.index < plot_two_date_threshold_two)
slide_two_plot.add_trace(
    go.Scatter(
        x=exchange_rates_df[mask].index,
        y=exchange_rates_df.loc[mask, 'CHF'],
        name=plot_two_segment_names[2],
        line=dict(color=plot_two_segment_colors[2], width=3),
        mode='lines'
    ),
)

# Subsegment three - 2008-2011
mask = (exchange_rates_df.index >= plot_two_date_threshold_two) & (exchange_rates_df.index < plot_two_date_threshold_three)
slide_two_plot.add_trace(
    go.Scatter(
        x=exchange_rates_df[mask].index,
        y=exchange_rates_df.loc[mask, 'CHF'],
        name=plot_two_segment_names[3],
        line=dict(color=plot_two_segment_colors[3], width=line_width)
    )
)

# Subsegment four - Eurozone Debt Crisis
mask = (exchange_rates_df.index >= plot_two_date_threshold_three) & (exchange_rates_df.index < plot_two_date_threshold_four)
slide_two_plot.add_trace(
    go.Scatter(
        x=exchange_rates_df[mask].index,
        y=exchange_rates_df.loc[mask, 'CHF'],
        name=plot_two_segment_names[4],
        line=dict(color=plot_two_segment_colors[4], width=3)
    )
)

#Adding annotations 
slide_two_plot.add_annotation(
    x='2008-10-27',
    y=1.4,
    text="Global",
    showarrow=False,
    yshift=10,
    textangle=0,
    font=dict(size=12)
)

slide_two_plot.add_annotation(
    x='2008-10-27',
    y=1.37,
    text="Financial",
    showarrow=False,
    yshift=10,
    textangle=0,
    font=dict(size=12)
)

slide_two_plot.add_annotation(
    x='2008-10-27',
    y=1.34,
    text="Crisis",
    showarrow=False,
    yshift=10,
    textangle=0,
    font=dict(size=12)
)

slide_two_plot.add_annotation(
    x='2011-05-31',
    y=1.4,
    text="Eurozone",
    showarrow=False,
    yshift=10,
    textangle=0,
    font=dict(size=12)
    
)

slide_two_plot.add_annotation(
    x='2011-05-31',
    y=1.37,
    text="Debt",
    showarrow=False,
    yshift=10,
    textangle=0,
    font=dict(size=12)
)

slide_two_plot.add_annotation(
    x='2011-05-31',
    y=1.34,
    text="Crisis",
    showarrow=False,
    yshift=10,
    textangle=0,
    font=dict(size=12)
)

slide_two_plot.update_layout(
    title=plot_two_title,
    xaxis_title=xaxis_title,
    yaxis_title=yaxis_title,
    legend_title="Financial Crisis",
    font=dict(
        # family="Courier New, monospace",
        size=14,
        color="#000000"
    )
)

slide_two_plot.add_vline(x='2008-09-22', line_width=1, line_dash="dash", line_color="grey")
slide_two_plot.add_vline(x='2008-10-27', line_width=1, line_dash="dash", line_color="grey")
slide_two_plot.add_vline(x='2011-03-11', line_width=1, line_dash="dash", line_color="grey")


slide_two_plot.show()


# ## Slide 2 - plot 3

# In[14]:


#Adding colors and threshold for the graph - Segment Three - SNB Peg
plot_three_segment_colors = {
    1: '#A9A9A9',
    2: segment_colors[3],
    3: '#A9A9A9',
    4: segment_colors[3],
}

plot_three_date_threshold_zero = date_threshold_two
plot_three_date_threshold_one = '2012-04-05'
plot_three_date_threshold_two = '2012-09-05'
plot_three_date_threshold_three = '2014-12-17'
plot_three_date_threshold_four = date_threshold_three

plot_three_segment_names = {
    1: 'Euro rises',
    2: 'Pegged at 1.2',
    3: '2012-2014',
    4: 'Flash Crash'
}

line_width=2
line_width_bold=3.5

plot_three_title = "SNB Peg"
xaxis_title = "Date"
yaxis_title = "Spot exchange rate"


# In[15]:


# Initialization
slide_two_plot = go.Figure()


# Subsegment one - Euro rises
mask = (exchange_rates_df.index >= plot_three_date_threshold_zero) & (exchange_rates_df.index < plot_three_date_threshold_one)
slide_two_plot.add_trace(
    go.Scatter(
        x=exchange_rates_df[mask].index,
        y=exchange_rates_df.loc[mask, 'CHF'],
        name=plot_three_segment_names[1],
        line=dict(color=plot_three_segment_colors[1], width=line_width)
    )
)

# Subsegment two - Pegged at 1.2
mask = (exchange_rates_df.index >= plot_three_date_threshold_one) & (exchange_rates_df.index < plot_three_date_threshold_two)
slide_two_plot.add_trace(
    go.Scatter(
        x=exchange_rates_df[mask].index,
        y=exchange_rates_df.loc[mask, 'CHF'],
        name=plot_three_segment_names[2],
        line=dict(color=plot_three_segment_colors[2], width=line_width_bold),
        mode='lines'
    ),
)

# Subsegment three - 2012 -2014(Value stable at 1.2)
mask = (exchange_rates_df.index >= plot_three_date_threshold_two) & (exchange_rates_df.index < plot_three_date_threshold_three)
slide_two_plot.add_trace(
    go.Scatter(
        x=exchange_rates_df[mask].index,
        y=exchange_rates_df.loc[mask, 'CHF'],
        name=plot_three_segment_names[3],
        line=dict(color=plot_three_segment_colors[3], width=line_width)
    )
)

# Subsegment four - Flash Crash
mask = (exchange_rates_df.index >= plot_three_date_threshold_three) & (exchange_rates_df.index < plot_three_date_threshold_four)
slide_two_plot.add_trace(
    go.Scatter(
        x=exchange_rates_df[mask].index,
        y=exchange_rates_df.loc[mask, 'CHF'],
        name=plot_three_segment_names[4],
        line=dict(color=plot_three_segment_colors[4], width=line_width_bold),
        mode='lines'
    )
)

#Adding annotations
slide_two_plot.add_annotation(
    x='2012-05-31',
    y=1.17,
    text="Peg mantained at 1.2",
    showarrow=False,
    yshift=10,
    textangle=0,
    font=dict(size=12)
)

slide_two_plot.add_annotation(
    x='2014-10-01',
    y=1.1,
    text="Flash Crash",
    showarrow=False,
    textangle=0,
    font=dict(size=12)
)

slide_two_plot.add_annotation(
    x='2014-07-01',
    y=1.07,
    text="Value of Euro drops by 20%",
    showarrow=False,
    textangle=0,
    font=dict(size=12)
)


slide_two_plot.update_layout(
    title=plot_three_title,
    xaxis_title=xaxis_title,
    yaxis_title=yaxis_title,
    legend_title="SNB Peg",
    font=dict(
        size=14,
        color="#000000"
    )
)

slide_two_plot.add_vline(x='2012-04-10', line_width=1, line_dash="dash", line_color="grey")
slide_two_plot.add_vline(x='2012-09-05', line_width=1, line_dash="dash", line_color="grey")
slide_two_plot.add_vline(x='2014-12-17', line_width=1, line_dash="dash", line_color="grey")

slide_two_plot.show()


# ## Slide 2 - plot 4

# In[16]:


#Setting colors and thresholds for Segment four graph - Recent times
plot_four_segment_colors = {
    1: segment_colors[4],
    2: '#9A4444',
    3: segment_colors[4],
    4: '#9C254D',
}

plot_four_date_threshold_zero = date_threshold_three
plot_four_date_threshold_one = '2017-04-21'
plot_four_date_threshold_two = '2018-01-23'
plot_four_date_threshold_three = '2022-06-09'
plot_four_date_threshold_four = date_threshold_four

plot_four_segment_names = {
    1: '2015-2017',
    2: 'Euro rising (2017)',
    3: '2018-2022',
    4: 'Euro downfall (2022)'
}

line_width=2
line_width_bold=3

plot_four_title = "Recent Times"
xaxis_title = "Date"
yaxis_title = "Exchange rate"


# In[17]:


# Initialization
slide_two_plot = go.Figure()


# Subsegment one - 2015-2017
mask = (exchange_rates_df.index >= plot_four_date_threshold_zero) & (exchange_rates_df.index < plot_four_date_threshold_one)
slide_two_plot.add_trace(
    go.Scatter(
        x=exchange_rates_df[mask].index,
        y=exchange_rates_df.loc[mask, 'CHF'],
        name=plot_four_segment_names[1],
        line=dict(color=plot_four_segment_colors[1], width=line_width)
    )
)

# Subsegment two - Euro rising(2017)
mask = (exchange_rates_df.index >= plot_four_date_threshold_one) & (exchange_rates_df.index < plot_four_date_threshold_two)
slide_two_plot.add_trace(
    go.Scatter(
        x=exchange_rates_df[mask].index,
        y=exchange_rates_df.loc[mask, 'CHF'],
        name=plot_four_segment_names[2],
        line=dict(color=plot_four_segment_colors[2], width=line_width_bold),
        mode='lines'
    ),
)

# Subsegment three - (2018-2022)
mask = (exchange_rates_df.index >= plot_four_date_threshold_two) & (exchange_rates_df.index < plot_four_date_threshold_three)
slide_two_plot.add_trace(
    go.Scatter(
        x=exchange_rates_df[mask].index,
        y=exchange_rates_df.loc[mask, 'CHF'],
        name=plot_four_segment_names[3],
        line=dict(color=plot_four_segment_colors[3], width=line_width)
    )
)

# Subsegment four - Euro downfall
mask = (exchange_rates_df.index >= plot_four_date_threshold_three) & (exchange_rates_df.index < plot_four_date_threshold_four)
slide_two_plot.add_trace(
    go.Scatter(
        x=exchange_rates_df[mask].index,
        y=exchange_rates_df.loc[mask, 'CHF'],
        name=plot_four_segment_names[4],
        line=dict(color=plot_four_segment_colors[4], width=line_width_bold),
        mode='lines'
    )
)


slide_two_plot.update_layout(
    title=plot_four_title,
    xaxis_title=xaxis_title,
    yaxis_title=yaxis_title,
    legend_title="Recent times",
    font=dict(
        # family="Courier New, monospace",
        size=14,
        color="#000000"
    )
)

slide_two_plot.add_annotation(
    x='2023-01-01',
    y=1.05,
    text="Euro",
    showarrow=False,
    textangle=1.05,
    font=dict(size=12)
)

slide_two_plot.add_annotation(
    x='2023-01-01',
    y=1.03,
    text="Downfall",
    showarrow=False,
    textangle=1.05,
    font=dict(size=12)
)

slide_two_plot.add_annotation(
    x='2017-10-01',
    y=1.05,
    text="Euro rising again",
    showarrow=False,
    textangle=0,
    font=dict(size=12)
)

slide_two_plot.add_vline(x='2017-04-21', line_width=1, line_dash="dash", line_color="grey")
slide_two_plot.add_vline(x='2018-01-23', line_width=1, line_dash="dash", line_color="grey")
slide_two_plot.add_vline(x='2022-06-09', line_width=1, line_dash="dash", line_color="grey")

slide_two_plot.show()


# In[18]:


exchange_rates_df.std().sort_values()


# In[19]:


exchange_rates_df.corr()[['CHF']]


# In[20]:


exchange_rates_df.info(max_cols=100)


# In[21]:


exchange_rates_df


# In[22]:


def get_cagr(rates: pd.Series):
    '''
        Function that calculates the compund Annual Growth rate of currencies
        CAGR = (Ending date / Beginning date) ** (1/number of years)
        
        Parameters:
        Input: rates (float)
        Returns: CAGR
    '''
    
    initial_date = rates.first_valid_index()
    final_date = rates.last_valid_index()
    num_years = (final_date - initial_date) / datetime.timedelta(days=365)

    initial_value = rates.loc[initial_date]
    final_value = rates.loc[final_date]
    # print(f"Initial date, final date, number of years, initial, final value: {initial_date}, {final_date}, {num_years}, {initial_value}, {final_value}.")

    return ((initial_value / final_value) ** (1 / num_years))


# In[23]:


# testing the aboove function
get_cagr(rates=exchange_rates_df['[Australian dollar ]'])


# In[24]:


cagr_df = pd.DataFrame(index=exchange_rates_df.columns)

for country in cagr_df.index:
    cagr_df.loc[country, 'CAGR'] = get_cagr(rates=exchange_rates_df[country])

cagr_df.head()


# In[25]:


# adding a column that shows which country the exchange rate refers to

cagr_df['Country'] = [
    'Australia', 'Bulgaria', 'Brazil', 'Canada', 'Switzerland', 'China', 'Cyprus', 'Czech Republic', 'Denmark',
    'Estonia', 'United Kingdom', 'Greece', 'Hong Kong', 'Croatia', 'Hungary', 'Indonesia', 'Israel', 'India', 'Iceland',
    'Japan', 'Korea', 'Lithuania', 'Lativa', 'Malta', 'Mexico', 'Malaysia', 'Norway', 'New Zealand', 'Philippines', 'Poland',
    'Romania', 'Russia', 'Sweden', 'Singapore', 'Slovenia', 'Slovak Republic', 'Thailand', 'Turkey', 'United States', 'South Africa'
]

cagr_df.head()


# In[26]:


# this dataframe now has 3-letter codes for most of the countries that we want
df = px.data.gapminder().query("year==2007")

# get the 3-letter code
cagr_df = pd.merge(
    df[['iso_alpha', 'country']],
    cagr_df,
    left_on='country',
    right_on='Country',
    how='right'
)

cagr_df


# In[27]:


# there are some countries for which we don't have the 3-letter code
cagr_df.loc[cagr_df['iso_alpha'].isna(), :]


# In[28]:


cagr_df.loc[cagr_df['Country']=='Cyprus', 'iso_alpha'] = 'CYP'
cagr_df.loc[cagr_df['Country']=='Estonia', 'iso_alpha'] = 'EST'
cagr_df.loc[cagr_df['Country']=='Hong Kong', 'iso_alpha'] = 'HKG'
cagr_df.loc[cagr_df['Country']=='Korea', 'iso_alpha'] = 'KOR'
cagr_df.loc[cagr_df['Country']=='Lithuania', 'iso_alpha'] = 'LTU'
cagr_df.loc[cagr_df['Country']=='Lativa', 'iso_alpha'] = 'LVA'
cagr_df.loc[cagr_df['Country']=='Malta', 'iso_alpha'] = 'MLT'
cagr_df.loc[cagr_df['Country']=='Russia', 'iso_alpha'] = 'RUS'

cagr_df.loc[cagr_df['iso_alpha'].isna(), :]


# In[29]:


cagr_df['iso_alpha'].isna().sum()


# In[30]:


fig = px.choropleth(
    cagr_df,
    locations="iso_alpha",
    color="CAGR", 
    hover_name="Country",
    hover_data=['Country', 'CAGR'],
    color_continuous_scale=px.colors.diverging.delta
)


fig.update_layout(
    title="Compound Annual Growth Rate (CAGR) of various currencies w.r.t. Euro",
    geo=dict(showframe=False, showcoastlines=False)
)


# In[31]:


#Checking the best 3 and worst 3 performers
cagr_df.sort_values(by = 'CAGR')


# In[ ]:





# In[ ]:




