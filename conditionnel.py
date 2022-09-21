

'''
print ("Bonjour")
print ("Donnez moi un nombre entier")
(nbre1) = float(input())

print ("{}".format(nbre1*0.5))
print(nbre1%2)
if nbre1%2 == 0:
    print("le nombre est pair")
else:
    print("le nombre est impair")
   '''


'''
print ("Bonjour")
print ("Donnez moi trois nombres")   
print ("Le premier")
(nbre1) = float(input())
print ("Le second")
(nbre2) = float(input())
print ("Le troisiéme")
(nbre3) = float(input())
if nbre1 > nbre2  and  nbre1 > nbre3:
    print( " Le premier nombre est le plus grand")
elif nbre2 > nbre1  and nbre2 > nbre3 :
     print( " Le second nombre est le plus grand")
else :
    print(" Le troisième nombre est le plus grand")
'''


def definir_pair_ou_impair():
    print ("Bonjour")
    print ("Donnez moi un nombre entier")
    (nbre1) = float(input())

    print ("{}".format(nbre1*0.5))
    print(nbre1%2)
    if nbre1%2 == 0:
        print("le nombre est pair")
    else:
        print("le nombre est impair")


#definir_pair_ou_impair()


def definir_est_pair(nb):
    if nb % 2 == 0:
        return True
    else:
        return False   


#definir_est_pair()


def le_nombre_le_plus_petit(nbre1,nbre2,nbre3):
    
    if nbre1 < nbre2  and  nbre1 < nbre3:
        return( " nbre1 est le plus petit")
    elif nbre2 <nbre1  and nbre2 < nbre3 :
        return( " nbre2 nombre est le plus petit")
    else :
        return("nbre3 nombre est le plus petit")



#le_nombre_le_plus_petit(10,30,75)

def valeur_absolue_de_la_multiplication():
    print ("Donnez moi 2 nombres , le premier")
    (nbre1) = float(input())
    print ("Donnez moi , le second")
    (nbre2) = float(input())
    resultat = (nbre1*nbre2)
    print("Le_resultat_de_la_multiplication_est ",(resultat))
    if (resultat) < 0:
        (resultat) = -(resultat)
    print("La_valeur_absolue_de_la_multiplication_est ",(resultat))



#valeur_absolue_de_la_multiplication()


def calculer_la_moyenne_de_trois_nombres(nbre1,nbre2,nbre3):
    moyenne = ((nbre1+nbre2+nbre3)/3)
    return(moyenne)


calculer_la_moyenne_de_trois_nombres(10,20,121)

