const express = require('express');
const trajectoryRoutes = express.Router();
const Trajectory_raw = require('../../model/trajectory_raw');
const Trajectory_sanitized = require('../../model/trajectory_sanitized');
const config = require('config');
let fs = require('fs');

async function run() {
  let data = await fs.readFileSync('../data/x_y_bsm.txt', 'utf8');
  let data_sanitized = await fs.readFileSync(
    '../data/x_y_bsm_sanitized.txt',
    'utf8'
  );
  await Trajectory_raw.replaceOne(
    { name: 'only data' },
    { name: 'only data', data: data }
  );
  await Trajectory_sanitized.replaceOne(
    { name: 'only data' },
    { name: 'only data', data: data_sanitized }
  );
}

trajectoryRoutes.post('/replace', async (req, res) => {
  try {
    setInterval(() => {
      run();
      console.log('Uploaded!');
    }, 1000);
  } catch (error) {
    console.log(e);
  }
});

trajectoryRoutes.get('/getData', async (req, res) => {
  try {
    setInterval(async () => {
      let data = await Trajectory_raw.find({});
      // console.log(data[0].data);
      let data_sanitized = await Trajectory_sanitized.find({});
      // console.log(data_sanitized[0].data);
      fs.writeFileSync('../output_raw.txt', data[0].data.toString());
      fs.writeFileSync(
        '../output_sanitized.txt',
        data_sanitized[0].data.toString()
      );
      console.log('Got new data!');
    }, 500);
  } catch (e) {
    console.log(e);
    res.status(500).send('Server Error');
  }
});

trajectoryRoutes.post('/new', async (req, res) => {
  try {
    let data = await fs.readFileSync('../data/x_y_bsm_sanitized.txt', 'utf8');
    const newTrajectory_raw = new Trajectory_sanitized({
      name: 'only data',
      data: data,
    });
    await newTrajectory_raw.save();
    res.json({ data });
  } catch (e) {
    console.log(e);
    res.status(500).send('Server Error');
  }
});

// trajectoryRoutes.post('/', async (req, res) => {
//   try {
//     //   await fs.readFile('../../x_y_bsm_sanitized.txt', 'utf8', async (err, data) => {
//     //     // let raw_data = await readTextFile('../../x_y_bsm.txt');
//     //     const newTrajectory_sanitized = new Trajectory_sanitized({ data: data });
//     //     const trajectory_sanitized = await newTrajectory_sanitized.save();
//     //     res.json(trajectory_sanitized);
//     //     // console.log(dataText);
//     //   })
//   } catch (e) {
//     console.log(e);
//     res.status(500).send('Server Error');
//   }
// });

trajectoryRoutes.get('/show', async (req, res) => {
  try {
    const data = await Trajectory_raw.find({});
    console.log(data.length);
    res.json({ msg: data });
  } catch (err) {
    console.error(err.message);
    res.status(500).send('Server Error');
  }
});

trajectoryRoutes.delete('/', async (req, res) => {
  try {
    // const post = await Trajectory_raw.find();
    const result = await Trajectory_raw.remove({}).exec();
    res.json({ msg: 'Post removed' });
  } catch (err) {
    console.error(err.message);

    res.status(500).send('Server Error');
  }
});

// trajectoryRoutes.get('/', async (req, res) => {
//     // const raw = database.collection("trajectory_raws");
//     // const sanitized = database.collection("trajectory_sanitizeds")
// function sleep(time) {
//   return new Promise((resolve) => setTimeout(resolve, time));
// }

// This code to send the data continuosly to the database
// for (let i = 0; i <= 10; i++) {
//   setTimeout(async function () {
//     await fs.readFile('../../x_y_bsm.txt', 'utf8', async (err, data) => {
//       // let raw_data = await readTextFile('../../x_y_bsm.txt');
//       const newTrajectory_raw = new Trajectory_raw({ data: data });
//       const trajectory_raw = await newTrajectory_raw.save();
//       res.json(trajectory_raw);
//       // console.log(dataText);
//     });
//   }, 5000);
// }
// for (i=0;i<=10;i++){
//     sleep(10000).then(() => {
//     fs.readFile('../../x_y_bsm.txt', 'utf8', async (err, data) => {
//     const newTrajectory_raw = new Trajectory_raw({ data: data });
//     const trajectory_raw = await newTrajectory_raw.save();
//     res.json(trajectory_raw);
//     // console.log(dataText);
//     })
// });

// var id = window.setInterval(function(){
//     if(i >= 10) {
//         clearInterval(id);
//         return;
//     }

//     console.log(i);
//     i++;
// }, 1000)

// })

let changeStream_raw;
let changeStream_sanitized;

changeStream_raw = Trajectory_raw.watch();
changeStream_sanitized = Trajectory_sanitized.watch();

changeStream_raw.on('change', (next) => {
  // process any change event
  console.log('received a change to the collection: \t');
});

module.exports = trajectoryRoutes;
