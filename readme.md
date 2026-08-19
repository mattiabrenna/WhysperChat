# W H Y S P E R   C H A T   1 . 1

Version: WhysperChat 1.1.0
Release: 19/08/2026

========================================================================================================================================================================================================================

OBBIETTIVO DEL PROGETTO:

WhysperChat è una applicazione di messaggistica sviluppata in Python che permette a due o più persone di comunicare attraverso una rete locale utilizzando messaggi cifrati.

L'obiettivo del progetto è comprendere in modo pratico il funzionamento delle comunicazioni client/server, delle reti informatiche e della crittografia simmetrica.

Il programma è composto da due elementi principali:
- un server che gestisce le connessioni e inoltra i messaggi.
- uno o più client che permettono agli utenti di comunicare.

Quando il server viene avviato, genera automaticamente una nuova chiave casuale che sarà valida solamente per quella specifica sessione. Tutti gli utenti che desiderano partecipare alla stessa conversazione dovranno utilizzare la medesima chiave.

Quando un utente scrive un messaggio:
1. Il messaggio viene associato al nome dell'utente (che viene richiesto all'inizio).
2. Il client cifra il messaggio utilizzando la chiave della sessione.
3. Il messaggio cifrato viene inviato al server.
4. Il server inoltra il messaggio agli altri partecipanti.
5. I client destinatari decifrano il messaggio e lo mostrano a schermo.

In questo modo il server non visualizza direttamente il contenuto in chiaro della comunicazione ma solamente i dati cifrati che transitano attraverso la rete.

========================================================================================================================================================================================================================

Requisiti:

- Python 3.13.15
- Libreria cryptography per sfruttare Fernet (da terminale: python -m pip install cryptography) (assicurarsi di aver prima installato python)
- Questa cartella con all'interno i file server.py, client.py e crypto.py
- Un PC che faccia da server
- Almeno un secondo PC che si colleghi al server tramite la stessa rete locale (e con almeno i file crypto.py e client.py, non necessariamente server.py)
- Tutti i partecipanti devono utilizzare la stessa chiave generata dal server per la specifica sessione

NOTA BENE: non sono necessari 3 PC diversi. Ne bastano due per comunicare tra persone diverse. Il PC che ospita il server può comunque essere utilizzato per comunicare aprendo un secondo terminale ed eseguendo client.py.

========================================================================================================================================================================================================================

Funzionamento:

AVVIO SERVER

- Aprire da un PC connesso alla rete il file server.py scrivendo da terminale (dopo essersi recati nella cartella corretta): python server.py
- Il server genererà automaticamente una nuova chiave casuale valida solamente per quella sessione, che sarà da condividere tra i partecipanti

INIZIO COMUNICAZIONE
- Dal PC di una delle persone che vogliono comunicare (può essere anche lo stesso PC che esegue server.py) avviare client.py da un nuovo terminale:

- Il programma richiederà:

    Inserisci l'indirizzo IP del server:   (se si prova il progetto dallo stesso pc possibile inserire da qualsiasi client ip 127.0.0.1)
    Inserisci il tuo nome:
    Inserisci la chiave della chat:

          INDIRIZZI IP

          - Per conoscere il proprio indirizzo IP locale:

              WINDOWS:
                  ipconfig
              Cercare la voce:
                  Indirizzo IPv4

              LINUX:
                  ip addr
              Cercare la voce:
                  inet


- Inserire i dati richiesti.

- Una volta effettuata la connessione sarà possibile inviare e ricevere messaggi.

IMPORTANTE:

Una volta avviato server.py, il terminale che ospita il server non deve essere chiuso durante la comunicazione.
Se si vuole utilizzare lo stesso PC anche come client è necessario aprire un secondo terminale.

========================================================================================================================================================================================================================

IDENTIFICAZIONE UTENTI

- Ogni partecipante sceglie un nome identificativo all'avvio del client, e poi questo nome verrà mostrato durante la comunicazione.

Esempio:

    [Marco] Ciao!
    [Luca] Buongiorno!

========================================================================================================================================================================================================================


CHIAVE DELLA SESSIONE

- Ogni volta che il server viene avviato viene generata una nuova chiave casuale.

- Le chiavi cambiano ad ogni nuova sessione.

- Tutti i partecipanti della stessa sessione devono utilizzare la stessa chiave.

- Se viene inserita una chiave diversa da quella utilizzata dagli altri utenti, i messaggi non potranno essere decifrati correttamente.

IMPORTANTE:

La chiave è un'informazione segreta e non dovrebbe essere condivisa tramite canali non sicuri, in quanto la comunicazione cryptata e nascosta a quel punto non sarebbe più nascosta e indecifrabile.

========================================================================================================================================================================================================================

CHIUSURA DELLA COMUNICAZIONE

- Per uscire dalla chat digitare:
    
  /exit

- In alternativa è possibile chiudere il terminale del client.
- Se il terminale che ospita il server viene chiuso, tutte le connessioni verranno interrotte e la sessione terminerà.

========================================================================================================================================================================================================================
