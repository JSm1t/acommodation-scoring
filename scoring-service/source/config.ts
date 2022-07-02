import 'dotenv/config';

export const config = {
  server: {
    host: process.env.HOST,
    port: process.env.PORT,
  },
  dataService: {
    baseUrl: process.env.DATA_SERVICE_BASE_URL,
  },
};
