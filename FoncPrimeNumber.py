
import time

# NOTE:     Fonctions PrimeNumber
#
#           Calcul tous les nombres premiers
#           Seuil entrer par l'utilisateur
#
# TODO:     while maxPrime != type(int()): or if maxPrime != type(int()): or ???? "
#           si champ mal rempli, il faut redemander d'entrer un nombre

def PrimeNumber():
    maxPrime = input("\nEntrer le seuil de nombre premier (NOMBRE ENTIER): > ")

    try:
        maxPrime = int(maxPrime)
    except:
        print("❌ ", " Entrer un nombre entier !")
        maxPrime = input("\n❗️ATTENTION, dernier essai, Entrer le seuil de nombre premier (NOMBRE ENTIER): > ")
        try:
            maxPrime = int(maxPrime)
        except TypeError:
            print("❌ ", " Erreur, vous devez entrer un NOMBRE ENTIER !")
        except ValueError:
            print("❌ ", " Erreur, vous devez entrer un NOMBRE ENTIER !")
        else:
            print("👍 ", " Champ correctement rempli !")
        finally:
            print("➡️ ", " Fin de programme")
    else:
        print("👍", " Champ bien rempli avec un entier...")
    finally:
        print("➡️ ", " Fin de programme !")

    isPrime = []
    primes = []

    tempsStart = time.time()

    for i in range(0,maxPrime):
        isPrime.append(True)

    isPrime[0] = False
    isPrime[1] = False

    for i in range(2,maxPrime):
        if isPrime[i] == True:
            j = i * i
            while j < maxPrime:
                isPrime[j] = False
                j += i
            primes.append(i)

    print("✅ Liste de tous les nombres premiers de 2 à", maxPrime,":",primes,"\n")
    print("✅ Quantité de nombres premiers: ",len(primes))
    print("✅ Premier et Dernier nombre premier de la liste: ","\n✅ First: ",primes[0],"\n✅ Last: ",primes[-1])

    tempsEnd = time.time()
    resultatTime = tempsEnd - tempsStart
    print("Le temps écoulé est de : " , resultatTime,"\n ")
    print("FIN DE LA FONCTION 'PrimeNumber': \n")
