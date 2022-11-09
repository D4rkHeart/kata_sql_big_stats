# Kata SQL


## 1. Création d'un fichier markdown avec les étapes du processus 
J'ai choisi de prendre comme outils [HACKMD](https://go.epfl.ch/HACKMDhttps://)


## 2. Forker le repos
On vas à sur le repos du kata disponible [ici](![](https://github.com/zuzu59/kata_sql_big_stats))
Puis on vas dans *CODE* -> *SSH* et on copie le lien.
![](https://i.imgur.com/3dPy2tu.png)

On vas ensuite dans un terminal et on vas dans le dossier ou l'on veut forker notre repos. Puis on écrit la commande : 
> git clone  git@github.com:zuzu59/kata_sql_big_stats.git

Puis on télécharge le fichier csv disponible [ici](https://drive.google.com/file/d/1GfPo476QDDcbwAL3x4aUvrO9pQOY1TlX/view)
On vas dans le dossier download et on écrit la commande suivante afin d'extraire le csv dans le répértoire ou l'on vas travailler  :
> sudo unzip -d /dest/directory/ states.csv


---

## 3. Analyser le csv, comprendre les types, les donnée, afin de crée une structure
Ne pouvant ouvrir le fichier sur un tableur tel que Excel ou SpreadSheat, il y'a selon moi 2.5 solutions : 

* Version **I'm a dev** et celle qui respecte le CDC du kata :
J'ai crée un "script" en python qui vas aller chercher la première ligne       du fichier et me l'afficher :+1: 
> with open("./Data/states.csv") as f:
    contents = f.readlines()
    print(contents[0])

* Version **I'm a lazy dev**
        Utiliser [WORKBENCH (Linux ,Windows, MacOs,)](https://dev.mysql.com/downloads/workbench/) en important le CSV directement dedans.([Tutoriel](https://dev.mysql.com/downloads/workbench/)) 
    
* Version **i don't use a mouse**
    Utiliser VIM ou EMACS pour l'ouvrir
    
```
PS : !!! A ne pas reproduire !!!! Version "I want to break my pc"(très déconseilé)
Ouvrir le CSV dans son IDE au risque et péril des ressources de votre pc
```


## 4. SQLite

1. Installation de SQLite 
> sudo apt install sqlite

2. Création de la base de donnée
> sqlite3 [nom de votre base de donnée].db;

4. Creation de Table en suivant le header 

***Header = IINDEX,C2,DEVICE,VALUE,C5,C6,C7,TIME,C9,C10,C11,C12,C13,C14,C15***

on vas donc crée une table contenant l'index,l'appareil,sa valeur,l'horodotage.Ce qui vas donner :
> CREATE TABLE Probe (
  ID    INTEGER PRIMARY KEY, 
  Name  TEXT NOT NULL,
  Value FLOAT NOT NULL,
  Date  TEXT NOT NULL
);

Pour vérifier si la table à été crée on écrit :
> .tables

Pour vérifier sa structure :
> .schema Probe
