/* Ellian Lessel — portada: catálogo, ecuación, reseñas, saga */
(function(){
'use strict';
var S=window.SITE,H=window.HOME,T=S.t,esc=EL.esc,R=S.root;
var CART=S.cart, INFO='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/></svg>';
var KND='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="5" y="2" width="14" height="20" rx="2"/><path d="M9 18h6"/></svg>';

/* Reseñas reales: agregar objetos con este formato, solo con autorización del lector:
   { libro:"ap1"|"tab"|"efi", autor:"Nombre o alias", texto:"…", estrellas:5 (opcional),
     fuente:"Amazon"|"Goodreads"|"Lector directo", url:"https://…" (opcional), fecha:"2026-11", idioma:"es" } */
var RESENAS = [];

var B=H.books, ORDER=['ap1','tab','efi'], F={ap1:'fic',tab:'est',efi:'ens'}, P={ap1:'p-fic',tab:'p-est',efi:'p-ens'};
var IMG={ap1:R+'assets/ap1.webp',tab:R+'assets/tablero.webp',efi:R+'assets/eficiencia.webp'};
function buyBtn(id,track){return '<a class="btn btn-amz js-amz" data-asin="'+H.asin[id]+'" href="'+EL.amz(H.asin[id])+'" target="_blank" rel="noopener" data-track="'+track+'">'+CART+esc(T.buy)+'</a>';}
function rateHTML(id){
  var rs=RESENAS.filter(function(r){return r.libro===id&&r.estrellas;});
  if(!rs.length) return '<span class="rate">'+esc(T.no_reviews)+' · <a href="#resenas">'+esc(T.first_review)+'</a></span>';
  var avg=rs.reduce(function(a,r){return a+r.estrellas;},0)/rs.length,n=Math.round(avg);
  return '<span class="rate" aria-label="'+esc(T.rating)+' '+avg.toFixed(1)+' '+esc(T.stars_of)+'">'+'★★★★★'.slice(0,n)+'<span style="opacity:.3">'+'★★★★★'.slice(n)+'</span> '+avg.toFixed(1)+'/5 · '+rs.length+' '+esc(T.reviews_word)+'</span>';
}

/* catálogo */
var booksEl=document.getElementById('books');
booksEl.innerHTML=ORDER.map(function(id){var b=B[id];
  return '<article class="book '+P[id]+' rv" data-f="'+F[id]+'">'+
   '<div class="cover"><img src="'+IMG[id]+'" alt="'+esc(T.cover_of+' '+H.full[id])+'" width="220" height="330" loading="lazy"></div>'+
   '<div class="book-body"><span class="label">'+esc(b.label)+'</span>'+
   '<h3 lang="es">'+esc(H.title[id])+'<small>'+esc(H.sub[id])+'</small></h3>'+
   (b.gloss?'<p class="gloss">'+esc(b.gloss)+'</p>':'')+
   '<p class="syn">'+esc(b.syn)+'</p>'+rateHTML(id)+
   '<div class="meta">'+b.meta.map(function(m,i){return '<span>'+(i===0?KND:'')+esc(m)+'</span>';}).join('')+'</div>'+
   '<div class="actions">'+buyBtn(id,'amazon-'+id)+'<button class="btn btn-line js-open" data-id="'+id+'">'+INFO+esc(T.details)+'</button></div>'+
   EL.storesHTML()+'</div></article>';
}).join('');
var chips=[].slice.call(document.querySelectorAll('#filters .chip'));
function count(f){return f==='all'?ORDER.length:ORDER.filter(function(id){return F[id]===f;}).length;}
chips.forEach(function(c){c.querySelector('.n').textContent='('+count(c.dataset.f)+')';});
function filter(f){
  chips.forEach(function(c){c.setAttribute('aria-pressed',String(c.dataset.f===f));});
  [].forEach.call(booksEl.children,function(el){el.classList.toggle('hide',!(f==='all'||el.dataset.f===f)); el.classList.add('in');});
  var n=count(f); document.getElementById('filterStatus').textContent=T.showing+' '+n+' '+(n===1?T.book1:T.bookN);
}
chips.forEach(function(c){c.addEventListener('click',function(){filter(c.dataset.f);});});
[].forEach.call(document.querySelectorAll('[data-go]'),function(a){a.addEventListener('click',function(){if(a.dataset.go!=='ens') filter(a.dataset.go);});});

/* ficha */
function revHTML(r){return '<article class="rev '+P[r.libro]+'"><span class="label">'+esc(H.full[r.libro])+'</span>'+(r.estrellas?'<span aria-label="'+r.estrellas+' '+esc(T.stars_of)+'" style="color:var(--gold2)">'+'★★★★★'.slice(0,r.estrellas)+'</span>':'')+'<blockquote'+(r.idioma?' lang="'+esc(r.idioma)+'"':'')+'>«'+esc(r.texto)+'»</blockquote><footer>— '+esc(r.autor)+' · '+(r.url?'<a href="'+esc(r.url)+'" target="_blank" rel="noopener">'+esc(r.fuente)+'</a>':esc(r.fuente))+(r.fecha?' · '+esc(r.fecha):'')+'</footer></article>';}
function bookModal(id){
  var b=B[id]; if(!b) return; var rs=RESENAS.filter(function(r){return r.libro===id;});
  var html='<div class="mgrid"><div class="mcov"><img src="'+IMG[id]+'" alt="'+esc(T.cover_of+' '+H.full[id])+'"></div><div>'+
   '<span class="label">'+esc(b.label)+'</span><h2 id="mtitle" lang="es">'+esc(H.full[id])+'</h2>'+(b.gloss?'<p class="gloss">'+esc(b.gloss)+'</p>':'')+
   b.ext.map(function(p){return '<p>'+esc(p)+'</p>';}).join('')+
   '<h3>'+esc(T.for_whom)+'</h3><ul>'+b.para.map(function(p){return '<li>'+esc(p)+'</li>';}).join('')+'</ul>'+
   '<h3>'+esc(T.specs)+'</h3><dl class="specs">'+b.specs.map(function(s){return '<dt>'+esc(s[0])+'</dt><dd>'+esc(s[1])+'</dd>';}).join('')+'</dl>'+
   '<h3>'+esc(T.opinions)+'</h3>'+(rs.length?rs.map(revHTML).join(''):'<p>'+esc(T.no_rev_book)+'</p>')+
   '<div class="actions" style="margin-top:1.2rem">'+buyBtn(id,'amazon-'+id+'-modal')+'<a class="btn btn-line js-amz" data-asin="'+H.asin[id]+'" href="'+EL.amz(H.asin[id])+'" target="_blank" rel="noopener">'+esc(T.leave_review)+'</a></div>'+EL.storesHTML()+'</div></div>';
  EL.openModal(html,P[id]);
}
document.addEventListener('click',function(e){var o=e.target.closest('.js-open'); if(o) bookModal(o.dataset.id);});

/* ecuación */
var SYM={E:'E',T:'T',Cc:'C<sub>c</sub>',Dm:'D<sub>m</sub>',Ili:'I<sub>li</sub>',Ee:'E<sub>e</sub>',B:'B',L:'Λ',Lc:'L<sub>c</sub>',G:'G'};
var V=H.vars, vmain=document.getElementById('vmain'), valt=document.getElementById('valt'), vpanel=document.getElementById('vpanel');
Object.keys(SYM).forEach(function(k){
  var v=V[k], alt=v[0]!=='f', b=document.createElement('button');
  b.className='vbtn'+(alt?' alt':''); b.dataset.v=k; b.setAttribute('aria-pressed','false');
  b.innerHTML='<b class="notranslate" translate="no">'+SYM[k]+'</b><span>'+esc(v[1])+'</span>'; (alt?valt:vmain).appendChild(b);
});
[].forEach.call(document.querySelectorAll('.eq .v'),function(b){b.setAttribute('aria-label',V[b.dataset.v][1]);});
function showVar(k){
  var v=V[k],alt=v[0]!=='f'; vpanel.className='vpanel'+(alt?' alt':'');
  vpanel.innerHTML='<div class="fade"><div class="sym notranslate" translate="no">'+SYM[k]+'</div><span class="typ">'+esc(alt?T.v_comp:T.v_fund)+'</span><h4>'+esc(v[1])+'</h4><p>'+esc(v[2])+'</p><dl><dt>'+esc(T.v_law)+'</dt><dd>'+esc(v[3])+'</dd><dt>'+esc(T.v_hum)+'</dt><dd>'+esc(v[4])+'</dd></dl></div>';
  [].forEach.call(document.querySelectorAll('.vbtn'),function(b){b.setAttribute('aria-pressed',String(b.dataset.v===k));});
  [].forEach.call(document.querySelectorAll('.eq .v'),function(b){b.classList.toggle('on',b.dataset.v===k);});
}
document.addEventListener('click',function(e){var t=e.target.closest('.vbtn,.eq .v'); if(!t) return; showVar(t.dataset.v);
  if(window.innerWidth<900&&t.classList.contains('vbtn')) vpanel.scrollIntoView({block:'nearest',behavior:EL.reduced()?'auto':'smooth'});});
showVar('Ee');
var GR=H.grados, HUE=[190,200,220,250,275,35], scale=document.getElementById('scale'), gdesc=document.getElementById('gdesc');
scale.innerHTML=GR.map(function(g,i){return '<button style="--h:'+HUE[i]+'" data-g="'+i+'" aria-pressed="false"><b>'+g[0]+'</b>'+esc(g[1])+'</button>';}).join('');
function showG(i){var g=GR[i];[].forEach.call(scale.children,function(b){b.setAttribute('aria-pressed',String(b.dataset.g==i));});
  gdesc.innerHTML='<strong>'+esc(T.gr_word)+' '+g[0]+' · '+esc(g[1])+'</strong> <span style="font-family:var(--f-mono);color:var(--amber)">('+g[2]+')</span><br>'+esc(g[3]);}
scale.addEventListener('click',function(e){var b=e.target.closest('button');if(b) showG(+b.dataset.g);});
showG(0);

/* reseñas */
var revsEl=document.getElementById('revs'), rchips=[].slice.call(document.querySelectorAll('#rfilters .chip'));
function emptyHTML(id){return '<div class="empty '+P[id]+'"><span class="label">'+esc(H.full[id])+'</span><h4>'+esc(T.empty_h4)+'</h4><p>'+esc(T.empty_p)+'</p><div><a class="btn btn-line js-amz" data-asin="'+H.asin[id]+'" href="'+EL.amz(H.asin[id])+'" target="_blank" rel="noopener">'+esc(T.empty_btn)+'</a></div></div>';}
rchips.forEach(function(c){var n=c.dataset.r==='all'?RESENAS.length:RESENAS.filter(function(r){return r.libro===c.dataset.r;}).length;c.querySelector('.n').textContent='('+n+')';});
function showRevs(k){
  rchips.forEach(function(c){c.setAttribute('aria-pressed',String(c.dataset.r===k));});
  var ids=k==='all'?ORDER:[k];
  revsEl.innerHTML=ids.map(function(id){var rs=RESENAS.filter(function(r){return r.libro===id;});return rs.length?rs.map(revHTML).join(''):emptyHTML(id);}).join('');
  EL.updateStores();
}
rchips.forEach(function(c){c.addEventListener('click',function(){showRevs(c.dataset.r);});});
showRevs('all');

/* saga */
var VO=H.vols, ST=H.stages, VIMG=[R+'assets/ap1.webp',R+'assets/ap2.webp',R+'assets/ap3.webp',R+'assets/ap4.webp',null];
var tl=document.getElementById('timeline'), vdet=document.getElementById('vdetail');
tl.innerHTML=VO.map(function(v,i){
  var img=VIMG[i]?'<img src="'+VIMG[i]+'" alt="'+esc(T.cover_of+' Ad Primordia, '+T.vol_word+' '+v[0]+': '+v[1]+(v[2]==='pub'?'':' ('+T.preview_word+')'))+'" width="420" height="630">'
     :'<div class="ghost-cover"><b class="gc-num">V</b><span>'+T.cover_soon+'</span></div>';
  return '<div class="vol '+v[2]+'"><button class="vcard" data-i="'+i+'" aria-expanded="false" aria-controls="vdetail"><div class="vimg">'+img+'<span class="ribbon">'+esc(v[3])+'</span></div><div class="vinfo"><small>'+esc(T.vol_word)+' '+v[0]+'</small><h3 lang="es">'+esc(v[1])+'</h3></div></button></div>';
}).join('');
function showVol(i){
  var v=VO[i], btn=tl.querySelector('[data-i="'+i+'"]'), open=btn.getAttribute('aria-expanded')==='true';
  [].forEach.call(tl.querySelectorAll('.vcard'),function(b){b.setAttribute('aria-expanded','false');});
  if(open){vdet.classList.remove('show');return;}
  btn.setAttribute('aria-expanded','true');
  var h='<small class="kicker" style="color:var(--purple2)">'+esc(T.vol_word)+' '+v[0]+' · '+esc(v[3])+'</small><h3>Ad Primordia · <span lang="es">'+esc(v[1])+'</span></h3><p class="lema">«'+esc(v[4])+'»</p><p>'+esc(v[5])+'</p>';
  if(v[2]==='dev'){h+='<ol class="stages" aria-label="'+esc(T.stages_aria)+'">'+ST.map(function(s,k){return '<li class="'+(k<1?'done':k===1?'now':'')+'">'+esc(s)+(k===1?' <span class="sr">('+esc(T.stage_now)+')</span>':'')+'</li>';}).join('')+'</ol><p><a href="#suscribir" style="color:var(--gold2)">'+esc(T.notify_link)+'</a></p>';}
  if(v[2]==='pub'){h+='<p>'+buyBtn('ap1','amazon-ap1-saga').replace('btn btn-amz','btn btn-gold')+'</p>';}
  vdet.innerHTML=h; vdet.classList.add('show'); EL.updateStores();
}
tl.addEventListener('click',function(e){var b=e.target.closest('.vcard');if(b) showVol(+b.dataset.i);});
EL.updateStores(); EL.reveal();
})();
