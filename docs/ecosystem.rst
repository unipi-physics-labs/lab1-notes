.. _ecosystem:

Ecosistema Python
=================

Queste brevi note danno alcune indicazioni di base per l'installazione di
Python e dell'ecosistema scientifico associato, e possono essere utili per
mettersi in condizione di eseguire i frammenti di codice contenuti nelle
dispense.

La pagina principale di `Python <https://www.python.org/>`_ è il punto di
ingresso fondamentale per tutte le questioni legate al linguaggio, comprese
l'installazione e la documentazione. Se non avete particolari esigenze (o non
sapete cosa vuol dire avere particolari esigenze) potete prendere l'ultima
versione stabile (e.g., 3.13.7 a settembre 2025).
Il tab "Downloads" in alto nella pagina web dovrebbe indirizzarvi di default
all'ultima versione stabile per il vostro sistema operativo.


Installazione
-------------

Se usate Mac OS o GNU/Linux è garantito che abbiate già una versione di
sistema di Python, e probabilmente questa va bene. Controllare solamente che
non sia più vecchia della 3.7, nel qual caso, probabilmente, vale la pena di
installarne una più recente.

Se invece utilizzate (una versione recente a 64 bit) di Windows, scaricate
l'installer dalla pagina web di Python, e.g.
https://www.python.org/ftp/python/3.13.7/python-3.13.7-amd64.exe

Quando lanciate l'installer potete selezionare l'installazione standard,
assicurandovi di spuntare la check box che aggiunge l'eseguibile ``Python.exe``
alla variabile d'ambiente ``PATH`` (dovrebbe essere in basso nella finestrella
di avvio). Questo vi permetterà di lanciare l'interprete da terminale.


Pacchetti aggiuntivi
--------------------

Oltre al linguaggio, avrete bisogno almeno di tre pacchetti esterni aggiuntivi,
da installare a parte:

* `numpy <https://numpy.org/>`_ per l'algebra lineare;
* `scipy <https://scipy.org/>`_ per il fitting;
* `matplotlib <https://matplotlib.org/>`_ per fare grafici.

Una volta installato Python dovreste essere in grado di installare qualsiasi
pacchetto aggiuntivo utilizzando il comando ``pip``.

.. code-block:: shell

    pip install numpy scipy matplotlib


Altre cose?
-----------

Si. Come minimo avrete bisogno di un `editor di testo`. In realtà è molto
probabile che, una volta che avete iniziato a programmare, vi convinciate
di aver bisogno di un `ambiente intergrato di sviluppo` (`integrated
development environment`, o IDE, in inglese).

Se volete replicare il setup utilizzato in laboratorio, installate
`Visual Studio Code <https://code.visualstudio.com/>`_.

