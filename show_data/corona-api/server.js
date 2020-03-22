const express = require("express");
const bodyParser = require("body-parser");
const cors = require("cors");
const DBCredentials =  require('./DBCredentials.ignore.js');
const Sequelize = require('sequelize');
const fs = require('fs')
const graphql = require('graphql-tools')
const graphqlHTTP = require('express-graphql')

const sequelize = new Sequelize(DBCredentials.getDatabase(), DBCredentials.getUsername(), DBCredentials.getPassword(), {
  host: DBCredentials.getServerName(),
  dialect: 'mysql',
  define: {
    timestamps: false,
    freezeTableName: true
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
}, {underscored: true, sequelize, modelName: 'state'});

class City extends Sequelize.Model {}
City.init({
id: {
  type: Sequelize.INTEGER,
  primaryKey: true
},
name: {
  type: Sequelize.TEXT
},
coordinates: {
  type: Sequelize.BLOB
}
}, {underscored: true, sequelize, modelName: 'city'})

class News extends Sequelize.Model {}
News.init({
  id: {
    type: Sequelize.INTEGER,
    primaryKey: true
  },
  state_id: {
    type: Sequelize.INTEGER
  },
  city_id: {
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
}, {underscored: true, sequelize, modelName: 'news'})

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
}, {underscored: true, sequelize, modelName: 'source'})
News.belongsTo(Source);
News.belongsTo(State);
News.belongsTo(City);
Source.hasMany(News);
City.hasMany(News);
City.belongsTo(State);
State.hasMany(News);
State.hasMany(City);

const app = express();
var corsOptions = {
  origin: "http://localhost:8081"
};
app.use(cors(corsOptions));

// register graphql module
const resolvers = {
  Query: {
      city: (_, { name }) => {
          return City.findOne({
              where: { name }
          })
      }
  },
  City: {
      news: async (city, args) => {
          return city.getNews()
      }
  }
}
const extensions = ({ document, variables, operationName, result, context }) => {
  return {
      runTime: `${(Date.now() - context.startTime) / 1000} seconds`
  }
}

const typeDefs = fs.readFileSync('./types.gql').toString()
const schema = graphql.makeExecutableSchema({
  typeDefs,
  resolvers
})
app.use('/graphql', graphqlHTTP({
  schema,
  extensions,
  graphiql: true
}))

// parse requests of content-type - application/json
app.use(bodyParser.json());

// parse requests of content-type - application/x-www-form-urlencoded
app.use(bodyParser.urlencoded({ extended: true }));

app.post("/get_articles_by_city", async (req, res) => {
  let city = await City.findOne({
    where: {name: req.body.name}
  });
  let news = await city.getNews();
  res.send(JSON.stringify(news));
});
app.post("/get_articles_by_state", async (req, res) => {
    let state = await State.findOne({
      where: {name: req.body.name}
    });
    let news = await state.getNews();
    //res.send(JSON.stringify(news));
    res.send(JSON.stringify(news));
});
app.post("/test", async (req, res) => {
  let states = await News.findOne();
  res.send(JSON.stringify(states));
});

// set port, listen for requests
const PORT = process.env.PORT || 8080;
app.listen(PORT, async () => {
  await sequelize.authenticate();
  console.log(`Server is running on port ${PORT}.`);
});
