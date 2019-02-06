const FIXED_DATE = new Date(2019, 1, 1).getTime()

describe('Visual regression testing for homepage', () => {
  beforeEach(function () {
    cy.clock(FIXED_DATE);
  });

  it('Loads the homepage', function() {
    cy.visit(`/`);
    cy.window().its('main-js:react:finished').should('equal', true);
    cy.wait(1000);
    cy.percySnapshot();
  });
});