const DBCredentials =  require('./DBCredentials.ignore.js');
const Sequelize = require('sequelize');

const sequelize = new Sequelize(DBCredentials.getDatabase(), DBCredentials.getUsername(), DBCredentials.getPassword(), {
  host: DBCredentials.getServerName(),
  dialect: 'mysql',
  define: {
    timestamps: false
  }
});

class State extends Sequelize.Model {}
State.init({
  id: {
    type: Sequelize.INTEGER,
    primaryKey: true
  },
  name: {
    type: Sequelize.STRING
  }
}, {sequelize, modelName: 'state'});
  class City extends Sequelize.Model {}
City.init({
  id: {
    type: Sequelize.INTEGER,
    primaryKey: true
  },
  name: {
    type: Sequelize.TEXT
  },
  state_id: {
    type: Sequelize.INTEGER
  },
  coordinates: {
    type: Sequelize.BLOB
  }
}, {sequelize, modelName: 'city'})

class News extends Sequelize.Model {}
News.init({
  id: {
    type: Sequelize.INTEGER,
    primaryKey: true
  },
  city_id: {
    type: Sequelize.INTEGER
  },
  state_id: {
    type: Sequelize.INTEGER
  },
  source_id: {
    type: Sequelize.INTEGER
  },
  date: {
    type: Sequelize.DATE
  },
  title: {
    type: Sequelize.STRING
  },
  url: {
    type: Sequelize.TEXT
  }
}, {sequelize, modelName: 'news'})
class Source extends Sequelize.Model {}
Source.init({
  id: {
    type: Sequelize.INTEGER,
    primaryKey: true
  },
  name: {
    type: Sequelize.STRING
  },
  type: {
    type: Sequelize.TEXT
  }
}, {sequelize, modelName: 'source'})


sequelize
  .authenticate()
  .then(() => {
    console.log('Connection has been established successfully.');
    News.findAll().then(states => {
      console.log(JSON.stringify(states));
    });
  })
  .catch(err => {
    console.error('Unable to connect to the database:', err);
  });
