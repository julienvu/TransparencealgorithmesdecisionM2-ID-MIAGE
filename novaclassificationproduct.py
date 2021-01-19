#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 21:20:59 2020

@author: JULIEN VU PROJET TRANSPARENCE MODELE NOVA
"""

#prend une liste de valeurs des 3 caractéristiques
#(produit, sous produit, nombre additifs produit
# de la classification nova en entrée
#et renvoie sa classification ( 1, 2, 3, 4)
def nova(produit):
    #intialisation des différents groupes de la classification NOVA(1,2,3,4)
    classe1='1'
    classe2='2'
    classe3='3'
    classe4='4'
    classenova=''
    #array ajoutant la classe NOVA du produit 
    listenova=[]
    #si longueur produit !=3 on retape"
    if len(produit)!= 3:
        print('Pas possible de donner la classe NOVA.Retapez la liste des valeurs produit')
    else:
        # a chaque condition if , on attribue une classe nova à chaque produit traité
        # si on a comme catégorie de produit sugary-snacks ou Sugary Snacks
         # alors c'est de classe 4, on ajoute la classe nova dans la liste
        if produit[0]==10 or produit[0]==11:
            classenova=classe4
            listenova.append(classenova)
        # si on a comme catégorie de produit fruits-and-vegetables ou Fruits and Vegetables
        # alors c'est de classe 1, on ajoute la classe nova dans la liste
        if produit[0]==6 or produit[0]==7:
            classenova=classe1
            listenova.append(classenova)
        # si on a comme catégorie de produit composite food, c'est de classe 3
        if produit[0]==3:
            classenova=classe3
            listenova.append(classenova)
         # si on a comme catégorie de produit beverages et sous-catégorie
         # fruit juices,  unsweetened beverages
         # alors c'est de classe 1, on ajoute la classe nova dans la liste
        if produit[0]==1 and produit[1]==15 or produit[1]==38 or produit[1]==29:
            classenova=classe1
            listenova.append(classenova)
        # si on a comme catégorie de produit beverages et sous-catégorie le reste
         # fruit nectars, sweetened beverages
         # alors c'est de classe 4, on ajoute la classe nova dans la liste
        if produit[0]==1 and produit[1]==2 or produit[1]==35 or produit[1]==40:
            classenova=classe4
            listenova.append(classenova)
        # si on a comme catégorie de produit cereals and potatoes et sous-produit Cereals
         # alors c'est de classe 1, on ajoute la classe nova dans la liste
        if produit[0]==2 and produit[1]==6:
            classenova=classe1
            listenova.append(classenova)
        # si on a comme catégorie de produit cereals and potatoes et sous-produit 
        #le 4 et le 5(bread potatoes)
        # et nombre d'additifs supérieure ou égal à 2
         # alors c'est de classe 4, on ajoute la classe nova dans la liste
        if produit[0]==2 and produit[1]==4 or produit[1]==5 and produit[2]>=2:
            classenova=classe4
            listenova.append(classenova)
         # si on a comme catégorie de produit cereals and potatoes et sous-produit 
        #le 4 bread
        # et nombre d'additifs inférieure ou égal à 2
         # alors c'est de classe 3, on ajoute la classe nova dans la liste
        if produit[0]==2 and produit[1]==4 and produit[2]<2:
            classenova=classe3
            listenova.append(classenova)
        #fat and sauces et sous -catégorie fats
         # alors c'est de classe 2, on ajoute la classe nova dans la liste
        if produit[0]==4 and produit[1]==13:
            classenova=classe2
            listenova.append(classenova)
        #fat and sauces et sous -catégorie dresseing and sauces et nombre additifs supérieure à 2
         # alors c'est de classe 4, on ajoute la classe nova dans la liste
        if produit[0]==4 and produit[1]==10 and produit[2]>=2:
            classenova=classe4
            listenova.append(classenova)
        #fat and sauces et sous -catégorie dresseing and sauces et nombre additifs inférieure à 2
         # alors c'est de classe 4, on ajoute la classe nova dans la liste
        if produit[0]==4 and produit[1]==10 and produit[2]<2:
            classenova=classe3
            listenova.append(classenova)
        #fish and meat et sous -catégorie 14(Fish and seafood)
         # alors c'est de classe 3, on ajoute la classe nova dans la liste
        if produit[0]==5 and produit[1]==14:
            classenova=classe3
            listenova.append(classenova)
        #fish and meat et sous -catégorie le reste 
        if produit[0]==5 and produit[1]==24 or produit[1]==22 or produit[1]==31:
            classenova=classe4
            listenova.append(classenova)
        #Milk and Dairy Product et sous-catégorie Cheese
        #fish and meat et sous -catégorie 14(Fish and seafood)
         # alors c'est de classe 3, on ajoute la classe nova dans la liste
        if produit[0]==8 and produit[1]==7:
            classenova=classe3
            listenova.append(classenova)
            listenova.append(classenova)
        #Milk and Dairy Product et sous-catégorie Cheese
        #fish and meat et sous -catégorie le reste(Ice cream, milk and yogurt)
         # alors c'est de classe 4, on ajoute la classe nova dans la liste
        if produit[0]==8 and produit[1]==9 or produit[1]==21:
            classenova=classe4
            listenova.append(classenova)
        #salty snacks et sous-catégorie nuts
         # alors c'est de classe 1, on ajoute la classe nova dans la liste
        if produit[0]==9 and produit[2]==22:
            classenova=classe1
            listenova.append(classenova)
        #salty snacks et sous-catégorie Salty and fatty products
         # alors c'est de classe 3, on ajoute la classe nova dans la liste 
        if produit[0]==9 and produit[2]==31:
            classenova=classe3
            listenova.append(classenova)
         #salty snacks et sous-catégorie Apetizers
         # alors c'est de classe 4, on ajoute la classe nova dans la liste 
        if produit[0]==9 and produit[2]==1:
            classenova=classe4
            listenova.append(classenova)
    classenovafinal=listenova[0]
    print(classenovafinal)
    return classenovafinal


#tests à faire sur la console du terminal
nova([4,13,4])   
nova([10,9,2])  
nova([6,9,2]) 
nova([4,13,2]) 
nova([2,4,2]) 
nova([5,14,1]) 
nova([5,14,1])
