import * as ScoringHandlers from './handlers/Scoring';

const scoringRoutes = [
  {
    method: 'GET',
    path: '/accommodations/{accommodationId}/scores',
    handler: ScoringHandlers.getAccommodationScores,
  },
];

export { scoringRoutes };
