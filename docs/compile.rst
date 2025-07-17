.. _compile:

Compilazione
============

Il grado di complessità di questo documento è meno che triviale, e queste brevi
note dovrebbero fornire tutte le informazioni necessarie per riuscire nell'impresa.


Pre-requisiti
-------------


Layout
------

La struttura del repositorio è tutto sommato abbastanza tipica, con i file
LaTeX principali al top level, insieme al Makefile ed alcuni file ancillari, ed
una serie di sottocartelle:

* ``figures``: contiene tutte le figure da includere nel documento LaTeX---principalmente
  in formato .pgf, ma anche file .pdf;
* ``macro``: contiene tutte le macro in Python per generare le figure;
* ``misc``: misto di file LaTeX con tutti i comandi e gli ambienti utilizzati nell
  documento;
* ``snippy``: contiene tutti i frammenti di codice in Python usati a scopo illustrativo
  nel documento;
* ``sniptex``: contiene tutti i frammenti di codice tradotti da Python in LaTeX
  per essere inclusi nel documento;
* ``tables``: contiene (alcune del)le tabelle in formato .tex;
* ``tools``: collezione di script in Python per il mantenimento del repositorio.


Figure
------


Frammenti
---------

I frammenti di codice embedded nel documento sono realizzati traducendo automaticamente
il contenuto dei file Python nella cartella ``snippy``. La traduzione è fatta con
lo script :file:`tools/py2tex.py`, che utilizza il pacchetto Pygments per generare
il codice LaTeX da includere nel documento.


Makefile
--------
