const mongoose = require('mongoose');
var Schema = mongoose.Schema;
var trajectory_sanitized = new Schema({
  name: String,
  data: String,
});
module.exports = mongoose.model('trajectory_sanitized', trajectory_sanitized);
