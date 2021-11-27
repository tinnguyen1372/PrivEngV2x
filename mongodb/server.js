const express = require('express'),
  path = require('path'),
  bodyParser = require('body-parser'),
  cors = require('cors'),
  mongoose = require('mongoose'),
  config = require('./config/db');
const connectDB = require('./config/db');
const app = express();
const trajectoryRoutes = require('./routes/api/trajectoryRoutes');

// Connect Database
connectDB();

app.use('/api', trajectoryRoutes);

// mongoose config
// mongoose.Promise = global.Promise;
// mongoose.connect(config.db).then(
//   () => {
//     console.log('Database is connected');
//   },
//   (err) => {
//     console.log('Can not connect to the database' + err);
//   }
// );

// CORS handle
// app.use(bodyParser.json());
app.use(bodyParser.json({ limit: '50mb' }));
app.use(
  bodyParser.urlencoded({
    limit: '50mb',
    extended: true,
    parameterLimit: 50000,
  })
);
app.use(cors());

const port = process.env.PORT || 5000;

app.listen(port, function () {
  console.log('Listening on port ' + port);
});
