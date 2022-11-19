#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np


# Cargar datos

# In[4]:


# Importamos el dataset de los datos de los pokemon
df = pd.read_csv("dataset_final.csv")
df.head()


# In[5]:


print(list(df.columns))


# In[6]:


'''
1. ¿Cuántos pokémon hay en el dataset?
'''
print("Hay", df["Name"].nunique(), "Pokemon")


# In[25]:


'''
2. ¿Cuántos pokémon hay de tipo Poison? (Type 1)
'''
len(df[df["Type 1"] == "Poison"])


# In[26]:


'''
3. ¿Cuántos tipos diferentes de pokémon hay? (Type 1)
'''
df["Type 1"].nunique()


# In[31]:


#2. ¿Cuántos pokémon hay de cada tipo? (Type 1)
df2=df.groupby(["Type 1"])["#"].count().reset_index(name='Count')
#2.1 ¿cual es el tipo de pokémon con más pokémon? (Type 1)

df_filtrado = df2[(df2["Count"] == df2["Count"].max())]

print(df2)
print("-------------------")
print(df_filtrado["Type 1"])


# In[7]:


'''
3. ¿Cuál es el pokémon más rápido?
'''
df_filtrado = df[(df["Speed"] == df["Speed"].max())]
print(df_filtrado["Name"])


# In[9]:


'''
4. ¿Cuántos pokemon tiene una defensa superior a 100?
'''
df_filtrado = df[(df["Defense"] >100)]
len(df_filtrado)


# In[10]:


'''
5. ¿Cuántos pokemon tiene una defensa superior a 100 y una velocidad superior a 100?
'''
df_filtrado = df[(df["Defense"] >100) & (df["Speed"] >100)]
len(df_filtrado)


# In[11]:


'''
6. Ordena el dataset por el tipo 1 y por el tipo 2

'''

df.sort_values(["Type 1", "Type 2"], ascending=[True, False])



# In[12]:


'''
7. Crea un nuevo dataset con los pokémon de tipo Water y Fire como primer tipo
'''
df_nuevo= df[(df["Type 1"] == "Water") | (df["Type 1"] == "Fire")]
df_nuevo


# In[13]:


'''
8. Crea un nuevo dataset con los pokemon Legendary
'''

df_nuevo= df[(df["Legendary"] == True)]
df_nuevo


# In[14]:


