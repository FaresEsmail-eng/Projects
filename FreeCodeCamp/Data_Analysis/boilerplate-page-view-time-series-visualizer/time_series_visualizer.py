import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv',index_col='date', parse_dates=True)

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))] 


def draw_line_plot():
    # Draw line plot

    fig, ax = plt.subplots(figsize=(15,5))
    sns.lineplot(df,x='date', y='value',ax=ax).set(xlabel='Date', ylabel='Page Views',title='Daily freeCodeCamp Forum Page Views 5/2016-12/2019')



    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()

    # Draw bar plot

    df_bar['month'] = df_bar.index.month_name()
    df_bar['year'] = df_bar.index.year

    month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    df_bar = df_bar.groupby(['year','month'])['value'].mean().unstack()
    df_bar = df_bar[month_order]

    fig = df_bar.plot(
        kind='bar',
        xlabel='Years',
        ylabel='Average Page Views',
        figsize=(10,8)
    ).figure

    plt.legend(title='Months')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)

    month_ord= ['Jan' ,'Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    fig,axe = plt.subplots(figsize=(20,7),nrows=1, ncols=2)

    sns.set_theme(style='darkgrid')

    sns.boxplot(df_box,x='year', y='value',ax=axe[0],hue='year',palette='bright',legend=False)
    axe[0].set(xlabel='Year',ylabel='Page Views',title='Year-wise Box Plot (Trend)')



    sns.boxplot(df_box,x='month', y='value',order=month_ord,ax=axe[1],hue='month',palette='bright',legend=False)
    axe[1].set(xlabel='Month',ylabel='Page Views',title='Month-wise Box Plot (Seasonality)')




    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
