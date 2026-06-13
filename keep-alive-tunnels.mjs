import localtunnel from 'localtunnel';

const startTunnel = async (port, subdomain, name) => {
  try {
    const tunnel = await localtunnel({ port, subdomain });
    console.log(`✅ ${name} deployed at: ${tunnel.url}`);

    tunnel.on('close', () => {
      console.log(`⚠️ ${name} tunnel closed. Restarting in 3 seconds...`);
      setTimeout(() => startTunnel(port, subdomain, name), 3000);
    });

    tunnel.on('error', (err) => {
      console.log(`❌ ${name} tunnel error:`, err);
    });
  } catch (err) {
    console.log(`❌ Failed to start ${name} tunnel. Retrying...`);
    setTimeout(() => startTunnel(port, subdomain, name), 3000);
  }
};

console.log('Starting permanent deployment tunnels...');
startTunnel(3000, 'smart-agri-api-99', 'Backend API');
startTunnel(5173, 'smart-agri-web-99', 'Frontend Web');
startTunnel(54874, 'smart-agri-flutter-99', 'Flutter App');

// Keep process alive
setInterval(() => {}, 1000 * 60 * 60);
