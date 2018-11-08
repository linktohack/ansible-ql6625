module.exports = {
  apps : [{
    name      : '{{ item.domain | domain(env) }}',
    script    : 'index.js',
    cwd       : 'app',
    env: {
      NODE_ENV: 'development',
      PORT: '{{ item.port }}',
      DEBUG: ''
    },
    env_production : {
      NODE_ENV: 'production',
      PORT: '{{ item.port }}',
      DEBUG: ''
    }
  }]
};
