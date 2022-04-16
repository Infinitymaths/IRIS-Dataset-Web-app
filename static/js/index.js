const tab = document.querySelectorAll(".tab");
tab[0].checked = true;
tab.forEach((e)=>{
    e.addEventListener("click",(event)=>{
        tab.forEach((e)=>{
            e.checked = false;
            e.parentElement.classList.remove("active");
        })
        event.target.checked=true;
        e.parentElement.classList.add("active");
    })
});