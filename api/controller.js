"use strict";

var properties = require("../package.json");
var trends = require("../service/trends");

var controllers = {
  about: function (req, res) {
    var aboutInfo = {
      name: properties.name,
      version: properties.version,
    };
    res.json(aboutInfo);
  },
  trending: function (req, res) {
    trends.find(req, res, function (err, dist) {
      if (err) res.send(err);
      res.json(dist);
    });
  },
};

module.exports = controllers;