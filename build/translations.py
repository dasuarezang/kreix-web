"""Textos de la web en catalán e inglés. La clave es el texto TAL CUAL está en index.html (castellano, que es la fuente);
el valor es (catalán, inglés). `build.py` sustituye cada clave en una sola pasada y avisa si alguna no aparece.

Criterio: cada idioma escribe los nombres de los idiomas y las pestañas del programa como los escribe el propio programa
(Inici / Comptes / Inversions / Importar / Configuració; Home / Accounts / Investments / Import / Settings)."""

T = {
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
    '>Descargar igualmente (38&nbsp;MB)</a>': (
        '>Descarrega-ho igualment (38&nbsp;MB)</a>',
        '>Download anyway (38&nbsp;MB)</a>'),
    '>Descargar para Windows</a>': (
        '>Descarrega per a Windows</a>',
        '>Download for Windows</a>'),
    'aria-label="Cambiar entre tema claro y oscuro" title="Cambiar tema"': (
        'aria-label="Canviar entre tema clar i fosc" title="Canviar tema"',
        'aria-label="Switch between light and dark theme" title="Change theme"'),
    'Kreix nunca te&nbsp;pide las claves de&nbsp;tu&nbsp;banco.': (
        'Kreix mai no et&nbsp;demana les claus del&nbsp;teu&nbsp;banc.',
        'Kreix never asks for your&nbsp;bank login&nbsp;details.'),
    'Versión 0.6.1 para Windows 10 y 11 (64 bits). Si Windows te avisa al abrirlo es porque el instalador aún no está firmado: pulsa «Más información» y luego «Ejecutar de todas formas».': (
        "Versió 0.6.1 per a Windows 10 i 11 (64 bits). Si Windows t'avisa en obrir-lo és perquè l'instal·lador encara no està signat: prem «Més informació» i després «Executa de totes maneres».",
        'Version 0.6.1 for Windows 10 and 11 (64-bit). If Windows warns you when you open it, that is because the installer is not signed yet: click “More info” and then “Run anyway”.'),
    'Sin tus claves del banco': (
        'Sense les claus del teu banc',
        'No bank login details'),
    'Tú descargas el extracto y lo sueltas en Kreix. Kreix nunca entra en tu banca ni guarda tus claves.': (
        "Tu descarregues l'extracte i el deixes anar a Kreix. Kreix mai no entra a la teva banca ni guarda les teves claus.",
        'You download the statement and drop it into Kreix. Kreix never logs in to your bank and never stores your login details.'),
    '100&nbsp;% sin conexión': (
        '100&nbsp;% sense connexió',
        '100% offline'),
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
    '¿Cómo lo instalo?': (
        "Com l'instal·lo?",
        'How do I install it?'),
    'Descarga el instalador y ábrelo. No pide permisos de administrador y crea un acceso directo en Inicio y en el escritorio. Como el instalador aún no está firmado, Windows puede avisarte la primera vez: pulsa «Más información» y «Ejecutar de todas formas».': (
        "Descarrega l'instal·lador i obre'l. No demana permisos d'administrador i crea una drecera a Inici i a l'escriptori. Com que l'instal·lador encara no està signat, Windows pot avisar-te la primera vegada: prem «Més informació» i «Executa de totes maneres».",
        'Download the installer and open it. It does not ask for administrator rights and it adds a shortcut to Start and to the desktop. Because the installer is not signed yet, Windows may warn you the first time: click “More info” and then “Run anyway”.'),
    'Descargas': (
        'Descàrregues',
        'Downloads'),
    'Guía de uso (PDF)': (
        "Guia d'ús (PDF)",
        'User guide (PDF)'),
    'Guía de uso en PDF': (
        "Guia d'ús en PDF",
        'User guide (PDF)'),
    'Todo Kreix explicado paso a paso, para leer con calma o imprimir.': (
        'Tot Kreix explicat pas a pas, per llegir amb calma o imprimir.',
        'All of Kreix explained step by step, to read at your own pace or print out.'),
    'Descargar la guía': (
        'Descarregar la guia',
        'Download the guide'),
    '100&nbsp;% Offline<br>100&nbsp;% Cifrado<br>100&nbsp;% Privado': (
        '100&nbsp;% Offline<br>100&nbsp;% Xifrat<br>100&nbsp;% Privat',
        '100% Offline<br>100% Encrypted<br>100% Private'),
    '</a>. Todos los derechos reservados.</span>': (
        '</a>. Tots els drets reservats.</span>',
        '</a>. All rights reserved.</span>'),
    'Kreix 0.6.1 es software propietario de <a href="https://github.com/dasuarezang/kreix">código disponible</a>': (
        'Kreix 0.6.1 és programari propietari de <a href="https://github.com/dasuarezang/kreix">codi disponible</a>',
        'Kreix 0.6.1 is proprietary, <a href="https://github.com/dasuarezang/kreix">source-available</a> software'),
    ': puedes usarlo, pero no copiarlo, redistribuirlo ni venderlo.</span>': (
        ': el pots fer servir, però no copiar-lo, redistribuir-lo ni vendre\'l.</span>',
        ': you may use it, but not copy, redistribute or sell it.</span>'),
    '<span>Los datos de las capturas son inventados.</span>': (
        '<span>Les dades de les captures són inventades.</span>',
        '<span>The data in the screenshots is made up.</span>'),
    '<p>Finanzas personales sin conexión, cifradas en tu equipo.</p>': (
        '<p>Finances personals sense connexió, xifrades al teu equip.</p>',
        '<p>Personal finance that works offline, encrypted on your computer.</p>'),
    'aria-label="Secciones"': (
        'aria-label="Seccions"',
        'aria-label="Sections"'),
    '<h2>Secciones</h2>': (
        '<h2>Seccions</h2>',
        '<h2>Sections</h2>'),
    '<h2>Descarga</h2>': (
        '<h2>Descàrrega</h2>',
        '<h2>Download</h2>'),
    '<h2>Idioma y tema</h2>': (
        '<h2>Idioma i tema</h2>',
        '<h2>Language and theme</h2>'),
    '>Código en GitHub</a>': (
        '>Codi a GitHub</a>',
        '>Code on GitHub</a>'),
    'aria-label="Tema"': (
        'aria-label="Tema"',
        'aria-label="Theme"'),
    '<span>Claro</span>': (
        '<span>Clar</span>',
        '<span>Light</span>'),
    '<span>Oscuro</span>': (
        '<span>Fosc</span>',
        '<span>Dark</span>'),
    'Y el código está a la vista: <a href="https://github.com/dasuarezang/kreix">léelo en GitHub</a>.': (
        'I el codi és a la vista: <a href="https://github.com/dasuarezang/kreix">llegeix-lo a GitHub</a>.',
        'And the code is in plain sight: <a href="https://github.com/dasuarezang/kreix">read it on GitHub</a>.'),
    'Volver arriba': (
        'Torna amunt',
        'Back to top'),
    '<span>Menú</span>': (
        '<span>Menú</span>',
        '<span>Menu</span>'),
    'Sin cuenta, sin nube y sin telemetría. Nadie sabe cuánto ganas ni en qué lo gastas, ni siquiera nosotros. Compruébalo: funciona igual sin internet.': (
        'Sense compte, sense núvol i sense telemetria. Ningú sap quant guanyes ni en què ho gastes, ni tan sols nosaltres. Comprova-ho: funciona igual sense internet.',
        'No account, no cloud and no telemetry. Nobody knows how much you earn or what you spend it on, not even us. Check it yourself: it works the same without internet.'),
    'Cuatro decisiones de diseño, y ninguna es negociable.': (
        'Quatre decisions de disseny, i cap no és negociable.',
        'Four design decisions, and none of them is negotiable.'),
    '>En el móvil</a>': (
        '>Al mòbil</a>',
        '>On your phone</a>'),
    'La app de finanzas personales para Windows y el móvil que no te vigila: <strong>funciona sin conexión</strong> y guarda todo <strong>cifrado en tu equipo</strong>.': (
        "L'app de finances personals per a Windows i el mòbil que no et vigila: <strong>funciona sense connexió</strong> i ho guarda tot <strong>xifrat al teu equip</strong>.",
        'The personal finance app for Windows and your phone that does not watch you: <strong>it works offline</strong> and keeps everything <strong>encrypted on your device</strong>.'),
    '>Kreix para el móvil</span>': (
        '>Kreix per al mòbil</span>',
        '>Kreix for your phone</span>'),
    '>Instalar la app</a>': (
        ">Instal·la l'app</a>",
        '>Install the app</a>'),
    'En el ordenador, Kreix es un programa para Windows: abre esta página en él para descargarlo.': (
        "A l'ordinador, Kreix és un programa per a Windows: obre-hi aquesta pàgina per descarregar-lo.",
        'On the computer, Kreix is a Windows program: open this page there to download it.'),
    'Nunca envía tus datos a ningún sitio. El programa de Windows no se conecta a internet ni para actualizarse; la app del móvil, solo para descargarse desde esta web.': (
        "Mai no envia les teves dades enlloc. El programa de Windows no es connecta a internet ni per actualitzar-se; l'app del mòbil, només per descarregar-se des d'aquest web.",
        'It never sends your data anywhere. The Windows program does not connect to the internet, not even to update itself; the phone app only does to download itself from this website.'),
    '>Kreix en el móvil</h2>': (
        '>Kreix al mòbil</h2>',
        '>Kreix on your phone</h2>'),
    'La misma app, adaptada al móvil: las mismas cifras, gráficos y explicaciones, con Blitzen y Black en Inicio. Se instala desde el navegador, sin tienda de apps, y guarda todo cifrado en el móvil.': (
        "La mateixa app, adaptada al mòbil: les mateixes xifres, gràfics i explicacions, amb Blitzen i Black a Inici. S'instal·la des del navegador, sense botiga d'apps, i ho guarda tot xifrat al mòbil.",
        'The same app, adapted to your phone: the same figures, charts and explanations, with Blitzen and Black on Home. It installs from the browser, with no app store, and keeps everything encrypted on the phone.'),
    '>Trae tus datos</h3>': (
        '>Porta les teves dades</h3>',
        '>Bring your data</h3>'),
    'Importa los extractos desde el móvil o pásale los del ordenador: en Kreix para Windows, Datos, Exportar y «Pasar al móvil», y escanea el código QR con la app. Sin cables ni conexión.': (
        "Importa els extractes des del mòbil o passa-li els de l'ordinador: a Kreix per a Windows, Dades, Exportar i «Passar al mòbil», i escaneja el codi QR amb l'app. Sense cables ni connexió.",
        'Import your statements from the phone or send it the ones on your computer: in Kreix for Windows, Data, Export and “Send to phone”, then scan the QR code with the app. No cables, no connection.'),
    '>Abrir Kreix en el móvil</a>': (
        '>Obre Kreix al mòbil</a>',
        '>Open Kreix on your phone</a>'),
    'Tus datos se quedan cifrados en el móvil con tu contraseña maestra. La app solo se conecta a esta web para descargarse y, cuando hay una versión nueva, para actualizarse. También funciona en el navegador de un Mac o de un ordenador con Linux.': (
        "Les teves dades es queden xifrades al mòbil amb la teva contrasenya mestra. L'app només es connecta a aquest web per descarregar-se i, quan hi ha una versió nova, per actualitzar-se. També funciona al navegador d'un Mac o d'un ordinador amb Linux.",
        'Your data stays encrypted on the phone with your master password. The app only connects to this website to download itself and, when there is a new version, to update. It also works in the browser on a Mac or a Linux computer.'),
    'En el móvil, sí: Android y iPhone tienen la app de Kreix, que se instala desde el navegador (mira «Kreix en el móvil»). En un Mac o en Linux puedes usar esa misma app desde el navegador. El programa con instalador es solo para Windows.': (
        "Al mòbil, sí: Android i iPhone tenen l'app de Kreix, que s'instal·la des del navegador (mira «Kreix al mòbil»). En un Mac o a Linux pots fer servir aquesta mateixa app des del navegador. El programa amb instal·lador és només per a Windows.",
        'On your phone, yes: Android and iPhone have the Kreix app, which installs from the browser (see “Kreix on your phone”). On a Mac or Linux you can use that same app in the browser. The program with an installer is Windows only.'),
    # ---- el tráiler de la portada (build/trailer.html) ----
    '<h2 class="sr-only">Tráiler: cómo funciona Kreix</h2>': (
        '<h2 class="sr-only">Tràiler: com funciona Kreix</h2>',
        '<h2 class="sr-only">Trailer: how Kreix works</h2>'),
    'data-play="Reproducir el tráiler" data-pause="Pausar el tráiler"': (
        'data-play="Reprodueix el tràiler" data-pause="Posa en pausa el tràiler"',
        'data-play="Play the trailer" data-pause="Pause the trailer"'),
    'data-again="Ver otra vez"': (
        'data-again="Torna-ho a veure"',
        'data-again="Watch again"'),
    '<span>Ver cómo funciona</span>': (
        '<span>Mira com funciona</span>',
        '<span>See how it works</span>'),
    '<li class="on">Así funciona Kreix, en un minuto.</li>': (
        "<li class=\"on\">Així funciona Kreix, en un minut.</li>",
        '<li class="on">How Kreix works, in one minute.</li>'),
    '<li>Descarga el extracto de tu banco, en CSV o Excel.</li>': (
        "<li>Descarrega l'extracte del teu banc, en CSV o Excel.</li>",
        '<li>Download your bank statement, as CSV or Excel.</li>'),
    '<li>Suéltalo en Kreix. Ves lo que ha leído antes de guardar nada.</li>': (
        "<li>Deixa'l anar a Kreix. Veus el que ha llegit abans de guardar res.</li>",
        '<li>Drop it into Kreix. You see what it read before anything is saved.</li>'),
    '<li>Inicio lo resume: patrimonio, ahorro del mes y previsión a fin de mes.</li>': (
        '<li>Inici ho resumeix: patrimoni, estalvi del mes i previsió a final de mes.</li>',
        '<li>Home sums it up: net worth, savings this month and end-of-month forecast.</li>'),
    '<li>Cuentas e Inversiones lo detallan: en qué gastas y cómo va tu cartera.</li>': (
        '<li>Comptes i Inversions ho detallen: en què gastes i com va la teva cartera.</li>',
        '<li>Accounts and Investments give the detail: what you spend on and how your portfolio is doing.</li>'),
    '<li>Si alguien mira por encima del hombro, un clic difumina las cantidades.</li>': (
        "<li>Si algú mira per sobre l'espatlla, un clic difumina les quantitats.</li>",
        '<li>If someone looks over your shoulder, one click blurs the amounts.</li>'),
    '<li>Y en el móvil, la misma app: pásale tus datos con un código QR, sin cables ni conexión.</li>': (
        '<li>I al mòbil, la mateixa app: passa-li les teves dades amb un codi QR, sense cables ni connexió.</li>',
        '<li>And on your phone, the same app: send it your data with a QR code, no cables and no connection.</li>'),
    '<li>Sin las claves de tu banco, sin conexión y con todo cifrado.</li>': (
        '<li>Sense les claus del teu banc, sense connexió i amb tot xifrat.</li>',
        '<li>No bank login details, no connection, everything encrypted.</li>'),
    '<li>Kreix, para Windows y para el móvil.</li>': (
        '<li>Kreix, per a Windows i per al mòbil.</li>',
        '<li>Kreix, for Windows and for your phone.</li>'),
    '<b>La app de finanzas que no te vigila</b>': (
        "<b>L'app de finances que no et vigila</b>",
        '<b>The finance app that does not watch you</b>'),
    '<b>Tu banco</b>': ('<b>El teu banc</b>', '<b>Your bank</b>'),
    '<b>Movimientos</b>': ('<b>Moviments</b>', '<b>Transactions</b>'),
    '<b>Descargar extracto</b>': ("<b>Descarregar l'extracte</b>", '<b>Download statement</b>'),
    '<b>extracto.csv</b>': ('<b>extracte.csv</b>', '<b>statement.csv</b>'),
    '<b>Tú lo descargas. Kreix nunca entra en tu banca.</b>': (
        '<b>Tu el descarregues. Kreix mai no entra a la teva banca.</b>',
        '<b>You download it. Kreix never logs in to your bank.</b>'),
    '<b>Inicio</b>': ('<b>Inici</b>', '<b>Home</b>'),
    '<b>Cuentas</b>': ('<b>Comptes</b>', '<b>Accounts</b>'),
    '<b>Inversiones</b>': ('<b>Inversions</b>', '<b>Investments</b>'),
    '<b>Datos</b>': ('<b>Dades</b>', '<b>Data</b>'),
    '<b>Ajustes</b>': ('<b>Configuració</b>', '<b>Settings</b>'),
    '<b>Importar extractos</b>': ('<b>Importar extractes</b>', '<b>Import statements</b>'),
    '<b>Arrastra aquí tus extractos</b>': ('<b>Arrossega aquí els teus extractes</b>', '<b>Drag your statements here</b>'),
    '<b>CSV o Excel de tu banco</b>': ('<b>CSV o Excel del teu banc</b>', '<b>CSV or Excel from your bank</b>'),
    '<b>Extracto de Imagin, 54 movimientos nuevos</b>': (
        "<b>Extracte d'Imagin, 54 moviments nous</b>",
        '<b>Imagin statement, 54 new transactions</b>'),
    '<b>Supermercado</b>': ('<b>Supermercat</b>', '<b>Groceries</b>'),
    '<b>Nómina</b>': ('<b>Nòmina</b>', '<b>Salary</b>'),
    '<b>Transporte</b>': ('<b>Transport</b>', '<b>Transport</b>'),
    '<b>Ocio</b>': ('<b>Oci</b>', '<b>Leisure</b>'),
    '<b>Restaurantes</b>': ('<b>Restaurants</b>', '<b>Restaurants</b>'),
    '<b>Suscripciones</b>': ('<b>Subscripcions</b>', '<b>Subscriptions</b>'),
    '<b>Importar</b>': ('<b>Importar</b>', '<b>Import</b>'),
    '<b>Importado</b>': ('<b>Importat</b>', '<b>Imported</b>'),
    '<b>54 movimientos importados</b>': ('<b>54 moviments importats</b>', '<b>54 transactions imported</b>'),
    '<b>Deshacer</b>': ('<b>Desfer</b>', '<b>Undo</b>'),
    '<b>Buenos días, Blitzen.</b>': ('<b>Bon dia, Blitzen.</b>', '<b>Good morning, Blitzen.</b>'),
    '<b>Buenas noches, Blitzen.</b>': ('<b>Bona nit, Blitzen.</b>', '<b>Good evening, Blitzen.</b>'),
    '<b>Patrimonio neto</b>': ('<b>Patrimoni net</b>', '<b>Net worth</b>'),
    '<b>frente al mes pasado</b>': ('<b>respecte al mes passat</b>', '<b>vs last month</b>'),
    '<b>rendimiento</b>': ('<b>rendiment</b>', '<b>return</b>'),
    '<b>Liquidez</b>': ('<b>Liquiditat</b>', '<b>Cash</b>'),
    '<b>Inversión</b>': ('<b>Inversió</b>', '<b>Investments</b>'),
    '<b>Rendimiento global</b>': ('<b>Rendiment global</b>', '<b>Overall return</b>'),
    '<b>Tasa de ahorro del mes</b>': ("<b>Taxa d'estalvi del mes</b>", '<b>Savings rate this month</b>'),
    '<b>Previsión a fin de mes</b>': ('<b>Previsió a final de mes</b>', '<b>End-of-month forecast</b>'),
    '<b>Gastos por categoría</b>': ('<b>Despeses per categoria</b>', '<b>Expenses by category</b>'),
    '<b>Valor de la cartera</b>': ('<b>Valor de la cartera</b>', '<b>Portfolio value</b>'),
    '<b>Cartera</b>': ('<b>Cartera</b>', '<b>Portfolio</b>'),
    '<b>Aportado</b>': ('<b>Aportat</b>', '<b>Contributed</b>'),
    '<b>Pasar al móvil</b>': ('<b>Passar al mòbil</b>', '<b>Send to phone</b>'),
    '<b>Escanea el código con la app de Kreix.</b>': ("<b>Escaneja el codi amb l'app de Kreix.</b>", '<b>Scan the code with the Kreix app.</b>'),
    '<b>Sin cables ni conexión</b>': ('<b>Sense cables ni connexió</b>', '<b>No cables, no connection</b>'),
    '<b>Recibiendo…</b>': ('<b>Rebent…</b>', '<b>Receiving…</b>'),
    '<b>Kreix nunca entra en tu banca.</b>': ('<b>Kreix mai no entra a la teva banca.</b>', '<b>Kreix never logs in to your bank.</b>'),
    '<b>Sin cuenta, sin nube y sin telemetría.</b>': ('<b>Sense compte, sense núvol i sense telemetria.</b>', '<b>No account, no cloud and no telemetry.</b>'),
    '<b>Solo se abre con tu contraseña maestra.</b>': ("<b>Només s'obre amb la teva contrasenya mestra.</b>", '<b>It only opens with your master password.</b>'),
    '<b>Para Windows y para el móvil</b>': ('<b>Per a Windows i per al mòbil</b>', '<b>For Windows and for your phone</b>'),
    'Lo que Kreix no tiene': (
        'El que Kreix no té',
        'What Kreix does not have'),
    '>Banco</th>': ('>Banc</th>', '>Bank</th>'),
    '>Estado</th>': ('>Estat</th>', '>Status</th>'),
    '>Listo</td>': ('>A punt</td>', '>Ready</td>'),
    '>En pruebas</td>': ('>En proves</td>', '>In testing</td>'),
    '>Te pregunta las columnas</td>': ('>Et pregunta les columnes</td>', '>Asks you for the columns</td>'),
    'aria-label="Código QR que abre la app de Kreix"': (
        'aria-label="Codi QR que obre l\'app de Kreix"',
        'aria-label="QR code that opens the Kreix app"'),
    '¿Estás en el ordenador? Apunta con la cámara del móvil y la app se abre allí.': (
        "Ets a l'ordinador? Apunta-hi amb la càmera del mòbil i l'app s'obre allà.",
        'On your computer? Point your phone camera at it and the app opens there.'),
    'También disponible para smartphones': (
        'També disponible per a smartphones',
        'Also available for smartphones'),
    '<s>Claves del banco</s>': (
        '<s>Claus del banc</s>',
        '<s>Bank login details</s>'),
    '<s>Envío de datos</s>': (
        '<s>Enviament de dades</s>',
        '<s>Sending your data</s>'),
    '<s>Cuenta, nube y telemetría</s>': (
        '<s>Compte, núvol i telemetria</s>',
        '<s>Account, cloud and telemetry</s>'),
    '<s>Datos sin cifrar</s>': (
        '<s>Dades sense xifrar</s>',
        '<s>Unencrypted data</s>'),
    'aria-label="Tipo de móvil"': (
        'aria-label="Tipus de mòbil"',
        'aria-label="Phone type"'),
    '>iPhone y iPad</button>': (
        '>iPhone i iPad</button>',
        '>iPhone and iPad</button>'),
    'Los pasos son los de Chrome. En Edge son casi iguales.': (
        'Els passos són els de Chrome. A Edge són gairebé iguals.',
        'These steps are for Chrome. In Edge they are almost the same.'),
    'aria-label="Navegador"': (
        'aria-label="Navegador"',
        'aria-label="Browser"'),
    'Los pasos son los de Samsung Internet, el navegador que traen los Samsung Galaxy.': (
        'Els passos són els de Samsung Internet, el navegador que porten els Samsung Galaxy.',
        'These steps are for Samsung Internet, the browser that comes on Samsung Galaxy phones.'),
    '<h3>Abre Kreix en Samsung Internet</h3>': (
        '<h3>Obre Kreix a Samsung Internet</h3>',
        '<h3>Open Kreix in Samsung Internet</h3>'),
    'Toca las tres rayas (≡), abajo a la derecha.': (
        'Toca les tres ratlles (≡), a baix a la dreta.',
        'Tap the three lines (≡) at the bottom right.'),
    '<h3>Toca «Añadir página a» y luego «Pantalla de inicio»</h3>': (
        "<h3>Toca «Afegeix la pàgina a» i després «Pantalla d'inici»</h3>",
        '<h3>Tap “Add page to” and then “Home screen”</h3>'),
    'Si tu versión muestra «Instalar», úsalo: hace lo mismo.': (
        "Si la teva versió mostra «Instal·la», fes-la servir: fa el mateix.",
        'If your version shows “Install”, use it: it does the same thing.'),
    'Toca «Añadir» en el cuadro que aparece. Tarda un segundo; sin tienda de apps y sin cuenta.': (
        "Toca «Afegeix» al quadre que apareix. Triga un segon; sense botiga d'apps i sense compte.",
        'Tap “Add” in the box that appears. It takes a second; no app store and no account.'),
    'Tiene que ser Safari: es donde «Añadir a pantalla de inicio» está siempre.': (
        "Ha de ser Safari: és on «Afegir a la pantalla d'inici» hi és sempre.",
        'It has to be Safari: that is where “Add to Home Screen” is always available.'),
    '<h3>Abre Kreix en Chrome</h3>': (
        '<h3>Obre Kreix a Chrome</h3>',
        '<h3>Open Kreix in Chrome</h3>'),
    'Pulsa «Abrir Kreix en el móvil», aquí abajo, desde el propio móvil. La primera vez descarga unos 20&nbsp;MB; después funciona sin conexión.': (
        'Prem «Obre Kreix al mòbil», aquí sota, des del mateix mòbil. La primera vegada descarrega uns 20&nbsp;MB; després funciona sense connexió.',
        'Tap “Open Kreix on your phone”, just below, from the phone itself. The first time it downloads about 20&nbsp;MB; after that it works offline.'),
    '<h3>Abre el menú</h3>': (
        '<h3>Obre el menú</h3>',
        '<h3>Open the menu</h3>'),
    'Toca los tres puntos (⋮), arriba a la derecha de Chrome.': (
        'Toca els tres punts (⋮), a dalt a la dreta de Chrome.',
        'Tap the three dots (⋮) at the top right of Chrome.'),
    '<h3>Toca «Instalar aplicación»</h3>': (
        "<h3>Toca «Instal·la l'aplicació»</h3>",
        '<h3>Tap “Install app”</h3>'),
    'Si no la ves, toca «Añadir a pantalla de inicio» y luego «Instalar». Hacen lo mismo.': (
        "Si no la veus, toca «Afegeix a la pantalla d'inici» i després «Instal·la». Fan el mateix.",
        'If you do not see it, tap “Add to Home screen” and then “Install”. Both do the same thing.'),
    '<h3>Confirma</h3>': (
        '<h3>Confirma</h3>',
        '<h3>Confirm</h3>'),
    'Toca «Instalar» en el cuadro que aparece. Tarda un segundo; sin tienda de apps y sin cuenta.': (
        "Toca «Instal·la» al quadre que apareix. Triga un segon; sense botiga d'apps i sense compte.",
        'Tap “Install” in the box that appears. It takes a second; no app store and no account.'),
    '<h3>Ábrela desde la pantalla de inicio</h3>': (
        "<h3>Obre-la des de la pantalla d'inici</h3>",
        '<h3>Open it from your home screen</h3>'),
    'Busca el icono de Kreix entre tus apps. Se abre a pantalla completa, como cualquier otra.': (
        "Busca la icona de Kreix entre les teves apps. S'obre a pantalla completa, com qualsevol altra.",
        'Look for the Kreix icon among your apps. It opens full screen, like any other app.'),
    '<h3>Abre Kreix en Safari</h3>': (
        '<h3>Obre Kreix a Safari</h3>',
        '<h3>Open Kreix in Safari</h3>'),
    'Pulsa «Abrir Kreix en el móvil», aquí abajo. Si el enlace se abre dentro de otra app (WhatsApp, Instagram…), cópialo y pégalo en Safari. La primera vez descarga unos 20&nbsp;MB.': (
        "Prem «Obre Kreix al mòbil», aquí sota. Si l'enllaç s'obre dins d'una altra app (WhatsApp, Instagram…), copia'l i enganxa'l a Safari. La primera vegada descarrega uns 20&nbsp;MB.",
        'Tap “Open Kreix on your phone”, just below. If the link opens inside another app (WhatsApp, Instagram…), copy it and paste it into Safari. The first time it downloads about 20&nbsp;MB.'),
    '<h3>Toca Compartir</h3>': (
        '<h3>Toca Compartir</h3>',
        '<h3>Tap Share</h3>'),
    'El cuadrado con una flecha hacia arriba: abajo en el iPhone, arriba a la derecha en el iPad.': (
        "El quadrat amb una fletxa cap amunt: a baix a l'iPhone, a dalt a la dreta a l'iPad.",
        'The square with an arrow pointing up: at the bottom on iPhone, at the top right on iPad.'),
    '<h3>Baja y toca «Añadir a pantalla de inicio»</h3>': (
        "<h3>Baixa i toca «Afegir a la pantalla d'inici»</h3>",
        '<h3>Scroll down and tap “Add to Home Screen”</h3>'),
    'La lista es larga: deslízala hacia arriba hasta ver la opción con un cuadrado y un «+».': (
        "La llista és llarga: fes-la lliscar cap amunt fins a veure l'opció amb un quadrat i un «+».",
        'The list is long: swipe it up until you see the option with a “+” square.'),
    '<h3>Ponle nombre y toca «Añadir»</h3>': (
        '<h3>Posa-li nom i toca «Afegeix»</h3>',
        '<h3>Name it and tap “Add”</h3>'),
    'Deja «Kreix» y toca «Añadir», arriba a la derecha.': (
        'Deixa «Kreix» i toca «Afegeix», a dalt a la dreta.',
        'Leave “Kreix” and tap “Add” at the top right.'),
    'Ábrela desde el icono, no desde Safari: así se ve a pantalla completa.': (
        'Obre-la des de la icona, no des de Safari: així es veu a pantalla completa.',
        'Open it from the icon, not from Safari: that way it runs full screen.'),
}
