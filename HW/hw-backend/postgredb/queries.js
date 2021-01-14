const Pool = require('pg').Pool

const config = require('./connectSetup')

const pool = new Pool({
  user: config.config.user,
  host: config.config.host,
  database: config.config.database,
  password: config.config.password,
  port: config.config.port,
})

const getNotes = (request, response) => {
    pool.query('SELECT * FROM notes ORDER BY id ASC', (error, results) => {
      if (error) {
        throw error
      }
      response.status(200).json(results.rows)
    })
}

const getImages = (request, response) => {
  pool.query('SELECT c.ID as ID, c.id_note as note, i.image as image FROM connections as c LEFT JOIN images as i ON c.id_image = i.ID' , (error,results) => {
    if(error) {
      throw error
    }
    response.status(200).json(results.rows)
  })
}

const getNoteById = (request, response) => {
  const id = parseInt(request.params.id)
  pool.query('SELECT * FROM notes WHERE id = $1', [id], (error, results) => {
    if (error) {
      throw error
    }
    response.status(200).json(results.rows)
  })
}

const getImagesById = (request, response) => {
  const id = parseInt(request.params.id)
  pool.query('SELECT c.ID as ID, c.id_note as note, i.image as image FROM connections as c LEFT JOIN images as i ON c.id_image = i.ID WHERE c.id_note = $1', [id], (error,results) => {
    if(error) {
      throw error
    }
    response.status(200).json(results.rows)
  })
}

module.exports = {
    getNotes,
    getImages,
    getNoteById,
    getImagesById,
}