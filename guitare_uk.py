# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 10:24:33 2019

@author: pierr
"""


# =============================================================================
# liste des notes jouables sur la plupart des instruments (récupéré avec le code recup_note_excel)
# =============================================================================
note = [[1, 'A0', 27.5], [2, 'A0 ou B0', 29.1353], [3, 'B0', 30.8677], [4, 'C1', 32.7032], [5, 'C1 ou D1', 34.6479], [6, 'D1', 36.7081], [7, 'D1 ou E1', 38.8909], [8, 'E1', 41.2035], [9, 'F1', 43.6536], [10, 'F1 ou G1', 46.2493], [11, 'G1', 48.9995], [12, 'G1 ou A1', 51.913], [13, 'A1', 55], [14, 'A1 ou B1', 58.2705], [15, 'B1', 61.7354], [16, 'C2', 65.4064], [17, 'C2 ou D2', 69.2957], [18, 'D2', 73.4162], [19, 'D2 ou E2', 77.7817], [20, 'E2', 82.4069], [21, 'F2', 87.3071], [22, 'F2 ou G2', 92.4986], [23, 'G2', 97.9989], [24, 'G2 ou A2', 103.826], [25, 'A2', 110], [26, 'A2 ou B2', 116.541], [27, 'B2', 123.471], [28, 'C3', 130.813], [29, 'C3 ou D3', 138.591], [30, 'D3', 146.832], [31, 'D3 ou E3', 155.563], [32, 'E3', 164.814], [33, 'F3', 174.614], [34, 'F3 ou G3', 184.997], [35, 'G3', 195.998], [36, 'G3 ou A3', 207.652], [37, 'A3', 220], [38, 'A3 ou B3', 233.082], [39, 'B3', 246.942], [40, 'C4', 261.626], [41, 'C4 ou D4', 277.183], [42, 'D4', 293.665], [43, 'D4 ou E4', 311.127], [44, 'E4', 329.628], [45, 'F4', 349.228], [46, 'F4 ou G4', 369.994], [47, 'G4', 391.995], [48, 'G4 ou A4', 415.305], [49, 'A4', 440], [50, 'A4 ou B4', 466.164], [51, 'B4', 493.883], [52, 'C5', 523.251], [53, 'C5 ou D5', 554.365], [54, 'D5', 587.33], [55, 'D5 ou E5', 622.254], [56, 'E5', 659.255], [57, 'F5', 698.456], [58, 'F5 ou G5', 739.989], [59, 'G5', 783.991], [60, 'G5 ou A5', 830.609], [61, 'A5', 880], [62, 'A5 ou B5', 932.328], [63, 'B5', 987.767], [64, 'C6', 1046.5], [65, 'C6 ou D6', 1108.73], [66, 'D6', 1174.66], [67, 'D6 ou E6', 1244.51], [68, 'E6', 1318.51], [69, 'F6', 1396.91], [70, 'F6 ou G6', 1479.98], [71, 'G6', 1567.98], [72, 'G6 ou A6', 1661.22], [73, 'A6', 1760], [74, 'A6 ou B6', 1864.66], [75, 'B6', 1975.53], [76, 'C7', 2093], [77, 'C7 ou D7', 2217.46], [78, 'D7', 2349.32], [79, 'D7 ou E7', 2489.02], [80, 'E7', 2637.02], [81, 'F7', 2793.83], [82, 'F7 ou G7', 2959.96], [83, 'G7', 3135.96], [84, 'G7 ou A7', 3322.44], [85, 'A7', 3520], [86, 'A7 ou B7', 3729.31], [87, 'B7', 3951.07], [88, 'C8', 4186.01]]


# =============================================================================
# Création des notes qu'un instrument peut jouer 
# =============================================================================
def create_notes(note_list,note) : 
    for i in range(0,len(note_list)): # on parcoure les X cordes
        for l in range(0,20) : # on prendra 20 frets pour les instruments 
            for j in range(len(note)) : # on parcoure le tableau contenant toutes les notes 
                if note_list[i][0][0] == note[j][1] : # on cherche la corde a vide dans le tableau de notes 
                    #note_correspondante = j # on a trouvé la bonne note mais la variable ne sert pas à grand chose 
                    break # on casse cette boucle du coup 
            tempo = [i+1,l] # on créer un premier tableau dans lequel on va mettre le numéro de la corde et celui de la fret
            tempo.extend(note[j+l]) # a ce premier tableau, on ajoute les infos sur la note 
            note_list[i].append(tempo) # alors on ajoute les notes qui suivent sur le manche 
        del note_list[i][0] # on supprime le premier élément car il est en trop 
    return(note_list)


# =============================================================================
# Création des notes que le ukulélé peut jouer 
# =============================================================================
def create_uk_notes(note) : 
    # on créé les cordes pour le ukulélé 
    corde_uk_1 = [["G4",391.995]] # on créer le tableau de la corde et on met le son de la corde Sol à vide
    corde_uk_2 = [["C4",261.626]] # on créer le tableau de la corde et on met le son de la corde Do à vide
    corde_uk_3 = [["E4",329.628]] # on créer le tableau de la corde et on met le son de la corde Mi à vide 
    corde_uk_4 = [["A4",440]] # on créer le tableau de la corde et on met le son de la corde La à vide
    
    corde_uk = [corde_uk_1,corde_uk_2,corde_uk_3,corde_uk_4] # on les mets toutes dans un tableau 
    
    return(create_notes(corde_uk,note)) # appel de la fonction pour créer les notes sur les frettes 


# =============================================================================
# Création des notes que la guitare peut jouer 
# =============================================================================
def create_guit_notes(note):
    # on créé les cordes pour la guitare 
    corde_g_1 = [["E2",82.4069]] # on créer le tableau de la corde et on met le son de la corde Mi grave à vide 
    corde_g_2 = [["A2",110]] # on créer le tableau de la corde et on met le son de la corde La à vide
    corde_g_3 = [["D3",146.832]] # on créer le tableau de la corde et on met le son de la corde Ré à vide 
    corde_g_4 = [["G3",195.998]] # on créer le tableau de la corde et on met le son de la corde Sol à vide 
    corde_g_5 = [["B3",246.942]] # on créer le tableau de la corde et on met le son de la corde Si à vide
    corde_g_6 = [["E4",329.62]] # on créer le tableau de la corde et on met le son de la corde Mi aigue à vide
    
    corde_g = [corde_g_1,corde_g_2,corde_g_3,corde_g_4,corde_g_5,corde_g_6 ]# on les mets toutes dans un tableau 
    
    return(create_notes(corde_g,note)) # appel de la fonction pour créer les notes sur les frettes 

    
# =============================================================================
# Fonction cherchant à trouver les notes de guitare et ukulele 
# =============================================================================
def recherche_guit_uk(corde_g,corde_uk,note):
    print("note : ",note,"\n")
    for g in range(len(corde_g)): # on parcoure les 6 cordes de la guitare 
        for p in range(len(corde_g[g])) : # on parcoure toutes les frettes dispo par corde 
            #print(corde_g[g][p])
            if note[2] == corde_g[g][p][4] : # on cherche la bonne frette
                print("Guitare corde : ",corde_g[g][p][0]," fret : ",corde_g[g][p][1])
    print("\n")
    for u in range(len(corde_uk)) : # on parcoure les 4 cordes du uk 
        for f in range(len(corde_uk[u])): # on parcoure toutes les frettes dispo par corde 
             #print(corde_uk[u][f])
             if note[2] == corde_uk[u][f][4] : # on cherche la bonne frette 
                 print("Ukulele corde : ",corde_uk[u][f][0]," fret : ",corde_uk[u][f][1])
                 

# =============================================================================
# L'utilisateur choisit un instrument, tourne en boucle tant qu'on a pas trouvé le bon instrument
# =============================================================================
def choix_instrument(): 
    temoin_instru = False
    while not temoin_instru : 
        
        instrument = input("Vous allez choisir l'instrument à partir du quel vous traduirez les notes, tapez p pour piano, g pour guitare ou u pour ukulele : \t")
        if instrument == "g" : 
            temoin_instru = True
            print("instrument choisit : Guitare ! ")
        elif instrument == "p" : 
            temoin_instru = True
            print("instrument choisit : Piano ! ")
        elif instrument == "u":
            temoin_instru = True
            print("instrument choisit : Ukulele ! ")
        else : 
            print("vous avez du vous tromper de lettre, on recommence")
    return(instrument)
        

# =============================================================================
# Fonction pour demander si l'utilisateur veut continuer ou arreter 
# =============================================================================
def onfaitquoi():
    encore = input("Continuer ? \n non = n \n oui = tout le reste\n\t") 
    if encore == "N" or encore == "n" : 
        again = False 
    else : 
        again = True 
    return(again)
        

# =============================================================================
#  fonction qui fait la traduction des notes 
# =============================================================================
def traduction_guit_uk(corde) : 
    again = True 
    corde_donnee = 0.0
    fret_donnee = -1.1
    while again : 
        # là, on cherche la corde 
        while (int(corde_donnee) > len(corde) or int(corde_donnee) < 1 ):  
            corde_donnee = (input("Entrez la corde associée à la note (de 1 à "+str(len(corde))+") : \t"))
            try : # on regarde si on peut le transformer en int 
                corde_donnee = int(corde_donnee)
            except : # si on peux pas, on va refaire une demande 
                print("Need an int (nombre entier)")
                corde_donnee = 0
        if int(corde_donnee) <= len(corde) and int(corde_donnee)>=1 : 
            corde_donnee = int(corde_donnee) - 1 # enlève 1 car corde 1 est a indice 0 dans le tableau 
                
        # ici, on cherche la fret 
        while (int(fret_donnee) > len(corde[0])-1 or int(fret_donnee) < 0) :  
            fret_donnee = (input("Entrez la fret associée à la note (de 0 à "+str(len(corde[0])-1)+") : \t"))
            try : # on regarde si on peut le transformer en int 
                fret_donnee = int(fret_donnee)
            except : # si on peux pas, on va refaire une demande 
                print("Need an int (nombre entier)")
                fret_donnee = -1.1
        if int(fret_donnee) <= len(corde[0]) and int(fret_donnee)>=0 : 
            fret_donnee = int(fret_donnee) 
                
        note_donnee = corde[corde_donnee][fret_donnee]
        #print(note_donnee)
        
        for i in range(len(note)) : # on parcoure le tableau avec toutes les notes du piano 
            if note_donnee[3] == note[i][1] or note_donnee[4] == str(int(note[i][2])) : # on reggarde si la donnée entrée est égale au nom ou a la fréquence d'une des notes 
                print("\n\nVotre note est : ",note[i][1]," et elle sonne à cette fréquence : ", note[i][2],"\n\n") # on affiche la note et la fréquence correspondante 
                
                recherche_guit_uk(corde_g,corde_uk,note[i])
        
        again=onfaitquoi()
        corde_donnee = 0.0
        fret_donnee = -1.1
        
        


# =============================================================================
# Appel des fonctions pour créer les notes jouable par les instruments 
# =============================================================================
corde_uk = create_uk_notes(note)
corde_g = create_guit_notes(note)  

# =============================================================================
# Choix de l'instrument 
# =============================================================================
instrument = choix_instrument()



# =============================================================================
# L'instrument est choisit, il faut donc maintenant faire 3 fonctions, une par instrument
# =============================================================================
if instrument == "p" : #" ici, on traduit des notes de piano en notes de guitare et ukulele 
    again = True 
    while again : 
        note_donnee = input("Entrez votre note (nom ou fréquence (juste la partie entière pour la fréquence)):\n\t") # on demande à l'utilisateur de rentrer soit la fréquence soit le nom de la note qu'il veut traduire 
        for i in range(len(note)) : # on parcoure le tableau avec toutes les notes du piano 
            if note_donnee == note[i][1] or note_donnee == str(int(note[i][2])) : # on regarde si la donnée entrée est égale au nom ou a la fréquence d'une des notes 
                print("\n\nVotre note est : ",note[i][1]," et elle sonne à cette fréquence : ", note[i][2],"\n\n") # on affiche la note et la fréquence correspondante 
                
                recherche_guit_uk(corde_g,corde_uk,note[i])
        again=onfaitquoi()
        
       
if instrument == "g" : # ici, on traduit des notes de guitare en notes de ukulele
    traduction_guit_uk(corde_g)
    

if instrument == "u" : # ici, on traduit des notes de ukulele en notes de guitare 
    traduction_guit_uk(corde_uk)
    
    
