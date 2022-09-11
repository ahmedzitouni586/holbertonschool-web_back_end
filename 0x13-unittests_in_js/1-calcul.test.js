const assert = require('assert');

const calculateNumber = require('./1-calcul');

describe('calculaNumber', () => {
    it('should return the sum', () => {
        assert.equal(calculateNumber('SUM', 1.4, 4.5), 6);
    });
    it('should return the subtraction', () => {
        assert.equal(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
    });
    it('should return the division', () => {
        assert.equal(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
    });
    it('should return Error string', () => {
        assert.equal(calculateNumber('DIVIDE', 1.4, 0), 'Error');
    });
});
