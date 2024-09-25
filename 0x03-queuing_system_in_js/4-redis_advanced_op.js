import { createClient, print } from "redis";
import {promisify } from 'util'

const client = createClient();

client.on('error', err => console.log(`Redis client not connected to the server: ${err}`));

client.on('connect', () => console.log('Redis client connected to the server'));

function setHset(key, field, value) {
  client.hset(key, field, value, print);
}

setHset('HolbertonSchools', 'Portland', '50');
setHset('HolbertonSchools', 'Seattle', '80');
setHset('HolbertonSchools', 'New York', '20');
setHset('HolbertonSchools', 'Bogota', '20');
setHset('HolbertonSchools', 'Cali', '40');
setHset('HolbertonSchools', 'Paris', '2');

client.hgetall('HolbertonSchools', (err, reply) => {
  console.log(reply);
} );
