import{r as h,u as N,j as s,L as m,a as R,b as W,g as J,c as Q,d as Y,e as K,f as O,C as U,p as X}from"./index-Df5d8b20.js";import{G as Z,I as ss,t as a,F as p,a as es,b as ts,c as as,d as ns,e as cs}from"./translations-DRhL8wSs.js";const ls="_container_k9yaw_1",os="_whatsbtn_k9yaw_8",rs="_float_k9yaw_1",is="_content_k9yaw_31",ds="_header_k9yaw_36",hs="_headerText_k9yaw_58",us="_btn_k9yaw_81",xs="_about_k9yaw_101",ms="_aboutText_k9yaw_112",_s="_samples_k9yaw_139",js="_sampleText_k9yaw_151",gs="_samplesContainer_k9yaw_175",ps="_sample_k9yaw_139",vs="_mid_k9yaw_212",bs="_services_k9yaw_243",ks="_serviceCards_k9yaw_260",Cs="_serviceCard_k9yaw_260",ys="_contact_k9yaw_294",Ns="_success_k9yaw_309",fs="_contactForm_k9yaw_327",c={container:ls,whatsbtn:os,float:rs,content:is,header:ds,headerText:hs,btn:us,about:xs,aboutText:ms,samples:_s,sampleText:js,samplesContainer:gs,sample:ps,mid:vs,services:bs,serviceCards:ks,serviceCard:Cs,contact:ys,success:Ns,contactForm:fs},ws="_navbar_st9s0_1",Ts="_container_st9s0_10",Ss="_centered_st9s0_19",Is="_btn_st9s0_24",Fs="_lang_st9s0_39",$s="_left_st9s0_68",Es="_toggle_st9s0_78",Ls="_actions_st9s0_81",Ms="_navlang_st9s0_94",Ds="_mobileNavbar_st9s0_107",qs="_head_st9s0_121",Bs="_content_st9s0_151",d={navbar:ws,container:Ts,centered:Ss,btn:Is,lang:Fs,left:$s,toggle:Es,actions:Ls,navlang:Ms,mobileNavbar:Ds,head:qs,content:Bs},y="/assets/logo-BgdC_uQP.png";function zs(_){return Z({tag:"svg",attr:{viewBox:"0 0 24 24",fill:"none",stroke:"currentColor",strokeWidth:"2",strokeLinecap:"round",strokeLinejoin:"round"},child:[{tag:"line",attr:{x1:"3",y1:"12",x2:"21",y2:"12"},child:[]},{tag:"line",attr:{x1:"3",y1:"6",x2:"21",y2:"6"},child:[]},{tag:"line",attr:{x1:"3",y1:"18",x2:"21",y2:"18"},child:[]}]})(_)}const Ps=()=>{const[_,v]=h.useState(!1),t=()=>{v(!_)},{language:l,changeLanguage:o}=N(),u=j=>{document.getElementById(j).scrollIntoView({behavior:"smooth"})};return _?s.jsxs("nav",{className:d.mobileNavbar,children:[s.jsxs("div",{className:d.head,children:[s.jsx("button",{onClick:()=>u("header"),children:s.jsx("img",{src:y,alt:"Smart Menu"})}),s.jsx("button",{className:d.toggle,onClick:t,children:s.jsx(ss,{})})]}),s.jsxs("div",{className:d.content,children:[s.jsx("button",{onClick:()=>{u("header"),t()},to:"/",children:a("home",l)}),s.jsx("button",{onClick:()=>{u("about"),t()},to:"/",children:a("about",l)}),s.jsx("button",{onClick:()=>{u("services"),t()},to:"/",children:a("services",l)}),s.jsx("button",{onClick:()=>{u("contact"),t()},to:"/",children:a("contact",l)}),l=="ar"?s.jsxs("button",{onClick:()=>{o("he"),t()},className:d.lang,children:[s.jsx(p,{}),"עברית"]}):s.jsxs("button",{onClick:()=>{o("ar"),t()},className:d.lang,children:[s.jsx(p,{}),"العربية"]})]})]}):s.jsx("nav",{className:d.navbar,children:s.jsxs("div",{className:d.container,children:[s.jsxs("div",{className:d.centered,children:[s.jsx("button",{onClick:()=>{u("header")},children:a("home",l)}),s.jsx("button",{onClick:()=>{u("about")},children:a("about",l)}),s.jsx("button",{onClick:()=>{u("services")},children:a("services",l)}),l=="ar"?s.jsxs("button",{className:d.lang,onClick:()=>{o("he")},children:[s.jsx(p,{}),"עברית"]}):s.jsxs("button",{className:d.lang,onClick:()=>{o("ar")},children:[s.jsx(p,{}),"العربية"]}),s.jsx("button",{className:d.btn,onClick:()=>{u("contact")},children:a("contact",l)})]}),s.jsx("div",{className:d.left,children:s.jsx("button",{onClick:()=>{u("header")},children:s.jsx("img",{src:y,alt:"Smart Menu"})})}),s.jsxs("div",{className:d.actions,children:[l=="ar"?s.jsx("button",{onClick:()=>{o("he")},className:d.navlang,children:s.jsx(p,{})}):s.jsx("button",{onClick:()=>{o("ar")},className:d.navlang,children:s.jsx(p,{})}),s.jsx("button",{onClick:t,className:d.toggle,children:s.jsx(zs,{})})]})]})})},Gs="_footer_1qhpp_1",Hs="_footerContent_1qhpp_26",Vs="_links_1qhpp_35",As="_link_1qhpp_35",Rs="_copy_1qhpp_51",Ws="_socials_1qhpp_76",x={footer:Gs,footerContent:Hs,links:Vs,link:As,copy:Rs,socials:Ws},Js="/assets/hosarylogo-CglyLz-J.jpg",Qs=()=>{let v=new Date().getFullYear();const{language:t}=N(),l=o=>{document.getElementById(o).scrollIntoView({behavior:"smooth"})};return s.jsxs("footer",{className:x.footer,children:[s.jsxs("div",{className:x.footerContent,children:[s.jsx(m,{to:"/",children:s.jsx("img",{src:y,alt:"smart menu"})}),s.jsxs("div",{className:x.links,children:[s.jsxs("div",{className:x.link,children:[s.jsx("p",{children:a("homePages",t)}),s.jsx("button",{onClick:()=>l("header"),children:a("home",t)}),s.jsx("button",{onClick:()=>l("about"),children:a("about",t)}),s.jsx("button",{onClick:()=>l("services"),children:a("services",t)})]}),s.jsxs("div",{className:x.link,children:[s.jsx("p",{children:a("contact",t)}),s.jsx("button",{onClick:()=>l("contact"),children:a("contact",t)})]}),s.jsxs("div",{className:x.link,children:[s.jsx("p",{children:a("terms",t)}),s.jsx(m,{to:"/",children:a("terms",t)})]})]})]}),s.jsxs("div",{className:x.copy,children:[s.jsxs("p",{children:["Smart Menu . ",a("allRights",t)," . © ",v]}),s.jsxs("div",{className:x.socials,children:[s.jsx(m,{to:"/",children:s.jsx(es,{})}),s.jsx(m,{to:"/",children:s.jsx(ts,{})}),s.jsx(m,{to:"/",children:s.jsx(as,{})})]}),s.jsx(m,{to:"https://www.hosary.tech/",children:s.jsx("img",{src:Js,target:"_blank",alt:"hosary tech"})})]})]})},Os=()=>{var F,$,E,L,M;const[_,v]=h.useState(null),[t,l]=h.useState(null),[o,u]=h.useState(null),[j,f]=h.useState(null),[k,q]=h.useState(null),{language:r}=N(),{contactLoading:B,contactError:w}=R(e=>e.main),[n,b]=h.useState({fullname:"",email:"",phone:"",subject:"",message:""}),[z,T]=h.useState(!0),[C,S]=h.useState(!1),g=W(),P=()=>{g(X(n)).then(e=>{e!=null&&e.payload&&(b({fullname:"",email:"",phone:"",subject:"",message:""}),S(!0))})},G=e=>{document.getElementById(e).scrollIntoView({behavior:"smooth"})};h.useEffect(()=>{g(J()).then(e=>{var i;v((i=e==null?void 0:e.payload)==null?void 0:i.results)}),g(Q()).then(e=>{l(e==null?void 0:e.payload)}),g(Y()).then(e=>{var i;q((i=e==null?void 0:e.payload)==null?void 0:i.results)}),g(K()).then(e=>{var i;u((i=e==null?void 0:e.payload)==null?void 0:i.results)}),g(O()).then(e=>{var i;f((i=e==null?void 0:e.payload)==null?void 0:i.results)})},[]),h.useEffect(()=>{n.fullname&&n.email&&n.phone&&n.message?T(!1):T(!0)},[n]),h.useEffect(()=>{C&&setTimeout(()=>{S(!1)},5e3)},[C]);const[H,V]=h.useState(0),[A,I]=h.useState(!0);return h.useEffect(()=>{const e=setInterval(()=>{I(!1),setTimeout(()=>{V(i=>{var D;return(i+1)%((D=t==null?void 0:t.images)==null?void 0:D.length)}),I(!0)},500)},5e3);return()=>clearInterval(e)},[t==null?void 0:t.images]),s.jsxs("section",{className:c.container,children:[s.jsx(Ps,{}),s.jsx(m,{to:"https://wa.me/972544860306",target:"_blank",className:c.whatsbtn,children:s.jsx(ns,{})}),s.jsxs("div",{className:c.content,children:[s.jsx("div",{className:c.header,id:"header",style:{backgroundImage:`url(${($=(F=t==null?void 0:t.images)==null?void 0:F[H])==null?void 0:$.image})`,backgroundSize:"cover",backgroundColor:"#000",backgroundPosition:"center",filter:A?"brightness(1)":"brightness(0.8)",transition:"filter 0.5s ease-in-out"},children:s.jsxs("div",{className:c.headerText,children:[s.jsx("h2",{children:t==null?void 0:t[`title_${r}`]}),s.jsx("p",{children:t==null?void 0:t[`description_${r}`]}),s.jsx("button",{className:c.btn,onClick:()=>G("contact"),children:a("startNow",r)})]})}),s.jsxs("div",{className:c.about,id:"about",children:[s.jsxs("div",{className:c.aboutText,children:[s.jsx("h4",{children:a("about",r)}),s.jsx("h3",{children:(E=o==null?void 0:o[0])==null?void 0:E[`title_${r}`]}),s.jsx("p",{children:(L=o==null?void 0:o[0])==null?void 0:L[`description_${r}`]})]}),s.jsx("img",{src:(M=o==null?void 0:o[0])==null?void 0:M.image,alt:"about"})]}),s.jsxs("div",{className:c.samples,children:[s.jsx("div",{className:c.sampleText,children:s.jsx("h4",{children:a("ourMenus",r)})}),s.jsx("div",{className:c.samplesContainer,children:j&&(j==null?void 0:j.map((e,i)=>s.jsxs("div",{className:i===1?c.mid:c.sample,children:[s.jsx("div",{className:c.imageContainer,children:s.jsx("img",{src:e==null?void 0:e.image,alt:"theme"})}),s.jsx(m,{to:e==null?void 0:e.url,target:"_blank",children:a("seeDemo",r)})]},i)))})]}),s.jsxs("div",{className:c.services,id:"services",children:[s.jsx("h3",{children:a("services",r)}),s.jsx("div",{className:c.serviceCards,children:k&&(k==null?void 0:k.map((e,i)=>s.jsxs("div",{className:c.serviceCard,children:[s.jsx("img",{src:e==null?void 0:e.image,alt:"service"}),s.jsx("h4",{children:e==null?void 0:e[`title_${r}`]}),s.jsx("p",{children:e==null?void 0:e[`description_${r}`]})]},e==null?void 0:e.id)))})]}),s.jsxs("div",{className:c.contact,id:"contact",children:[s.jsx("h3",{children:a("contact",r)}),C&&s.jsxs("div",{className:c.success,children:[s.jsx(cs,{size:70,style:{color:"var(--purpleColor)"}}),s.jsx("p",{children:a("success",r)})]}),!C&&s.jsxs("div",{className:c.contactForm,children:[s.jsx("input",{type:"text",placeholder:a("fullname",r),value:n==null?void 0:n.fullname,onChange:e=>b({...n,fullname:e.target.value})}),s.jsx("input",{type:"email",placeholder:a("email",r),value:n==null?void 0:n.email,onChange:e=>b({...n,email:e.target.value})}),s.jsx("input",{type:"text",placeholder:a("phone",r),value:n==null?void 0:n.phone,onChange:e=>{/^\d*$/.test(e.target.value)&&b({...n,phone:e.target.value})}}),s.jsx("textarea",{name:"message",id:"message",placeholder:a("message",r),value:n==null?void 0:n.message,onChange:e=>b({...n,message:e.target.value})}),s.jsx("button",{disabled:z,onClick:P,children:B?s.jsx(U,{size:14,style:{color:"var(--purpleColor)"}}):a("send",r)}),w&&s.jsx("p",{className:"error",children:w})]})]})]}),s.jsx(Qs,{})]})};export{Os as default};
