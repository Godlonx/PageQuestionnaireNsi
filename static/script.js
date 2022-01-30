const list = document.querySelectorAll('.list');
        function activeLink(){
            list.forEach((item) =>
            item.classList.remove('active'));
            this.classList.add('active');
        }
        list.forEach((item) =>
        item.addEventListener('click', activeLink))


let time;
let fin;
let temps;
let min;
let sec;
let msec;

function debut_timer(){
    time = Date.now();
}

function fin_timer(){
    min = String(~~((~~((Date.now() - time)/1000))/60))
    sec = String(~~((Date.now() - time)/1000)%60)
    msec = String((Date.now() - time)%1000)
    fin = min+","+sec+","+msec

    console.log(fin)
}