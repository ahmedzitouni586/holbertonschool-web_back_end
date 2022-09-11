const { expect } = require('chai');

const calculateNumber = require('./2-calcul_chai');

describe('calculaNumber', () => {
    it('should return the sum', () => {
        expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
    });
    it('should return the subtraction', () => {
        expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
    });
    it('should return the division', () => {
        expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
    });
    it('should return Error string', () => {
        expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
    });
});
