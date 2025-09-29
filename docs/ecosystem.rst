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

Se usate Mac OS o GNU/Linux è più o meno garantito che abbiate già una versione di
sistema di Python, e probabilmente questa va bene. Controllare solamente che
non sia più vecchia della 3.7, nel qual caso, probabilmente, vale la pena di
installarne una più recente.

Se utilizzate Windows (e non avete Python installato sul vostro sistema), scaricate
l'installer dalla `pagina web dei downloads <https://www.python.org/downloads/>`_ ed
eseguitelo.

.. note::

    Quando lanciate l'installer di Windows potete selezionare l'installazione standard,
    `assicurandovi di spuntare la check box che aggiunge l'eseguibile ``Python.exe``
    alla variabile d'ambiente ``PATH``` (dovrebbe essere in basso nella finestrella
    di avvio). Questo vi permetterà di lanciare l'interprete da terminale.

Arrivati al termine dell'installazione, ed indipendentemente dal sistema operativo,
assicuratevi di poter lanciare correttamente l'interprete Python dal vostro terminale, i.e.,
digitando ``pyton`` e premendo INVIO dovreste vedere qualcosa di simile a

.. code-block::

    python
    Python 3.13.7 (main, Aug 14 2025, 00:00:00) [GCC 15.2.1 20250808 (Red Hat 15.2.1-1)] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

Se vedete apparire i tre caratteri ``>>>`` siete a cavallo---potete iniziare ad eseguire
comandi Python interattivamente. In caso contrario fate un respiro profondo e cercate di
capire se e cosa non è andato secondo i piani, perché con ogni probabilità non avrete fortuna
con la prossima sezione.

.. warning::

    A seconda del sistema operativo (e.g., con versioni recenti di Mac OS) è possibile che
    il comando per lanciare l'interprete Python non si chiami ``python`` ma ``python3``.
    Si tratta di accidente storico che, nel 2025, è estremamente poco interessante; il
    messaggio è: se non funziona il prima provate il secondo prima di gettare la spugna.


Pacchetti aggiuntivi
--------------------

Una volta installato Python siete a buon punto, ma non ancora alla fine: oltre al linguaggio,
avrete bisogno almeno di tre pacchetti esterni aggiuntivi, da installare a parte:

* `numpy <https://numpy.org/>`_ per l'algebra lineare;
* `scipy <https://scipy.org/>`_ per il fitting (tra le altre cose);
* `matplotlib <https://matplotlib.org/>`_ per fare grafici.

La buona notizia è che, se potete lanciare l'interprete Python da terminale, con ogni
probabilità potete anche lanciare il `package installer`, ``pip``:

.. code-block:: shell

    pip install numpy scipy matplotlib

Se tutto è andato come doveva, a questo punto dovreste essere in grado di lanciare
l'inteprete Python ed importare i pacchetti

.. code-block::

    python
    Python 3.13.7 (main, Aug 14 2025, 00:00:00) [GCC 15.2.1 20250808 (Red Hat 15.2.1-1)] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import numpy
    >>> import scipy
    >>> import matplotlib
    >>>

Se tutti e tre i comandi di import arrivano a completamento senza messaggi d'errore,
congratulazione: siete quasi pronti! Se invece vedete qualcosa di simile a

.. code-block::

    >>> import numpy
    Traceback (most recent call last):
      File "<python-input-0>", line 1, in <module>
        import numpy
    ModuleNotFoundError: No module named 'numpy'
    >>>

allora, purtroppo, qualcosa è andato storto.

.. warning::

    Se siete su uno di quei sistemi (e.g., Mac OS) in cui l'inteprete Python si chiama
    ``python3`` e non ``python``, allora con ogni probabilità il `package manager` si chiama
    ``pip3`` e non ``pip``. Vale quanto detto prima: in questo caso provate

    .. code-block:: shell

        pip3 install numpy scipy matplotlib



Altre cose?
-----------

Si. Come minimo avrete bisogno di un `editor di testo`. In realtà è molto
probabile che, una volta che avete iniziato a programmare, vi convinciate
di aver bisogno di un `ambiente intergrato di sviluppo` (`integrated
development environment`, o IDE, in inglese).

Se volete replicare il setup utilizzato in laboratorio, installate
`Visual Studio Code <https://code.visualstudio.com/>`_.



Funziona tutto?
---------------

Prova a copiare ed incollare il codice qui sotto nel tuo editor preferito e ad eseguirlo.
Se appare un grafico con dei punti ed una retta dovresti essere `up and running`!


.. code-block:: python

    import numpy as np
    from matplotlib import pyplot as plt
    from scipy.optimize import curve_fit

    def fit_model(x, m, q):
        return m * x + q

    t = np.array([1., 2., 3., 4., 5., 6., 7., 8., 9., 10.])
    z = np.array([2.4, 4.3, 5.2, 8.55, 9.38, 12.2, 14.5, 16.2, 17.3, 19.5])
    sigma_z = 0.5

    popt, pcov = curve_fit(fit_model, t, z, sigma=sigma_z)

    plt.errorbar(t, z, sigma_z, fmt='o')
    plt.plot(t, fit_model(t, *popt))
    plt.xlabel('Tempo [s]')
    plt.ylabel('Spazio percorso [cm]')

    plt.show()