"""Textos de la web en catalán e inglés. La clave es el texto TAL CUAL está en index.html (castellano, que es la fuente);
el valor es (catalán, inglés). `build.py` sustituye cada clave en una sola pasada y avisa si alguna no aparece.

Criterio: cada idioma escribe los nombres de los idiomas y las pestañas del programa como los escribe el propio programa
(Inici / Comptes / Inversions / Importar / Configuració; Home / Accounts / Investments / Import / Settings)."""

T = {
    '<title>Kreix, guía de usuario</title>': (
        "<title>Kreix, guia d'usuari</title>",
        '<title>Kreix, user guide</title>'),
    'Kreix es la app de finanzas personales que no te vigila: no te pide las claves del banco, funciona sin conexión y guarda todo cifrado en tu ordenador. Esta es su guía.': (
        "Kreix és l'app de finances personals que no et vigila: no et demana les claus del banc, funciona sense connexió i ho guarda tot xifrat al teu ordinador. Aquesta és la seva guia.",
        'Kreix is the personal finance app that does not watch you: it never asks for your bank login details, works offline and keeps everything encrypted on your computer. This is its guide.'),
    'Kreix nunca te pide las claves de tu banco': (
        'Kreix mai no et demana les claus del teu banc',
        'Kreix never asks for your bank login details'),
    'La app de finanzas que no te vigila: sin claves del banco, sin conexión y con todo cifrado en tu ordenador.': (
        "L'app de finances que no et vigila: sense claus del banc, sense connexió i amb tot xifrat al teu ordinador.",
        'The finance app that does not watch you: no bank login details, no connection, everything encrypted on your computer.'),
    'Saltar al contenido': (
        'Salta al contingut',
        'Skip to content'),
    'aria-label="Kreix, inicio"': (
        'aria-label="Kreix, inici"',
        'aria-label="Kreix, home"'),
    'aria-label="Principal"': (
        'aria-label="Principal"',
        'aria-label="Main"'),
    'aria-label="Idioma"': (
        'aria-label="Idioma"',
        'aria-label="Language"'),
    '>Primeros pasos</a>': (
        '>Primers passos</a>',
        '>Getting started</a>'),
    '>La guía</a>': (
        '>La guia</a>',
        '>The guide</a>'),
    '>Seguridad</a>': (
        '>Seguretat</a>',
        '>Security</a>'),
    '>Preguntas</a>': (
        '>Preguntes</a>',
        '>Questions</a>'),
    '>Kreix es para Windows</span>': (
        '>Kreix és per a Windows</span>',
        '>Kreix is for Windows</span>'),
    'data-done="Enlace copiado"': (
        'data-done="Enllaç copiat"',
        'data-done="Link copied"'),
    '>Copiar enlace</button>': (
        ">Copia l'enllaç</button>",
        '>Copy link</button>'),
    'Abre esta página en tu ordenador para descargarlo.': (
        "Obre aquesta pàgina a l'ordinador per descarregar-lo.",
        'Open this page on your computer to download it.'),
    '>Descargar igualmente (37&nbsp;MB)</a>': (
        '>Descarrega-ho igualment (37&nbsp;MB)</a>',
        '>Download anyway (37&nbsp;MB)</a>'),
    '>Descargar</a>': (
        '>Descarrega</a>',
        '>Download</a>'),
    '>Descargar para Windows</a>': (
        '>Descarrega per a Windows</a>',
        '>Download for Windows</a>'),
    'aria-label="Cambiar entre tema claro y oscuro" title="Cambiar tema"': (
        'aria-label="Canviar entre tema clar i fosc" title="Canviar tema"',
        'aria-label="Switch between light and dark theme" title="Change theme"'),
    'Kreix nunca te&nbsp;pide las claves de&nbsp;tu&nbsp;banco.': (
        'Kreix mai no et&nbsp;demana les claus del&nbsp;teu&nbsp;banc.',
        'Kreix never asks for your&nbsp;bank login&nbsp;details.'),
    'La app de finanzas personales para Windows que no te vigila: <strong>funciona sin conexión</strong> y guarda todo <strong>cifrado en tu ordenador</strong>.': (
        "L'app de finances personals per a Windows que no et vigila: <strong>funciona sense connexió</strong> i ho guarda tot <strong>xifrat al teu ordinador</strong>.",
        'The personal finance app for Windows that does not watch you: <strong>it works offline</strong> and keeps everything <strong>encrypted on your computer</strong>.'),
    'Empezar la guía': (
        'Comença la guia',
        'Start the guide'),
    'Cómo se protegen tus datos': (
        'Com es protegeixen les teves dades',
        'How your data is protected'),
    'Versión 0.5.0 para Windows 10 y 11 (64 bits). Si Windows te avisa al abrirlo es porque el instalador aún no está firmado: pulsa «Más información» y luego «Ejecutar de todas formas».': (
        "Versió 0.5.0 per a Windows 10 i 11 (64 bits). Si Windows t'avisa en obrir-lo és perquè l'instal·lador encara no està signat: prem «Més informació» i després «Executa de totes maneres».",
        'Version 0.5.0 for Windows 10 and 11 (64-bit). If Windows warns you when you open it, that is because the installer is not signed yet: click “More info” and then “Run anyway”.'),
    'Sin tus claves del banco': (
        'Sense les claus del teu banc',
        'No bank login details'),
    'Tú descargas el extracto y lo sueltas en Kreix. Kreix nunca entra en tu banca ni guarda tus claves.': (
        "Tu descarregues l'extracte i el deixes anar a Kreix. Kreix mai no entra a la teva banca ni guarda les teves claus.",
        'You download the statement and drop it into Kreix. Kreix never logs in to your bank and never stores your login details.'),
    '100&nbsp;% sin conexión': (
        '100&nbsp;% sense connexió',
        '100% offline'),
    'No se conecta a internet: ni para actualizarse ni para enviar nada. Sin cuenta, sin nube, sin anuncios y sin telemetría.': (
        'No es connecta a internet: ni per actualitzar-se ni per enviar res. Sense compte, sense núvol, sense anuncis i sense telemetria.',
        'It never connects to the internet: not to update itself, not to send anything. No account, no cloud, no ads and no telemetry.'),
    'Tus datos, cifrados': (
        'Les teves dades, xifrades',
        'Your data, encrypted'),
    'Todo lo que guarda Kreix va cifrado con tu contraseña maestra. Sin ella, nadie puede leerlo, tampoco nosotros. Exportar también puede cifrarse.': (
        "Tot el que guarda Kreix va xifrat amb la teva contrasenya mestra. Sense ella, ningú ho pot llegir, tampoc nosaltres. L'exportació també es pot xifrar.",
        'Everything Kreix stores is encrypted with your master password. Without it, nobody can read it, not even us. Exports can be encrypted too.'),
    'Pantalla de Inicio de Kreix: patrimonio neto, rendimiento, tasa de ahorro y previsión a fin de mes.': (
        "Pantalla d'Inici de Kreix: patrimoni net, rendiment, taxa d'estalvi i previsió a final de mes.",
        'Kreix Home screen: net worth, return, savings rate and end-of-month forecast.'),
    'Pantalla de Inicio de Kreix en tema claro.': (
        "Pantalla d'Inici de Kreix en tema clar.",
        'Kreix Home screen in the light theme.'),
    'Empieza en tres pasos': (
        'Comença en tres passos',
        'Start in three steps'),
    'Sin enlazar cuentas y sin dar acceso a nadie: solo un archivo que ya puedes descargar de tu banco.': (
        'Sense enllaçar comptes i sense donar accés a ningú: només un arxiu que ja pots descarregar del teu banc.',
        'Without linking accounts or giving anyone access: just a file you can already download from your bank.'),
    'Descarga el extracto': (
        "Descarrega l'extracte",
        'Download the statement'),
    'Desde la web o la app de tu banco, en CSV o Excel. Es el mismo archivo que bajarías para guardarlo.': (
        "Des del web o l'app del teu banc, en CSV o Excel. És el mateix arxiu que baixaries per guardar-lo.",
        "From your bank's website or app, as CSV or Excel. It is the same file you would download to keep."),
    'Suéltalo en Kreix': (
        "Deixa'l anar a Kreix",
        'Drop it into Kreix'),
    'Arrástralo a Importar. Kreix te enseña lo que ha leído y no guarda nada hasta que pulses Importar. Si repites un extracto, no duplica movimientos.': (
        "Arrossega'l a Importar. Kreix et mostra el que ha llegit i no guarda res fins que premis Importar. Si repeteixes un extracte, no duplica moviments.",
        'Drag it onto Import. Kreix shows you what it read and saves nothing until you press Import. If you import the same statement again, Kreix does not duplicate transactions.'),
    'Mira tu dinero': (
        'Mira els teus diners',
        'See your money'),
    'Inicio resume tu patrimonio, tu ahorro del mes y lo que está por venir. Cuentas e Inversiones lo detallan.': (
        'Inici resumeix el teu patrimoni, el teu estalvi del mes i el que ha de venir. Comptes i Inversions ho detallen.',
        'Home summarises your net worth, your savings this month and what is coming. Accounts and Investments give the detail.'),
    'La guía, pantalla a pantalla': (
        'La guia, pantalla a pantalla',
        'The guide, screen by screen'),
    'Cada pestaña de la barra lateral, en pocas palabras. Los datos de las capturas son inventados.': (
        'Cada pestanya de la barra lateral, en poques paraules. Les dades de les captures són inventades.',
        'Each tab in the sidebar, in a few words. The data in the screenshots is made up.'),
    'aria-label="Pantallas de Kreix"': (
        'aria-label="Pantalles de Kreix"',
        'aria-label="Kreix screens"'),
    '>Inicio</button>': (
        '>Inici</button>',
        '>Home</button>'),
    '>Cuentas</button>': (
        '>Comptes</button>',
        '>Accounts</button>'),
    '>Inversiones</button>': (
        '>Inversions</button>',
        '>Investments</button>'),
    '>Importar</button>': (
        '>Importar</button>',
        '>Import</button>'),
    '>Ajustes</button>': (
        '>Configuració</button>',
        '>Settings</button>'),
    'Todo lo importante de un vistazo': (
        "Tot l'important d'un cop d'ull",
        'Everything important at a glance'),
    'Tu patrimonio neto, la rentabilidad y la tasa de ahorro del mes.': (
        "El teu patrimoni net, la rendibilitat i la taxa d'estalvi del mes.",
        "Your net worth, your return and this month's savings rate."),
    'Una previsión de cuánto dinero tendrás a fin de mes, con tus pagos fijos.': (
        'Una previsió de quants diners tindràs a final de mes, amb els teus pagaments fixos.',
        'A forecast of how much money you will have at the end of the month, counting your fixed payments.'),
    'Próximos pagos, presupuestos y los movimientos que aún no tienen categoría.': (
        'Pròxims pagaments, pressupostos i els moviments que encara no tenen categoria.',
        'Upcoming payments, budgets and the transactions that have no category yet.'),
    'Inicio de Kreix en tema oscuro.': (
        'Inici de Kreix en tema fosc.',
        'Kreix Home in the dark theme.'),
    'Inicio de Kreix en tema claro.': (
        'Inici de Kreix en tema clar.',
        'Kreix Home in the light theme.'),
    'Tus gastos, claros': (
        'Les teves despeses, clares',
        'Your spending, made clear'),
    'Gastos por categoría y evolución del saldo, de un mes o de todo el historial.': (
        "Despeses per categoria i evolució del saldo, d'un mes o de tot l'historial.",
        'Spending by category and balance over time, for one month or the whole history.'),
    'Cambia la categoría de un movimiento con clic derecho, o crea tus propias reglas.': (
        "Canvia la categoria d'un moviment amb clic dret, o crea les teves pròpies regles.",
        "Change a transaction's category with a right click, or create your own rules."),
    'Presupuestos por categoría y pagos recurrentes detectados.': (
        'Pressupostos per categoria i pagaments recurrents detectats.',
        'Budgets by category and detected recurring payments.'),
    'Cuentas en tema oscuro: saldo, ingresos, gastos y gráficos.': (
        'Comptes en tema fosc: saldo, ingressos, despeses i gràfics.',
        'Accounts in the dark theme: balance, income, expenses and charts.'),
    'Cuentas en tema claro.': (
        'Comptes en tema clar.',
        'Accounts in the light theme.'),
    'Tu cartera de fondos': (
        'La teva cartera de fons',
        'Your fund portfolio'),
    'Valor de la cartera, lo aportado, la plusvalía y la rentabilidad.': (
        "Valor de la cartera, l'aportat, la plusvàlua i la rendibilitat.",
        'Portfolio value, amount contributed, gain and return.'),
    'Distribución por fondo y evolución frente a lo que has aportado.': (
        'Distribució per fons i evolució respecte al que has aportat.',
        'Breakdown by fund and growth compared with what you have contributed.'),
    'Se alimenta de las operaciones y la cartera que exportas de MyInvestor.': (
        "S'alimenta de les operacions i la cartera que exportes de MyInvestor.",
        'It is built from the orders and the portfolio you export from MyInvestor.'),
    'Inversiones en tema oscuro: valor de la cartera y distribución por fondo.': (
        'Inversions en tema fosc: valor de la cartera i distribució per fons.',
        'Investments in the dark theme: portfolio value and breakdown by fund.'),
    'Inversiones en tema claro.': (
        'Inversions en tema clar.',
        'Investments in the light theme.'),
    'Soltar y revisar': (
        'Deixar anar i revisar',
        'Drop and review'),
    'Arrastra los CSV o Excel de tu banco a la zona de importación.': (
        "Arrossega els CSV o Excel del teu banc a la zona d'importació.",
        "Drag your bank's CSV or Excel files onto the import area."),
    'Ves qué se ha leído antes de guardar, y casi todo se puede deshacer.': (
        "Veus què s'ha llegit abans de guardar, i gairebé tot es pot desfer.",
        'You see what was read before saving, and almost everything can be undone.'),
    'Si Kreix no reconoce el archivo, te pregunta qué columna es cada cosa y lo recuerda.': (
        "Si Kreix no reconeix l'arxiu, et pregunta quina columna és cada cosa i ho recorda.",
        'If Kreix does not recognise the file, it asks you which column is which and remembers it.'),
    'Importar en tema oscuro: zona para soltar extractos y resultado de la importación.': (
        'Importar en tema fosc: zona per deixar anar extractes i resultat de la importació.',
        'Import in the dark theme: area to drop statements and the import result.'),
    'Importar en tema claro.': (
        'Importar en tema clar.',
        'Import in the light theme.'),
    'A tu manera': (
        'A la teva manera',
        'Your way'),
    'Castellano, catalán o inglés, con cambio al instante.': (
        "Castellà, català o anglès, amb canvi a l'instant.",
        'Spanish, Catalan or English, switching instantly.'),
    'Tema claro u oscuro, tamaño del texto y cielo animado en Inicio.': (
        'Tema clar o fosc, mida del text i cel animat a Inici.',
        'Light or dark theme, text size and an animated sky on Home.'),
    'Contraseña, bloqueo automático y copias de seguridad cifradas.': (
        'Contrasenya, bloqueig automàtic i còpies de seguretat xifrades.',
        'Password, automatic lock and encrypted backups.'),
    'Ajustes en tema oscuro: nombre, idioma y lo que te interesa.': (
        "Configuració en tema fosc: nom, idioma i el que t'interessa.",
        'Settings in the dark theme: name, language and what you are interested in.'),
    'Ajustes en tema claro.': (
        'Configuració en tema clar.',
        'Settings in the light theme.'),
    'Un ojo para cuando miran por encima del hombro': (
        "Un ull per a quan et miren per sobre l'espatlla",
        'An eye for when someone looks over your shoulder'),
    'Con un clic, o con Ctrl+H, Kreix difumina todas las cantidades: en cifras, tablas y gráficos. Se nota que hay un número, pero no cuál. Pruébalo.': (
        'Amb un clic, o amb Ctrl+H, Kreix difumina totes les quantitats: en xifres, taules i gràfics. Es nota que hi ha un número, però no quin. Prova-ho.',
        'With one click, or Ctrl+H, Kreix blurs every amount, in figures, tables and charts. You can tell there is a number, but not which one. Try it.'),
    'Patrimonio neto (datos de ejemplo)': (
        "Patrimoni net (dades d'exemple)",
        'Net worth (sample data)'),
    '8.586,64&nbsp;€': (
        '8.586,64&nbsp;€',
        '€8,586.64'),
    'Cantidad oculta': (
        'Quantitat oculta',
        'Amount hidden'),
    '+66,64&nbsp;€ frente al mes pasado': (
        '+66,64&nbsp;€ respecte al mes passat',
        '+€66.64 vs last month'),
    'data-hide="Ocultar cantidades" data-show="Mostrar cantidades"': (
        'data-hide="Amagar les quantitats" data-show="Mostrar les quantitats"',
        'data-hide="Hide amounts" data-show="Show amounts"'),
    '>Ocultar cantidades<': (
        '>Amagar les quantitats<',
        '>Hide amounts<'),
    'Categorías automáticas': (
        'Categories automàtiques',
        'Automatic categories'),
    'Kreix clasifica tus gastos por sí mismo, y tus reglas mandan sobre las suyas.': (
        'Kreix classifica les teves despeses tot sol, i les teves regles manen sobre les seves.',
        'Kreix sorts your spending by itself, and your rules take priority over its own.'),
    '<h3>Pagos recurrentes</h3>': (
        '<h3>Pagaments recurrents</h3>',
        '<h3>Recurring payments</h3>'),
    'Detecta suscripciones y recibos, y te dice cuándo toca el siguiente. Quitas los que ya no pagas.': (
        'Detecta subscripcions i rebuts, i et diu quan toca el següent. Treus els que ja no pagues.',
        'It detects subscriptions and bills, and tells you when the next one is due. You remove the ones you no longer pay.'),
    'Casi todo se puede deshacer': (
        'Gairebé tot es pot desfer',
        'Almost everything can be undone'),
    'Cada cambio importante muestra un aviso con el botón Deshacer.': (
        'Cada canvi important mostra un avís amb el botó Desfer.',
        'Every important change shows a notice with an Undo button.'),
    'Tus datos no salen de tu ordenador': (
        'Les teves dades no surten del teu ordinador',
        'Your data never leaves your computer'),
    'No hay que fiarse de una promesa: Kreix está hecho para que no tenga nada que enviar ni a dónde enviarlo.': (
        "No cal refiar-se d'una promesa: Kreix està fet perquè no tingui res a enviar ni on enviar-ho.",
        'You do not have to trust a promise: Kreix is built so that it has nothing to send and nowhere to send it.'),
    'Cómo viajan tus datos': (
        'Com viatgen les teves dades',
        'How your data travels'),
    'Tú descargas el extracto de tu banco y lo llevas a Kreix, en tu ordenador, donde se guarda cifrado. No hay ninguna conexión entre Kreix e internet.': (
        "Tu descarregues l'extracte del teu banc i el portes a Kreix, al teu ordinador, on es guarda xifrat. No hi ha cap connexió entre Kreix i internet.",
        'You download the statement from your bank and bring it to Kreix, on your computer, where it is stored encrypted. There is no connection between Kreix and the internet.'),
    'font-size="24" font-weight="700">Tu banco</text>': (
        'font-size="21" font-weight="700">El teu banc</text>',
        'font-size="24" font-weight="700">Your bank</text>'),
    'font-size="23" font-weight="700">Tu banco</text>': (
        'font-size="23" font-weight="700">El teu banc</text>',
        'font-size="23" font-weight="700">Your bank</text>'),
    '>extracto</text>': (
        '>extracte</text>',
        '>statement</text>'),
    '>CSV o Excel</text>': (
        '>CSV o Excel</text>',
        '>CSV or Excel</text>'),
    '>Tu ordenador</text>': (
        '>El teu ordinador</text>',
        '>Your computer</text>'),
    '>cálculos y gráficos</text>': (
        '>càlculs i gràfics</text>',
        '>figures and charts</text>'),
    '>Archivo cifrado</text>': (
        '>Arxiu xifrat</text>',
        '>Encrypted file</text>'),
    '>AES + contraseña maestra</text>': (
        '>AES + contrasenya mestra</text>',
        '>AES + master password</text>'),
    '>Sin conexión</text>': (
        '>Sense xarxa</text>',
        '>Offline</text>'),
    '<h3>Sin red</h3>': (
        '<h3>Sense xarxa</h3>',
        '<h3>No network</h3>'),
    'Kreix no incluye funciones de conexión a internet: ni para actualizarse, ni para enviar datos, ni para medir cómo lo usas.': (
        "Kreix no inclou funcions de connexió a internet: ni per actualitzar-se, ni per enviar dades, ni per mesurar com l'uses.",
        'Kreix has no features that use the internet: it does not update itself, send data or track how you use it.'),
    'Cifrado de verdad': (
        'Xifratge de debò',
        'Real encryption'),
    'Los datos se cifran con AES y una clave que sale de tu contraseña (PBKDF2-SHA256 con 600.000 iteraciones). Si alguien lo manipula, deja de abrirse.': (
        "Les dades es xifren amb AES i una clau que surt de la teva contrasenya (PBKDF2-SHA256 amb 600.000 iteracions). Si algú manipula l'arxiu, deixa d'obrir-se.",
        'Your data is encrypted with AES and a key derived from your password (PBKDF2-SHA256 with 600,000 iterations). If anyone tampers with the file, it will no longer open.'),
    'Nada en claro en el disco': (
        'Res en clar al disc',
        'Nothing unencrypted on disk'),
    'Al abrir Kreix, tus datos se descifran solo en memoria. No se escriben archivos temporales sin cifrar.': (
        "En obrir Kreix, les teves dades es desxifren només a la memòria. No s'escriuen arxius temporals sense xifrar.",
        'When you open Kreix, your data is decrypted only in memory. No unencrypted temporary files are written.'),
    'La contraseña es solo tuya': (
        'La contrasenya és només teva',
        'Only you hold the password'),
    'Nadie más la tiene. Por eso, si la olvidas, tampoco se puede recuperar nada: tendrías que empezar de cero.': (
        "Ningú més la té. Per això, si l'oblides, tampoc es pot recuperar res: hauries de començar de zero.",
        'Nobody else has it. That is why, if you forget it, nothing can be recovered: you would have to start from scratch.'),
    'Compruébalo tú': (
        'Comprova-ho tu',
        'Check it yourself'),
    'Desconecta el wifi o el cable de red.': (
        'Desconnecta el wifi o el cable de xarxa.',
        'Disconnect Wi-Fi or the network cable.'),
    'Abre Kreix y úsalo con normalidad: importa, mira tus gráficos, cambia categorías. Todo funciona igual, porque nunca ha necesitado conexión.': (
        'Obre Kreix i fes-lo servir amb normalitat: importa, mira els teus gràfics, canvia categories. Tot funciona igual, perquè mai no ha necessitat connexió.',
        'Open Kreix and use it as usual: import, look at your charts, change categories. Everything works the same, because it never needed a connection.'),
    'Para más garantías, crea en el Firewall de Windows una regla de salida que bloquee Kreix y comprueba que sigue funcionando.': (
        'Per a més garanties, crea al Tallafoc de Windows una regla de sortida que bloquegi Kreix i comprova que continua funcionant.',
        'For extra assurance, create an outbound rule in Windows Firewall that blocks Kreix and check that it keeps working.'),
    'Lo que conviene saber': (
        'Què convé saber',
        'Good to know'),
    'El archivo que crea Exportar (.kreix) puede cifrarse con tu contraseña, pero no es obligatorio. Si no lo cifras, guárdalo en un sitio seguro. Y apunta tu contraseña maestra en un lugar seguro: si la pierdes, no hay forma de recuperar tus datos.': (
        "L'arxiu que crea Exportar (.kreix) es pot xifrar amb la teva contrasenya, però no és obligatori. Si no el xifres, guarda'l en un lloc segur. I apunta la teva contrasenya mestra en un lloc segur: si la perds, no hi ha manera de recuperar les teves dades.",
        'The file that Export creates (.kreix) can be encrypted with your password, but that is optional. If you do not encrypt it, keep it somewhere safe. And write down your master password somewhere safe: if you lose it, there is no way to recover your data.'),
    'Funciona con tu banco': (
        'Funciona amb el teu banc',
        'Works with your bank'),
    'Kreix lee CSV y Excel (.xlsx y el antiguo .xls). Reconoce estos formatos por sus columnas habituales.': (
        "Kreix llegeix CSV i Excel (.xlsx i l'antic .xls). Reconeix aquests formats per les seves columnes habituals.",
        'Kreix reads CSV and Excel (.xlsx and the older .xls). It recognises these formats by their usual columns.'),
    '>Cualquier otro<': (
        '>Qualsevol altre<',
        '>Any other bank<'),
    'Si Kreix no reconoce un archivo, te enseña sus primeras filas y te pregunta qué columna es la fecha, el concepto y el importe. Lo recuerda para la próxima vez. Los formatos de CaixaBank, Santander, Revolut y Trade Republic están incluidos, pero todavía en pruebas.': (
        "Si Kreix no reconeix un arxiu, et mostra les primeres files i et pregunta quina columna és la data, el concepte i l'import. Ho recorda per a la propera vegada. Els formats de CaixaBank, Santander, Revolut i Trade Republic estan inclosos, però encara en proves.",
        'If Kreix does not recognise a file, it shows you the first rows and asks which column is the date, the description and the amount. It remembers for next time. The CaixaBank, Santander, Revolut and Trade Republic formats are included but still being tested.'),
    'Preguntas frecuentes': (
        'Preguntes freqüents',
        'Frequently asked questions'),
    '¿Kreix necesita mis claves o acceso a mi banco?': (
        'Necessita Kreix les meves claus o accés al meu banc?',
        'Does Kreix need my login details or access to my bank?'),
    'No, nunca. Kreix no se conecta a tu banco. Trabaja con los extractos que descargas tú.': (
        'No, mai. Kreix no es connecta al teu banc. Treballa amb els extractes que descarregues tu.',
        'No, never. Kreix does not connect to your bank. It works with the statements you download yourself.'),
    '¿Se conecta a internet?': (
        'Es connecta a internet?',
        'Does it connect to the internet?'),
    'No. Funciona exactamente igual sin conexión, y no incluye nada para enviar información fuera de tu ordenador.': (
        'No. Funciona exactament igual sense connexió, i no inclou res per enviar informació fora del teu ordinador.',
        'No. It works exactly the same offline, and it has nothing to send information outside your computer.'),
    '¿Dónde se guardan mis datos?': (
        'On es guarden les meves dades?',
        'Where is my data stored?'),
    'En un archivo cifrado dentro de tu carpeta de datos de aplicación (en Windows, %APPDATA%\\Kreix). Solo se descifran en memoria mientras Kreix está abierto.': (
        "En un arxiu xifrat dins de la teva carpeta de dades d'aplicació (a Windows, %APPDATA%\\Kreix). Només es desxifren a la memòria mentre Kreix està obert.",
        'In an encrypted file inside your application data folder (on Windows, %APPDATA%\\Kreix). It is only decrypted in memory while Kreix is open.'),
    '¿Qué pasa si olvido la contraseña?': (
        'Què passa si oblido la contrasenya?',
        'What happens if I forget the password?'),
    'No se puede recuperar: no existe ninguna llave de repuesto, y por eso nadie más puede leer tus datos. Podrás empezar de cero con una contraseña nueva. Guarda copias de seguridad y apunta la contraseña en un sitio seguro.': (
        'No es pot recuperar: no hi ha cap clau de recanvi, i per això ningú més pot llegir les teves dades. Podràs començar de zero amb una contrasenya nova. Guarda còpies de seguretat i apunta la contrasenya en un lloc segur.',
        'It cannot be recovered: there is no spare key, which is why nobody else can read your data. You can start from scratch with a new password. Keep backups and write the password down somewhere safe.'),
    '¿Qué pasa si importo dos veces el mismo extracto?': (
        'Què passa si importo dues vegades el mateix extracte?',
        'What happens if I import the same statement twice?'),
    'Nada: Kreix reconoce los movimientos que ya tiene y no los duplica.': (
        'Res: Kreix reconeix els moviments que ja té i no els duplica.',
        'Nothing: Kreix recognises the transactions it already has and does not duplicate them.'),
    '¿Puedo llevarme mis datos a otro ordenador?': (
        'Puc endur-me les meves dades a un altre ordinador?',
        'Can I take my data to another computer?'),
    'Sí. Exportar crea un archivo .kreix que sueltas en Importar en el otro equipo. Puedes cifrarlo con tu contraseña. Importarlo reemplaza los datos que hubiera allí.': (
        "Sí. Exportar crea un arxiu .kreix que deixes anar a Importar a l'altre equip. El pots xifrar amb la teva contrasenya. Importar-lo substitueix les dades que hi hagués.",
        'Yes. Export creates a .kreix file that you drop into Import on the other computer. You can encrypt it with your password. Importing it replaces any data that was there.'),
    '¿Puedo deshacer un cambio?': (
        'Puc desfer un canvi?',
        'Can I undo a change?'),
    'Casi todos los cambios importantes muestran un aviso con el botón Deshacer: importar, cambiar categorías, crear reglas, presupuestos y borrados.': (
        'Gairebé tots els canvis importants mostren un avís amb el botó Desfer: importar, canviar categories, crear regles, pressupostos i esborrats.',
        'Almost every important change shows a notice with an Undo button: imports, category changes, new rules, budgets and deletions.'),
    '¿En qué idiomas está?': (
        'En quins idiomes està?',
        'Which languages is it available in?'),
    'Castellano, catalán e inglés. Se elige la primera vez que lo abres y se cambia cuando quieras en Ajustes.': (
        "Castellà, català i anglès. S'escull la primera vegada que l'obres i es canvia quan vulguis a Configuració.",
        'Spanish, Catalan and English. You choose when you first open it and can change it at any time in Settings.'),
    '¿Funciona en Mac o en el móvil?': (
        'Funciona en Mac o al mòbil?',
        'Does it work on Mac or on a phone?'),
    'Por ahora, solo en Windows. Una versión para el móvil está en estudio.': (
        'Per ara, només a Windows. Una versió per al mòbil està en estudi.',
        'For now, only on Windows. A phone version is being considered.'),
    '¿Cómo lo instalo?': (
        "Com l'instal·lo?",
        'How do I install it?'),
    'Descarga el instalador y ábrelo. No pide permisos de administrador y crea un acceso directo en Inicio y en el escritorio. Como el instalador aún no está firmado, Windows puede avisarte la primera vez: pulsa «Más información» y «Ejecutar de todas formas».': (
        "Descarrega l'instal·lador i obre'l. No demana permisos d'administrador i crea una drecera a Inici i a l'escriptori. Com que l'instal·lador encara no està signat, Windows pot avisar-te la primera vegada: prem «Més informació» i «Executa de totes maneres».",
        'Download the installer and open it. It does not ask for administrator rights and it adds a shortcut to Start and to the desktop. Because the installer is not signed yet, Windows may warn you the first time: click “More info” and then “Run anyway”.'),
    'Tu dinero, tu ordenador, tus reglas.': (
        'Els teus diners, el teu ordinador, les teves regles.',
        'Your money, your computer, your rules.'),
    '© 2026 Daniel Suárez Angosto. Todos los derechos reservados.': (
        '© 2026 Daniel Suárez Angosto. Tots els drets reservats.',
        '© 2026 Daniel Suárez Angosto. All rights reserved.'),
    'Kreix 0.5.0 es software propietario de código disponible: puedes usarlo, pero no copiarlo, redistribuirlo ni venderlo. Los datos de las capturas son inventados.': (
        'Kreix 0.5.0 és programari propietari de codi disponible: el pots fer servir, però no copiar-lo, redistribuir-lo ni vendre\'l. Les dades de les captures són inventades.',
        'Kreix 0.5.0 is proprietary, source-available software: you may use it, but not copy, redistribute or sell it. The data in the screenshots is made up.'),
    'Volver arriba': (
        'Torna amunt',
        'Back to top'),
    '<span>Menú</span>': (
        '<span>Menú</span>',
        '<span>Menu</span>'),
    'No te vigila': (
        'No et vigila',
        'It never watches you'),
    'Sin cuenta, sin nube y sin telemetría. Nadie sabe cuánto ganas ni en qué lo gastas, ni siquiera nosotros. Compruébalo: funciona igual sin internet.': (
        'Sense compte, sense núvol i sense telemetria. Ningú sap quant guanyes ni en què ho gastes, ni tan sols nosaltres. Comprova-ho: funciona igual sense internet.',
        'No account, no cloud and no telemetry. Nobody knows how much you earn or what you spend it on, not even us. Check it yourself: it works the same without internet.'),
    'Seguridad sin atajos': (
        'Seguretat sense dreceres',
        'Security with no shortcuts'),
    'Todo lo que guarda va cifrado con tu contraseña maestra. Se descifra solo en memoria, se bloquea solo cuando no lo usas y, sin tu contraseña, no hay forma de abrirlo.': (
        "Tot el que guarda va xifrat amb la teva contrasenya mestra. Es desxifra només a la memòria, es bloqueja sol quan no l'uses i, sense la teva contrasenya, no hi ha manera d'obrir-lo.",
        'Everything it stores is encrypted with your master password. It is decrypted only in memory, locks itself when you are not using it and, without your password, there is no way to open it.'),
    'Tu dinero, a la vista': (
        'Els teus diners, a la vista',
        'Your money, in plain sight'),
    'Patrimonio, ahorro del mes, previsión a fin de mes, presupuestos, pagos recurrentes e inversiones. Inicio lo resume todo en una sola pantalla.': (
        'Patrimoni, estalvi del mes, previsió a final de mes, pressupostos, pagaments recurrents i inversions. Inici ho resumeix tot en una sola pantalla.',
        'Net worth, savings this month, end-of-month forecast, budgets, recurring payments and investments. Home sums it all up on a single screen.'),
    'Fácil desde el primer minuto': (
        'Fàcil des del primer minut',
        'Easy from the first minute'),
    'Sueltas el extracto de tu banco y ya está. Sin enlazar cuentas ni configurar nada. Si tu banco no está en la lista, Kreix te pregunta una vez qué columna es cada cosa y lo recuerda.': (
        "Deixes anar l'extracte del teu banc i ja està. Sense enllaçar comptes ni configurar res. Si el teu banc no és a la llista, Kreix et pregunta una vegada quina columna és cada cosa i ho recorda.",
        'You drop your bank statement in and that is it. No linking accounts, nothing to set up. If your bank is not on the list, Kreix asks you once which column is which and remembers it.'),
    'Por qué Kreix': (
        'Per què Kreix',
        'Why Kreix'),
    'Cuatro decisiones de diseño, y ninguna es negociable.': (
        'Quatre decisions de disseny, i cap no és negociable.',
        'Four design decisions, and none of them is negotiable.'),
}
