#Librairies utilisees pour la classification NPOVA
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# code pour voir la structure de l'arbre
# méthode classification arbre de décision de type NOVA

def createExcelNovaDecisionTree(file_name_path):
    #Lecture du fichier file_name
    print("Le fichier utilisé est ", file_name_path)
    #lecture du fichier file_name_path
    novaclass=pd.read_excel(file_name_path)
    print(novaclass.shape)
    mycolumnsnova = ['pnns_groups_1','pnns_groups_2','additives_n','nova_group'] 
    print('Les colonnes qui vont nous servir pour la classification NOVA sont:', mycolumnsnova)
    #tableauxdonnees a 4 colonnes
    tableauxdonnes=novaclass[['pnns_groups_1', 'pnns_groups_2','additives_n','nova_group']]
    print('Tableau des donnees')
    tableauxdonnes=tableauxdonnes.replace("unknown",0)
    #convertir les colonnes pnns_groups_1 et pnns_groups_2 en valeurs numériques
    tableauxdonnes['pnns_groups_1']=tableauxdonnes['pnns_groups_1'].astype('category').cat.codes
    tableauxdonnes['pnns_groups_2']=tableauxdonnes['pnns_groups_2'].astype('category').cat.codes
    #unknown=11 pour pnns_groups_1 unknown=41 pour pnns_groups_2
    #supprimer les valeurs NaN pour un produit alimentaire non classé
    tableauxdonnes=tableauxdonnes.fillna(0.0)
    print(tableauxdonnes)
    #donner les 3 caractéristiques 'pnns_groups_1','pnns_groups_2','additives_n'
    X=tableauxdonnes.iloc[:,:3]
    print('Donnees des Caracteristiques')
    print(X)
    #le label classe nova
    y=tableauxdonnes.iloc[:,-1]
    print("Donnees des labels")
    print(y)
    
     # split the data into training and testing sets as per above code cell method
     #Controls the shuffling applied to the data before applying the split.
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)
    #create une instance d'un classifier d'arbre de décision
    clf=DecisionTreeClassifier(max_depth=8,max_leaf_nodes=8, random_state=20)
    print(clf)
    #apprendre sur les données existantes X_train et y_train
    clf.fit(X_train,y_train)
    
    #choix du graphe de taille 32*32 de l'arbre de décision
    fig, ax = plt.subplots(figsize=(17, 17))  
    c=plot_tree(clf, ax=ax)
    print(c)
    #enregistrement du fichier contenant l'arbre
    #nom du fichier: decisiontree_individualtree.png
    fig.savefig('decisiontree_individualtree.png')
    
    # prédire la valeur des données test( celles qu'on ne connait pas à l'avance)
    #Voir Adequation du modèle : performance du modèle et précision
    accu_train=np.sum(clf.predict(X_train)==y_train)/len(y_train)
    print('Classification des donnees d aprentissage:',accu_train)
    accu_test=np.sum(clf.predict(X_test)==y_test)/len(y_test)
    print('Classification des donnees de test:',accu_test)
    

   
#------------------------Main (Instanciation des fonctions)------------------------    

#changer le chemin selon l'emplacement des données servant à la classification NOVA
createExcelNovaDecisionTree('/Users/julien/Master_Info_Dauphine/M2_ID_INITIALE/Transparence algorithmes decision/Datasets/openfoodfacts_simplified_database.xlsx')
