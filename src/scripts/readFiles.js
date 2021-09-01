const path = require('path')
const fs = require('fs')
const csv = require('csv-parse')
// const Papa = require('papaparse')

function readFiles(){

    console.log(__dirname)
    const targetDir = path.join(__dirname,'../Input');

    fs.readdir(targetDir, function (err, files) {
        //handling error
        if (err) {
            return console.log('Unable to scan directory: ' + err);
        } 
        //listing all files using forEach
        files.forEach(function (file) {
            // Do whatever you want to do with the file
            console.log(file); 
            // console.log(path.extname(file) == '.csv'); 
            if(path.extname(file) === '.csv'){
                console.log("running CSV Parser")
                parseCSV(file)
                console.log("==============================================")
            } else if(path.extname(file) === '.xml'){
                console.log("running XML Parser")
                console.log("==============================================")

            } else if(path.extname(file) === '.json'){
                console.log("running JSON Parser")
                console.log("==============================================")

            }else{
                console.log("Filetype currently not supported")
                console.log("==============================================")

            }

        });
    });



}

function parseCSV(file) {
    fs.createReadStream(file)
    .pipe(csv({}))
    .on('data',(data)=> results.push(data))
    .on('end',()=>{
        console.log(results)
    });

}


readFiles();