import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class Analyser():
    def __init__(self,df):
        self.df = df
        self.data_groups = ['WEING','WEISH','SENTO','PB','HP']
        self.unique_conjuntos = df['CONJUNTO'].unique()
        self.unique_vizinhos = df['VIZINHOS'].unique()

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

    def best_data(self):
        dataframe = pd.DataFrame()
        for conjunto in self.unique_conjuntos:
            for vizinho in self.unique_vizinhos:
                df = self.df[self.df['CONJUNTO'] == conjunto]
                df = df[df['VIZINHOS'] == vizinho]
                dataframe = dataframe.append(df.sort_values('GAP').iloc[0])
        return dataframe

    def filter_data(self,dataset,filter_dataset,kind_of_boxplot):
        df = dataset[dataset['CONJUNTO'].str.contains(filter_dataset)]
        if kind_of_boxplot == 'gap':
            self.boxplot_gap(df)
            plt.savefig('output_images/boxplot_gap_{}.png'.format(filter_dataset))
        elif kind_of_boxplot == 'time':
            self.boxplot_time(df)
            plt.savefig('output_images/boxplot_time_{}.png'.format(filter_dataset))

    def plot_vector(self,vetor,label):
        return plt.plot(vetor,label=label)
        
    def plot_many_vectors(self,data):
        for d in data:
            vector,label = d
            self.plot_vector(vector,label)
        plt.legend()
        plt.show()



if __name__ == "__main__":

    df = pd.read_csv('GRASP.csv')
    analiser = Analyser(df)
    analiser.filter_data(df,'WEISH','gap')


    # df_best = analiser.best_data()
    # for data_group in analiser.data_groups:
    #     for vizinho in ['1t','2t']:
    #         data = df_best[df_best['CONJUNTO'].str.contains(data_group)]
    #         data = data[data['VIZINHOS'].str.contains(vizinho)]
    #         for index,information in data.iterrows():
    #             # print(information['VETOR'])
    #             # print(information['PROGRESSAO_CUSTO'].strip('][').split(','))
    #             analiser.plot_vector(information['PROGRESSAO_CUSTO'].strip('][').split(','),information['CONJUNTO'])
    #         plt.legend()
    #         plt.show()

