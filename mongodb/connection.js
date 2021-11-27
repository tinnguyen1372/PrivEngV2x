const { MongoClient } = require('mongodb');
// import sanitizedText from "../x_"

async function main() {
  const uri =
    'mongodb+srv://huybq:huy26062002@cluster0.1f7ja.mongodb.net/myFirstDatabase?retryWrites=true&w=majority';
  const client = new MongoClient(uri);

  // try {
  //   await client.connect();
  //   await readTextFile('../x_y_bsm_sanitized_test.txt');
  // } catch (e) {
  //   console.log(e);
  // }
}

function readTextFile(fileName) {
  var fs = require('fs');
  fs.readFile(fileName, 'utf8', function (err, data) {
    if (err) throw err;
    console.log('OK: ' + fileName);
    console.log(data);
  });
}

main().catch(console.error);
