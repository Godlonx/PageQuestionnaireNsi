const list = document.querySelectorAll('.list');
        function activeLink(){
            list.forEach((item) =>
            item.classList.remove('active'));
            this.classList.add('active');
        }
        list.forEach((item) =>
        item.addEventListener('click', activeLink))


let time_deb; /* Temps au début du questionnaire (en ms)*/
let time_fin; /* Durée totale du questionnaire (en ms)*/


function debut_timer(){
    time_deb = Date.now();
}

function fin_timer(){
    time_fin = Date.now() - time_deb
    console.log(time_fin)
    document.getElementById("temps").value = time_fin;
}