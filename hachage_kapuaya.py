def hash_kapuaya_kaja(texte_a_hacher):
    
    sel_personnel = "KAPUAYA_KAJA"
    texte_combine = texte_a_hacher + sel_personnel
    
    valeur_hachage = 0
    
    for position, caractere in enumerate(texte_combine):
        valeur_hachage = (valeur_hachage * 31) + (ord(caractere) * (position + 1))
        
    return hex(abs(valeur_hachage))[2:]

# --- Zone de test ---
if __name__ == "__main__":
    message = "Mon premier test de hachage"
    resultat = hash_kapuaya_kaja(message)
    
    print(f"--- Algorithme de Hachage KAPUAYA KAJA ---")
    print(f"Message original : '{message}'")
    print(f"Résultat du hachage : {resultat}")