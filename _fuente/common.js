/* Ellian Lessel — funciones comunes a todas las páginas */
(function(){
'use strict';
var S = window.SITE || {}, T = S.t || {};
window.EL = {};
var mail = ['ellian.lessel','gmail.com'].join('@');
EL.mail = mail;
EL.esc = function(s){return String(s).replace(/[&<>"']/g,function(c){return {"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c];});};
EL.reduced = function(){return window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;};

/* ---------- idioma: guardar elección ---------- */
[].forEach.call(document.querySelectorAll('[data-setlang]'),function(a){
  a.addEventListener('click',function(){try{localStorage.setItem('el_lang',a.getAttribute('data-setlang'));}catch(e){}});
});

/* ---------- tienda de Amazon según país ---------- */
var STORES = {'com':'Amazon.com','es':'Amazon.es','com.mx':'Amazon.com.mx','com.br':'Amazon.com.br'};
function detectStore(){
  try{var s=localStorage.getItem('el_store'); if(s&&STORES[s]) return s;}catch(e){}
  var l=((navigator.languages&&navigator.languages[0])||navigator.language||'').toLowerCase();
  if(l==='es-es'||l==='ca'||l.indexOf('ca-')===0||l==='eu'||l==='gl'||l.indexOf('pt-pt')===0) return 'es';
  if(l==='es-mx') return 'com.mx';
  if(l.indexOf('pt')===0) return 'com.br';
  return 'com';
}
EL.store = detectStore();
EL.amz = function(asin,store){return 'https://www.amazon.'+(store||EL.store)+'/dp/'+asin;};
EL.updateStores = function(){
  [].forEach.call(document.querySelectorAll('.js-amz'),function(a){a.href=EL.amz(a.getAttribute('data-asin'));});
  [].forEach.call(document.querySelectorAll('.js-storename'),function(s){s.textContent=STORES[EL.store];});
  [].forEach.call(document.querySelectorAll('.stores button'),function(b){b.setAttribute('aria-pressed',String(b.getAttribute('data-store')===EL.store));});
};
EL.storesHTML = function(){
  return '<details class="stores"><summary>'+EL.esc(T.other_stores||'Otras tiendas')+' · <span class="js-storename"></span></summary><div>'+
    Object.keys(STORES).map(function(k){return '<button type="button" data-store="'+k+'" aria-pressed="false">'+STORES[k]+'</button>';}).join('')+'</div></details>';
};
document.addEventListener('click',function(e){
  var b=e.target.closest('.stores button'); if(!b) return;
  EL.store=b.getAttribute('data-store'); try{localStorage.setItem('el_store',EL.store);}catch(x){}
  EL.updateStores();
});

/* ---------- correo ---------- */
EL.fillMail = function(){[].forEach.call(document.querySelectorAll('.js-mail'),function(a){a.href='mailto:'+mail;a.textContent=mail;});};

/* ---------- modal ---------- */
var modal=document.getElementById('modal'),dialog=document.getElementById('dialog'),mbody=document.getElementById('mbody'),lastFocus=null;
EL.openModal=function(html,cls){
  lastFocus=document.activeElement; mbody.innerHTML=html; dialog.className='dialog '+(cls||'');
  modal.classList.add('open'); modal.setAttribute('aria-hidden','false'); document.body.style.overflow='hidden';
  EL.updateStores(); setTimeout(function(){document.getElementById('mclose').focus();},30);
};
function closeModal(){
  if(!modal.classList.contains('open')) return;
  modal.classList.remove('open'); modal.setAttribute('aria-hidden','true'); document.body.style.overflow='';
  if(lastFocus&&lastFocus.focus) lastFocus.focus();
}
document.getElementById('mclose').addEventListener('click',closeModal);
modal.addEventListener('click',function(e){if(e.target===modal) closeModal();});
document.addEventListener('keydown',function(e){
  if(!modal.classList.contains('open')) return;
  if(e.key==='Escape'){e.preventDefault();closeModal();return;}
  if(e.key==='Tab'){
    var f=[].slice.call(dialog.querySelectorAll('a[href],button:not([disabled]),input,textarea,select,summary,[tabindex]:not([tabindex="-1"])')).filter(function(x){return x.offsetParent!==null;});
    if(!f.length) return; var first=f[0],last=f[f.length-1];
    if(e.shiftKey&&document.activeElement===first){e.preventDefault();last.focus();}
    else if(!e.shiftKey&&document.activeElement===last){e.preventDefault();first.focus();}
  }
});
document.addEventListener('click',function(e){
  var p=e.target.closest('.js-privacy'); if(p){e.preventDefault();EL.openModal('<div class="legaltext">'+S.privacy.replace('{mail}',mail)+'</div>','');}
});

/* ---------- formularios (Formspree) ---------- */
[].forEach.call(document.querySelectorAll('.js-form'),function(form){
  form.addEventListener('submit',function(e){
    e.preventDefault(); var msg=form.querySelector('.formmsg'); msg.className='formmsg';
    if(!form.checkValidity()){msg.classList.add('err');msg.textContent=T.form_invalid;var bad=form.querySelector(':invalid');if(bad)bad.focus();return;}
    msg.textContent=T.sending;
    var mailLink=' <a href="mailto:'+mail+'">'+mail+'</a>.';
    if(location.protocol==='file:'){msg.classList.add('err');msg.innerHTML=EL.esc(T.preview)+mailLink;return;}
    var sel=form.querySelector('select[name="categoria"]'), subj=form.querySelector('input[name="_subject"]');
    if(sel&&subj&&!subj.dataset.base){subj.dataset.base=subj.value;}
    if(sel&&subj){subj.value=subj.dataset.base+' · '+sel.options[sel.selectedIndex].text;}
    fetch(form.action,{method:'POST',headers:{'Accept':'application/json'},body:new FormData(form)})
     .then(function(r){if(!r.ok) throw 0; form.reset(); msg.classList.add('ok'); msg.textContent=T[form.getAttribute('data-ok')]||T.ok_contact;})
     .catch(function(){msg.classList.add('err'); msg.innerHTML=EL.esc(T.fail)+mailLink;});
  });
});

/* ---------- menú, volver arriba, revelado ---------- */
var burger=document.getElementById('burger'),menu=document.getElementById('menu');
function setMenu(o){menu.classList.toggle('open',o);burger.setAttribute('aria-expanded',String(o));burger.setAttribute('aria-label',o?burger.dataset.close:burger.dataset.open);}
burger.addEventListener('click',function(){setMenu(!menu.classList.contains('open'));});
menu.addEventListener('click',function(e){if(e.target.closest('a')) setMenu(false);});
document.addEventListener('keydown',function(e){if(e.key==='Escape'&&menu.classList.contains('open')){setMenu(false);burger.focus();}});
var totop=document.getElementById('totop');
totop.addEventListener('click',function(){window.scrollTo({top:0,behavior:EL.reduced()?'auto':'smooth'});document.querySelector('.brand').focus();});
var links=[].slice.call(document.querySelectorAll('.menu a[href*="#"]')).filter(function(a){var h=a.getAttribute('href');return h.charAt(0)==='#'||document.getElementById(h.split('#')[1])&&a.pathname===location.pathname;});
function onScroll(){
  totop.classList.toggle('show',window.scrollY>700);
  if(!links.length) return;
  var y=window.scrollY+120,cur=-1;
  links.forEach(function(a,i){var s=document.getElementById(a.getAttribute('href').split('#')[1]); if(s&&s.offsetTop<=y) cur=i;});
  links.forEach(function(a,i){a.classList.toggle('on',i===cur); if(i===cur) a.setAttribute('aria-current','true'); else a.removeAttribute('aria-current');});
}
window.addEventListener('scroll',onScroll,{passive:true}); onScroll();
EL.reveal=function(root){
  var els=(root||document).querySelectorAll('.rv:not(.in)');
  if('IntersectionObserver' in window){
    var io=new IntersectionObserver(function(es){es.forEach(function(en){if(en.isIntersecting){en.target.classList.add('in');io.unobserve(en.target);}});},{threshold:.1});
    [].forEach.call(els,function(el){io.observe(el);});
  }else{[].forEach.call(els,function(el){el.classList.add('in');});}
};
document.addEventListener('DOMContentLoaded',function(){EL.fillMail();EL.updateStores();EL.reveal();});
if(document.readyState!=='loading'){EL.fillMail();EL.updateStores();EL.reveal();}
})();
