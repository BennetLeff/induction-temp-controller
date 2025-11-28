const pako = require('pako');
const fs = require('fs');

const diagram = fs.readFileSync('hardware-diagram.mmd', 'utf8');

const state = {
  code: diagram,
  mermaid: JSON.stringify({ theme: 'default' }),
  autoSync: true,
  updateDiagram: true
};

const json = JSON.stringify(state);
const data = new TextEncoder().encode(json);
const compressed = pako.deflate(data, { level: 9 });
const base64 = Buffer.from(compressed).toString('base64')
  .replace(/\+/g, '-')
  .replace(/\//g, '_')
  .replace(/=/g, '');

console.log(`http://localhost:8000/edit#pako:${base64}`);
