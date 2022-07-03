import { DateTime } from 'luxon';
import * as ScoringService from './Scoring';

describe('Scoring service', () => {
  describe('#calculateWeightedAverage', () => {
    it('should calculate the weighted average for a set of ratings', () => {
      const ratings = [
        // Weight: 3.2188758248682006
        // Weighted: 28.969882423813804
        {
          rating: 9,
          reviewDate: DateTime.now().toJSDate(),
        },
        // Weight: 3.091042453358316
        // Weighted: 18.546254720149896
        {
          rating: 6,
          reviewDate: DateTime.now().minus({ months: 3 }).toJSDate(),
        },
        // Weight: 2.70805020110221
        // Weighted: 21.66440160881768
        {
          rating: 8,
          reviewDate: DateTime.now().minus({ months: 10 }).toJSDate(),
        },
        // Weight: 0.5709795465857378
        // Weighted: 3.4258772795144266
        {
          rating: 6,
          reviewDate: DateTime.now().minus({ months: 24 }).toJSDate(),
        },
      ];

      // Total weight: 9.588948025914465
      // Total weighted: 72.60641603229581

      const result = ScoringService.calculateWeightedAverage(ratings);

      expect(result).toBe(7.57);
    });

    it('should ignore null values when calculating the weighted average', () => {
      const ratings = [
        // Weight: 2.995732273553991
        // Weighted: 26.961590461985917
        {
          rating: 9,
          reviewDate: DateTime.now().minus({ months: 5 }).toJSDate(),
        },
        {
          rating: null,
          reviewDate: DateTime.now().minus({ months: 25 }).toJSDate(),
        },
        {
          // Weight: 2.995732273553991
          // Weighted: 23.965858188431927
          rating: 8,
          reviewDate: DateTime.now().minus({ months: 5 }).toJSDate(),
        },
        {
          rating: null,
          reviewDate: DateTime.now().minus({ months: 3 }).toJSDate(),
        },
      ];

      // Total Weight: 50.927448650417844
      // Total Weighted: 5.991464547107982

      const result = ScoringService.calculateWeightedAverage(ratings);

      expect(result).toBe(8.5);
    });

    it('should return null when no ratings were available', () => {
      const ratings = [
        {
          rating: null,
          reviewDate: DateTime.now().minus({ months: 5 }).toJSDate(),
        },
        {
          rating: null,
          reviewDate: DateTime.now().minus({ months: 25 }).toJSDate(),
        },
        {
          rating: null,
          reviewDate: DateTime.now().minus({ months: 5 }).toJSDate(),
        },
        {
          rating: null,
          reviewDate: DateTime.now().minus({ months: 3 }).toJSDate(),
        },
      ];

      const result = ScoringService.calculateWeightedAverage(ratings);

      expect(result).toBeNull();
    });
  });
});
