import { Request, ResponseToolkit } from '@hapi/hapi';

async function errorHandler(request: Request, h: ResponseToolkit) {
  if (request.response instanceof Error) {
    console.error(request.response);
  }

  return h.continue;
}

export { errorHandler };
