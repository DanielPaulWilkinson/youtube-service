const { spawn } = require("child_process");
const { PythonShell } = require("python-shell");

var trends = {
  find: function (req, res, next) {
    let options = {
      pythonPath: "py",
      scriptPath: "./service/",
    };

    PythonShell.run("youtube_trends.py", options, function (err, results) {
      if (err) console.log(err);
      res.send(JSON.parse(results));
    });
  },
};

module.exports = trends;
