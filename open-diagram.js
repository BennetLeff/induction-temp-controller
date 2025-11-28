const pako = require('pako');
const fs = require('fs');
const { execSync } = require('child_process');

const diagramFile = process.argv[2];
if (!diagramFile) {
  console.error('Usage: node open-diagram.js <diagram-file>');
  process.exit(1);
}

try {
  const diagram = fs.readFileSync(diagramFile, 'utf8');
  
  const state = {
    code: diagram,
    mermaid: JSON.stringify({ theme: 'default' }),
    autoSync: true,
    updateDiagram: true
  };
  
  const json = JSON.stringify(state);
  const data = Buffer.from(json, 'utf8');
  const compressed = pako.deflate(data, { level: 9 });
  const base64 = Buffer.from(compressed)
    .toString('base64')
    .replace(/\+/g, '-')
    .replace(/\//g, '_')
    .replace(/=/g, '');
  
  const url = `http://localhost:8000/edit#pako:${base64}`;
  console.log('Opening:', diagramFile);
  console.log('URL length:', url.length);
  
  execSync(`open "${url}"`);
} catch (error) {
  console.error('Error:', error.message);
  process.exit(1);
}
