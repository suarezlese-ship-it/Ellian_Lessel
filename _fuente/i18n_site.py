# -*- coding: utf-8 -*-
# Textos de la web en tres idiomas. Clave: {'es':..., 'en':..., 'pt':...}
# Español: norma rioplatense (voseo), RAE. Inglés: estadounidense, Chicago Manual of Style.
# Portugués: brasileño, Acordo Ortográfico de 1990 / ABL.

LANGS = ['es', 'en', 'pt']

S = {
# ---------- meta ----------
'html_lang': {'es':'es','en':'en','pt':'pt-BR'},
'og_locale': {'es':'es_UY','en':'en_US','pt':'pt_BR'},
'title': {
 'es':'Ellian Lessel — Ficción, estrategia y cosmos | Sitio oficial del autor',
 'en':'Ellian Lessel — Fiction, Strategy, and the Cosmos | Official Author Website',
 'pt':'Ellian Lessel — Ficção, estratégia e cosmos | Site oficial do autor'},
'description': {
 'es':'Sitio oficial de Ellian Lessel, autor de la saga de ciencia ficción Ad Primordia, El tablero de césped y La eficiencia espaciotemporal. Disponibles en Kindle.',
 'en':'Official website of Ellian Lessel, author of the science fiction saga Ad Primordia, El tablero de césped, and La eficiencia espaciotemporal. Available on Kindle, in Spanish.',
 'pt':'Site oficial de Ellian Lessel, autor da saga de ficção científica Ad Primordia, El tablero de césped e La eficiencia espaciotemporal. Disponíveis no Kindle, em espanhol.'},
'og_desc': {
 'es':'Mitos que guardan memoria, tableros que piensan en tiempo real y civilizaciones medidas por su eficiencia. Tres universos, un mismo rigor.',
 'en':'Myths that keep memory, boards that think in real time, and civilizations measured by their efficiency. Three universes, one standard of rigor.',
 'pt':'Mitos que guardam memória, tabuleiros que pensam em tempo real e civilizações medidas por sua eficiência. Três universos, um mesmo rigor.'},

# ---------- navegación ----------
'skip': {'es':'Saltar al contenido','en':'Skip to content','pt':'Pular para o conteúdo'},
'home_aria': {'es':'Ellian Lessel, ir al inicio','en':'Ellian Lessel, go to home','pt':'Ellian Lessel, ir para o início'},
'menu_open': {'es':'Abrir menú','en':'Open menu','pt':'Abrir menu'},
'menu_close': {'es':'Cerrar menú','en':'Close menu','pt':'Fechar menu'},
'nav_aria': {'es':'Principal','en':'Main','pt':'Principal'},
'nav_home': {'es':'Inicio','en':'Home','pt':'Início'},
'nav_catalog': {'es':'Catálogo','en':'Books','pt':'Catálogo'},
'nav_eq': {'es':'Ecuación Maestra','en':'Master Equation','pt':'Equação Mestra'},
'nav_reviews': {'es':'Reseñas','en':'Reviews','pt':'Resenhas'},
'nav_saga': {'es':'Saga Ad Primordia','en':'Ad Primordia Saga','pt':'Saga Ad Primordia'},
'nav_news': {'es':'Novedades','en':'News','pt':'Novidades'},
'nav_author': {'es':'Sobre el autor','en':'About the Author','pt':'Sobre o autor'},
'lang_label': {'es':'Idioma','en':'Language','pt':'Idioma'},
'ig_aria': {'es':'Instagram de Ellian Lessel','en':'Ellian Lessel on Instagram','pt':'Instagram de Ellian Lessel'},
'amz_author': {'es':'Página de autor en Amazon','en':'Amazon author page','pt':'Página de autor na Amazon'},
'amz_aria': {'es':'Ellian Lessel en Amazon (página de autor)','en':'Ellian Lessel on Amazon (author page)','pt':'Ellian Lessel na Amazon (página de autor)'},
'gr_aria': {'es':'Goodreads de Ellian Lessel','en':'Ellian Lessel on Goodreads','pt':'Goodreads de Ellian Lessel'},

# ---------- hero ----------
'hero_kicker': {'es':'Ficción · Estrategia · Ciencia','en':'Fiction · Strategy · Science','pt':'Ficção · Estratégia · Ciência'},
'firma_alt': {'es':'Ellian Lessel escrito en signos cuneiformes','en':'Ellian Lessel written in cuneiform signs','pt':'Ellian Lessel escrito em sinais cuneiformes'},
'hero_sub': {
 'es':'Mitos que guardan memoria. Tableros que piensan en tiempo real. Civilizaciones medidas por su eficiencia. <em>Tres universos, un mismo rigor.</em>',
 'en':'Myths that keep memory. Boards that think in real time. Civilizations measured by their efficiency. <em>Three universes, one standard of rigor.</em>',
 'pt':'Mitos que guardam memória. Tabuleiros que pensam em tempo real. Civilizações medidas por sua eficiência. <em>Três universos, um mesmo rigor.</em>'},
'hero_lead': {
 'es':'Ciencia ficción dura entrelazada con la mitología comparada, la estrategia del ajedrez aplicada al fútbol y una nueva forma de clasificar a las civilizaciones del cosmos. Los tres libros ya están disponibles en Kindle.',
 'en':'Hard science fiction woven with comparative mythology, chess strategy applied to soccer, and a new way to classify the civilizations of the cosmos. All three books are now available on Kindle.',
 'pt':'Ficção científica hard entrelaçada com a mitologia comparada, a estratégia do xadrez aplicada ao futebol e uma nova forma de classificar as civilizações do cosmos. Os três livros já estão disponíveis no Kindle.'},
'lang_note': {'es':'',
 'en':'All books are written and published in Spanish.',
 'pt':'Todos os livros foram escritos e publicados em espanhol.'},
'cta_explore': {'es':'Explorar obras','en':'Explore the books','pt':'Explorar as obras'},
'cta_follow_ig': {'es':'Seguir en Instagram','en':'Follow on Instagram','pt':'Seguir no Instagram'},
'trio_aria': {'es':'Los tres universos del autor','en':"The author's three universes",'pt':'Os três universos do autor'},
'tag_fic': {'es':'Ficción','en':'Fiction','pt':'Ficção'},
'tag_est': {'es':'Estrategia','en':'Strategy','pt':'Estratégia'},
'tag_ens': {'es':'Ensayo','en':'Essay','pt':'Ensaio'},
'uni_fic': {
 'es':'Una voz sepultada seis mil años bajo el polvo de Mesopotamia. Ciencia ficción dura y mitología comparada.',
 'en':'A voice buried for six thousand years beneath the dust of Mesopotamia. Hard science fiction and comparative mythology.',
 'pt':'Uma voz sepultada por seis mil anos sob a poeira da Mesopotâmia. Ficção científica hard e mitologia comparada.'},
'uni_est': {
 'es':'Un tablero de 64 casillas sobre el campo. El ajedrez convertido en sistema operativo del fútbol.',
 'en':'A 64-square board laid over the pitch. Chess turned into an operating system for soccer.',
 'pt':'Um tabuleiro de 64 casas sobre o campo. O xadrez transformado em sistema operacional do futebol.'},
'uni_ens': {
 'es':'Seis variables y una Ecuación Maestra para medir el avance de cualquier civilización.',
 'en':'Six variables and a Master Equation to measure the progress of any civilization.',
 'pt':'Seis variáveis e uma Equação Mestra para medir o avanço de qualquer civilização.'},

# ---------- catálogo ----------
'cat_kicker': {'es':'Catálogo oficial','en':'Official catalog','pt':'Catálogo oficial'},
'cat_h2': {'es':'Tres obras, tres mundos','en':'Three books, three worlds','pt':'Três obras, três mundos'},
'cat_lead': {
 'es':'Elegí tu puerta de entrada. Cada libro está disponible en formato Kindle; las ediciones impresas llegan en las próximas semanas.',
 'en':'Choose your way in. Each book is available on Kindle, in Spanish; print editions arrive in the coming weeks.',
 'pt':'Escolha sua porta de entrada. Cada livro está disponível no Kindle, em espanhol; as edições impressas chegam nas próximas semanas.'},
'filter_aria': {'es':'Filtrar catálogo por género','en':'Filter books by genre','pt':'Filtrar catálogo por gênero'},
'f_all': {'es':'Todos','en':'All','pt':'Todos'},
'f_fic': {'es':'Ficción: Ad Primordia','en':'Fiction: Ad Primordia','pt':'Ficção: Ad Primordia'},
'f_est': {'es':'Estrategia: El tablero de césped','en':'Strategy: El tablero de césped','pt':'Estratégia: El tablero de césped'},
'f_ens': {'es':'Ensayo: Eficiencia espaciotemporal','en':'Essay: Eficiencia espaciotemporal','pt':'Ensaio: Eficiencia espaciotemporal'},

# ---------- ecuación ----------
'eq_kicker': {'es':'Explorador interactivo · La eficiencia espaciotemporal','en':'Interactive explorer · La eficiencia espaciotemporal','pt':'Explorador interativo · La eficiencia espaciotemporal'},
'eq_h2': {'es':'La Ecuación Maestra','en':'The Master Equation','pt':'A Equação Mestra'},
'eq_lead': {
 'es':'Para Kardashev, una civilización avanza cuanta más energía consume. Este ensayo propone otra medida: con cuánta eficiencia la emplea. Tocá cada variable para descubrir qué mide y qué ley física le pone techo.',
 'en':'For Kardashev, a civilization advances the more energy it consumes. This essay proposes a different yardstick: how efficiently it uses that energy. Tap each variable to see what it measures and which physical law sets its ceiling.',
 'pt':'Para Kardashev, uma civilização avança quanto mais energia consome. Este ensaio propõe outra medida: com quanta eficiência ela a emprega. Toque em cada variável para descobrir o que ela mede e qual lei física lhe impõe um teto.'},
'eq_aria': {'es':'Ecuación Maestra del Índice de Eficiencia Espaciotemporal','en':'Master Equation of the Spacetime Efficiency Index','pt':'Equação Mestra do Índice de Eficiência Espaçotemporal'},
'eq_cap': {
 'es':'Índice de Eficiencia Espaciotemporal (Φ). La raíz equilibra energía, tecnología y cognición: si una cae a cero, el índice colapsa. La fracción premia la extensión que se mantiene cohesionada y la eficiencia entrópica.',
 'en':'Spacetime Efficiency Index (Φ). The square root balances energy, technology, and cognition: if any of them falls to zero, the index collapses. The fraction rewards reach that stays cohesive, together with entropic efficiency.',
 'pt':'Índice de Eficiência Espaçotemporal (Φ). A raiz equilibra energia, tecnologia e cognição: se uma delas cai a zero, o índice colapsa. A fração premia a extensão que se mantém coesa e a eficiência entrópica.'},
'eq_g1': {'es':'6 variables fundamentales · componen Φ','en':'6 core variables · they make up Φ','pt':'6 variáveis fundamentais · compõem Φ'},
'eq_g2': {'es':'4 variables complementarias · fuera de la ecuación','en':'4 complementary variables · outside the equation','pt':'4 variáveis complementares · fora da equação'},
'v_fund': {'es':'Variable fundamental','en':'Core variable','pt':'Variável fundamental'},
'v_comp': {'es':'Variable complementaria','en':'Complementary variable','pt':'Variável complementar'},
'v_law': {'es':'Ley o referente','en':'Law or reference','pt':'Lei ou referência'},
'v_hum': {'es':'Humanidad 2025','en':'Humanity, 2025','pt':'Humanidade, 2025'},
'gr_h3': {'es':'Los Grados de Eficiencia Espaciotemporal','en':'The Grades of Spacetime Efficiency','pt':'Os Graus de Eficiência Espaçotemporal'},
'gr_p': {
 'es':'Seis Grados, del 0 al 5, con criterios físicos aplicables a cualquier civilización del universo. Tocá un Grado.',
 'en':'Six Grades, from 0 to 5, defined by physical criteria that apply to any civilization in the universe. Tap a Grade.',
 'pt':'Seis Graus, do 0 ao 5, com critérios físicos aplicáveis a qualquer civilização do universo. Toque em um Grau.'},
'grades_aria': {'es':'Grados 0 a 5','en':'Grades 0 to 5','pt':'Graus 0 a 5'},
'gr_word': {'es':'Grado','en':'Grade','pt':'Grau'},
'gr_you': {
 'es':'La humanidad hoy: Φ ≈ 0,002 · Grado 0, fase 0-B, unas cuarenta veces por debajo del Grado 1.',
 'en':'Humanity today: Φ ≈ 0.002 · Grade 0, phase 0-B, roughly forty times below Grade 1.',
 'pt':'A humanidade hoje: Φ ≈ 0,002 · Grau 0, fase 0-B, cerca de quarenta vezes abaixo do Grau 1.'},
'eq_note': {
 'es':'La Teoría de la Eficiencia Espaciotemporal es una propuesta teórica abierta a la contrastación. El libro la formula con predicciones falsables y declara que todavía no fue sometida a revisión por pares.',
 'en':'The Theory of Spacetime Efficiency is a theoretical proposal open to testing. The book states it with falsifiable predictions and declares that it has not yet undergone peer review.',
 'pt':'A Teoria da Eficiência Espaçotemporal é uma proposta teórica aberta à verificação. O livro a formula com previsões falseáveis e declara que ela ainda não passou por revisão por pares.'},
'eq_cta': {
 'es':'El libro desarrolla cada variable, el Doble y el Triple Reloj, el Principio de Invisibilidad Elegante y seis predicciones falsables. ¿Qué variable le falta a la ecuación, o cuál le sobra?',
 'en':'The book develops each variable, the Double and Triple Clock, the Principle of Elegant Invisibility, and six falsifiable predictions. Which variable is the equation missing, and which one does it not need?',
 'pt':'O livro desenvolve cada variável, o Duplo e o Triplo Relógio, o Princípio da Invisibilidade Elegante e seis previsões falseáveis. Que variável falta à equação, ou qual delas sobra?'},

# ---------- botones comunes ----------
'buy': {'es':'Comprar en Amazon','en':'Buy on Amazon','pt':'Comprar na Amazon'},
'details': {'es':'Ficha y reseñas','en':'Details & reviews','pt':'Ficha e resenhas'},
'other_stores': {'es':'Otras tiendas','en':'Other stores','pt':'Outras lojas'},
'store_label': {'es':'Tienda','en':'Store','pt':'Loja'},
'available_es': {'es':'','en':'In Spanish','pt':'Em espanhol'},

# ---------- reseñas ----------
'rev_kicker': {'es':'Lectores','en':'Readers','pt':'Leitores'},
'rev_h2': {'es':'Reseñas','en':'Reviews','pt':'Resenhas'},
'rev_lead': {
 'es':'Solo publicamos opiniones reales de lectores, con su autorización y su fuente. Los libros acaban de salir: tu reseña puede ser de las primeras.',
 'en':'We only publish genuine reader opinions, with their permission and source. The books have just come out, so your review could be one of the first.',
 'pt':'Só publicamos opiniões reais de leitores, com autorização e fonte. Os livros acabaram de sair: sua resenha pode estar entre as primeiras.'},
'rev_aria': {'es':'Filtrar reseñas por libro','en':'Filter reviews by book','pt':'Filtrar resenhas por livro'},
'r_all': {'es':'Todas','en':'All','pt':'Todas'},
'empty_h4': {'es':'Sé la primera voz','en':'Be the first voice','pt':'Seja a primeira voz'},
'empty_p': {
 'es':'Este libro todavía no tiene reseñas publicadas aquí. Si ya lo leíste, dejá tu opinión en Amazon; con tu permiso, la sumamos a esta página.',
 'en':'This book has no reviews published here yet. If you have read it, leave your opinion on Amazon; with your permission, we will add it to this page.',
 'pt':'Este livro ainda não tem resenhas publicadas aqui. Se você já o leu, deixe sua opinião na Amazon; com sua permissão, nós a incluiremos nesta página.'},
'empty_btn': {'es':'Reseñar en Amazon','en':'Review on Amazon','pt':'Avaliar na Amazon'},
'no_reviews': {'es':'Sin reseñas todavía','en':'No reviews yet','pt':'Ainda sem resenhas'},
'first_review': {'es':'dejá la primera','en':'leave the first one','pt':'deixe a primeira'},
'reviews_word': {'es':'reseñas','en':'reviews','pt':'resenhas'},

# ---------- saga ----------
'saga_kicker': {'es':'Horizonte editorial','en':'Publishing horizon','pt':'Horizonte editorial'},
'saga_h2': {'es':'La pentalogía Ad Primordia','en':'The Ad Primordia Pentalogy','pt':'A pentalogia Ad Primordia'},
'saga_lead': {
 'es':'Cinco volúmenes para una sola historia: la de quienes cruzaron las estrellas antes de nuestro tiempo y la de quienes, seis mil años después, empiezan a escucharlos. Tocá cada volumen.',
 'en':'Five volumes, one story: that of those who crossed the stars before our time, and of those who, six thousand years later, begin to hear them. Tap each volume.',
 'pt':'Cinco volumes para uma só história: a dos que cruzaram as estrelas antes do nosso tempo e a dos que, seis mil anos depois, começam a escutá-los. Toque em cada volume.'},
'vol_word': {'es':'Volumen','en':'Volume','pt':'Volume'},
'cover_soon': {'es':'Portada en<br>preparación','en':'Cover in<br>preparation','pt':'Capa em<br>preparação'},
'cover_of': {'es':'Portada de','en':'Cover of','pt':'Capa de'},
'preview_word': {'es':'avance','en':'preview','pt':'prévia'},
'stages_aria': {'es':'Etapas de producción','en':'Production stages','pt':'Etapas de produção'},
'stage_now': {'es':'etapa actual','en':'current stage','pt':'etapa atual'},
'notify_link': {'es':'Avisame cuando salga →','en':'Let me know when it comes out →','pt':'Avise-me quando sair →'},
'sub_kicker': {'es':'Lista de lectores','en':'Reader list','pt':'Lista de leitores'},
'sub_h3': {'es':'Avisame cuando salga <em>Creación</em>','en':'Tell me when <em>Creación</em> comes out','pt':'Avise-me quando sair <em>Creación</em>'},
'sub_p': {
 'es':'Recibí un único correo cuando el Volumen II esté disponible, y las novedades de los próximos libros. Sin spam; te das de baja cuando quieras.',
 'en':'Get a single email when Volume II is available, plus news about upcoming books. No spam; unsubscribe whenever you like.',
 'pt':'Receba um único e-mail quando o Volume II estiver disponível, além das novidades dos próximos livros. Sem spam; cancele quando quiser.'},
'email_label': {'es':'Correo electrónico','en':'Email address','pt':'E-mail'},
'email_ph': {'es':'tu@correo.com','en':'you@email.com','pt':'voce@email.com'},
'subscribe_btn': {'es':'Suscribirme','en':'Subscribe','pt':'Inscrever-me'},
'consent_sub': {
 'es':'Acepto recibir correos de Ellian Lessel y la <button type="button" class="js-privacy">política de privacidad</button>.',
 'en':'I agree to receive emails from Ellian Lessel and accept the <button type="button" class="js-privacy">privacy policy</button>.',
 'pt':'Aceito receber e-mails de Ellian Lessel e a <button type="button" class="js-privacy">política de privacidade</button>.'},
'sub_formname': {'es':'Lista de lectores (aviso de Creación)','en':'Reader list (Creación alert) — EN','pt':'Lista de leitores (aviso de Creación) — PT'},
'sub_subject': {'es':'Nueva suscripción — web Ellian Lessel','en':'New subscription (EN) — Ellian Lessel website','pt':'Nova inscrição (PT) — site Ellian Lessel'},
'fut_tab_h4': {'es':'El tablero de césped · segundo volumen','en':'El tablero de césped · second volume','pt':'El tablero de césped · segundo volume'},
'fut_tab_p': {
 'es':'El epílogo ya lo anuncia: el fuera de juego como frontera móvil, la falta táctica como sacrificio consentido, la presión de las gradas, el clima y la capa de datos en tiempo real.',
 'en':'The epilogue already announces it: offside as a moving frontier, the tactical foul as a deliberate sacrifice, the pressure of the stands, the weather, and the real-time data layer.',
 'pt':'O epílogo já o anuncia: o impedimento como fronteira móvel, a falta tática como sacrifício consentido, a pressão das arquibancadas, o clima e a camada de dados em tempo real.'},
'fut_efi_h4': {'es':'La eficiencia espaciotemporal · actualizaciones','en':'La eficiencia espaciotemporal · updates','pt':'La eficiencia espaciotemporal · atualizações'},
'fut_efi_p': {
 'es':'Una teoría que se ofrece para ser desafiada: las próximas ediciones incorporarán nuevos datos, la revisión crítica de los lectores y la interacción entre civilizaciones de distinto Grado.',
 'en':'A theory offered up to be challenged: future editions will add new data, readers’ critical review, and the interaction between civilizations of different Grades.',
 'pt':'Uma teoria que se oferece para ser desafiada: as próximas edições incorporarão novos dados, a revisão crítica dos leitores e a interação entre civilizações de Graus diferentes.'},
'translations_line': {
 'es':'Traducciones al inglés y al portugués: en el horizonte del autor.',
 'en':'English and Portuguese translations: on the author’s horizon.',
 'pt':'Traduções para o inglês e o português: no horizonte do autor.'},

# ---------- novedades (portada) ----------
'news_kicker': {'es':'Novedades','en':'News','pt':'Novidades'},
'news_h2': {'es':'Lo último del autor','en':'Latest from the author','pt':'O mais recente do autor'},
'news_lead': {
 'es':'Mitologías antiguas, física, cosmos y estrategia: textos para seguir pensando más allá de las páginas.',
 'en':'Ancient mythologies, physics, the cosmos, and strategy: writing to keep you thinking beyond the page.',
 'pt':'Mitologias antigas, física, cosmos e estratégia: textos para continuar pensando além das páginas.'},
'news_all': {'es':'Ver todas las novedades','en':'See all news','pt':'Ver todas as novidades'},
'read_more': {'es':'Leer','en':'Read','pt':'Ler'},
'min_read': {'es':'min de lectura','en':'min read','pt':'min de leitura'},

# ---------- autor ----------
'author_kicker': {'es':'Sobre el autor','en':'About the author','pt':'Sobre o autor'},
'portrait_alt': {'es':'Retrato de Ellian Lessel','en':'Portrait of Ellian Lessel','pt':'Retrato de Ellian Lessel'},
'bio1': {
 'es':'Ellian Lessel es un autor radicado en Montevideo cuya obra recorre tres territorios que rara vez comparten estante: la ciencia ficción épica, el análisis estratégico del deporte y el ensayo científico sobre el futuro de las civilizaciones. Los une una misma pregunta: cómo piensan, deciden y perduran los sistemas complejos, sea un pueblo que abandona su mundo, un equipo sobre el césped o una especie que mira las estrellas.',
 'en':'Ellian Lessel is a Montevideo-based author whose work spans three territories that rarely share a shelf: epic science fiction, the strategic analysis of sport, and the scientific essay on the future of civilizations. A single question ties them together: how complex systems think, decide, and endure, whether a people abandoning its world, a team on the pitch, or a species looking up at the stars.',
 'pt':'Ellian Lessel é um autor radicado em Montevidéu cuja obra percorre três territórios que raramente dividem a mesma estante: a ficção científica épica, a análise estratégica do esporte e o ensaio científico sobre o futuro das civilizações. Une-os uma mesma pergunta: como pensam, decidem e perduram os sistemas complexos, seja um povo que abandona seu mundo, uma equipe em campo ou uma espécie que olha para as estrelas.'},
'bio2': {
 'es':'Su mirada se formó en el estudio de la estrategia. Es licenciado en Ciencias Militares y profesor de Historia de los Conflictos Armados. Tiene una Maestría en Dirección y Administración de Negocios (MBA) y es magíster en Estrategia Nacional, con posgrados de especialización en Inteligencia Estratégica y en Seguridad y Defensa.',
 'en':'His outlook was shaped by the study of strategy. He holds a bachelor’s degree in Military Sciences and is a professor of the History of Armed Conflicts. He holds an MBA and a master’s degree in National Strategy, along with postgraduate specializations in Strategic Intelligence and in Security and Defense.',
 'pt':'Seu olhar formou-se no estudo da estratégia. É bacharel em Ciências Militares e professor de História dos Conflitos Armados. Tem um MBA em Direção e Administração de Empresas e é mestre em Estratégia Nacional, com pós-graduações de especialização em Inteligência Estratégica e em Segurança e Defesa.'},
'bio3': {
 'es':'Es docente de la Maestría en Estrategia Nacional y de los posgrados de especialización del Centro de Altos Estudios Nacionales (CALEN) y del Instituto Militar de Estudios Superiores (IMES). Allí enseña a leer el conflicto, la decisión y el largo plazo, las mismas claves que sostienen su escritura.',
 'en':'He teaches in the Master’s in National Strategy and in the postgraduate specialization programs of Uruguay’s Center for Advanced National Studies (CALEN) and the Military Institute of Higher Studies (IMES). There he teaches how to read conflict, decision-making, and the long term, the same keys that sustain his writing.',
 'pt':'É docente do Mestrado em Estratégia Nacional e das pós-graduações de especialização do Centro de Altos Estudos Nacionais (CALEN) e do Instituto Militar de Estudos Superiores (IMES), no Uruguai. Ali ensina a ler o conflito, a decisão e o longo prazo, as mesmas chaves que sustentam sua escrita.'},
'bio4': {
 'es':'Esa formación atraviesa cada uno de sus libros. En la saga <em>Ad Primordia</em>, iniciada con <em>Despertar</em>, la mitología comparada de Sumeria, Babilonia, Asiria, Persia y la tradición judeocristiana se cruza con la ciencia ficción dura y el primer contacto. En <em>El tablero de césped</em> traduce el vocabulario del ajedrez (la clavada, la horquilla, el zugzwang) a un sistema operativo para analizar el fútbol en tiempo real. En <em>La eficiencia espaciotemporal</em> propone una Ecuación Maestra para clasificar civilizaciones, en diálogo con Kardashev, Sagan, Drake y Fermi.',
 'en':'That background runs through each of his books. In the <em>Ad Primordia</em> saga, which opens with <em>Despertar</em>, the comparative mythology of Sumer, Babylon, Assyria, Persia, and the Judeo-Christian tradition meets hard science fiction and first contact. In <em>El tablero de césped</em> he translates the vocabulary of chess (the pin, the fork, zugzwang) into an operating system for analyzing soccer in real time. In <em>La eficiencia espaciotemporal</em> he proposes a Master Equation for classifying civilizations, in dialogue with Kardashev, Sagan, Drake, and Fermi.',
 'pt':'Essa formação atravessa cada um de seus livros. Na saga <em>Ad Primordia</em>, iniciada com <em>Despertar</em>, a mitologia comparada da Suméria, Babilônia, Assíria, Pérsia e da tradição judaico-cristã cruza-se com a ficção científica hard e o primeiro contato. Em <em>El tablero de césped</em>, traduz o vocabulário do xadrez (a cravada, o garfo, o zugzwang) em um sistema operacional para analisar o futebol em tempo real. Em <em>La eficiencia espaciotemporal</em>, propõe uma Equação Mestra para classificar civilizações, em diálogo com Kardashev, Sagan, Drake e Fermi.'},
'bio5': {
 'es':'Escribe con una convicción que comparten sus tres obras: una idea vale en la medida en que resiste el examen. Por eso no ofrece verdades cerradas, sino marcos para pensar, e invita al lector a discutirlos, recalcularlos y desafiarlos.',
 'en':'He writes with a conviction shared by all three books: an idea is worth only as much as it withstands scrutiny. That is why he offers not closed truths but frameworks for thinking, and invites readers to debate them, recalculate them, and challenge them.',
 'pt':'Escreve com uma convicção que suas três obras compartilham: uma ideia vale na medida em que resiste ao exame. Por isso não oferece verdades fechadas, mas marcos para pensar, e convida o leitor a discuti-los, recalculá-los e desafiá-los.'},
'creds_aria': {'es':'Formación','en':'Education','pt':'Formação'},
'creds': {
 'es':['MBA','Magíster en Estrategia Nacional','Esp. Inteligencia Estratégica','Esp. Seguridad y Defensa','Prof. Historia de los Conflictos Armados','Lic. Ciencias Militares'],
 'en':['MBA','M.A. in National Strategy','Spec. in Strategic Intelligence','Spec. in Security and Defense','Prof. of the History of Armed Conflicts','B.Sc. in Military Sciences'],
 'pt':['MBA','Mestre em Estratégia Nacional','Esp. em Inteligência Estratégica','Esp. em Segurança e Defesa','Prof. de História dos Conflitos Armados','Bacharel em Ciências Militares']},
'ai_note': {
 'es':'<b>Nota de transparencia.</b> En la elaboración de estos libros se usaron herramientas de inteligencia artificial como apoyo en la redacción, la verificación, la corrección y la creación de portadas e imágenes. La concepción de cada obra, su canon y todas las decisiones creativas son del autor, que revisó y aprobó cada página. Cada libro detalla este proceso en una nota final. Las traducciones de este sitio y las ilustraciones de Novedades también se elaboraron con IA y fueron revisadas.',
 'en':'<b>Transparency note.</b> Artificial intelligence tools were used in preparing these books, as support for drafting, fact-checking, copyediting, and creating covers and images. The conception of each work, its canon, and every creative decision belong to the author, who reviewed and approved every page. Each book describes this process in a closing note. The translations on this website and the illustrations in News were also produced with AI and reviewed.',
 'pt':'<b>Nota de transparência.</b> Na elaboração destes livros, foram usadas ferramentas de inteligência artificial como apoio à redação, à verificação, à revisão e à criação de capas e imagens. A concepção de cada obra, seu cânone e todas as decisões criativas são do autor, que revisou e aprovou cada página. Cada livro detalha esse processo em uma nota final. As traduções deste site e as ilustrações de Novidades também foram elaboradas com IA e revisadas.'},
'contact_h3': {'es':'Escribile al autor','en':'Write to the author','pt':'Escreva ao autor'},
'contact_p': {
 'es':'Lectores, prensa, clubes de lectura e instituciones. También podés escribir a',
 'en':'Readers, press, book clubs, and institutions. You can also write to',
 'pt':'Leitores, imprensa, clubes de leitura e instituições. Você também pode escrever para'},
'name_ph': {'es':'Nombre','en':'Name','pt':'Nome'},
'msg_ph': {'es':'Tu mensaje','en':'Your message','pt':'Sua mensagem'},
'consent_read': {
 'es':'Leí la <button type="button" class="js-privacy">política de privacidad</button>.',
 'en':'I have read the <button type="button" class="js-privacy">privacy policy</button>.',
 'pt':'Li a <button type="button" class="js-privacy">política de privacidade</button>.'},
'send_btn': {'es':'Enviar mensaje','en':'Send message','pt':'Enviar mensagem'},
'contact_formname': {'es':'Contacto','en':'Contact — EN','pt':'Contato — PT'},
'contact_subject': {'es':'Nuevo mensaje de contacto — web Ellian Lessel','en':'New contact message (EN) — Ellian Lessel website','pt':'Nova mensagem de contato (PT) — site Ellian Lessel'},

# ---------- footer ----------
'foot_tag': {
 'es':'Ficción, estrategia y cosmos. Edición independiente del autor · Montevideo, Uruguay.',
 'en':'Fiction, strategy, and the cosmos. Independently published by the author · Montevideo, Uruguay.',
 'pt':'Ficção, estratégia e cosmos. Edição independente do autor · Montevidéu, Uruguai.'},
'foot_books': {'es':'Obras','en':'Books','pt':'Obras'},
'foot_comm': {'es':'Comunidad','en':'Community','pt':'Comunidade'},
'foot_list': {'es':'Lista de lectores','en':'Reader list','pt':'Lista de leitores'},
'privacy': {'es':'Política de privacidad','en':'Privacy policy','pt':'Política de privacidade'},
'rights': {'es':'© 2026 Ellian Lessel. Todos los derechos reservados.','en':'© 2026 Ellian Lessel. All rights reserved.','pt':'© 2026 Ellian Lessel. Todos os direitos reservados.'},
'made_in': {'es':'Hecho en Uruguay','en':'Made in Uruguay','pt':'Feito no Uruguai'},
'totop': {'es':'Volver arriba','en':'Back to top','pt':'Voltar ao topo'},
'close': {'es':'Cerrar','en':'Close','pt':'Fechar'},

# ---------- mensajes JS ----------
'js': {
 'es':{'showing':'Mostrando','book1':'libro','bookN':'libros','for_whom':'Para quién es','specs':'Ficha técnica','opinions':'Opiniones de lectores',
       'no_rev_book':'Todavía no hay reseñas publicadas de este libro. Si ya lo leíste, tu opinión ayuda a otros lectores a encontrarlo.',
       'leave_review':'Dejar una reseña','form_invalid':'Revisá los campos y aceptá la política de privacidad.','sending':'Enviando…',
       'preview':'Vista previa: el formulario se activa al publicar el sitio. Mientras tanto, escribí a','fail':'No se pudo enviar. Probá de nuevo en unos minutos o escribí a',
       'ok_sub':'¡Listo! Te avisaremos cuando salga Creación.','ok_contact':'Mensaje enviado. ¡Gracias por escribir!','ok_mailbox':'Mensaje recibido. ¡Gracias por sumar tu voz!',
       'ig_pending':'Instagram: enlace en preparación','gr_pending':'Goodreads: perfil en aprobación','stars_of':'de 5','rating':'Valoración','buy_in':'Comprar en'},
 'en':{'showing':'Showing','book1':'book','bookN':'books','for_whom':'Who it is for','specs':'Details','opinions':'Reader reviews',
       'no_rev_book':'There are no reviews of this book published here yet. If you have read it, your opinion helps other readers find it.',
       'leave_review':'Leave a review','form_invalid':'Please check the fields and accept the privacy policy.','sending':'Sending…',
       'preview':'Preview: the form becomes active once the site is published. In the meantime, write to','fail':'The message could not be sent. Please try again in a few minutes or write to',
       'ok_sub':'All set! We will let you know when Creación comes out.','ok_contact':'Message sent. Thank you for writing!','ok_mailbox':'Message received. Thank you for adding your voice!',
       'ig_pending':'Instagram: link coming soon','gr_pending':'Goodreads: profile pending approval','stars_of':'out of 5','rating':'Rating','buy_in':'Buy on'},
 'pt':{'showing':'Mostrando','book1':'livro','bookN':'livros','for_whom':'Para quem é','specs':'Ficha técnica','opinions':'Opiniões de leitores',
       'no_rev_book':'Ainda não há resenhas publicadas deste livro. Se você já o leu, sua opinião ajuda outros leitores a encontrá-lo.',
       'leave_review':'Deixar uma resenha','form_invalid':'Revise os campos e aceite a política de privacidade.','sending':'Enviando…',
       'preview':'Prévia: o formulário será ativado quando o site for publicado. Enquanto isso, escreva para','fail':'Não foi possível enviar. Tente novamente em alguns minutos ou escreva para',
       'ok_sub':'Pronto! Avisaremos quando Creación for lançado.','ok_contact':'Mensagem enviada. Obrigado por escrever!','ok_mailbox':'Mensagem recebida. Obrigado por somar sua voz!',
       'ig_pending':'Instagram: link em preparação','gr_pending':'Goodreads: perfil em aprovação','stars_of':'de 5','rating':'Avaliação','buy_in':'Comprar na'}},

# ---------- privacidad ----------
'privacy_html': {
 'es':'<h2 id="mtitle">Política de privacidad</h2><p><strong>Responsable.</strong> Ellian Lessel, autor con domicilio en Montevideo, Uruguay. Contacto: {mail}.</p><p><strong>Qué datos se recogen.</strong> Solo los que escribís en los formularios: tu correo electrónico (lista de lectores) y, en los formularios de contacto y del buzón del lector, tu nombre o alias, la categoría elegida y tu mensaje.</p><p><strong>Para qué.</strong> Para avisarte de nuevos libros y novedades del autor, y para responder tus mensajes. Un mensaje del buzón solo se publica, resumido y con tu nombre de pila o alias, si marcaste la casilla de autorización. No se venden ni se ceden datos a terceros.</p><p><strong>Dónde se guardan.</strong> En Formspree, el servicio que recibe los formularios de este sitio y los reenvía al correo del autor.</p><p><strong>Tus derechos.</strong> Podés pedir acceso, rectificación, actualización o eliminación de tus datos, retirar una autorización de publicación o darte de baja de la lista, escribiendo al correo indicado. Esta política se rige por la Ley n.º 18.331 de Protección de Datos Personales de la República Oriental del Uruguay.</p><p><strong>Enlaces externos.</strong> Los botones de compra y de redes llevan a Amazon, Instagram y Goodreads, que aplican sus propias políticas.</p><p style="color:var(--mut)">Última actualización: noviembre de 2026.</p>',
 'en':'<h2 id="mtitle">Privacy policy</h2><p><strong>Data controller.</strong> Ellian Lessel, an author based in Montevideo, Uruguay. Contact: {mail}.</p><p><strong>What data is collected.</strong> Only what you type into the forms: your email address (reader list) and, in the contact and reader mailbox forms, your name or alias, the category you choose, and your message.</p><p><strong>Why.</strong> To let you know about new books and the author’s news, and to answer your messages. A mailbox message is published, summarized and with your first name or alias, only if you ticked the authorization box. Data is never sold or shared with third parties.</p><p><strong>Where it is stored.</strong> With Formspree, the service that receives this website’s forms and forwards them to the author’s email.</p><p><strong>Your rights.</strong> You may request access to, correction, updating, or deletion of your data, withdraw a publication authorization, or unsubscribe from the list by writing to the address above. This policy is governed by Law No. 18,331 on the Protection of Personal Data of the Oriental Republic of Uruguay.</p><p><strong>External links.</strong> The purchase and social media buttons lead to Amazon, Instagram, and Goodreads, which apply their own policies.</p><p style="color:var(--mut)">Last updated: November 2026.</p>',
 'pt':'<h2 id="mtitle">Política de privacidade</h2><p><strong>Responsável.</strong> Ellian Lessel, autor com domicílio em Montevidéu, Uruguai. Contato: {mail}.</p><p><strong>Que dados são coletados.</strong> Apenas os que você escreve nos formulários: seu e-mail (lista de leitores) e, nos formulários de contato e da caixa do leitor, seu nome ou apelido, a categoria escolhida e sua mensagem.</p><p><strong>Para quê.</strong> Para avisá-lo sobre novos livros e novidades do autor e para responder às suas mensagens. Uma mensagem da caixa do leitor só é publicada, resumida e com seu primeiro nome ou apelido, se você marcou a caixa de autorização. Os dados não são vendidos nem cedidos a terceiros.</p><p><strong>Onde são armazenados.</strong> No Formspree, o serviço que recebe os formulários deste site e os encaminha ao e-mail do autor.</p><p><strong>Seus direitos.</strong> Você pode solicitar acesso, retificação, atualização ou exclusão de seus dados, retirar uma autorização de publicação ou cancelar a inscrição na lista, escrevendo para o e-mail indicado. Esta política rege-se pela Lei n.º 18.331 de Proteção de Dados Pessoais da República Oriental do Uruguai.</p><p><strong>Links externos.</strong> Os botões de compra e de redes sociais levam à Amazon, ao Instagram e ao Goodreads, que aplicam suas próprias políticas.</p><p style="color:var(--mut)">Última atualização: novembro de 2026.</p>'},
}
