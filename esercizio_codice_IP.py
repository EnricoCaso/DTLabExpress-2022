"""
Data una stringa di caratteri che rappresenta l'indirizzo IP A.B.C.D esempio 192.168.2.10
Ogni numero dell'indirizzo IP è formato da 8 bit per un totale di 32 bit aaaaaaaa.bbbbbbbb.cccccccc.dddddddd
E tutto l'indirizzo IP può essere visto come un unico numero che va da 0-2^32-1
Per esempio per trasformare l'indirizzo IP in un numero intero eseguire questa operazione:
    N = A*2^24 + B*2^16 + C*2^8 + D
Una volta calcolato il numero intero trasformarlo in binario bin() , da ricordare che la funzione bin() ritorna un numero binario con antecedente 0b e quindi come
output vogliamo il numero binario senza 0b

In python il primo carattere di una stringa si indica con indice 0 , esempio s = 'ciao' s[0]=c s[1]=i s[2]=a s[3]=0 attenzione che s[4] da un errore
E data una stringa la notazione s=[i:j] indica una sottostringa contenente i caratteri da s[i] incluso ed s[j] escluso
Se i è omesso la stringa parte dal primo carattere s[:4]
Se j è omesso la stringa termina fino all ultimo carattere s[i:]
Se l'indice i:j sono negativi indicano i caratteri al contrario partendo da -1 da dx a sx

Data una stringa s per sapere se nella stringa s è presente una sottostringa s1 si invoca la funzione find() che accetta due argomenti:
- la stringa da cercare
- la posizione da cui deve inziare a cercare
- sintassi s.pos(s1,pos) e tale funzione ritorna la posizione dove è presente s1
- Se s1 non è presente nella stringa viene ritornato dalla funzione -1



# Esempio indici strighe
a = 'ciao'
print(a[0])        # indice 0 = c
print(a[:4])       # mostra tutta la stringa
print(a[0:])       # mostra tutta la stringa
print(a[-1:])      # mostra il carattere o 
print(a[-4])       # mostra il carattere c


# cercare tramite find() caratteri e ricevere dalla funzione la loro posizione
Char = input('Inserisci il carattere che cerchi: ')
pos = a.find(char,0)
print('La posizione del carattere cercato è: ',pos,a[pos],sep=' ')


PSEUDOCODICE
- Chiedere all'utente l'indirizzo ip completo in stringa
- Estrapolare ogni numero dalla stringa
    - cercare tramite find() e dato che trova la prima posizione del '.' , dopo ricevuta la posizione cercare altre due volte sommando 1 alla posizione riceuta
- Trasformare ogni numero in intero e dopo eseguire questa operazione aritmetica N = A*2^24 + B*2^16 + C*2^8 + D
- Trasformarlo in binario ed eliminare 0b
"""

# Chiediamo all utente l'indirizzo IP
ip = input('Inserisci indirizzo IP A.B.C.D :')
print('L\'indirizzo IP inserito è: ',ip)


# aggiungo un po di spazio
print('-' * 50)


# cerchiamo posizione del '.'
pos1 = ip.find('.',0)
print('La prima posizione del . è ',pos1)


# estrapolo il primo ottetto A
a = int(ip[0:pos1])
print(a,type(a),pos1,sep=' ')


# aggiungo un po di spazio
print('-' * 50)


# cerchiamo posizione del '.'
pos2 = ip.find('.',pos1+1)
print('La seconda posizione del . è ',pos2)


# estrapolo il secondo ottetto B
b = int(ip[pos1+1:pos2])
print(b,type(b),pos2,sep=' ')


# aggiungo un po di spazio
print('-' * 50)


# erchiamo posizione del '.'
pos3 = ip.find('.',pos2+1)
print('La terza posizione del . è ',pos3)


# estrapolo il terzo ottetto C
c = int(ip[pos2+1:pos3])
print(c,type(c),pos3,sep=' ')


# aggiungo un po di spazio
print('-' * 50)


# ora sapendo l'ultima posizione del . estrapoliamo l'intero nell ultimo ottetto D
d = int(ip[pos3+1:])  # omettiamo l'altro indice in quanto omettendolo viene iterato fino alla fine della stringa
print("L'ultimo ottetto è: ",d,type(d),sep=' ')
print('-' * 50)


# stampiamo l'indirizzo estrapolato
print("L'indirizzo estrapolato è: ",a,b,c,d,sep=' ')


# effettuiamo operazione aritmetica per estrapolare la somma intera
num = ( (a * 2 ** 24) + (b * 2 ** 16) + (c * 2 ** 8) + d )
print("La somma dell'indirizzo IP è : ",num,type(num))


# trasformiamo la somma intera in binario
binario = bin(num)
print("L'intero: ",num," È trasformato in binario: ",binario)

print("Il binario senza 0b è : ",binario[2:10],binario[10:18],binario[18:26],binario[26:],sep=' ')
