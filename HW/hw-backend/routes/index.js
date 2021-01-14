var express = require('express');
var router = express.Router();

const db = require('../postgredb/queries')

/* GET home page. */
router.get('/', db.getNotes);
router.get('/images', db.getImages);
router.get('/list/:id', db.getNoteById)
router.get('/images/:id', db.getImagesById)

module.exports = router;
