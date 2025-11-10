import tkinter as tk
import re

fenetre = tk.Tk()
fenetre.title("Calculatrice")
fenetre.configure(bg="#a9c9dd")
fenetre.resizable(True, True)

label_titre = tk.Label(fenetre, text="Calculatrice", bg="#a9c9dd", fg="#000000", font=("Helvetica", 25, "bold"))
label_titre.pack(pady=10)

affichage = tk.Entry(fenetre, font=("Helvetica", 18), bd=10, relief=tk.FLAT, bg="#E8EDDF", justify='right')
affichage.pack(padx=10, pady=10, ipadx=10, ipady=10, fill="x")

"Créer un conteneur Frame pr le clavier"
frame_clavier = tk.Frame(fenetre)
frame_clavier.pack(padx=10, pady=10, side=tk.BOTTOM, expand=True, fill="both")
for i in range(5):
    frame_clavier.rowconfigure(i, weight=1)
for j in range(4):
    frame_clavier.columnconfigure(j, weight=1)

"définition fonction ajouter chiffre"
def ajouter_chiffre(chiffre):
        affichage.insert(tk.END, chiffre)

"déficition fonction evaluer"
def evaluer():
    calcul = affichage.get()
    try:
        calcul = calcul.replace("÷", "/")
        calcul = calcul.replace("×", "*") 
        calcul_modifie = traiter_pourcentage(calcul)
        resultat = eval(calcul_modifie)
        affichage.delete(0, tk.END)
        affichage.insert(0, str(resultat))
    except:
        affichage.delete(0, tk.END)
        affichage.insert(0, "Erreur")

"C = tout effacer"
def effacer():
    affichage.delete(0, tk.END)

"DEL = supprimer dernier carractere"
def supprimer_dernier():
    texte_actuel = affichage.get()
    if texte_actuel:  
        affichage.delete(0, tk.END)
        affichage.insert(0, texte_actuel[:-1]) 



"Traitement du pourcentage"
def traiter_pourcentage(expression):
    expression = re.sub(r'(\d+(\.\d+)?)%', r'(\1/100)', expression)
    return expression


"Gestion clavier physique"
def gestion_touche(event):
    touche = event.keysym
    caractere = event.char

    if caractere in "0123456789.+-*/%":
        ajouter_chiffre(caractere)
    elif touche == "Return":
        evaluer()
    elif touche == "BackSpace":
        supprimer_dernier()
    elif caractere.lower() == "c":
        effacer()
fenetre.bind("<Key>", gestion_touche)



"Grille de chiffres"

def creer_bouton(texte, ligne, colonne, couleur, commande, colspan=1, fg="white"):
    bouton = tk.Button(frame_clavier, text=texte, command=commande, bg=couleur, fg=fg,
                   font=("Helvetica", 16), bd=1, relief=tk.RAISED, width=7, height=2)
    bouton.grid(row=ligne, column=colonne, columnspan=colspan, sticky="nsew", padx=1, pady=1)



creer_bouton('1', 3, 0, "#88a2c4", lambda: ajouter_chiffre("1"))
creer_bouton('2', 3, 1, "#88a2c4", lambda: ajouter_chiffre("2"))
creer_bouton('3', 3, 2, "#88a2c4", lambda: ajouter_chiffre("3"))
creer_bouton('4', 2, 0, "#88a2c4", lambda: ajouter_chiffre("4"))
creer_bouton('5', 2, 1, "#88a2c4", lambda: ajouter_chiffre("5"))
creer_bouton('6', 2, 2, "#88a2c4", lambda: ajouter_chiffre("6"))
creer_bouton('7', 1, 0, "#88a2c4", lambda: ajouter_chiffre("7"))
creer_bouton('8', 1, 1, "#88a2c4", lambda: ajouter_chiffre("8"))
creer_bouton('9', 1, 2, "#88a2c4", lambda: ajouter_chiffre("9"))
creer_bouton('0', 4, 1, "#88a2c4", lambda: ajouter_chiffre("0"))
creer_bouton(',', 4, 2, "#88a2c4", lambda: ajouter_chiffre("."))

creer_bouton('÷', 1, 3, "#677bab", lambda: ajouter_chiffre("÷"))
creer_bouton('×', 2, 3, "#677bab", lambda: ajouter_chiffre("×"))
creer_bouton('-', 3, 3, "#677bab", lambda: ajouter_chiffre("-"))
creer_bouton('+', 4, 3, "#677bab", lambda: ajouter_chiffre("+"))
creer_bouton('%', 0, 0, "#677bab", lambda: ajouter_chiffre('%'))

creer_bouton('=', 4, 0, "#475492", evaluer)
creer_bouton('C', 0, 2, "#03045e", effacer)
creer_bouton('⌫', 0, 3, "#03045e", supprimer_dernier)
creer_bouton('CE', 0, 1, "#03045e", effacer)



fenetre.mainloop()



# executer le code:  

# cd "C:\Users\kadet\OneDrive\Bureau\CODE\Python

# python Calculatrice.py
