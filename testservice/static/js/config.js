function dropHandler(ev) {
    console.log('File(s) dropped');

    // Prevent default behavior (Prevent file from being opened)
    ev.preventDefault();

    if (ev.dataTransfer.items) {
        // Use DataTransferItemList interface to access the file(s)
        for (var i=0; i < ev.dataTransfer.items.length; i++) {
            // If dropped items aren't files, reject them
            if (ev.dataTransfer.items[i].kind == 'file') {
                var file = ev.dataTransfer.items[i].getAsFile();
                console.log('... file[' + i +'].name = ' + file.name);

                var reader = new FileReader();

                reader.onload = (function (theFile) {
                    return function (e) {
                        console.log('e readAsText = ', e);
                        console.log('e readAsText target =', e.target);
                        try {
                            const json = JSON.parse(e.target.result);
                            alert('json global var has been set to parsed json of this file here = \n' + JSON.stringify(json));
                            // Loop through items in JSON data...
                            Object.keys(json.tests).forEach(function(key) {
                                var btn = document.createElement("BUTTON");
                                btn.innerHTML = "TestID : " + json.tests[key].testid;
                                btn.onclick = function(){
                                    var string = document.createElement("P");
                                    string.innerHTML = "you started test :" + json.tests[key].testid;
                                    document.body.appendChild(string);
                                    Object.keys(json.tests[key].direction).forEach(function(dir) {
                                        const loop = setInterval(loopfunc, 1000);
                                        var time = 0;
                                        var count = 0;
                                        function loopfunc() {
                                            data = {"name" : [json.tests[key].direction[count].container, json.tests[key].direction[count].container]};
                                            // alert(json.tests[key].direction[dir].container);
                                            // ws.send(JSON.stringify(data));
                                            // ws.send(JSON.stringify(data));
                                            string.innerHTML = "container : " + json.tests[key].direction[count].container + " #" + time + " " + dir;
                                            document.body.appendChild(string);
                                            time += 1;
                                            if (time > json.tests[key].direction[count].time) {
                                                time = 0;
                                                count += 1;
                                                if (count > dir){
                                                    clearInterval(loop);
                                                };
                                            };

                                        };
                                    })
                                }
                                document.body.appendChild(btn);
                                var des = document.createElement("P");
                                des.innerHTML = "TestId : " + json.tests[key].testid + " | Description : " + json.tests[key].description + " | Time : " + json.tests[key].totaltime;
                                document.getElementById("descriptions").appendChild(des);
                            });
                        } catch (ex) {
                            alert('ex when trying to parse json = ' + ex);
                        }
                    }
                })(file);
                reader.readAsText(file);
            }
        }
    } else {
        // use DataTransfer interface to access the file(s)
        for (var i=0; i < ev.dataTransfer.files.length; i++) {
            console.log('... file[' + i +'].name = ' + ev.dataTransfer.files[i].name);
        }
    }
}

function dragOverHandler(ev) {
    console.log('File(s) in drop zone');

    // Preven default behavior (Prevent file from being opened)
    ev.preventDefault();
}

function clickHandler() {
    var string = "you clicked me";
    // string.innerHTML = "you started test : " + data.tests[id].testid;
    document.body.appendChild(string);
}