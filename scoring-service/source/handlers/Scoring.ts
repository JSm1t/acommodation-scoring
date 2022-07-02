import { Request } from '@hapi/hapi';
import * as Boom from '@hapi/boom';
import * as ScoringService from '../services/Scoring';

async function getAccommodationScores(request: Request) {
  const results = await ScoringService.getAccommodationScores(
    request.params.accommodationId
  );

  return {
    data: results,
  };
}

export { getAccommodationScores };
