import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def basic_summary_plots(data_col, filepath, save=False):
    """
    Plots two figures: boxplot and density plot for
    a specified data column.

    params
    ------
    data_col : {pandas Series data}
    filepath : {string} - the destination path to save plots
    """
    f, axes = plt.subplots(1, 2, figsize=(13, 5))
    axes[0].set_title('Box Plot')
    axes[1].set_title('Density Plot')
    f.suptitle('Feature : '+ data_col.name, fontsize = 15)
    data_col = data_col.dropna()
    sns.boxplot(data_col, ax=axes[0])
    sns.distplot(data_col, ax=axes[1])
    
    if save:
        plt.savefig(filepath+'/bp_'+data_col.name+'.png')
        plt.close()
        
        
def categ_summary(data_col):
    """ Prints the unique values and its frequency
    for a categorical feature.

    params
    ------
    data_col : - pd.Series of data
    """

    data_col.value_counts().plot('bar')
    plt.title('Feature : '+ data_col.name, fontsize = 15)