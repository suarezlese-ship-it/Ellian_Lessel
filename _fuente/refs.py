# -*- coding: utf-8 -*-
# Referencias en formato APA (7.ª ed.). Las obras religiosas clásicas (Génesis) se citan solo en el texto, según APA.
L_ES = {
 'a':'Lessel, E. (2026a). <em>Ad Primordia: Vol. I. Despertar</em>.',
 'b':'Lessel, E. (2026b). <em>El tablero de césped: Sistema operativo de ajedrez dinámico aplicado al fútbol</em>.',
 'c':'Lessel, E. (2026c). <em>La eficiencia espaciotemporal: Una propuesta teórica de clasificación universal de la evolución de las civilizaciones</em>.'}
L_EN = {
 'a':'Lessel, E. (2026a). <em>Ad Primordia: Vol. I. Despertar</em> [Awakening].',
 'b':'Lessel, E. (2026b). <em>El tablero de césped: Sistema operativo de ajedrez dinámico aplicado al fútbol</em> [The turf board: A dynamic chess operating system applied to soccer].',
 'c':'Lessel, E. (2026c). <em>La eficiencia espaciotemporal: Una propuesta teórica de clasificación universal de la evolución de las civilizaciones</em> [Spacetime efficiency: A theoretical proposal for a universal classification of the evolution of civilizations].'}
L_PT = {
 'a':'Lessel, E. (2026a). <em>Ad Primordia: Vol. I. Despertar</em> [Despertar].',
 'b':'Lessel, E. (2026b). <em>El tablero de césped: Sistema operativo de ajedrez dinámico aplicado al fútbol</em> [O tabuleiro de grama: sistema operacional de xadrez dinâmico aplicado ao futebol].',
 'c':'Lessel, E. (2026c). <em>La eficiencia espaciotemporal: Una propuesta teórica de clasificación universal de la evolución de las civilizaciones</em> [A eficiência espaçotemporal: uma proposta teórica de classificação universal da evolução das civilizações].'}
LESSEL = {'es':L_ES,'en':L_EN,'pt':L_PT}
def single(lang,k):  # una sola obra del autor en la lista: sin letra
    return LESSEL[lang][k].replace('2026'+k,'2026')

KARD = 'Kardashev, N. S. (1964). Transmission of information by extraterrestrial civilizations. <em>Soviet Astronomy, 8</em>(2), 217–221.'
LAYARD = 'Layard, A. H. (1853). <em>Discoveries in the ruins of Nineveh and Babylon</em>. John Murray.'
SMITH = 'Smith, G. (1873). The Chaldean account of the Deluge. <em>Transactions of the Society of Biblical Archaeology, 2</em>, 213–234.'
KRAMER = 'Kramer, S. N. (1961). <em>Sumerian mythology: A study of spiritual and literary achievement in the third millennium B.C.</em> (Rev. ed.). Harper &amp; Brothers.'
def LAMBERT(lang): return 'Lambert, W. G., {} Millard, A. R. (1969). <em>Atra-ḫasīs: The Babylonian story of the Flood</em>. Clarendon Press.'.format('y' if lang=='es' else '&amp;')
GEORGE = 'George, A. R. (2003). <em>The Babylonian Gilgamesh epic: Introduction, critical edition and cuneiform texts</em> (Vols. 1–2). Oxford University Press.'
NICK = 'Nickelsburg, G. W. E. (2001). <em>1 Enoch 1: A commentary on the Book of 1 Enoch, chapters 1–36; 81–108</em>. Fortress Press.'
SAGAN = 'Sagan, C. (1973). <em>The cosmic connection: An extraterrestrial perspective</em>. Anchor Press.'
JONES = 'Jones, E. M. (1985). <em>“Where is everybody?” An account of Fermi’s question</em> (Report LA-10311-MS). Los Alamos National Laboratory.'
def DRAKE(lang):
    en = {'es':'En','en':'In','pt':'In'}[lang]; eds = {'es':'(Eds.)','en':'(Eds.)','pt':'(Eds.)'}[lang]
    y = 'y' if lang=='es' else '&amp;'
    return f'Drake, F. D. (1965). The radio search for intelligent extraterrestrial life. {en} G. Mamikunian {y} M. H. Briggs {eds}, <em>Current aspects of exobiology</em> (pp. 323–345). Pergamon Press.'
EHMAN = 'Ehman, J. R. (1998). <em>The Big Ear Wow! signal: What we know and don’t know about it after 20 years</em>. Big Ear Radio Observatory. <a href="https://bigear.org/wow20th.htm" target="_blank" rel="noopener">https://bigear.org/wow20th.htm</a>'

def refs(pid, lang):
    if pid=='bienvenida': return [KARD, LESSEL[lang]['a'], LESSEL[lang]['b'], LESSEL[lang]['c']]
    if pid=='mitos': return [GEORGE, KRAMER, LAMBERT(lang), LAYARD, single(lang,'a'), NICK, SMITH]
    if pid=='tablero': return [single(lang,'b')]
    if pid=='civilizaciones': return [DRAKE(lang), EHMAN, JONES, KARD, single(lang,'c'), SAGAN]
    return []
TITLE = {'es':'Referencias','en':'References','pt':'Referências'}
NOTE = {'es':'Citas en formato APA (7.ª ed.). Los pasajes bíblicos se citan solo en el texto.',
        'en':'Citations follow APA style (7th ed.). Biblical passages are cited in the text only.',
        'pt':'Citações no formato APA (7.ª ed.). As passagens bíblicas são citadas apenas no texto.'}
