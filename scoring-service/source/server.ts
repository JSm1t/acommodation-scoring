import Qs from 'qs';
import Hapi, { Util } from '@hapi/hapi';
import { scoringRoutes } from './routes';
import { config } from './config';

main();

async function main(): Promise<void> {
  const server = Hapi.server({
    host: config.server.host,
    port: config.server.port,
    query: {
      parser: (query: Util.Dictionary<string>) => Qs.parse(query),
    },
  });

  server.route([...scoringRoutes]);

  server.ext('onPreResponse', async (request, h) => {
    if (request.response instanceof Error) {
      console.error(request.response);
    }

    return h.continue;
  });

  try {
    await server.start();
  } catch (err) {
    console.error(err);
  }

  console.log(
    `Scoring service running at: ${config.server.host}:${config.server.port}`
  );

  process.on('unhandledRejection', (err: any) => {
    console.error('Catched unhandled promise rejection', err);
  });
}
