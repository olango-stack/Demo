//Checks a URL and returns the status code that signifies if website is up or down

const https = require('https');
let url = "https://www.olangopxtder.com";

exports.handler = async function(event) {
    let statusCode;
    await new Promise(function(resolve, reject) {
        https.get(url, (res) => {
            statusCode = res.statusCode;
            resolve(statusCode);
        }).on("error", (e) => {
            reject(Error(e));
        });
    });
    console.log(statusCode);
    return statusCode;
};