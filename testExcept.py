
d=[567,788,99,100, 887]

while True:
    try:
            nb=input("Entrer un index entre 0 et 4: ")
            nb=int(nb)
            print(f"Element a la position {nb} est {d[nb]}")
            break
    except ValueError as ex:
        print(f"Traitement 1:")
    except IndexError as ex:
        print(f"Traitement 2: {ex}") 
    except:
        print("Autre traitement")
    finally:
        print("Toujours execute")
    
print("The end")