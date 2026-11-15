# -*- coding: utf-8 -*-
BLOG_PATH = {'es':'novedades/','en':'en/news/','pt':'pt/novidades/'}
HOME_PATH = {'es':'','en':'en/','pt':'pt/'}
CATS = {
 'editorial':{'es':'Novedades editoriales','en':'Publishing News','pt':'Novidades editoriais'},
 'ap':{'es':'Detrás de Ad Primordia','en':'Behind Ad Primordia','pt':'Bastidores de Ad Primordia'},
 'juego':{'es':'Estrategia y juego','en':'Strategy & Play','pt':'Estratégia e jogo'},
 'cosmos':{'es':'Ciencia y cosmos','en':'Science & Cosmos','pt':'Ciência e cosmos'},
 'lectores':{'es':'Respuestas a lectores','en':'Reader Q&A','pt':'Respostas aos leitores'},
}
CAT_COLOR = {'editorial':'gold','ap':'purple','juego':'grass','cosmos':'cyan','lectores':'amber'}
B = {
'blog_title': {'es':'Novedades — Ellian Lessel','en':'News — Ellian Lessel','pt':'Novidades — Ellian Lessel'},
'blog_desc': {'es':'Novedades editoriales, mitologías antiguas, estrategia, ciencia y cosmos. Textos de Ellian Lessel y respuestas a lectores.',
              'en':'Publishing news, ancient mythologies, strategy, science, and the cosmos. Writing by Ellian Lessel and answers to readers.',
              'pt':'Novidades editoriais, mitologias antigas, estratégia, ciência e cosmos. Textos de Ellian Lessel e respostas aos leitores.'},
'blog_kicker': {'es':'Novedades','en':'News','pt':'Novidades'},
'blog_h1': {'es':'Para seguir pensando más allá de las páginas','en':'To keep thinking beyond the page','pt':'Para continuar pensando além das páginas'},
'blog_lead': {'es':'Cada quince días o cada mes: mitologías de las civilizaciones antiguas, física y cosmos, estrategia y juego, y las preguntas de los lectores.',
              'en':'Every two weeks or every month: the mythologies of ancient civilizations, physics and the cosmos, strategy and play, and readers’ questions.',
              'pt':'A cada quinze dias ou a cada mês: mitologias das civilizações antigas, física e cosmos, estratégia e jogo, e as perguntas dos leitores.'},
'cat_aria': {'es':'Filtrar por sección','en':'Filter by section','pt':'Filtrar por seção'},
'all_sections': {'es':'Todas','en':'All','pt':'Todas'},
'empty_cat': {'es':'Todavía no hay entradas en esta sección. ¿Querés proponer un tema? Escribinos en el buzón.',
              'en':'There are no posts in this section yet. Would you like to suggest a topic? Write to us in the mailbox.',
              'pt':'Ainda não há textos nesta seção. Quer sugerir um tema? Escreva-nos na caixa do leitor.'},
'mb_kicker': {'es':'Buzón del lector','en':'Reader mailbox','pt':'Caixa do leitor'},
'mb_h2': {'es':'Tu voz también cuenta','en':'Your voice counts too','pt':'Sua voz também conta'},
'mb_p': {'es':'Dejá un mensaje, una sugerencia, una recomendación de lectura o un tema que te gustaría ver tratado. Llega directamente al autor. Si marcás la casilla de autorización, podremos responderlo en «Respuestas a lectores», resumido y solo con tu nombre de pila o alias.',
         'en':'Leave a message, a suggestion, a reading recommendation, or a topic you would like to see covered. It goes straight to the author. If you tick the authorization box, we may answer it in “Reader Q&A,” summarized and with only your first name or alias.',
         'pt':'Deixe uma mensagem, uma sugestão, uma recomendação de leitura ou um tema que gostaria de ver tratado. Chega diretamente ao autor. Se você marcar a caixa de autorização, poderemos respondê-la em “Respostas aos leitores”, resumida e apenas com seu primeiro nome ou apelido.'},
'mb_cat': {'es':'Tipo de mensaje','en':'Type of message','pt':'Tipo de mensagem'},
'mb_opts': {'es':['Mensaje','Sugerencia','Recomendación de lectura','Tema propuesto para Novedades'],
            'en':['Message','Suggestion','Reading recommendation','Suggested topic for News'],
            'pt':['Mensagem','Sugestão','Recomendação de leitura','Tema sugerido para Novidades']},
'mb_name': {'es':'Nombre de pila o alias','en':'First name or alias','pt':'Primeiro nome ou apelido'},
'mb_publish': {'es':'Autorizo que mi mensaje se publique, resumido, con mi nombre de pila o alias.','en':'I authorize publication of my message, summarized, with my first name or alias.','pt':'Autorizo a publicação da minha mensagem, resumida, com meu primeiro nome ou apelido.'},
'mb_send': {'es':'Enviar al buzón','en':'Send to the mailbox','pt':'Enviar para a caixa'},
'mb_formname': {'es':'Buzón del lector','en':'Reader mailbox — EN','pt':'Caixa do leitor — PT'},
'mb_subject': {'es':'Buzón del lector — web Ellian Lessel','en':'Reader mailbox (EN) — Ellian Lessel website','pt':'Caixa do leitor (PT) — site Ellian Lessel'},
'published': {'es':'Publicado el','en':'Published','pt':'Publicado em'},
'by': {'es':'Por','en':'By','pt':'Por'},
'q_title': {'es':'Te dejamos estas preguntas','en':'A few questions for you','pt':'Deixamos estas perguntas'},
'q_cta': {'es':'Respondé en el buzón del lector','en':'Answer in the reader mailbox','pt':'Responda na caixa do leitor'},
'related': {'es':'El libro de esta entrada','en':'The book behind this post','pt':'O livro deste texto'},
'ill_note': {'es':'Ilustración original generada con IA para este sitio.','en':'Original illustration generated with AI for this website.','pt':'Ilustração original gerada com IA para este site.'},
'back': {'es':'← Todas las novedades','en':'← All news','pt':'← Todas as novidades'},
'more': {'es':'Seguir leyendo','en':'Keep reading','pt':'Continue lendo'},
'share': {'es':'Compartir','en':'Share','pt':'Compartilhar'},
'copied': {'es':'Enlace copiado','en':'Link copied','pt':'Link copiado'},
'months': {'es':['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre'],
           'en':['January','February','March','April','May','June','July','August','September','October','November','December'],
           'pt':['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']},
}
def fmt_date(iso, lang):
    y,m,d = iso.split('-'); mo = B['months'][lang][int(m)-1]
    if lang=='en': return f'{mo} {int(d)}, {y}'
    return f'{int(d)} de {mo} de {y}'
