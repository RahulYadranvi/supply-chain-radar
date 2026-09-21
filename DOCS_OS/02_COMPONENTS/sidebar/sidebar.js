const sidebar=document.querySelector(".sidebar");
const button=document.getElementById("menuButton");
const overlay=document.getElementById("overlay");

button?.addEventListener("click",()=>{
sidebar.classList.toggle("open");
overlay.classList.toggle("show");
});

overlay?.addEventListener("click",()=>{
sidebar.classList.remove("open");
overlay.classList.remove("show");
});

const search=document.getElementById("searchInput");

search?.addEventListener("keyup",(e)=>{

const value=e.target.value.toLowerCase();

document.querySelectorAll(".doc-link").forEach(link=>{

const text=link.innerText.toLowerCase();

link.style.display=text.includes(value)?"block":"none";

});

});