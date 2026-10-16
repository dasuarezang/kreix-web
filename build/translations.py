"""Textos de la web en catalán e inglés. La clave es el texto TAL CUAL está en index.html (castellano, que es la fuente);
el valor es (catalán, inglés). `build.py` sustituye cada clave en una sola pasada y avisa si alguna no aparece.

Criterio: cada idioma escribe los nombres de los idiomas y las pestañas del programa como los escribe el propio programa
(Inici / Comptes / Inversions / Importar / Configuració; Home / Accounts / Investments / Import / Settings)."""

T = {
    # --- cabecera del documento
    "<title>Kreix, guía de usuario</title>": ("<title>Kreix, guia d'usuari</title>", "<title>Kreix, user guide</title>"),
    "Kreix es una aplicación de finanzas personales que no te pide las claves de tu banco, funciona sin conexión y guarda todo cifrado en tu ordenador. Esta es su guía.": (
        "Kreix és una aplicació de finances personals que no et demana les claus del teu banc, funciona sense connexió i ho guarda tot xifrat al teu ordinador. Aquesta és la seva guia.",
        "Kreix is a personal finance app that never asks for your bank login details, works offline and keeps everything encrypted on your computer. This is its guide."),
    "Kreix nunca te pide las claves de tu banco": ("Kreix mai no et demana les claus del teu banc", "Kreix never asks for your bank login details"),
    "Finanzas personales para Windows: sin conexión y con tus datos guardados cifrados en tu ordenador.": (
        "Finances personals per a Windows: sense connexió i amb les teves dades guardades xifrades al teu ordinador.",
        "Personal finance for Windows: offline, with your data stored encrypted on your computer."),
    # --- cabecera de la página
    "Saltar al contenido": ("Salta al contingut", "Skip to content"),
    'aria-label="Kreix, inicio"': ('aria-label="Kreix, inici"', 'aria-label="Kreix, home"'),
    'aria-label="Principal"': ('aria-label="Principal"', 'aria-label="Main"'),
    'aria-label="Secciones"': ('aria-label="Seccions"', 'aria-label="Sections"'),
    'aria-label="Idioma"': ('aria-label="Idioma"', 'aria-label="Language"'),
    ">Primeros pasos</a>": (">Primers passos</a>", ">Getting started</a>"),
    ">La guía</a>": (">La guia</a>", ">The guide</a>"),
    ">Seguridad</a>": (">Seguretat</a>", ">Security</a>"),
    ">Preguntas</a>": (">Preguntes</a>", ">Questions</a>"),
    "Descarga: próximamente": ("Descàrrega: aviat", "Download: coming soon"),
    'aria-label="Cambiar entre tema claro y oscuro" title="Cambiar tema"': (
        'aria-label="Canviar entre tema clar i fosc" title="Canviar tema"', 'aria-label="Switch between light and dark theme" title="Change theme"'),
    # --- portada
    "Kreix nunca te&nbsp;pide las claves de&nbsp;tu&nbsp;banco.": (
        "Kreix mai no et&nbsp;demana les claus del&nbsp;teu&nbsp;banc.", "Kreix never asks for your&nbsp;bank login&nbsp;details."),
    "Una aplicación de finanzas personales para Windows. <strong>Funciona sin conexión</strong> y guarda todo <strong>cifrado en tu ordenador</strong>.": (
        "Una aplicació de finances personals per a Windows. <strong>Funciona sense connexió</strong> i ho guarda tot <strong>xifrat al teu ordinador</strong>.",
        "A personal finance app for Windows. <strong>It works offline</strong> and keeps everything <strong>encrypted on your computer</strong>."),
    "Empezar la guía": ("Comença la guia", "Start the guide"),
    "Cómo se protegen tus datos": ("Com es protegeixen les teves dades", "How your data is protected"),
    "La descarga llegará pronto a esta misma página.": ("La descàrrega arribarà aviat a aquesta mateixa pàgina.", "The download is coming soon to this same page."),
    "Sin tus claves del banco": ("Sense les claus del teu banc", "No bank login details"),
    "Tú descargas el extracto desde tu banco y lo sueltas en Kreix. Kreix no entra nunca en tu banca.": (
        "Tu descarregues l'extracte des del teu banc i el deixes anar a Kreix. Kreix no entra mai a la teva banca en línia.",
        "You download the statement from your bank and drop it into Kreix. Kreix never logs in to your bank."),
    "100&nbsp;% sin conexión": ("100&nbsp;% sense connexió", "100% offline"),
    "No se conecta a internet. Sin cuenta, sin nube y sin anuncios. Tus datos no viajan a ningún sitio.": (
        "No es connecta a internet. Sense compte, sense núvol i sense anuncis. Les teves dades no viatgen enlloc.",
        "It never connects to the internet, and there is no account, no cloud and no ads. Your data goes nowhere."),
    "Tus datos, cifrados": ("Les teves dades, xifrades", "Your data, encrypted"),
    "Lo que guarda Kreix va cifrado con tu contraseña maestra. Sin ella, nadie puede leerlo. Exportar también puede cifrarse.": (
        "Tot el que guarda Kreix va xifrat amb la teva contrasenya mestra. Sense ella, ningú ho pot llegir. L'exportació també es pot xifrar.",
        "Everything Kreix stores is encrypted with your master password. Without it, nobody can read it. Exports can be encrypted too."),
    "Pantalla de Inicio de Kreix: patrimonio neto, rendimiento, tasa de ahorro y previsión a fin de mes.": (
        "Pantalla d'Inici de Kreix: patrimoni net, rendiment, taxa d'estalvi i previsió a final de mes.",
        "Kreix Home screen: net worth, return, savings rate and end-of-month forecast."),
    "Pantalla de Inicio de Kreix en tema claro.": ("Pantalla d'Inici de Kreix en tema clar.", "Kreix Home screen in the light theme."),
    # --- primeros pasos
    "Empieza en tres pasos": ("Comença en tres passos", "Start in three steps"),
    "No hace falta conectar nada. Solo un archivo que ya puedes descargar de tu banco.": (
        "No cal connectar res. Només un arxiu que ja pots descarregar del teu banc.", "There is nothing to connect. Just a file you can already download from your bank."),
    "Descarga el extracto": ("Descarrega l'extracte", "Download the statement"),
    "Desde la web o la app de tu banco, en CSV o Excel. Es el mismo archivo que bajarías para guardarlo.": (
        "Des del web o l'app del teu banc, en CSV o Excel. És el mateix arxiu que baixaries per guardar-lo.",
        "From your bank's website or app, as CSV or Excel. It is the same file you would download to keep."),
    "Suéltalo en Kreix": ("Deixa'l anar a Kreix", "Drop it into Kreix"),
    "Arrástralo a Importar. Kreix te enseña lo que ha leído y no guarda nada hasta que pulses Importar. Si repites un extracto, no duplica movimientos.": (
        "Arrossega'l a Importar. Kreix et mostra el que ha llegit i no guarda res fins que premis Importar. Si repeteixes un extracte, no duplica moviments.",
        "Drag it onto Import. Kreix shows you what it read and saves nothing until you press Import. If you import the same statement again, Kreix does not duplicate transactions."),
    "Mira tu dinero": ("Mira els teus diners", "See your money"),
    "Inicio resume tu patrimonio, tu ahorro del mes y lo que está por venir. Cuentas e Inversiones lo detallan.": (
        "Inici resumeix el teu patrimoni, el teu estalvi del mes i el que ha de venir. Comptes i Inversions ho detallen.",
        "Home summarises your net worth, your savings this month and what is coming. Accounts and Investments give the detail."),
    # --- guia
    "La guía, pantalla a pantalla": ("La guia, pantalla a pantalla", "The guide, screen by screen"),
    "Cada pestaña de la barra lateral, en pocas palabras. Los datos de las capturas son inventados.": (
        "Cada pestanya de la barra lateral, en poques paraules. Les dades de les captures són inventades.",
        "Each tab in the sidebar, in a few words. The data in the screenshots is made up."),
    'aria-label="Pantallas de Kreix"': ('aria-label="Pantalles de Kreix"', 'aria-label="Kreix screens"'),
    ">Inicio</button>": (">Inici</button>", ">Home</button>"),
    ">Cuentas</button>": (">Comptes</button>", ">Accounts</button>"),
    ">Inversiones</button>": (">Inversions</button>", ">Investments</button>"),
    ">Importar</button>": (">Importar</button>", ">Import</button>"),
    ">Ajustes</button>": (">Configuració</button>", ">Settings</button>"),
    "Todo lo importante de un vistazo": ("Tot l'important d'un cop d'ull", "Everything important at a glance"),
    "Tu patrimonio neto, la rentabilidad y la tasa de ahorro del mes.": (
        "El teu patrimoni net, la rendibilitat i la taxa d'estalvi del mes.", "Your net worth, your return and this month's savings rate."),
    "Una previsión de cuánto dinero tendrás a fin de mes, con tus pagos fijos.": (
        "Una previsió de quants diners tindràs a final de mes, amb els teus pagaments fixos.",
        "A forecast of how much money you will have at the end of the month, counting your fixed payments."),
    "Próximos pagos, presupuestos y los movimientos que aún no tienen categoría.": (
        "Pròxims pagaments, pressupostos i els moviments que encara no tenen categoria.",
        "Upcoming payments, budgets and the transactions that have no category yet."),
    "Inicio de Kreix en tema oscuro.": ("Inici de Kreix en tema fosc.", "Kreix Home in the dark theme."),
    "Inicio de Kreix en tema claro.": ("Inici de Kreix en tema clar.", "Kreix Home in the light theme."),
    "Tus gastos, claros": ("Les teves despeses, clares", "Your spending, made clear"),
    "Gastos por categoría y evolución del saldo, de un mes o de todo el historial.": (
        "Despeses per categoria i evolució del saldo, d'un mes o de tot l'historial.", "Spending by category and balance over time, for one month or the whole history."),
    "Cambia la categoría de un movimiento con clic derecho, o crea tus propias reglas.": (
        "Canvia la categoria d'un moviment amb clic dret, o crea les teves pròpies regles.",
        "Change a transaction's category with a right click, or create your own rules."),
    "Presupuestos por categoría y pagos recurrentes detectados.": (
        "Pressupostos per categoria i pagaments recurrents detectats.", "Budgets by category and detected recurring payments."),
    "Cuentas en tema oscuro: saldo, ingresos, gastos y gráficos.": (
        "Comptes en tema fosc: saldo, ingressos, despeses i gràfics.", "Accounts in the dark theme: balance, income, expenses and charts."),
    "Cuentas en tema claro.": ("Comptes en tema clar.", "Accounts in the light theme."),
    "Tu cartera de fondos": ("La teva cartera de fons", "Your fund portfolio"),
    "Valor de la cartera, lo aportado, la plusvalía y la rentabilidad.": (
        "Valor de la cartera, l'aportat, la plusvàlua i la rendibilitat.", "Portfolio value, amount contributed, gain and return."),
    "Distribución por fondo y evolución frente a lo que has aportado.": (
        "Distribució per fons i evolució respecte al que has aportat.", "Breakdown by fund and growth compared with what you have contributed."),
    "Se alimenta de las operaciones y la cartera que exportas de MyInvestor.": (
        "S'alimenta de les operacions i la cartera que exportes de MyInvestor.", "It is built from the orders and the portfolio you export from MyInvestor."),
    "Inversiones en tema oscuro: valor de la cartera y distribución por fondo.": (
        "Inversions en tema fosc: valor de la cartera i distribució per fons.", "Investments in the dark theme: portfolio value and breakdown by fund."),
    "Inversiones en tema claro.": ("Inversions en tema clar.", "Investments in the light theme."),
    "Soltar y revisar": ("Deixar anar i revisar", "Drop and review"),
    "Arrastra los CSV o Excel de tu banco a la zona de importación.": (
        "Arrossega els CSV o Excel del teu banc a la zona d'importació.", "Drag your bank's CSV or Excel files onto the import area."),
    "Ves qué se ha leído antes de guardar, y casi todo se puede deshacer.": (
        "Veus què s'ha llegit abans de guardar, i gairebé tot es pot desfer.", "You see what was read before saving, and almost everything can be undone."),
    "Si Kreix no reconoce el archivo, te pregunta qué columna es cada cosa y lo recuerda.": (
        "Si Kreix no reconeix l'arxiu, et pregunta quina columna és cada cosa i ho recorda.",
        "If Kreix does not recognise the file, it asks you which column is which and remembers it."),
    "Importar en tema oscuro: zona para soltar extractos y resultado de la importación.": (
        "Importar en tema fosc: zona per deixar anar extractes i resultat de la importació.", "Import in the dark theme: area to drop statements and the import result."),
    "Importar en tema claro.": ("Importar en tema clar.", "Import in the light theme."),
    "A tu manera": ("A la teva manera", "Your way"),
    "Castellano, catalán o inglés, con cambio al instante.": ("Castellà, català o anglès, amb canvi a l'instant.", "Spanish, Catalan or English, switching instantly."),
    "Tema claro u oscuro, tamaño del texto y cielo animado en Inicio.": (
        "Tema clar o fosc, mida del text i cel animat a Inici.", "Light or dark theme, text size and an animated sky on Home."),
    "Contraseña, bloqueo automático y copias de seguridad cifradas.": (
        "Contrasenya, bloqueig automàtic i còpies de seguretat xifrades.", "Password, automatic lock and encrypted backups."),
    "Ajustes en tema oscuro: nombre, idioma y lo que te interesa.": (
        "Configuració en tema fosc: nom, idioma i el que t'interessa.", "Settings in the dark theme: name, language and what you are interested in."),
    "Ajustes en tema claro.": ("Configuració en tema clar.", "Settings in the light theme."),
    # --- demo del ojo y extras
    "Un ojo para cuando miran por encima del hombro": ("Un ull per a quan et miren per sobre l'espatlla", "An eye for when someone looks over your shoulder"),
    "Con un clic, o con Ctrl+H, Kreix difumina todas las cantidades: en cifras, tablas y gráficos. Se nota que hay un número, pero no cuál. Pruébalo.": (
        "Amb un clic, o amb Ctrl+H, Kreix difumina totes les quantitats: en xifres, taules i gràfics. Es nota que hi ha un número, però no quin. Prova-ho.",
        "With one click, or Ctrl+H, Kreix blurs every amount, in figures, tables and charts. You can tell there is a number, but not which one. Try it."),
    "Patrimonio neto (datos de ejemplo)": ("Patrimoni net (dades d'exemple)", "Net worth (sample data)"),
    "8.586,64&nbsp;€": ("8.586,64&nbsp;€", "€8,586.64"),
    "Cantidad oculta": ("Quantitat oculta", "Amount hidden"),
    "+66,64&nbsp;€ frente al mes pasado": ("+66,64&nbsp;€ respecte al mes passat", "+€66.64 vs last month"),
    'data-hide="Ocultar cantidades" data-show="Mostrar cantidades"': ('data-hide="Amagar les quantitats" data-show="Mostrar les quantitats"', 'data-hide="Hide amounts" data-show="Show amounts"'),
    ">Ocultar cantidades<": (">Amagar les quantitats<", ">Hide amounts<"),
    "Categorías automáticas": ("Categories automàtiques", "Automatic categories"),
    "Kreix clasifica tus gastos por sí mismo, y tus reglas mandan sobre las suyas.": (
        "Kreix classifica les teves despeses tot sol, i les teves regles manen sobre les seves.", "Kreix sorts your spending by itself, and your rules take priority over its own."),
    "<h3>Pagos recurrentes</h3>": ("<h3>Pagaments recurrents</h3>", "<h3>Recurring payments</h3>"),
    "Detecta suscripciones y recibos, y te dice cuándo toca el siguiente. Quitas los que ya no pagas.": (
        "Detecta subscripcions i rebuts, i et diu quan toca el següent. Treus els que ja no pagues.",
        "It detects subscriptions and bills, and tells you when the next one is due. You remove the ones you no longer pay."),
    "Casi todo se puede deshacer": ("Gairebé tot es pot desfer", "Almost everything can be undone"),
    "Cada cambio importante muestra un aviso con el botón Deshacer.": (
        "Cada canvi important mostra un avís amb el botó Desfer.", "Every important change shows a notice with an Undo button."),
    # --- seguridad
    "Tus datos no salen de tu ordenador": ("Les teves dades no surten del teu ordinador", "Your data never leaves your computer"),
    "No hay que fiarse de una promesa: Kreix está hecho para que no tenga nada que enviar ni a dónde enviarlo.": (
        "No cal refiar-se d'una promesa: Kreix està fet perquè no tingui res a enviar ni on enviar-ho.",
        "You do not have to trust a promise: Kreix is built so that it has nothing to send and nowhere to send it."),
    "Cómo viajan tus datos": ("Com viatgen les teves dades", "How your data travels"),
    "Tú descargas el extracto de tu banco y lo llevas a Kreix, en tu ordenador, donde se guarda cifrado. No hay ninguna conexión entre Kreix e internet.": (
        "Tu descarregues l'extracte del teu banc i el portes a Kreix, al teu ordinador, on es guarda xifrat. No hi ha cap connexió entre Kreix i internet.",
        "You download the statement from your bank and bring it to Kreix, on your computer, where it is stored encrypted. There is no connection between Kreix and the internet."),
    'font-size="24" font-weight="700">Tu banco</text>': ('font-size="21" font-weight="700">El teu banc</text>', 'font-size="24" font-weight="700">Your bank</text>'),
    'font-size="23" font-weight="700">Tu banco</text>': ('font-size="23" font-weight="700">El teu banc</text>', 'font-size="23" font-weight="700">Your bank</text>'),
    ">extracto</text>": (">extracte</text>", ">statement</text>"),
    'font-size="16" class="soft">que bajas tú</text>': ('font-size="15" class="soft">que baixes tu</text>', 'font-size="15" class="soft">you download</text>'),
    ">extracto que</text>": (">extracte que</text>", ">statement</text>"),
    ">bajas tú</text>": (">baixes tu</text>", ">you download</text>"),
    ">Tu ordenador</text>": (">El teu ordinador</text>", ">Your computer</text>"),
    'font-size="18" class="soft">calcula y te lo enseña</text>': ('font-size="17" class="soft">calcula i t' + chr(39) + 'ho ensenya</text>', 'font-size="16" class="soft">calculates and shows it</text>'),
    'font-size="17" class="soft">calcula y te lo enseña</text>': ('font-size="17" class="soft">calcula i t' + chr(39) + 'ho ensenya</text>', 'font-size="15" class="soft">calculates and shows it</text>'),
    ">Archivo cifrado</text>": (">Arxiu xifrat</text>", ">Encrypted file</text>"),
    'font-size="16" class="soft">solo se abre con tu contraseña</text>': (
        'font-size="15" class="soft">només s\'obre amb la contrasenya</text>', 'font-size="15" class="soft">only opens with your password</text>'),
    ">solo se abre con</text>": (">només s'obre amb</text>", ">only opens with</text>"),
    ">tu contraseña</text>": (">la teva contrasenya</text>", ">your password</text>"),
    ">Sin conexión</text>": (">Sense xarxa</text>", ">Offline</text>"),
    "<h3>Sin red</h3>": ("<h3>Sense xarxa</h3>", "<h3>No network</h3>"),
    "Kreix no incluye funciones de conexión a internet: ni para actualizarse, ni para enviar datos, ni para medir cómo lo usas.": (
        "Kreix no inclou funcions de connexió a internet: ni per actualitzar-se, ni per enviar dades, ni per mesurar com l'uses.",
        "Kreix has no features that use the internet: it does not update itself, send data or track how you use it."),
    "Cifrado de verdad": ("Xifratge de debò", "Real encryption"),
    "Los datos se cifran con AES y una clave que sale de tu contraseña (PBKDF2-SHA256 con 600.000 iteraciones). Si alguien lo manipula, deja de abrirse.": (
        "Les dades es xifren amb AES i una clau que surt de la teva contrasenya (PBKDF2-SHA256 amb 600.000 iteracions). Si algú manipula l'arxiu, deixa d'obrir-se.",
        "Your data is encrypted with AES and a key derived from your password (PBKDF2-SHA256 with 600,000 iterations). If anyone tampers with the file, it will no longer open."),
    "Nada en claro en el disco": ("Res en clar al disc", "Nothing unencrypted on disk"),
    "Al abrir Kreix, tus datos se descifran solo en memoria. No se escriben archivos temporales sin cifrar.": (
        "En obrir Kreix, les teves dades es desxifren només a la memòria. No s'escriuen arxius temporals sense xifrar.",
        "When you open Kreix, your data is decrypted only in memory. No unencrypted temporary files are written."),
    "La contraseña es solo tuya": ("La contrasenya és només teva", "Only you hold the password"),
    "Nadie más la tiene. Por eso, si la olvidas, tampoco se puede recuperar nada: tendrías que empezar de cero.": (
        "Ningú més la té. Per això, si l'oblides, tampoc es pot recuperar res: hauries de començar de zero.",
        "Nobody else has it. That is why, if you forget it, nothing can be recovered: you would have to start from scratch."),
    "Compruébalo tú": ("Comprova-ho tu", "Check it yourself"),
    "Desconecta el wifi o el cable de red.": ("Desconnecta el wifi o el cable de xarxa.", "Disconnect Wi-Fi or the network cable."),
    "Abre Kreix y úsalo con normalidad: importa, mira tus gráficos, cambia categorías. Todo funciona igual, porque nunca ha necesitado conexión.": (
        "Obre Kreix i fes-lo servir amb normalitat: importa, mira els teus gràfics, canvia categories. Tot funciona igual, perquè mai no ha necessitat connexió.",
        "Open Kreix and use it as usual: import, look at your charts, change categories. Everything works the same, because it never needed a connection."),
    "Para más garantías, crea en el Firewall de Windows una regla de salida que bloquee Kreix y comprueba que sigue funcionando.": (
        "Per a més garanties, crea al Tallafoc de Windows una regla de sortida que bloquegi Kreix i comprova que continua funcionant.",
        "For extra assurance, create an outbound rule in Windows Firewall that blocks Kreix and check that it keeps working."),
    "Lo que conviene saber": ("Què convé saber", "Good to know"),
    "El archivo que crea Exportar (.kreix) puede cifrarse con tu contraseña, pero no es obligatorio. Si no lo cifras, guárdalo en un sitio seguro. Y apunta tu contraseña maestra en un lugar seguro: si la pierdes, no hay forma de recuperar tus datos.": (
        "L'arxiu que crea Exportar (.kreix) es pot xifrar amb la teva contrasenya, però no és obligatori. Si no el xifres, guarda'l en un lloc segur. I apunta la teva contrasenya mestra en un lloc segur: si la perds, no hi ha manera de recuperar les teves dades.",
        "The file that Export creates (.kreix) can be encrypted with your password, but that is optional. If you do not encrypt it, keep it somewhere safe. And write down your master password somewhere safe: if you lose it, there is no way to recover your data."),
    # --- bancos
    "Funciona con tu banco": ("Funciona amb el teu banc", "Works with your bank"),
    "Kreix lee CSV y Excel (.xlsx y el antiguo .xls). Reconoce estos formatos por sus columnas habituales.": (
        "Kreix llegeix CSV i Excel (.xlsx i l'antic .xls). Reconeix aquests formats per les seves columnes habituals.",
        "Kreix reads CSV and Excel (.xlsx and the older .xls). It recognises these formats by their usual columns."),
    ">Cualquier otro<": (">Qualsevol altre<", ">Any other bank<"),
    "Si Kreix no reconoce un archivo, te enseña sus primeras filas y te pregunta qué columna es la fecha, el concepto y el importe. Lo recuerda para la próxima vez. Los formatos de CaixaBank, Santander, Revolut y Trade Republic están incluidos, pero todavía en pruebas.": (
        "Si Kreix no reconeix un arxiu, et mostra les primeres files i et pregunta quina columna és la data, el concepte i l'import. Ho recorda per a la propera vegada. Els formats de CaixaBank, Santander, Revolut i Trade Republic estan inclosos, però encara en proves.",
        "If Kreix does not recognise a file, it shows you the first rows and asks which column is the date, the description and the amount. It remembers for next time. The CaixaBank, Santander, Revolut and Trade Republic formats are included but still being tested."),
    # --- preguntas
    "Preguntas frecuentes": ("Preguntes freqüents", "Frequently asked questions"),
    "¿Kreix necesita mis claves o acceso a mi banco?": ("Necessita Kreix les meves claus o accés al meu banc?", "Does Kreix need my login details or access to my bank?"),
    "No, nunca. Kreix no se conecta a tu banco. Trabaja con los extractos que descargas tú.": (
        "No, mai. Kreix no es connecta al teu banc. Treballa amb els extractes que descarregues tu.",
        "No, never. Kreix does not connect to your bank. It works with the statements you download yourself."),
    "¿Se conecta a internet?": ("Es connecta a internet?", "Does it connect to the internet?"),
    "No. Funciona exactamente igual sin conexión, y no incluye nada para enviar información fuera de tu ordenador.": (
        "No. Funciona exactament igual sense connexió, i no inclou res per enviar informació fora del teu ordinador.",
        "No. It works exactly the same offline, and it has nothing to send information outside your computer."),
    "¿Dónde se guardan mis datos?": ("On es guarden les meves dades?", "Where is my data stored?"),
    "En un archivo cifrado dentro de tu carpeta de datos de aplicación (en Windows, %APPDATA%\\Kreix). Solo se descifran en memoria mientras Kreix está abierto.": (
        "En un arxiu xifrat dins de la teva carpeta de dades d'aplicació (a Windows, %APPDATA%\\Kreix). Només es desxifren a la memòria mentre Kreix està obert.",
        "In an encrypted file inside your application data folder (on Windows, %APPDATA%\\Kreix). It is only decrypted in memory while Kreix is open."),
    "¿Qué pasa si olvido la contraseña?": ("Què passa si oblido la contrasenya?", "What happens if I forget the password?"),
    "No se puede recuperar: no existe ninguna llave de repuesto, y por eso nadie más puede leer tus datos. Podrás empezar de cero con una contraseña nueva. Guarda copias de seguridad y apunta la contraseña en un sitio seguro.": (
        "No es pot recuperar: no hi ha cap clau de recanvi, i per això ningú més pot llegir les teves dades. Podràs començar de zero amb una contrasenya nova. Guarda còpies de seguretat i apunta la contrasenya en un lloc segur.",
        "It cannot be recovered: there is no spare key, which is why nobody else can read your data. You can start from scratch with a new password. Keep backups and write the password down somewhere safe."),
    "¿Qué pasa si importo dos veces el mismo extracto?": ("Què passa si importo dues vegades el mateix extracte?", "What happens if I import the same statement twice?"),
    "Nada: Kreix reconoce los movimientos que ya tiene y no los duplica.": (
        "Res: Kreix reconeix els moviments que ja té i no els duplica.", "Nothing: Kreix recognises the transactions it already has and does not duplicate them."),
    "¿Puedo llevarme mis datos a otro ordenador?": ("Puc endur-me les meves dades a un altre ordinador?", "Can I take my data to another computer?"),
    "Sí. Exportar crea un archivo .kreix que sueltas en Importar en el otro equipo. Puedes cifrarlo con tu contraseña. Importarlo reemplaza los datos que hubiera allí.": (
        "Sí. Exportar crea un arxiu .kreix que deixes anar a Importar a l'altre equip. El pots xifrar amb la teva contrasenya. Importar-lo substitueix les dades que hi hagués.",
        "Yes. Export creates a .kreix file that you drop into Import on the other computer. You can encrypt it with your password. Importing it replaces any data that was there."),
    "¿Puedo deshacer un cambio?": ("Puc desfer un canvi?", "Can I undo a change?"),
    "Casi todos los cambios importantes muestran un aviso con el botón Deshacer: importar, cambiar categorías, crear reglas, presupuestos y borrados.": (
        "Gairebé tots els canvis importants mostren un avís amb el botó Desfer: importar, canviar categories, crear regles, pressupostos i esborrats.",
        "Almost every important change shows a notice with an Undo button: imports, category changes, new rules, budgets and deletions."),
    "¿En qué idiomas está?": ("En quins idiomes està?", "Which languages is it available in?"),
    "Castellano, catalán e inglés. Se elige la primera vez que lo abres y se cambia cuando quieras en Ajustes.": (
        "Castellà, català i anglès. S'escull la primera vegada que l'obres i es canvia quan vulguis a Configuració.",
        "Spanish, Catalan and English. You choose when you first open it and can change it at any time in Settings."),
    "¿Funciona en Mac o en el móvil?": ("Funciona en Mac o al mòbil?", "Does it work on Mac or on a phone?"),
    "Por ahora, solo en Windows. Una versión para el móvil está en estudio.": (
        "Per ara, només a Windows. Una versió per al mòbil està en estudi.", "For now, only on Windows. A phone version is being considered."),
    "¿Cuándo se podrá descargar?": ("Quan es podrà descarregar?", "When will it be available to download?"),
    "Pronto. Esta página será el sitio de descarga y seguirá siendo la guía.": (
        "Aviat. Aquesta pàgina serà el lloc de descàrrega i continuarà sent la guia.", "Soon. This page will be the download site and will stay the guide."),
    # --- cierre y pie
    "Kreix para Windows. Próximamente.": ("Kreix per a Windows. Aviat.", "Kreix for Windows. Coming soon."),
    "Esta página será el sitio de descarga y seguirá siendo la guía. Sin cuenta, sin registro y sin conexión.": (
        "Aquesta pàgina serà el lloc de descàrrega i continuarà sent la guia. Sense compte, sense registre i sense connexió.",
        "This page will be the download site and will stay the guide. No account, no sign-up and no connection."),
    "Descarga para Windows: próximamente": ("Descàrrega per a Windows: aviat", "Download for Windows: coming soon"),
    "Kreix 0.5.0, un proyecto personal. Los datos de las capturas son inventados.": (
        "Kreix 0.5.0, un projecte personal. Les dades de les captures són inventades.", "Kreix 0.5.0, a personal project. The data in the screenshots is made up."),
    "Volver arriba": ("Torna amunt", "Back to top"),
}
