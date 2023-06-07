import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class Analyser():
    def __init__(self,df):
        self.df = df
        self.data_groups = ['WEING','WEISH','SENTO','PB','HP']

    def group_data(self,mean_or_min):
        if mean_or_min == 'mean':
            df_grouped = self.df.groupby(['CONJUNTO','VIZINHOS']).mean()
        elif mean_or_min == 'min':
            df_grouped = self.df.groupby(['CONJUNTO','VIZINHOS']).min()
        else:
            return self.df

        df_grouped = df_grouped.reset_index()

        return df_grouped


    def boxplot_gap(self,dataset):
        return sns.boxplot(dataset, y = 'CONJUNTO', x = 'GAP', hue = 'VIZINHOS')
    
    def boxplot_time(self,dataset):
        return sns.boxplot(dataset, y = 'CONJUNTO', x = 'TIME', hue = 'VIZINHOS')


    def filter_data(self,dataset,filter_dataset,kind_of_boxplot):
        df = dataset[dataset['CONJUNTO'].str.contains(filter_dataset)]
        if kind_of_boxplot == 'gap':
            self.boxplot_gap(df)
            plt.savefig('output_images/boxplot_gap_{}.png'.format(filter_dataset))
        elif kind_of_boxplot == 'time':
            self.boxplot_time(df)
            plt.savefig('output_images/boxplot_time_{}.png'.format(filter_dataset))



if __name__ == "__main__":

    df = pd.read_csv('GRASP.csv')
    analiser = Analyser(df)
    analiser.filter_data(df,'HP','time')