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

module.exports = {
    getNotes,
}