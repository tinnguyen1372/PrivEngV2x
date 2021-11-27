const mongoose = require('mongoose');
var Schema = mongoose.Schema;
var trajectory_raw = new Schema({
  name: String,
  data: String,
});
module.exports = mongoose.model('trajectory_raw', trajectory_raw);
