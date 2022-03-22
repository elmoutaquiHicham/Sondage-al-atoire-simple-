import numpy as np
import pandas as pd
import scipy.stats as stat
import math
import random
import scipy.special 
import plotly.express as px



class pesr:
    def __init__(self, data,n):
        self.data = data
        self.n = n

    
    def ech_poss(self):                        ## fonction qui retourne les echantillons possibles vu le mode de prélévement.
        k= scipy.special.binom(len(self.data),self.n).astype(int)
        c=1
        L = [i for i in range(len(self.data))]
        z = random.sample(L, self.n)
        R = [set(z)]
        while c<k:
            z = random.sample(L, self.n)
            if set(z) in R:
                pass
            else:
                R.append(set(z))
                c+=1
        return R
    
    def samples_as(self):
        import pandas as pd
        import numpy as np
        import scipy.special
        k = scipy.special.binom(len(self.data), self.n)
        k = k.astype(int)
        obj = [[] for i in range(k)]                      ### Création des DataFrames des différents échantillons possibles.
        dfs = [pd.DataFrame() for i in range(k)]
        for i,x in enumerate(self.ech_poss()):
            for y in x:
                obj[i].append(self.data[y])
                dfs[i] = pd.Series(np.array(obj[i])).to_frame()
                c = f"echantillon {i+1}"
                dfs[i].columns = [c]
        horizontal_concat = pd.concat([dfs[i] for i in range(k)], axis=1)
        print('Les échantillons possibles à prélever vu le mode de prélevement (probabilités égales sans remise) sont présentés\n dans le tableau ci-dessous: ')
        return horizontal_concat
    
    def box_plot(self,df): ## Méthode donnant les boites à moustache (BoxPlots) associés aux différants échantillons dans le meme graphique.
        fig = px.box(df)    ## la méthode prend la DataFrame que l'on a eu avec la méthode samples_as()
        fig.show()


class Sondage:                    ## Définition de la class Sondage
    def __init__(self,Column,N,x):
        self.Column = Column
        self.mean_ = x[self.Column].mean()      ## Moyenne de l'échantillon
        self.var_corr = None   ## variance corrigée de l'echantillon
        self.n = None          ## Taille de l'echantillion
        self.N = N             ## Taille de la population
        self.sd_ = None        ## ecart-type corrigé
        self.x = x             ## DataFrame
        self.dwa = None         ## Incertitude absolue
        self.dwr = None
        self.n_min = None
        self.ckn = None

## Définitions des propriétés applicables aux abjets de type Sondage        
        
    def taux_sondage(self):                                     ## Méthode qui calcule le taux de sondage (f = n/N)
        self.n = len(self.x[self.Column])
        print('le taux de sondage vaut :',  self.n/self.N)
        
    def var_cor(self):                                          ## Méthode qui calcule la variance corrigé de l'echantillon(estimateur san bias de la variance corrigée de la population)
        self.mean_ = self.x[self.Column].mean()
        self.var_corr = sum((self.x[self.Column]-self.mean_)**2)/(len(self.x[self.Column])-1)
        print("la variance corrigée de l'échantillon vaut: ", self.var_corr )
    
    def ecart_type_cor(self):                                  ## Méthode qui calcule l'ecart type-corrigé de l'echantillon.
        self.mean_ = self.x[self.Column].mean()
        self.var_corr = sum((self.x[self.Column]-self.mean_)**2)/(len(self.x[self.Column])-1)
        print("L'ecart-type corrigé de l'échantillon vaut: ", self.var_corr**(1/2))
        
    def IC(self,niveau):                                      ## Méthode qui calcule l'intervalle de confiance de la moyenne de la population à un niveau donné.
        z = stat.norm.ppf(niveau, loc=0, scale=1)
        a = self.mean_ - (z*np.sqrt((1-(self.n/self.N))*(sum((self.x[self.Column]-self.mean_)**2)/(len(self.x[self.Column])-1)/(self.n))))
        b = self.mean_ + (z*np.sqrt(((1-(self.n/self.N))*(sum((self.x[self.Column]-self.mean_)**2)/(len(self.x[self.Column])-1)/(self.n)))))
        self.IC_ = [a,b]
        print(self.IC_) 
        
    def incertitude_absolue(self, niveau):                    ## méthode qui calcule l'incertitude absolue.
        z = stat.norm.ppf(niveau, loc=0, scale=1)
        dwa = z*np.sqrt((1-(self.n/self.N))*(sum((self.x[self.Column]-self.mean_)**2)/(len(self.x[self.Column])-1)/(self.n)))
        print("L'incertitude absolue vaut : ", dwa)
        
        
    def incertitude_relative(self,niveau):                  ## Méthode qui calcule l'incertitude relative.
        z = stat.norm.ppf(niveau, loc=0, scale=1)
        dw = z*np.sqrt((1-(self.n/self.N))*(sum((self.x[self.Column]-self.mean_)**2)/(len(self.x[self.Column])-1)/(self.n)))
        dwr = dw/self.mean_
        print("L'incertitude relative vaut : ", dwr)
        
    def minimum_n(self, niveau,d0):                         ## Le plus petit entier tel que l'incertitude absolue est inférieure à un certain nombre determiné par le statisticien.
        z = stat.norm.ppf(niveau, loc=0, scale=1)
        s_carr= sum((self.x[self.Column]-self.mean_)**2)/(len(self.x[self.Column])-1)
        n_min = ((self.N)*(z**2)*(s_carr**2))/((self.N)*(d0**2)+ (z**2)*(s_carr**2))
        print("Le plus petit entier tel que l'incertitude absolue est inférieure à ", d0, " est égal à :", n_min )
        
    def comb_possible(self):                               ## Méthode qui calcule le nombre d'échantillons possibles.
        ckn = math.factorial(self.N)/(math.factorial(self.n)*math.factorial(self.N-len(self.x[self.Column])))
        print("Le nombre d'échantillons possibles vu le mode de prélévement (PESR) est :", ckn)
    
    def box(self):                                        ## méthode qui retourne la boite à moustache de l'echantillon en question.
        fig = px.box(self.x,y=self.Column, points="all" )
        fig.show()
    
        
        
