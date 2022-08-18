const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculateNumber', function() {
  it('should return the sum', function() {
    assert.equal(calculateNumber('SUM', 1.4, 4.5), 6);
  })
  it('should subtract the numbers', function() {
    assert.equal(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
  })
  it('should divide the numbers', function() {
    assert.equal(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
  })
  it('should return Error', function() {
    assert.equal(calculateNumber('DIVIDE', 1.4, 0), 'Error')
  })
});