'''
9. Calcula el promedio de stats de los pokemon Legendary (HP, Attack, Defense, Sp. Atk, Sp. Def, Speed) y los no Legendary
'''
df2=df[["HP", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed", "Legendary"]]
df2.groupby(['Legendary']).mean()


# In[15]:


'''
10. Crea un nuevo dataframe con el resultado del anterior ejercicio comparando ambos promedios

ejemplo:
                HP  Attack  Defense  Sp. Atk  Sp. Def  Speed
Legendary       99      90       89       91       94     90
No Legendary    80      95       75       12       43     87

'''
df2=df[["HP", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed", "Legendary"]]
df_nuevo=df2.groupby(['Legendary']).mean()
df_nuevo


# In[38]:


'''
11. Añade una nueva colunma ['Doble tipo'] al dataframe inicial que inndique si el pokemo tiene dos tipos o no
'''
df_con_dob_tipo=df["Doble tipo"]=np.where(df["Type 2"].isnull()|df["Type 1"].isnull(),"False", "True")
df_con_dob_tipo


# In[17]:


'''
12. Muestra las columas Name, Type 1, Type 2 de los pokémon que tienen dos tipos y ordenalos por Type 1 , Type 2 y Name

'''

df[df["Name", "Type 1", "Type 2"] == "Doble tipo"]
df1 = df[["Type 1", "Type 2", "Name"]]


# In[20]:


from functools import reduce

'''
13. Dada una lista de Artículos con sus precio. Define las siguientes funciones:
Puedes definir más funciones si lo consideras necesario.
'''
articulos = {
    'Camisa': 20,
    'Pantalón': 30,
    'Calcetines': 5,
    'Zapatos': 50,
    'Gorra': 10,
    'Bufanda': 15,
    'Gafas': 25,
    'Reloj': 35,
    'Corbata': 40,
}

compra = ['Camisa', 'Pantalón', 'Pantalón', 'Gorra', 'Gafas', 'Corbata']







# In[19]:


def suma_compra(articulos,compra):
    precio_compra = 0
    for i in compra:
        precio_compra=precio_compra+articulos[i]
    return(precio_compra)
suma_compra(articulos,compra)


# In[21]:


# B. Una función que calcule el precio total de la compra con un descuento del 10%
def suma_compra_10(articulos,compra):
    precio_compra = 0
    for i in compra:
        precio_compra=precio_compra+articulos[i]
    return(precio_compra*0.9)
suma_compra_10(articulos,compra)


# In[23]:


# C. Una función que calcule el precio total de la compra con un descuento del 10% si la compra supera los 100€
def suma_compra_if10(articulos,compra):
    precio_compra = 0
    for i in compra:
        precio_compra=precio_compra+articulos[i]
    if precio_compra > 100:
        return(precio_compra*0.9)
    else:
        return(precio_compra)
suma_compra_if10(articulos,compra)


# In[24]:


# D. Una función que calcule el precio total aplicando el IVA (21%)
def suma_compra_iva(articulos,compra):
    precio_compra = 0
    for i in compra:
        precio_compra=precio_compra+articulos[i]
    return(precio_compra*1.21)
suma_compra_iva(articulos,compra)


# In[25]:


# E.lista los artículos cuyo precio es superior a 20€
def listar_articulos(articulos,compra):
    lista_barata = []
    for i in compra:
        if articulos[i]>20:
            if i not in lista_barata:
                lista_barata.append(i)
    return(lista_barata)
listar_articulos(articulos,compra)


# In[36]:


'''
14. Dada una lista de tuplas con el nombre de un alumno, apellidos, curso y sus notas. 

 Define una funcion que reciba el curso y saque una lista en la que aparezca e nombre y apellidos y el promedio de sus notas.
 Puedes definir más funciones si lo consideras necesario.
'''

alumnos = [('Juan', 'Pérez', '1', [5, 6, 7, 8, 9]),
            ('Ana', 'García', '2', [5, 6, 7, 8, 9]),
            ('Luis', 'González', '1', [5, 6, 7, 8, 9]),
            ('María', 'Martínez', '2', [5, 6, 7, 8, 9]),
            ('Pedro', 'Rodríguez', '1', [5, 6, 7, 8, 9]),
            ('Lucía', 'Hernández', '2', [5, 6, 7, 8, 9]),
            ('Marta', 'López', '1', [5, 6, 7, 8, 9]),
            ('Sara', 'Díaz', '2', [5, 6, 7, 8, 9]),
            ('Javier', 'Sánchez', '1', [5, 6, 7, 8, 9]),
            ('Miguel', 'Fernández', '2', [5, 6, 7, 8, 9]),
            ('Sergio', 'Jiménez', '1', [5, 6, 7, 8, 9]),
            ('Sandra', 'Ruiz', '2', [5, 6, 7, 8, 9]),
            ('Pablo', 'Álvarez', '1', [5, 6, 7, 8, 9]),
            ('María', 'Gómez', '2', [5, 6, 7, 8, 9]),
]


# In[37]:


def notas_medias(curso):
    for i in alumnos:
        if i[2]==curso:
            print(i[0],i[1], sum(i[3])/len(i[3]))
curso="2"
notas_medias(curso)
def notas_medias(curso):
    lista_alumnos_nota=[]
    for i in alumnos:
        if i[2]==curso:
            Avengers=i[0] +" "+ i[1]+" "+ str(sum(i[3])/len(i[3]))
            lista_alumnos_nota.append(Avengers)
    return(lista_alumnos_nota)
curso='2'
notas_medias(curso)


# In[ ]:





# In[ ]:




