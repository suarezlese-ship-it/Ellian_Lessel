# -*- coding: utf-8 -*-
"""Generador del sitio trilingüe de Ellian Lessel. Uso: python3 build.py <carpeta_salida>"""
import json, os, re, sys, shutil, html
sys.path.insert(0, os.path.dirname(__file__))
from i18n_site import S, LANGS
from i18n_data import ASIN, FULL, SUB, TITLE, BOOKS, VARS, GR, VOLS, STAGES
from i18n_blog import BLOG_PATH, HOME_PATH, CATS, CAT_COLOR, B, fmt_date
from posts_es import POSTS_ES
from posts_en import POSTS_EN
from posts_pt import POSTS_PT

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, 'out')
BASE = 'https://suarezlese-ship-it.github.io/Ellian_Lessel/'
POSTS = {'es': POSTS_ES, 'en': POSTS_EN, 'pt': POSTS_PT}
DATE = {'bienvenida': '2026-11-15', 'mitos': '2026-11-15', 'tablero': '2026-11-15', 'civilizaciones': '2026-11-15'}
ORDER = ['bienvenida', 'mitos', 'tablero', 'civilizaciones']
CART = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/><path d="M1 1h4l2.7 13.4a2 2 0 0 0 2 1.6h9.7a2 2 0 0 0 2-1.6L23 6H6"/></svg>'
LANG_NAME = {'es': 'ES', 'en': 'EN', 'pt': 'PT'}
LANG_FULL = {'es': 'Español', 'en': 'English', 'pt': 'Português'}
JS_KEYS = ['buy','details','other_stores','no_reviews','first_review','reviews_word','cover_of','v_comp','v_fund','v_law','v_hum',
           'gr_word','empty_h4','empty_p','empty_btn','vol_word','preview_word','cover_soon','stages_aria','stage_now','notify_link']

def rd(p): return open(os.path.join(HERE, p), encoding='utf-8').read()
def tr(key, lang): return S[key][lang]
def render(tpl, ctx):
    def rep(m):
        k = m.group(1)
        if k not in ctx: raise KeyError('Falta clave: ' + k)
        return str(ctx[k])
    return re.sub(r'\{\{(\w+)\}\}', rep, tpl)
def words(htmltext): return len(re.sub(r'<[^>]+>', ' ', htmltext).split())
def post(lang, pid): return [p for p in POSTS[lang] if p['id'] == pid][0]
def rel(from_dir_depth): return '../' * from_dir_depth

def depth(path):  # path relativo a la raíz del sitio, p. ej. 'en/news/x.html'
    return path.count('/')

def alt_paths(kind, pid=None):
    if kind == 'home': return {l: HOME_PATH[l] for l in LANGS}
    if kind == 'blog': return {l: BLOG_PATH[l] for l in LANGS}
    return {l: BLOG_PATH[l] + post(l, pid)['slug'] + '.html' for l in LANGS}

def common_ctx(lang, path, kind, pid=None, title=None, desc=None, og_type='website', jsonld=None, og_image=None):
    root = rel(depth(path))
    alts = alt_paths(kind, pid)
    alt_rel = {l: (root + a) if a else (root or './') for l, a in alts.items()}
    hreflang = '\n'.join(f'<link rel="alternate" hreflang="{S["html_lang"][l]}" href="{BASE}{a}">' for l, a in alts.items())
    hreflang += f'\n<link rel="alternate" hreflang="x-default" href="{BASE}{alts["es"]}">'
    switch = ''.join(f'<a href="{alt_rel[l]}" hreflang="{S["html_lang"][l]}" lang="{S["html_lang"][l]}" data-setlang="{l}" title="{LANG_FULL[l]}"'
                     + (' aria-current="true"' if l == lang else '') + f'>{LANG_NAME[l]}</a>' for l in LANGS)
    tjs = dict(S['js'][lang]); tjs.update({k: S[k][lang] for k in JS_KEYS})
    site = {'lang': lang, 'root': root, 't': tjs, 'privacy': S['privacy_html'][lang], 'cart': CART}
    ctx = {k: v[lang] for k, v in S.items() if isinstance(v, dict) and lang in v and isinstance(v[lang], str)}
    ctx.update({
        'lang': lang, 'root': root, 'home': root + HOME_PATH[lang], 'news_url': root + BLOG_PATH[lang],
        'news_active': 'on-page' if kind != 'home' else '',
        'page_title': html.escape(title or S['title'][lang]), 'page_desc': html.escape(desc or S['description'][lang]),
        'canonical': BASE + path.replace('index.html', ''), 'hreflang': hreflang, 'og_type': og_type,
        'og_image': og_image or (BASE + 'og-ellian-lessel.jpg'),
        'alt_json': json.dumps(alt_rel, ensure_ascii=False), 'lang_switch': switch,
        'jsonld': json.dumps(jsonld or {}, ensure_ascii=False), 'site_json': json.dumps(site, ensure_ascii=False),
        'cart_svg': CART, 'page_script': '',
    })
    return ctx

def post_card(lang, p, root):
    cat = p['cat']; mins = max(1, round(words(p['body']) / 220))
    url = root + BLOG_PATH[lang] + p['slug'] + '.html'
    return (f'<a class="post rv" href="{url}" data-cat="{cat}"><img src="{root}assets/{p["img"]}" alt="" loading="lazy" width="1200" height="630">'
            f'<div class="pb"><span class="cat cat-{CAT_COLOR[cat]}">{CATS[cat][lang]}</span><h3>{html.escape(p["title"])}</h3>'
            f'<p>{html.escape(p["dek"])}</p><span class="pm">{fmt_date(DATE[p["id"]], lang)} · {mins} {S["min_read"][lang]}</span></div></a>')

def person_ld(lang):
    return {"@type": "Person", "@id": BASE + "#autor", "name": "Ellian Lessel", "url": BASE,
            "sameAs": ["https://www.instagram.com/ellian.lessel/", "https://www.goodreads.com/user/show/206427856-ellian-lessel"],
            "homeLocation": {"@type": "Place", "name": "Montevideo, Uruguay"}}

def build_home(lang):
    path = HOME_PATH[lang] + 'index.html'
    isbn = {'ap1': '978-9915-44-774-2', 'tab': '978-9915-45-197-8', 'efi': '978-9915-45-083-4'}
    ld = {"@context": "https://schema.org", "@graph": [person_ld(lang)] + [
        {"@type": "Book", "name": FULL[k], "author": {"@id": BASE + "#autor"}, "inLanguage": "es", "bookFormat": "https://schema.org/EBook",
         "isbn": isbn[k], "url": "https://www.amazon.com/dp/" + ASIN[k]} for k in ['ap1', 'tab', 'efi']]}
    ctx = common_ctx(lang, path, 'home', jsonld=ld, desc=S['description'][lang])
    root = ctx['root']
    ctx['lang_note_html'] = f'<p class="lang-note">{S["lang_note"][lang]}</p>' if S['lang_note'][lang] else ''
    ctx['creds_html'] = ''.join(f'<li>{c}</li>' for c in S['creds'][lang])
    ctx['latest_posts'] = ''.join(post_card(lang, post(lang, i), root) for i in ORDER[:3])
    home = {'books': BOOKS[lang], 'vars': VARS[lang], 'grados': GR[lang], 'vols': VOLS[lang], 'stages': STAGES[lang],
            'asin': ASIN, 'full': FULL, 'title': TITLE, 'sub': SUB}
    ctx['page_script'] = '<script>window.HOME=' + json.dumps(home, ensure_ascii=False) + ';</script>\n<script src="' + root + 'assets/home.js"></script>'
    page = render(rd('tpl_head.html'), ctx) + render(rd('tpl_home.html'), ctx) + render(rd('tpl_foot.html'), ctx)
    write(path, page)

def mailbox(lang):
    opts = ''.join(f'<option>{o}</option>' for o in B['mb_opts'][lang])
    return f'''<section class="mailbox rv" id="buzon">
  <div><p class="kicker">{B['mb_kicker'][lang]}</p><h2>{B['mb_h2'][lang]}</h2><p class="lead">{B['mb_p'][lang]}</p></div>
  <form name="buzon" method="POST" action="https://formspree.io/f/xbgogydj" class="js-form" data-ok="ok_mailbox" novalidate>
    <input type="hidden" name="formulario" value="{B['mb_formname'][lang]}">
    <input type="hidden" name="_subject" value="{B['mb_subject'][lang]}">
    <input type="hidden" name="idioma" value="{lang}">
    <p class="hp"><label>—<input name="_gotcha" tabindex="-1" autocomplete="off"></label></p>
    <label class="flabel" for="mb-cat">{B['mb_cat'][lang]}</label>
    <select id="mb-cat" name="categoria" required>{opts}</select>
    <div class="row">
      <label class="sr" for="mb-name">{B['mb_name'][lang]}</label><input id="mb-name" type="text" name="nombre" placeholder="{B['mb_name'][lang]}" autocomplete="given-name" required>
      <label class="sr" for="mb-email">{S['email_label'][lang]}</label><input id="mb-email" type="email" name="email" placeholder="{S['email_label'][lang]}" autocomplete="email" required>
    </div>
    <label class="sr" for="mb-msg">{S['msg_ph'][lang]}</label><textarea id="mb-msg" name="mensaje" placeholder="{S['msg_ph'][lang]}" required></textarea>
    <label class="check"><input type="checkbox" name="autoriza_publicacion" value="sí"> <span>{B['mb_publish'][lang]}</span></label>
    <label class="check"><input type="checkbox" name="consentimiento" required> <span>{S['consent_read'][lang]}</span></label>
    <div><button class="btn btn-gold" type="submit">{B['mb_send'][lang]}</button></div>
    <p class="formmsg" role="status"></p>
  </form>
</section>'''

BLOG_JS = '''<script>(function(){var ch=[].slice.call(document.querySelectorAll('#cats .chip')),ps=[].slice.call(document.querySelectorAll('.posts .post')),em=document.querySelector('.empty-cat');
ch.forEach(function(c){c.addEventListener('click',function(){var k=c.dataset.c,n=0;ch.forEach(function(x){x.setAttribute('aria-pressed',String(x===c));});
ps.forEach(function(p){var s=(k==='all'||p.dataset.cat===k);p.classList.toggle('hide',!s);if(s){n++;p.classList.add('in');}});em.classList.toggle('show',n===0);});});})();</script>'''

def build_blog_index(lang):
    path = BLOG_PATH[lang] + 'index.html'
    ld = {"@context": "https://schema.org", "@type": "Blog", "name": B['blog_title'][lang], "inLanguage": S['html_lang'][lang],
          "url": BASE + BLOG_PATH[lang], "author": person_ld(lang)}
    ctx = common_ctx(lang, path, 'blog', title=B['blog_title'][lang], desc=B['blog_desc'][lang], jsonld=ld)
    root = ctx['root']
    chips = f'<button class="chip" data-c="all" aria-pressed="true">{B["all_sections"][lang]}</button>' + ''.join(
        f'<button class="chip" data-c="{k}" aria-pressed="false">{v[lang]}</button>' for k, v in CATS.items())
    cards = ''.join(post_card(lang, post(lang, i), root) for i in ORDER)
    body = f'''<main id="main"><section class="blog-hero"><div class="wrap">
  <p class="kicker">{B['blog_kicker'][lang]}</p><h1>{B['blog_h1'][lang]}</h1><p class="lead">{B['blog_lead'][lang]}</p></div></section>
<section style="padding-top:0"><div class="wrap">
  <div class="filters" role="group" aria-label="{B['cat_aria'][lang]}" id="cats">{chips}</div>
  <div class="posts">{cards}</div><p class="empty-cat">{B['empty_cat'][lang]}</p>
  {mailbox(lang)}
</div></section></main>'''
    ctx['page_script'] = BLOG_JS
    write(path, render(rd('tpl_head.html'), ctx) + body + render(rd('tpl_foot.html'), ctx))

def build_post(lang, p):
    path = BLOG_PATH[lang] + p['slug'] + '.html'
    d = DATE[p['id']]; mins = max(1, round(words(p['body']) / 220))
    ld = {"@context": "https://schema.org", "@type": "BlogPosting", "headline": p['title'], "description": p['dek'],
          "datePublished": d, "inLanguage": S['html_lang'][lang], "author": person_ld(lang),
          "image": BASE + 'og-ellian-lessel.jpg', "mainEntityOfPage": BASE + path}
    ctx = common_ctx(lang, path, 'post', pid=p['id'], title=p['title'] + ' — Ellian Lessel', desc=p['dek'], og_type='article', jsonld=ld)
    root = ctx['root']; cat = p['cat']
    qs = ''.join(f'<li>{html.escape(q)}</li>' for q in p['questions'])
    rel_html = ''
    if p['book']:
        k = p['book']; img = {'ap1': 'ap1.webp', 'tab': 'tablero.webp', 'efi': 'eficiencia.webp'}[k]
        gloss = BOOKS[lang][k]['gloss']
        rel_html = (f'<aside class="related"><img src="{root}assets/{img}" alt="" width="110" height="165"><div><p class="kicker">{B["related"][lang]}</p>'
                    f'<h3 lang="es">{FULL[k]}</h3>' + (f'<p class="gloss">{html.escape(gloss)}</p>' if gloss else '') +
                    f'<p><a class="btn btn-gold js-amz" data-asin="{ASIN[k]}" href="https://www.amazon.com/dp/{ASIN[k]}" target="_blank" rel="noopener">{CART}{S["buy"][lang]}</a></p></div></aside>')
    body = f'''<main id="main"><section><div class="wrap"><article class="article">
  <a class="backlink" href="{root}{BLOG_PATH[lang]}">{B['back'][lang]}</a><br>
  <span class="cat cat-{CAT_COLOR[cat]}">{CATS[cat][lang]}</span>
  <h1>{html.escape(p['title'])}</h1>
  <p class="dek">{html.escape(p['dek'])}</p>
  <p class="meta-line"><span>{B['by'][lang]} Ellian Lessel</span><span>·</span><time datetime="{d}">{B['published'][lang]} {fmt_date(d, lang)}</time><span>·</span><span>{mins} {S['min_read'][lang]}</span></p>
  <figure><img src="{root}assets/{p['img']}" alt="" width="1200" height="630"><figcaption>{B['ill_note'][lang]}</figcaption></figure>
  <div class="prose">{p['body']}</div>
  <section class="questions" aria-labelledby="q-h"><h2 id="q-h">{B['q_title'][lang]}</h2><ol>{qs}</ol>
    <a class="btn btn-ghost" href="{root}{BLOG_PATH[lang]}#buzon">{B['q_cta'][lang]} →</a></section>
  {rel_html}
  <div class="share"><span>{B['share'][lang]}:</span>
    <a href="https://wa.me/?text={html.escape(p['title'])}%20{BASE}{path}" target="_blank" rel="noopener">WhatsApp</a>
    <a href="https://www.facebook.com/sharer/sharer.php?u={BASE}{path}" target="_blank" rel="noopener">Facebook</a>
    <a href="https://x.com/intent/post?url={BASE}{path}" target="_blank" rel="noopener">X</a>
    <button type="button" class="js-copy" data-ok="{B['copied'][lang]}">{B['share'][lang]} ↗</button></div>
  <a class="backlink" href="{root}{BLOG_PATH[lang]}">{B['back'][lang]}</a>
</article></div></section></main>'''
    ctx['page_script'] = '''<script>(function(){var b=document.querySelector('.js-copy');if(!b)return;b.addEventListener('click',function(){var u=location.href.split('#')[0];
if(navigator.share){navigator.share({title:document.title,url:u}).catch(function(){});return;}
if(navigator.clipboard){navigator.clipboard.writeText(u).then(function(){b.textContent=b.dataset.ok;});}});})();</script>'''
    write(path, render(rd('tpl_head.html'), ctx) + body + render(rd('tpl_foot.html'), ctx))

def write(path, content):
    full = os.path.join(OUT, path); os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, 'w', encoding='utf-8').write(content)

def main():
    os.makedirs(os.path.join(OUT, 'assets'), exist_ok=True)
    css = rd('base.css') + rd('extra.css')
    open(os.path.join(OUT, 'assets', 'site.css'), 'w', encoding='utf-8').write(css)
    for f in ['common.js', 'home.js']: shutil.copy(os.path.join(HERE, f), os.path.join(OUT, 'assets', f))
    for f in ['ap1', 'ap2', 'ap3', 'ap4', 'tablero', 'eficiencia', 'autor', 'emblema', 'firma']:
        shutil.copy(os.path.join(HERE, f + '.webp'), os.path.join(OUT, 'assets', f + '.webp'))
    for f in os.listdir(os.path.join(HERE, 'out', 'assets')):
        if f.startswith('blog-'): shutil.copy(os.path.join(HERE, 'out', 'assets', f), os.path.join(OUT, 'assets', f))
    urls = []
    for lang in LANGS:
        build_home(lang); urls.append(HOME_PATH[lang])
        build_blog_index(lang); urls.append(BLOG_PATH[lang])
        for p in POSTS[lang]: build_post(lang, p); urls.append(BLOG_PATH[lang] + p['slug'] + '.html')
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + \
         ''.join(f'  <url><loc>{BASE}{u}</loc><lastmod>2026-11-15</lastmod></url>\n' for u in urls) + '</urlset>\n'
    open(os.path.join(OUT, 'sitemap.xml'), 'w').write(sm)
    open(os.path.join(OUT, 'robots.txt'), 'w').write(f'User-agent: *\nAllow: /\nSitemap: {BASE}sitemap.xml\n')
    open(os.path.join(OUT, '.nojekyll'), 'w').write('')
    for lang in LANGS:
        for p in POSTS[lang]: print(lang, p['id'], words(p['body']), 'palabras')
    print('OK', len(urls), 'páginas')

if __name__ == '__main__':
    main()
