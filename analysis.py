import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class Analyser():
    def __init__(self,df):
        self.df = df
        self.data_groups = ['WEING','WEISH','SENTO','PB','HP']
    
    def group_df(self,list_of_columns,group_type):
        if group_type == 'mean':
            df_c = self.df.groupby(list_of_columns).mean()
        elif group_type == 'min':
            df_c = self.df.groupby(list_of_columns).min()
        df_c = df_c.reset_index()
        return df_c
    
    def occur_by_column(self, df_with_id, column, values):
        result = df_with_id.pivot(index='ID',columns=column,values=values).reset_index()
        return result
    
    def plot_line(self,df,x,y,hue):
        plt.figure()
        sns.lineplot(df, x = x, y = y, hue = hue)
        plt.show()
    
    def plot_boxplot(self,df,conjunto,x,y,hue):
        df = df[df['CONJUNTO'].str.contains(conjunto)]
        plt.figure()
        plt.title('{}_{}_{}'.format(x,y,hue))
        sns.boxplot(df,x=x,y=y,hue=hue)
        plt.show()
    
    def separate_plot_boxplot(self,columns_to_plot):
        for conjunto in self.data_groups:
            for col in columns_to_plot:
                print('GAP x {}'.format(col))
                self.plot_boxplot(conjunto=conjunto,df=self.df,y='CONJUNTO',x='GAP',hue=col)
                print('GAP x {}'.format(col))
                self.plot_boxplot(conjunto=conjunto,df=self.df,y='CONJUNTO',x='TIME',hue=col)


if __name__ == "__main__":

    # ------------------------------------------------------------------------------------------------- GRASP

    df = pd.read_csv('GRASP.csv')
    analiser = Analyser(df)

    analiser.separate_plot_boxplot(['VIZINHOS','AMOSTRAS'])

    print('MEAN')

    df_c = analiser.group_df(['CONJUNTO','AMOSTRAS','PORCENTAGEM','VIZINHOS'],'mean')

    df_c['ID'] = df_c['CONJUNTO'] + '-' + df_c['AMOSTRAS'].astype(str) + '-' + df_c['PORCENTAGEM'].astype(str)
    df_o = analiser.occur_by_column(df_c,'VIZINHOS','GAP')
    df_o = df_o[df_o['3t'].notna()]
    print(df_o.to_markdown())

    analiser.plot_line(df_c,x='ID',y='GAP',hue='VIZINHOS')

    df_c['ID'] = df_c['CONJUNTO'] + '-' + df_c['AMOSTRAS'].astype(str) + '-' + df_c['VIZINHOS'].astype(str)
    df_o = analiser.occur_by_column(df_c,'PORCENTAGEM','GAP')
    df_o = df_o[df_o[0.9].notna()]
    print(df_o.to_markdown())

    analiser.plot_line(df_c,x='ID',y='GAP',hue='PORCENTAGEM')

    df_c['ID'] = df_c['CONJUNTO'] + '-' + df_c['PORCENTAGEM'].astype(str) + '-' + df_c['VIZINHOS'].astype(str)
    df_o = analiser.occur_by_column(df_c,'AMOSTRAS','GAP')
    df_o = df_o[df_o[10].notna()]
    print(df_o.to_markdown())

    analiser.plot_line(df_c,x='ID',y='GAP',hue='AMOSTRAS')

    print('BEST')

    df_c = analiser.group_df(['CONJUNTO','AMOSTRAS','PORCENTAGEM','VIZINHOS'],'min')

    df_c['ID'] = df_c['CONJUNTO'] + '-' + df_c['AMOSTRAS'].astype(str) + '-' + df_c['PORCENTAGEM'].astype(str)
    df_o = analiser.occur_by_column(df_c,'VIZINHOS','GAP')
    df_o = df_o[df_o['3t'].notna()]
    print(df_o.to_markdown())

    analiser.plot_line(df_c,x='ID',y='GAP',hue='VIZINHOS')

    df_c['ID'] = df_c['CONJUNTO'] + '-' + df_c['AMOSTRAS'].astype(str) + '-' + df_c['VIZINHOS'].astype(str)
    df_o = analiser.occur_by_column(df_c,'PORCENTAGEM','GAP')
    df_o = df_o[df_o[0.9].notna()]
    print(df_o.to_markdown())

    analiser.plot_line(df_c,x='ID',y='GAP',hue='PORCENTAGEM')

    df_c['ID'] = df_c['CONJUNTO'] + '-' + df_c['PORCENTAGEM'].astype(str) + '-' + df_c['VIZINHOS'].astype(str)
    df_o = analiser.occur_by_column(df_c,'AMOSTRAS','GAP')
    df_o = df_o[df_o[10].notna()]
    print(df_o.to_markdown())

    analiser.plot_line(df_c,x='ID',y='GAP',hue='AMOSTRAS')

    # ------------------------------------------------------------------------------------------------- GA

    # df = pd.read_csv('genetic.csv')
    # analiser = Analyser(df)

    # analiser.separate_plot_boxplot(['CHANCE_OF_MUTATION','AMOSTRAS'])

    # print('MEAN')

    # df_c = analiser.group_df(['CONJUNTO','AMOSTRAS','PORCENTAGEM','PARTS','CHANCE_OF_MUTATION'],'mean')

    # df_c['ID'] = df_c['CONJUNTO'] + '-' + df_c['AMOSTRAS'].astype(str) + '-' + df_c['PORCENTAGEM'].astype(str) + '-' + df_c['PARTS'].astype(str)
    # df_o = analiser.occur_by_column(df_c,'CHANCE_OF_MUTATION','GAP')
    # # df_o = df_o[df_o[4].notna()]
    # print(df_o.to_markdown())

    # analiser.plot_line(df_c,x='ID',y='GAP',hue='CHANCE_OF_MUTATION')

    # df_c['ID'] = df_c['CONJUNTO'] + '-' + df_c['PORCENTAGEM'].astype(str) + '-' + df_c['PARTS'].astype(str) + '-' + df_c['CHANCE_OF_MUTATION'].astype(str)
    # df_o = analiser.occur_by_column(df_c,'AMOSTRAS','GAP')
    # # df_o = df_o[df_o[10].notna()]
    # print(df_o.to_markdown())

    # analiser.plot_line(df_c,x='ID',y='GAP',hue='AMOSTRAS')

    # print('BEST')

    # df_c = analiser.group_df(['CONJUNTO','AMOSTRAS','PORCENTAGEM','PARTS','N_GENETIC_OUTPUT','CHANCE_OF_MUTATION'],'min')

    # df_c['ID'] = df_c['CONJUNTO'] + '-' + df_c['AMOSTRAS'].astype(str) + '-' + df_c['PORCENTAGEM'].astype(str) + '-' + df_c['PARTS'].astype(str)
    # df_o = analiser.occur_by_column(df_c,'CHANCE_OF_MUTATION','GAP')
    # # df_o = df_o[df_o[4].notna()]
    # print(df_o.to_markdown())

    # analiser.plot_line(df_c,x='ID',y='GAP',hue='CHANCE_OF_MUTATION')

    # df_c['ID'] = df_c['CONJUNTO'] + '-' + df_c['PORCENTAGEM'].astype(str) + '-' + df_c['PARTS'].astype(str) + '-' + df_c['CHANCE_OF_MUTATION'].astype(str)
    # df_o = analiser.occur_by_column(df_c,'AMOSTRAS','GAP')
    # # df_o = df_o[df_o[10].notna()]
    # print(df_o.to_markdown())

    # analiser.plot_line(df_c,x='ID',y='GAP',hue='AMOSTRAS')