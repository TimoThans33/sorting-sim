function demo_function(string){
    document.getElementById(string).innerHTML = "Hello JavaScript !";
}

function rotateImage(img) {
    img.style.transform = 'rotate(180deg)';
}

function pad(n, width, z){
    z = z || '0';
    n = n + '';
    return n.length >= width ? n : new Array(width - n.length + 1).join(z) + n;
}

function formatDate(date) {
    var d = new Date(date),
        month = '' + (d.getMonth()+1),
        day = '' + d.getDate(),
        year = '' + d.getFullYear();
    if (month.length < 2)
        month = '0' + month;
    if (day.lenght < 2)
        day = '0' + day;
    return [year, month, day].join('-');
}

function formatTime(date) {
    var d = new Date(date),
        h = '' + (d.getHours()),
        m = '' + (d.getMinutes()),
        s = '' + (d.getSeconds());
    if (h.length < 2)
        h = '0' + h;
    if (m.length < 2)
        m = '0' + m;
    if (s.length < 2)
        s = '0' + s;
    return [h, m, s].join(':');
}

function generate_direction(min, max) {
    direc = Math.floor(Math.random() * (max - min) ) + min;
    zf_dir = pad(direc, 3);
    return zf_dir, direc;
}

function compose_msg(scanner_id=1, min=1, max=24, barcode = 4206005698049202090135079104324001) {
    zf_dir, direc = generate_direction(min, max);
    station_id = '\x02MSA-12345-001'
    scanner_id = str(scaner_id)
    barcode = str(barcode)
    var d = new Date();
    var date = formatDate(d);
    var date_str = date.toString();
    var time = fromatTime(d);
    var time_str = time.toString();
    eos = 'Z\x03'
    return (station_id +","+ scanner_id +","+ zf_dir +","+ barcode +","+ direc +","+ date_str + "T" + time_str + eos)
}



function main(img) {
    img.style.transform = 'rotate(180deg)'

}